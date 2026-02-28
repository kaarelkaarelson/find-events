#!/usr/bin/env python3
"""Build an LLM prompt by injecting all event source files from ./data."""

from __future__ import annotations

import argparse
import json
import os
from math import ceil
from datetime import date, datetime, timedelta
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"
RUNS_DIR = DATA_DIR / "evaluate_runs"
SKIP_FILES = {"evaluate_events_prompt.txt", "evaluate_events.py", "token_count_helper.py"}
CURRENT_DATE = date.fromisoformat("2026-02-28")
DEFAULT_MODEL = "gemini-2.5-flash-lite"
GEMINI_API_BASE = "https://generativelanguage.googleapis.com/v1beta/models"
DEFAULT_MAX_OUTPUT_TOKENS = 8192
DEFAULT_MAX_INPUT_TOKENS = 220000
PER_SOURCE_MAX_CHARS = 60000
DEFAULT_MAX_ITEMS_PER_JSON_SOURCE = 300


def load_dotenv(path: Path) -> None:
    """Load KEY=VALUE pairs from .env into environment if not already set."""
    if not path.exists():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("'").strip('"')
        if key and key not in os.environ:
            os.environ[key] = value


def load_sources() -> list[tuple[str, str]]:
    sources: list[tuple[str, str]] = []
    source_files = sorted(p for p in DATA_DIR.iterdir() if p.is_file())
    window_end = CURRENT_DATE + timedelta(weeks=4)
    for path in source_files:
        if path.name in SKIP_FILES:
            continue
        if path.name.startswith("evaluate_events_"):
            continue
        if path.name.startswith("awesome_events_"):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        compact_text = compact_source_text(
            name=path.name,
            text=text,
            window_start=CURRENT_DATE,
            window_end=window_end,
            max_chars=PER_SOURCE_MAX_CHARS,
            max_items=DEFAULT_MAX_ITEMS_PER_JSON_SOURCE,
        )
        sources.append((path.name, compact_text))
    return sources


def estimate_tokens(text: str) -> int:
    # Fast approximation for quota/budget guarding.
    return ceil(len(text) / 4)


def _extract_date_like(item: dict) -> str:
    for key in ("start_at", "date", "start", "start_date", "week_start"):
        value = item.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return ""


def _in_window(date_str: str, window_start: date, window_end: date) -> bool:
    if not date_str:
        return False
    candidate = date_str.strip().replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(candidate)
        return window_start <= dt.date() <= window_end
    except ValueError:
        try:
            d = date.fromisoformat(candidate[:10])
            return window_start <= d <= window_end
        except ValueError:
            return False


def _compact_json_payload(
    payload: dict | list,
    window_start: date,
    window_end: date,
    max_items: int,
) -> str:
    if isinstance(payload, list):
        records: list[dict] = [x for x in payload if isinstance(x, dict)]
        if records:
            in_window = [x for x in records if _in_window(_extract_date_like(x), window_start, window_end)]
            chosen = in_window if in_window else records
            return json.dumps(chosen[:max_items], ensure_ascii=True, separators=(",", ":"))
        return json.dumps(payload[:max_items], ensure_ascii=True, separators=(",", ":"))

    if isinstance(payload, dict):
        # Common wrappers: keep list-ish fields compact.
        compact: dict = {}
        for key, value in payload.items():
            if isinstance(value, list):
                records = [x for x in value if isinstance(x, dict)]
                if records:
                    in_window = [x for x in records if _in_window(_extract_date_like(x), window_start, window_end)]
                    chosen = in_window if in_window else records
                    compact[key] = chosen[:max_items]
                else:
                    compact[key] = value[:max_items]
            else:
                compact[key] = value
        return json.dumps(compact, ensure_ascii=True, separators=(",", ":"))

    return json.dumps(payload, ensure_ascii=True, separators=(",", ":"))


def compact_source_text(
    name: str,
    text: str,
    window_start: date,
    window_end: date,
    max_chars: int,
    max_items: int,
) -> str:
    raw = text.strip()
    if not raw:
        return raw

    # Compact JSON sources first.
    if name.endswith(".json"):
        try:
            payload = json.loads(raw)
            raw = _compact_json_payload(payload, window_start, window_end, max_items=max_items)
        except json.JSONDecodeError:
            pass

    if len(raw) > max_chars:
        return raw[:max_chars]
    return raw


def enforce_prompt_budget(
    sources: list[tuple[str, str]],
    max_input_tokens: int,
) -> list[tuple[str, str]]:
    def build_with(s: list[tuple[str, str]]) -> str:
        return build_prompt(s)

    current = list(sources)
    prompt = build_with(current)
    if estimate_tokens(prompt) <= max_input_tokens:
        return current

    # Iteratively trim largest sources until within budget.
    current_map = {name: content for name, content in current}
    while True:
        prompt = build_with(list(current_map.items()))
        if estimate_tokens(prompt) <= max_input_tokens:
            break
        largest_name = max(current_map, key=lambda n: len(current_map[n]))
        largest_value = current_map[largest_name]
        if len(largest_value) <= 2000:
            # Can't reduce further in a meaningful way.
            break
        current_map[largest_name] = largest_value[: int(len(largest_value) * 0.8)]

    # Stable ordering by source name.
    return sorted(current_map.items(), key=lambda x: x[0])


def build_prompt(sources: list[tuple[str, str]]) -> str:
    today = CURRENT_DATE
    window_end = today + timedelta(weeks=4)
    header = (
        "You are a professional event evaluator.\n"
        "Your goal is to filter out only the highest-signal events from all provided sources.\n"
        "Some sources have rich descriptions, some have little context. Use judgment and still select the best events.\n"
        "\n"
        f"Current date context: {today.isoformat()}.\n"
        f"Selection window: from {today.isoformat()} through {window_end.isoformat()} (next 4 weeks).\n"
        "\n"
        "Person profile:\n"
        "- 23-year-old working in tech.\n"
        "- Lives in San Francisco.\n"
        "- Flexible around the Bay Area.\n"
        "- Can travel to other major cities only for very special, unusually high-signal events.\n"
        "- Wants to meet many smart, ambitious, interesting people.\n"
        "- Cannot attend many events; prioritize only the strongest options.\n"
        "- Also interested in social activities (for example, got asked about tennis).\n"
        "\n"
        "Evaluation objective:\n"
        "- Return weekly picks for the next 4 weeks.\n"
        "- Select exactly 5 high-signal events per week (total 20).\n"
        "- Also return exactly 3 overall can't-miss picks across the full 4-week window.\n"
        "- Within each week, rank events by signal quality (best to worst), not by date/time.\n"
        "- Maximize quality of people, network upside, and relevance to tech/AI/startups.\n"
        "- Penalize low-signal, generic, or poorly-specified events.\n"
        "- Include concise reasoning for each selected event.\n"
        "\n"
        "Output format (STRICT):\n"
        "- Return ONLY valid JSON.\n"
        "- No markdown, no prose outside JSON.\n"
        "- Use this shape exactly:\n"
        "{\n"
        '  "top_3_picks": [\n'
        "    {\n"
        '      "title": "string",\n'
        '      "date": "start ISO date/time string or best available",\n'
        '      "end_date": "end ISO date/time string if known, else empty string",\n'
        '      "location": "string",\n'
        '      "reason": "short explanation of why high-signal",\n'
        '      "link": "URL string"\n'
        "    }\n"
        "  ],\n"
        '  "weeks": [\n'
        "    {\n"
        '      "week_label": "Week 1",\n'
        '      "week_start": "YYYY-MM-DD",\n'
        '      "week_end": "YYYY-MM-DD",\n'
        '      "events": [\n'
        "        {\n"
        '          "rank_in_week": 1,\n'
        '          "title": "string",\n'
        '          "date": "start ISO date/time string or best available",\n'
        '          "end_date": "end ISO date/time string if known, else empty string",\n'
        '          "location": "string",\n'
        '          "reason": "short explanation of why high-signal",\n'
        '          "link": "URL string"\n'
        "        }\n"
        "      ]\n"
        "    }\n"
        "  ]\n"
        "}\n"
        "- Include exactly 4 week objects.\n"
        "- Include exactly 5 events per week object.\n"
        "- Include exactly 3 objects in top_3_picks.\n"
        "- For each week, set rank_in_week as unique integers 1..5 (1 is strongest event that week).\n"
        "\n"
        "Source data follows.\n"
    )

    blocks = [header]
    for name, content in sources:
        blocks.append(f"\n=== SOURCE: {name} ===\n")
        blocks.append(content)
        blocks.append("\n")
    return "".join(blocks)


def get_gemini_api_key() -> str:
    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not key:
        raise RuntimeError("Missing GEMINI_API_KEY (or GOOGLE_API_KEY) in .env/environment.")
    return key


def call_gemini(prompt: str, model: str, max_output_tokens: int = DEFAULT_MAX_OUTPUT_TOKENS) -> dict:
    """Call Gemini generateContent API and return parsed JSON response."""
    api_key = get_gemini_api_key()
    url = f"{GEMINI_API_BASE}/{model}:generateContent?key={api_key}"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "maxOutputTokens": max_output_tokens,
            "temperature": 0.2,
            "responseMimeType": "application/json",
            "thinkingConfig": {"thinkingBudget": 0},
            "responseSchema": {
                "type": "OBJECT",
                "properties": {
                    "top_3_picks": {
                        "type": "ARRAY",
                        "minItems": 3,
                        "maxItems": 3,
                        "items": {
                            "type": "OBJECT",
                            "properties": {
                                "title": {"type": "STRING"},
                                "date": {"type": "STRING"},
                                "end_date": {"type": "STRING"},
                                "location": {"type": "STRING"},
                                "reason": {"type": "STRING"},
                                "link": {"type": "STRING"},
                            },
                            "required": ["title", "date", "location", "reason", "link"],
                        },
                    },
                    "weeks": {
                        "type": "ARRAY",
                        "minItems": 4,
                        "maxItems": 4,
                        "items": {
                            "type": "OBJECT",
                            "properties": {
                                "week_label": {"type": "STRING"},
                                "week_start": {"type": "STRING"},
                                "week_end": {"type": "STRING"},
                                "events": {
                                    "type": "ARRAY",
                                    "minItems": 5,
                                    "maxItems": 5,
                                    "items": {
                                        "type": "OBJECT",
                                        "properties": {
                                            "rank_in_week": {"type": "INTEGER"},
                                            "title": {"type": "STRING"},
                                            "date": {"type": "STRING"},
                                            "end_date": {"type": "STRING"},
                                            "location": {"type": "STRING"},
                                            "reason": {"type": "STRING"},
                                            "link": {"type": "STRING"},
                                        },
                                        "required": [
                                            "rank_in_week",
                                            "title",
                                            "date",
                                            "location",
                                            "reason",
                                            "link",
                                        ],
                                    },
                                },
                            },
                            "required": ["week_label", "week_start", "week_end", "events"],
                        },
                    },
                },
                "required": ["top_3_picks", "weeks"],
            },
        },
    }

    req = Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urlopen(req, timeout=120) as response:
            raw = response.read().decode("utf-8", errors="replace")
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Gemini HTTP {exc.code}: {detail}") from exc
    except URLError as exc:
        raise RuntimeError(f"Gemini request failed: {exc}") from exc

    data = json.loads(raw)
    if not isinstance(data, dict):
        raise RuntimeError("Unexpected Gemini response format: expected JSON object.")
    return data


def extract_text_from_gemini_response(data: dict) -> str:
    candidates = data.get("candidates", [])
    if not isinstance(candidates, list):
        return ""
    chunks: list[str] = []
    for cand in candidates:
        if not isinstance(cand, dict):
            continue
        content = cand.get("content", {})
        if not isinstance(content, dict):
            continue
        parts = content.get("parts", [])
        if not isinstance(parts, list):
            continue
        for part in parts:
            if isinstance(part, dict) and isinstance(part.get("text"), str):
                chunks.append(part["text"])
    return "\n\n".join(chunks).strip()


def first_finish_reason(data: dict) -> str:
    candidates = data.get("candidates", [])
    if isinstance(candidates, list) and candidates and isinstance(candidates[0], dict):
        value = candidates[0].get("finishReason", "")
        if isinstance(value, str):
            return value
    return ""


def try_parse_json_text(text: str) -> dict | list | None:
    candidate = text.strip()
    if candidate.startswith("```"):
        candidate = candidate.strip("`")
        if candidate.startswith("json"):
            candidate = candidate[4:].strip()
    try:
        parsed = json.loads(candidate)
        if isinstance(parsed, (dict, list)):
            return parsed
    except json.JSONDecodeError:
        pass

    # Fallback: extract first JSON object/array span from mixed text.
    starts = [i for i in (candidate.find("{"), candidate.find("[")) if i != -1]
    if not starts:
        return None
    start = min(starts)
    ends = [i for i in (candidate.rfind("}"), candidate.rfind("]")) if i != -1]
    if not ends:
        return None
    end = max(ends)
    if end <= start:
        return None
    try:
        parsed = json.loads(candidate[start : end + 1])
    except json.JSONDecodeError:
        return None
    if isinstance(parsed, (dict, list)):
        return parsed
    return None


def make_run_dir() -> Path:
    """Create a unique run output directory."""
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    # Lexicographically sortable and unique by timestamp.
    run_id = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    run_dir = RUNS_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    return run_dir


def render_weekly_readme(structured: dict) -> str:
    """Render weekly event picks into GitHub-friendly README markdown."""
    lines: list[str] = []
    lines.append("# Awesome SF Events")
    lines.append("")
    lines.append("High Signal Weekly Picks for SF Bay Area Builders for March.")
    lines.append(f"Updated: `{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}`.")
    lines.append("")

    top_3 = structured.get("top_3_picks", []) if isinstance(structured, dict) else []
    if not isinstance(top_3, list):
        top_3 = []
    if top_3:
        lines.append("## Can't-Miss Picks")
        lines.append("If you only attend three events this month, RSVP to these first.")
        lines.append("")
        for idx, event in enumerate(top_3[:3], start=1):
            if not isinstance(event, dict):
                continue
            title = str(event.get("title", "")).strip()
            date_value = str(event.get("date", "")).strip()
            location = str(event.get("location", "")).strip()
            reason = str(event.get("reason", "")).strip()
            link = str(event.get("link", "")).strip()
            if link:
                lines.append(f"{idx}. **[{title}]({link})**")
            else:
                lines.append(f"{idx}. **{title}**")
            lines.append(f"   - Date: {date_value}")
            lines.append(f"   - Location: {location}")
            lines.append(f"   - Why: {reason}")
            lines.append("")
        lines.append("---")
        lines.append("")

    weeks = structured.get("weeks", []) if isinstance(structured, dict) else []
    if not isinstance(weeks, list):
        weeks = []

    for week in weeks:
        if not isinstance(week, dict):
            continue
        label = str(week.get("week_label", "Week"))
        start = str(week.get("week_start", ""))
        end = str(week.get("week_end", ""))
        lines.append(f"## {label} ({start} to {end})")
        lines.append("")

        events = week.get("events", [])
        if not isinstance(events, list):
            events = []
        else:
            ranked = [e for e in events if isinstance(e, dict) and isinstance(e.get("rank_in_week"), int)]
            if len(ranked) == len(events):
                events = sorted(events, key=lambda e: int(e.get("rank_in_week", 999)))

        for idx, event in enumerate(events, start=1):
            if not isinstance(event, dict):
                continue
            title = str(event.get("title", "")).strip()
            date_value = str(event.get("date", "")).strip()
            location = str(event.get("location", "")).strip()
            reason = str(event.get("reason", "")).strip()
            link = str(event.get("link", "")).strip()

            lines.append(f"{idx}. **{title}**")
            lines.append(f"   - Date: {date_value}")
            lines.append(f"   - Location: {location}")
            lines.append(f"   - Why high-signal: {reason}")
            lines.append(f"   - Link: {link}")
            lines.append("")

    return "\n".join(lines).strip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Build and optionally evaluate event prompt with Gemini.")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Gemini model id (e.g. gemini-2.5-flash-lite)")
    parser.add_argument(
        "--max-output-tokens",
        type=int,
        default=DEFAULT_MAX_OUTPUT_TOKENS,
        help="Max output tokens for Gemini response",
    )
    parser.add_argument(
        "--run-gemini",
        action="store_true",
        help="Call Gemini API after generating prompt",
    )
    parser.add_argument(
        "--max-input-tokens",
        type=int,
        default=DEFAULT_MAX_INPUT_TOKENS,
        help="Approximate max input tokens for the prompt",
    )
    args = parser.parse_args()

    load_dotenv(PROJECT_ROOT / ".env")
    sources = load_sources()
    sources = enforce_prompt_budget(sources=sources, max_input_tokens=args.max_input_tokens)
    prompt = build_prompt(sources)
    run_dir = make_run_dir()
    out_file = run_dir / "evaluate_events_prompt.txt"
    out_response_file = run_dir / "evaluate_events_response.txt"
    out_response_json_file = run_dir / "evaluate_events_response_raw.json"
    out_structured_file = run_dir / "evaluate_events_structured.json"
    out_readme_file = run_dir / "awesome_readme.md"

    out_file.write_text(prompt, encoding="utf-8")
    run_id = run_dir.name
    print(f"Run dir: {run_dir}")
    print(f"Saved: {out_file}")
    print(f"Sources injected: {len(sources)}")
    print(f"Estimated prompt tokens: ~{estimate_tokens(prompt)}")

    if not args.run_gemini:
        return

    response = call_gemini(prompt=prompt, model=args.model, max_output_tokens=args.max_output_tokens)
    text = extract_text_from_gemini_response(response)
    parsed = try_parse_json_text(text)
    finish_reason = first_finish_reason(response)
    if parsed is None and finish_reason == "MAX_TOKENS":
        retry_tokens = max(args.max_output_tokens * 2, DEFAULT_MAX_OUTPUT_TOKENS)
        print(f"Retrying due to truncated JSON (MAX_TOKENS). New max_output_tokens={retry_tokens}")
        response = call_gemini(prompt=prompt, model=args.model, max_output_tokens=retry_tokens)
        text = extract_text_from_gemini_response(response)
        parsed = try_parse_json_text(text)

    out_response_json_file.write_text(json.dumps(response, indent=2, ensure_ascii=True), encoding="utf-8")
    out_response_file.write_text(text, encoding="utf-8")
    if parsed is not None:
        if not isinstance(parsed, dict):
            raise RuntimeError("Parsed model output must be a JSON object.")
        out_structured_file.write_text(json.dumps(parsed, indent=2, ensure_ascii=True), encoding="utf-8")
        rendered = render_weekly_readme(parsed)
        out_readme_file.write_text(rendered, encoding="utf-8")
        print(f"Saved: {out_structured_file}")
        print(f"Saved: {out_readme_file}")

    else:
        print("Warning: model output was not valid JSON text.")
    print(f"Saved: {out_response_file}")
    print(f"Saved: {out_response_json_file}")


if __name__ == "__main__":
    main()
