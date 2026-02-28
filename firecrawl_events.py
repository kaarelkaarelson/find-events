"""Fetch Cerebral Valley events through Firecrawl.

Usage:
  # Option A: set env var
  export FIRECRAWL_API_KEY=fc-...
  # Option B: put FIRECRAWL_API_KEY=... in .env
  python3 firecrawl_events.py
"""

from __future__ import annotations

import json
import os
import re
import sys
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


FIRECRAWL_API_URL = "https://api.firecrawl.dev/v2/scrape"
TARGET_URL = "https://cerebralvalley.ai/events?locations=BAY_AREA"


MONTH_TOKEN_RE = re.compile(r"^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\d{1,2}$")
LINK_RE = re.compile(r"^(?:-\s*)?\[(?:\*\*)?(.*?)(?:\*\*)?\]\((https?://[^)]+)\)$")


def firecrawl_scrape_events(
    url: str = TARGET_URL,
    api_key: str | None = None,
    timeout: int = 90,
) -> dict[str, Any]:
    """Return structured events parsed from Firecrawl markdown output."""

    key = api_key or os.environ.get("FIRECRAWL_API_KEY")
    if not key:
        raise ValueError("Missing API key. Set FIRECRAWL_API_KEY or pass api_key.")

    normalized_url = url if url.startswith(("http://", "https://")) else f"https://{url}"

    payload = {
        "url": normalized_url,
        "maxAge": 0,
        "formats": ["markdown"],
    }

    request = Request(
        FIRECRAWL_API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )

    try:
        with urlopen(request, timeout=timeout) as response:
            body = response.read().decode("utf-8", errors="replace")
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Firecrawl HTTP {exc.code}: {detail}") from exc
    except URLError as exc:
        raise RuntimeError(f"Firecrawl request failed: {exc}") from exc

    data = json.loads(body)
    if not data.get("success"):
        raise RuntimeError(f"Firecrawl returned success=false: {data}")

    markdown = data.get("data", {}).get("markdown")
    if not isinstance(markdown, str) or not markdown.strip():
        raise RuntimeError(f"No markdown found in Firecrawl response: {data}")

    events = parse_events_from_markdown(markdown)
    return {"events": events}


def parse_events_from_markdown(markdown: str) -> list[dict[str, str]]:
    """Parse event cards from markdown scraped from the Cerebral Valley events page."""

    lines = [line.strip() for line in markdown.splitlines() if line.strip()]
    events: list[dict[str, str]] = []
    current_date_token: str | None = None

    i = 0
    while i < len(lines):
        line = lines[i]

        if MONTH_TOKEN_RE.match(line):
            current_date_token = line
            i += 1
            continue

        link_match = LINK_RE.match(line)
        if not link_match:
            i += 1
            continue

        title = link_match.group(1)
        url = link_match.group(2)
        date = current_date_token or ""
        location = ""
        description = ""

        j = i + 1
        # Find first location-like line near the event heading.
        while j < min(i + 12, len(lines)):
            candidate = lines[j]
            if LINK_RE.match(candidate) or MONTH_TOKEN_RE.match(candidate):
                break
            if "," in candidate and ("CA" in candidate or "San Francisco" in candidate or "Bay Area" in candidate):
                location = candidate
                break
            j += 1

        # Find a descriptive sentence after heading metadata.
        j = i + 1
        while j < min(i + 30, len(lines)):
            candidate = lines[j]
            if LINK_RE.match(candidate) or MONTH_TOKEN_RE.match(candidate):
                break
            if len(candidate) > 80 and "[" not in candidate and "](" not in candidate:
                description = candidate
                break
            j += 1

        events.append(
            {
                "title": title,
                "date": date,
                "location": location,
                "url": url,
                "description": description,
            }
        )
        i += 1

    # Deduplicate by URL while preserving order.
    seen_urls: set[str] = set()
    deduped: list[dict[str, str]] = []
    for event in events:
        if event["url"] in seen_urls:
            continue
        seen_urls.add(event["url"])
        deduped.append(event)
    return deduped


def load_dotenv(path: str = ".env") -> None:
    """Load KEY=VALUE pairs from .env into environment if not already set."""
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as file:
        for raw in file:
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip("'").strip('"')
            if key and key not in os.environ:
                os.environ[key] = value


def main() -> int:
    try:
        load_dotenv()
        result = firecrawl_scrape_events()
    except Exception as exc:  # pragma: no cover - CLI path
        print(str(exc), file=sys.stderr)
        return 1

    print(json.dumps(result, indent=2, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
