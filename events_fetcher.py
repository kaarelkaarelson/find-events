"""Simple helper for fetching Cerebral Valley event data."""

from __future__ import annotations

import argparse
import json
import re
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen


BASE_URL = "https://cerebralvalley.ai/events"


def fetch_cerebral_valley_events(location: str = "BAY_AREA", timeout: int = 15) -> Any:
    """Fetch events page data for a given location.

    Returns parsed JSON from the page when available. If no embedded JSON is
    found, returns the raw HTML string.
    """

    query = urlencode({"locations": location})
    url = f"{BASE_URL}?{query}"

    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(request, timeout=timeout) as response:
        content_type = response.headers.get("Content-Type", "")
        body = response.read().decode("utf-8", errors="replace")

    if "Vercel Security Checkpoint" in body:
        raise RuntimeError(
            "Blocked by Vercel Security Checkpoint. Fetch with a real browser "
            "session (or browser automation) and pass those session cookies."
        )

    if "application/json" in content_type:
        return json.loads(body)

    match = re.search(
        r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',
        body,
        re.DOTALL,
    )
    if match:
        payload = json.loads(match.group(1))
        page_props = payload.get("props", {}).get("pageProps")
        return page_props if page_props is not None else payload

    return body


def extract_events(data: Any) -> list[dict[str, Any]]:
    """Extract the most likely events list from nested page data."""
    if isinstance(data, list) and all(isinstance(item, dict) for item in data):
        return data
    if not isinstance(data, dict):
        return []

    key_candidates = ("events", "allEvents", "upcomingEvents", "items")
    for key in key_candidates:
        value = data.get(key)
        if isinstance(value, list) and all(isinstance(item, dict) for item in value):
            return value

    def walk(node: Any) -> list[list[dict[str, Any]]]:
        found: list[list[dict[str, Any]]] = []
        if isinstance(node, dict):
            for value in node.values():
                found.extend(walk(value))
        elif isinstance(node, list):
            if node and all(isinstance(item, dict) for item in node):
                found.append(node)
            for value in node:
                found.extend(walk(value))
        return found

    candidates = walk(data)
    if not candidates:
        return []

    event_like_fields = {"title", "name", "eventName", "date", "startDate", "url", "link"}

    def score(events: list[dict[str, Any]]) -> tuple[int, int]:
        match_count = 0
        for event in events:
            if any(field in event for field in event_like_fields):
                match_count += 1
        return (match_count, len(events))

    return max(candidates, key=score)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch Cerebral Valley events.")
    parser.add_argument("--location", default="BAY_AREA", help="Location filter value")
    parser.add_argument("--timeout", type=int, default=15, help="Request timeout in seconds")
    parser.add_argument(
        "--raw",
        action="store_true",
        help="Print full raw parsed payload instead of just extracted events",
    )
    args = parser.parse_args()

    try:
        data = fetch_cerebral_valley_events(location=args.location, timeout=args.timeout)
    except RuntimeError as exc:
        print(str(exc))
        raise SystemExit(1)
    if args.raw:
        print(json.dumps(data, indent=2, ensure_ascii=True))
    else:
        events = extract_events(data)
        print(json.dumps(events, indent=2, ensure_ascii=True))
