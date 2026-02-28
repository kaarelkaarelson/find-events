#!/usr/bin/env python3
"""Build an LLM prompt by injecting all event source files from ./data."""

from __future__ import annotations

import argparse
import json
import os
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
    for path in sorted(DATA_DIR.iterdir()):
        if not path.is_file():
            continue
        if path.name in SKIP_FILES:
            continue
        if path.name.startswith("evaluate_events_"):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        sources.append((path.name, text))
    return sources


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
        "- Maximize quality of people, network upside, and relevance to tech/AI/startups.\n"
        "- Penalize low-signal, generic, or poorly-specified events.\n"
        "- Include concise reasoning for each selected event.\n"
        "\n"
        "Output format (STRICT):\n"
        "- Return ONLY valid JSON.\n"
        "- No markdown, no prose outside JSON.\n"
        "- Use this shape exactly:\n"
        "{\n"
        '  "weeks": [\n'
        "    {\n"
        '      "week_label": "Week 1",\n'
        '      "week_start": "YYYY-MM-DD",\n'
        '      "week_end": "YYYY-MM-DD",\n'
        '      "events": [\n'
        "        {\n"
        '          "title": "string",\n'
        '          "date": "ISO date/time string or best available",\n'
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
                                            "title": {"type": "STRING"},
                                            "date": {"type": "STRING"},
                                            "location": {"type": "STRING"},
                                            "reason": {"type": "STRING"},
                                            "link": {"type": "STRING"},
                                        },
                                        "required": ["title", "date", "location", "reason", "link"],
                                    },
                                },
                            },
                            "required": ["week_label", "week_start", "week_end", "events"],
                        },
                    },
                },
                "required": ["weeks"],
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
    lines.append(
        f"High-signal weekly event picks for SF/Bay Area builders. Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."
    )
    lines.append("")
    lines.append("Selection format: top 5 events per week for the next 4 weeks.")
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
    args = parser.parse_args()

    load_dotenv(PROJECT_ROOT / ".env")
    sources = load_sources()
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
