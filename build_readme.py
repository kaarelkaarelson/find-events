#!/usr/bin/env python3
"""Build local awesome events README from evaluate run output."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"
RUNS_DIR = DATA_DIR / "evaluate_runs"
LOCAL_PREVIEW_README = DATA_DIR / "awesome_events_README.md"


def latest_run_dir() -> Path:
    if not RUNS_DIR.exists():
        raise RuntimeError(f"Missing runs directory: {RUNS_DIR}")
    dirs = [p for p in RUNS_DIR.iterdir() if p.is_dir()]
    if not dirs:
        raise RuntimeError(f"No run directories found in: {RUNS_DIR}")
    return sorted(dirs, key=lambda p: p.name)[-1]


def render_weekly_readme(structured: dict[str, Any], run_id: str) -> str:
    weeks = structured.get("weeks", [])
    if not isinstance(weeks, list):
        raise RuntimeError("Invalid structured data: missing weeks array")

    lines: list[str] = []
    lines.append("# Awesome SF Events")
    lines.append("")
    lines.append(
        f"High-signal weekly picks for SF/Bay Area builders. Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."
    )
    lines.append(f"Source run: `{run_id}`")
    lines.append("")
    lines.append("Format: top 5 events per week for the next 4 weeks.")
    lines.append("")

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

    run_dir = latest_run_dir() if args.run_dir == "latest" else Path(args.run_dir).expanduser().resolve()
    local_readme, local_snapshot = build_local_readme(run_dir=run_dir)
    print(f"Saved local README: {local_readme}")
    print(f"Saved run snapshot: {local_snapshot}")


if __name__ == "__main__":
    main()
