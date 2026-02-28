#!/usr/bin/env python3
"""Build local awesome events README from evaluate run output."""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse, urlunparse

from zoneinfo import ZoneInfo


PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"
RUNS_DIR = DATA_DIR / "evaluate_runs"
LOCAL_PREVIEW_README = DATA_DIR / "awesome_events_README.md"


def normalize_event_url(url: str) -> str:
    raw = (url or "").strip()
    if not raw:
        return ""
    try:
        parsed = urlparse(raw)
        # Strip query/fragment for stable matching across tracking params.
        normalized = urlunparse((parsed.scheme, parsed.netloc, parsed.path.rstrip("/"), "", "", ""))
        return normalized.lower()
    except Exception:
        return raw.lower()


def _extract_event_like_nodes(node: Any, out: list[dict[str, Any]]) -> None:
    if isinstance(node, dict):
        has_url = isinstance(node.get("url"), str) and node.get("url")
        has_time = any(isinstance(node.get(k), str) and node.get(k) for k in ("start_at", "end_at", "date", "end_date"))
        if has_url and has_time:
            out.append(node)
        for value in node.values():
            _extract_event_like_nodes(value, out)
    elif isinstance(node, list):
        for item in node:
            _extract_event_like_nodes(item, out)


def load_source_time_overrides() -> dict[str, dict[str, str]]:
    """Build url->time/location map from raw data sources to correct LLM date drift."""
    overrides: dict[str, dict[str, str]] = {}
    if not DATA_DIR.exists():
        return overrides

    for path in sorted(DATA_DIR.iterdir()):
        if not path.is_file() or not path.name.endswith(".json"):
            continue
        if path.name.startswith("evaluate_") or path.name.startswith("awesome_events_"):
            continue
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue

        nodes: list[dict[str, Any]] = []
        _extract_event_like_nodes(payload, nodes)
        for item in nodes:
            link = normalize_event_url(str(item.get("url", "")))
            if not link:
                continue
            start = str(item.get("start_at") or item.get("date") or "").strip()
            end = str(item.get("end_at") or item.get("end_date") or "").strip()
            loc = str(item.get("location") or "").strip()
            if not start and not end and not loc:
                continue
            overrides[link] = {
                "date": start,
                "end_date": end,
                "location": loc,
            }
    return overrides


def latest_run_dir() -> Path:
    if not RUNS_DIR.exists():
        raise RuntimeError(f"Missing runs directory: {RUNS_DIR}")
    dirs = [p for p in RUNS_DIR.iterdir() if p.is_dir()]
    if not dirs:
        raise RuntimeError(f"No run directories found in: {RUNS_DIR}")
    return sorted(dirs, key=lambda p: p.name)[-1]


def latest_valid_weekly_run_dir() -> Path:
    """Find newest run with parseable structured JSON containing weeks array."""
    if not RUNS_DIR.exists():
        raise RuntimeError(f"Missing runs directory: {RUNS_DIR}")
    dirs = sorted([p for p in RUNS_DIR.iterdir() if p.is_dir()], key=lambda p: p.name, reverse=True)
    for run_dir in dirs:
        structured_path = run_dir / "evaluate_events_structured.json"
        if not structured_path.exists():
            continue
        try:
            payload = json.loads(structured_path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if isinstance(payload, dict) and isinstance(payload.get("weeks"), list):
            return run_dir
    raise RuntimeError("No valid run with structured weekly JSON found.")


def render_weekly_readme(structured: dict[str, Any], run_id: str) -> str:
    time_overrides = load_source_time_overrides()
    top_3_picks = structured.get("top_3_picks", [])
    if not isinstance(top_3_picks, list):
        top_3_picks = []

    weeks = structured.get("weeks", [])
    if not isinstance(weeks, list):
        raise RuntimeError("Invalid structured data: missing weeks array")

    def sanitize_text(value: str) -> str:
        text = (value or "").strip()
        # Strip renderer-style metadata fragments if they leak into source text.
        text = re.sub(r"\s*\{#[^}]+\}", "", text)
        text = re.sub(r"\s*data-source-line=\"[^\"]+\"", "", text)
        return text.strip()

    def sanitize_title(value: str) -> str:
        text = sanitize_text(value)
        # Remove corrupted/combining unicode artifacts from model output.
        text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
        text = re.sub(r"\bRenssance\b", "Renaissance", text, flags=re.IGNORECASE)
        return re.sub(r"\s+", " ", text).strip()

    def _clean_leading_zero(s: str) -> str:
        # Make day/hour look natural: "Mar 07" -> "Mar 7", "09:00" -> "9:00"
        text = s.replace(" 0", " ")
        # Also handle start-of-string hours from "%I" (e.g. "09:00 AM").
        return re.sub(r"^0(\d:)", r"\1", text)

    def format_date_human(value: str) -> str:
        raw = (value or "").strip()
        if not raw:
            return "TBD"
        try:
            iso = raw.replace("Z", "+00:00")
            dt = datetime.fromisoformat(iso)
            if dt.tzinfo is None:
                # If timezone is missing, treat source value as local Pacific time.
                dt = dt.replace(tzinfo=ZoneInfo("America/Los_Angeles"))
            dt_local = dt.astimezone(ZoneInfo("America/Los_Angeles"))
            label = dt_local.strftime("%a, %b %d at %I:%M %p").strip()
            return _clean_leading_zero(label)
        except Exception:
            return raw

    def format_when_range(start_value: str, end_value: str) -> str:
        start_raw = (start_value or "").strip()
        if not start_raw:
            return "TBD"
        # Weekly view keeps only start time for clean scanning.
        return format_date_human(start_raw)

    def format_when_compact(start_value: str) -> str:
        raw = (start_value or "").strip()
        if not raw:
            return "TBD"
        try:
            dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
            if dt.tzinfo is None:
                # If timezone is missing, treat source value as local Pacific time.
                dt = dt.replace(tzinfo=ZoneInfo("America/Los_Angeles"))
            local = dt.astimezone(ZoneInfo("America/Los_Angeles"))
            return _clean_leading_zero(local.strftime("%a, %b %d at %I:%M %p"))
        except Exception:
            return raw

    def format_week_range(start: str, end: str) -> str:
        s = (start or "").strip()
        e = (end or "").strip()
        if not s or not e:
            return f"{s} to {e}".strip()
        try:
            ds = datetime.fromisoformat(s)
            de = datetime.fromisoformat(e)
            text = f"{ds.strftime('%b %d')} to {de.strftime('%b %d')}"
            return _clean_leading_zero(text)
        except Exception:
            return f"{s} to {e}"

    lines: list[str] = []
    lines.append("# Awesome SF Events")
    lines.append("")
    lines.append("High Signal Weekly Picks for SF Bay Area Builders.")
    lines.append(f"Updated: `{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}`.")
    lines.append("")

    if top_3_picks:
        lines.append("## Top Picks for March")
        lines.append("")
        for idx, event in enumerate(top_3_picks[:3], start=1):
            if not isinstance(event, dict):
                continue
            title = sanitize_title(str(event.get("title", "")))
            date_value = sanitize_text(str(event.get("date", "")))
            end_date_value = sanitize_text(str(event.get("end_date", "")))
            location = sanitize_text(str(event.get("location", "")))
            link = sanitize_text(str(event.get("link", "")))

            override = time_overrides.get(normalize_event_url(link), {})
            if isinstance(override, dict):
                date_value = sanitize_text(str(override.get("date") or date_value))
                end_date_value = sanitize_text(str(override.get("end_date") or end_date_value))
                if override.get("location"):
                    location = sanitize_text(str(override.get("location")))

            when_compact = format_when_compact(date_value)

            stars = "⭐" * max(1, 4 - idx)
            title_text = f"{stars} **{title}**"
            if link:
                lines.append(f"{title_text} — **[Sign up ->]({link})**")
                lines.append(f"`{when_compact} | {location}`")
            else:
                lines.append(title_text)
                lines.append(f"`{when_compact} | {location}`")
            lines.append("")
        lines.append("")
        lines.append("---")
        lines.append("")

    for week in weeks:
        if not isinstance(week, dict):
            continue
        label = sanitize_text(str(week.get("week_label", "Week")))
        start = str(week.get("week_start", ""))
        end = str(week.get("week_end", ""))
        lines.append(f"## {label} — {format_week_range(start, end)}")
        lines.append("")

        events = week.get("events", [])
        if not isinstance(events, list):
            events = []
        else:
            # Prefer model-provided weekly signal ranking if available.
            ranked = [e for e in events if isinstance(e, dict) and isinstance(e.get("rank_in_week"), int)]
            if len(ranked) == len(events):
                events = sorted(events, key=lambda e: int(e.get("rank_in_week", 999)))

        for idx, event in enumerate(events, start=1):
            if not isinstance(event, dict):
                continue
            title = sanitize_title(str(event.get("title", "")))
            date_value = sanitize_text(str(event.get("date", "")))
            end_date_value = sanitize_text(str(event.get("end_date", "")))
            location = sanitize_text(str(event.get("location", "")))
            reason = sanitize_text(str(event.get("reason", "")))
            link = sanitize_text(str(event.get("link", "")))

            override = time_overrides.get(normalize_event_url(link), {})
            if isinstance(override, dict):
                date_value = sanitize_text(str(override.get("date") or date_value))
                end_date_value = sanitize_text(str(override.get("end_date") or end_date_value))
                if override.get("location"):
                    location = sanitize_text(str(override.get("location")))

            when_where = f"{format_when_range(date_value, end_date_value)} | {location}"

            if link:
                lines.append(f"{idx}. **{title}** — **[Sign up ->]({link})**")
                lines.append(f"   `{when_where}`")
            else:
                lines.append(f"{idx}. **{title}**")
                lines.append(f"   `{when_where}`")
            lines.append(f"   {reason}")
            lines.append("")

        lines.append("---")
        lines.append("")

    return "\n".join(lines).strip() + "\n"


def build_local_readme(run_dir: Path) -> tuple[Path, Path]:
    """Build local README + run snapshot from a run directory."""
    structured_path = run_dir / "evaluate_events_structured.json"
    if not structured_path.exists():
        raise RuntimeError(f"Missing structured file in run: {structured_path}")

    structured = json.loads(structured_path.read_text(encoding="utf-8"))
    if not isinstance(structured, dict):
        raise RuntimeError("Structured payload must be a JSON object.")

    run_id = run_dir.name
    markdown = render_weekly_readme(structured=structured, run_id=run_id)

    LOCAL_PREVIEW_README.write_text(markdown, encoding="utf-8")
    local_snapshot = run_dir / "awesome_readme_published.md"
    local_snapshot.write_text(markdown, encoding="utf-8")
    return (LOCAL_PREVIEW_README, local_snapshot)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build local README from latest evaluate run.")
    parser.add_argument(
        "--run-dir",
        default="latest",
        help="Run dir path or 'latest' (default)",
    )
    args = parser.parse_args()

    if args.run_dir == "latest":
        run_dir = latest_run_dir()
        try:
            # Validate latest; fallback to newest valid weekly run if malformed.
            _ = json.loads((run_dir / "evaluate_events_structured.json").read_text(encoding="utf-8"))
        except Exception:
            run_dir = latest_valid_weekly_run_dir()
    else:
        run_dir = Path(args.run_dir).expanduser().resolve()
    local_readme, local_snapshot = build_local_readme(run_dir=run_dir)
    print(f"Saved local README: {local_readme}")
    print(f"Saved run snapshot: {local_snapshot}")


if __name__ == "__main__":
    main()
