"""Simple helper for fetching Cerebral Valley event data."""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Any
from urllib.parse import urlencode
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


BASE_URL = "https://cerebralvalley.ai/events"
LUMA_EVENTS_URL = "https://api2.luma.com/home/get-events"
LUMA_DISCOVER_EVENTS_URL = "https://api2.luma.com/discover/get-paginated-events"
LUMA_SF_DISCOVER_PLACE_API_ID = "discplace-BDj7GNbGlsF7Cka"
LUMA_GENAI_SF_URL = "https://luma.com/genai-sf"
LUMA_TECH_URL = "https://luma.com/tech"
LUMA_AI_URL = "https://luma.com/ai"
LUMA_TECH_SLUG = "tech"
LUMA_AI_SLUG = "ai"
LUMA_SF_LATITUDE = 37.77493
LUMA_SF_LONGITUDE = -122.41942


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


def _paginate_all_luma_pages(fetch_page_fn: Any) -> dict[str, Any]:
    """Fetch all cursor pages from a Luma paginated endpoint."""
    first_page = fetch_page_fn(None)
    all_entries = list(first_page.get("entries", []))
    next_cursor = first_page.get("next_cursor")
    has_more = bool(first_page.get("has_more"))
    pages = 1
    seen_cursors: set[str] = set()

    while has_more and next_cursor:
        cursor = str(next_cursor)
        if cursor in seen_cursors:
            break
        seen_cursors.add(cursor)
        page = fetch_page_fn(cursor)
        all_entries.extend(page.get("entries", []))
        next_cursor = page.get("next_cursor")
        has_more = bool(page.get("has_more"))
        pages += 1

    result = dict(first_page)
    result["entries"] = all_entries
    result["has_more"] = has_more
    result["next_cursor"] = next_cursor
    result["pages_fetched"] = pages
    return result


def fetch_luma_me_page_events(
    period: str = "future",
    timeout: int = 20,
    cookie: str | None = None,
) -> dict[str, Any]:
    """Fetch events from Luma 'me/home page' events API."""
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0",
        "Origin": "https://luma.com",
        "Referer": "https://luma.com/",
        "x-luma-client-type": "luma-web",
    }

    cookie_value = cookie or os.environ.get("LUMA_COOKIE")
    if cookie_value:
        headers["Cookie"] = cookie_value

    def fetch_page(cursor: str | None = None) -> dict[str, Any]:
        params: dict[str, Any] = {"period": period}
        if cursor:
            params["pagination_cursor"] = cursor
        query = urlencode(params)
        url = f"{LUMA_EVENTS_URL}?{query}"
        request = Request(url, headers=headers, method="GET")
        try:
            with urlopen(request, timeout=timeout) as response:
                body = response.read().decode("utf-8", errors="replace")
        except HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Luma HTTP {exc.code}: {detail}") from exc
        except URLError as exc:
            raise RuntimeError(f"Luma request failed: {exc}") from exc

        data = json.loads(body)
        if not isinstance(data, dict):
            raise RuntimeError("Unexpected Luma response format: expected JSON object.")
        return data

    return _paginate_all_luma_pages(fetch_page)


def fetch_luma_sf_events(
    discover_place_api_id: str = LUMA_SF_DISCOVER_PLACE_API_ID,
    timeout: int = 20,
    cookie: str | None = None,
) -> dict[str, Any]:
    """Fetch events from Luma SF discover page API."""
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0",
        "Origin": "https://luma.com",
        "Referer": "https://luma.com/",
        "x-luma-client-type": "luma-web",
        "x-luma-web-url": "https://luma.com/sf",
    }

    client_version = os.environ.get("LUMA_CLIENT_VERSION")
    if client_version:
        headers["x-luma-client-version"] = client_version

    cookie_value = cookie or os.environ.get("LUMA_COOKIE")
    if cookie_value:
        headers["Cookie"] = cookie_value

    def fetch_page(cursor: str | None = None) -> dict[str, Any]:
        params: dict[str, Any] = {
            "discover_place_api_id": discover_place_api_id,
        }
        if cursor:
            params["pagination_cursor"] = cursor
        query = urlencode(params)
        url = f"{LUMA_DISCOVER_EVENTS_URL}?{query}"
        request = Request(url, headers=headers, method="GET")
        try:
            with urlopen(request, timeout=timeout) as response:
                body = response.read().decode("utf-8", errors="replace")
        except HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Luma SF HTTP {exc.code}: {detail}") from exc
        except URLError as exc:
            raise RuntimeError(f"Luma SF request failed: {exc}") from exc

        data = json.loads(body)
        if not isinstance(data, dict):
            raise RuntimeError("Unexpected Luma SF response format: expected JSON object.")
        return data

    return _paginate_all_luma_pages(fetch_page)


def fetch_luma_discover_events(
    discover_place_api_id: str,
    web_url: str,
    timeout: int = 20,
    cookie: str | None = None,
) -> dict[str, Any]:
    """Fetch events from a generic Luma discover page API."""
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0",
        "Origin": "https://luma.com",
        "Referer": "https://luma.com/",
        "x-luma-client-type": "luma-web",
        "x-luma-web-url": web_url,
    }

    client_version = os.environ.get("LUMA_CLIENT_VERSION")
    if client_version:
        headers["x-luma-client-version"] = client_version

    cookie_value = cookie or os.environ.get("LUMA_COOKIE")
    if cookie_value:
        headers["Cookie"] = cookie_value

    def fetch_page(cursor: str | None = None) -> dict[str, Any]:
        params: dict[str, Any] = {
            "discover_place_api_id": discover_place_api_id,
        }
        if cursor:
            params["pagination_cursor"] = cursor
        query = urlencode(params)
        url = f"{LUMA_DISCOVER_EVENTS_URL}?{query}"
        request = Request(url, headers=headers, method="GET")
        try:
            with urlopen(request, timeout=timeout) as response:
                body = response.read().decode("utf-8", errors="replace")
        except HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Luma discover HTTP {exc.code}: {detail}") from exc
        except URLError as exc:
            raise RuntimeError(f"Luma discover request failed: {exc}") from exc

        data = json.loads(body)
        if not isinstance(data, dict):
            raise RuntimeError("Unexpected Luma discover response format: expected JSON object.")
        return data

    return _paginate_all_luma_pages(fetch_page)


def resolve_luma_discover_place_api_id(
    page_url: str,
    timeout: int = 20,
    cookie: str | None = None,
) -> str:
    """Resolve discover_place_api_id from a Luma discover page HTML."""
    headers = {"User-Agent": "Mozilla/5.0", "Accept": "text/html"}
    cookie_value = cookie or os.environ.get("LUMA_COOKIE")
    if cookie_value:
        headers["Cookie"] = cookie_value

    request = Request(page_url, headers=headers, method="GET")
    try:
        with urlopen(request, timeout=timeout) as response:
            html = response.read().decode("utf-8", errors="replace")
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Luma page HTTP {exc.code}: {detail}") from exc
    except URLError as exc:
        raise RuntimeError(f"Luma page request failed: {exc}") from exc

    match = re.search(r"(discplace-[A-Za-z0-9]+)", html)
    if not match:
        raise RuntimeError("Could not find discover_place_api_id in page HTML.")
    return match.group(1)


def fetch_luma_genai_sf_events(
    page_url: str = LUMA_GENAI_SF_URL,
    discover_place_api_id: str | None = None,
    timeout: int = 20,
    cookie: str | None = None,
) -> dict[str, Any]:
    """Fetch events from Luma GenAI SF discover page."""
    place_id = discover_place_api_id or resolve_luma_discover_place_api_id(
        page_url=page_url, timeout=timeout, cookie=cookie
    )
    return fetch_luma_discover_events(
        discover_place_api_id=place_id,
        web_url=page_url,
        timeout=timeout,
        cookie=cookie,
    )


def fetch_luma_tech_events(
    slug: str = LUMA_TECH_SLUG,
    latitude: float = LUMA_SF_LATITUDE,
    longitude: float = LUMA_SF_LONGITUDE,
    timeout: int = 20,
    cookie: str | None = None,
) -> dict[str, Any]:
    """Fetch events from Luma discover taxonomy endpoint (e.g., /tech)."""
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0",
        "Origin": "https://luma.com",
        "Referer": "https://luma.com/",
        "x-luma-client-type": "luma-web",
        "x-luma-web-url": f"https://luma.com/{slug}",
    }

    client_version = os.environ.get("LUMA_CLIENT_VERSION")
    if client_version:
        headers["x-luma-client-version"] = client_version

    cookie_value = cookie or os.environ.get("LUMA_COOKIE")
    if cookie_value:
        headers["Cookie"] = cookie_value

    def fetch_page(cursor: str | None = None) -> dict[str, Any]:
        params: dict[str, Any] = {
            "slug": slug,
            "latitude": latitude,
            "longitude": longitude,
        }
        if cursor:
            params["pagination_cursor"] = cursor
        query = urlencode(params)
        url = f"{LUMA_DISCOVER_EVENTS_URL}?{query}"
        request = Request(url, headers=headers, method="GET")
        try:
            with urlopen(request, timeout=timeout) as response:
                body = response.read().decode("utf-8", errors="replace")
        except HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Luma tech HTTP {exc.code}: {detail}") from exc
        except URLError as exc:
            raise RuntimeError(f"Luma tech request failed: {exc}") from exc

        data = json.loads(body)
        if not isinstance(data, dict):
            raise RuntimeError("Unexpected Luma tech response format: expected JSON object.")
        return data

    return _paginate_all_luma_pages(fetch_page)


def fetch_luma_ai_events(
    slug: str = LUMA_AI_SLUG,
    latitude: float = LUMA_SF_LATITUDE,
    longitude: float = LUMA_SF_LONGITUDE,
    timeout: int = 20,
    cookie: str | None = None,
) -> dict[str, Any]:
    """Fetch events from Luma discover taxonomy endpoint for AI."""
    return fetch_luma_tech_events(
        slug=slug,
        latitude=latitude,
        longitude=longitude,
        timeout=timeout,
        cookie=cookie,
    )


def fetch_luma_category_page_data(
    page_url: str,
    timeout: int = 20,
    cookie: str | None = None,
) -> dict[str, Any]:
    """Fetch Luma category page and return initialData payload from __NEXT_DATA__."""
    headers = {"User-Agent": "Mozilla/5.0", "Accept": "text/html"}
    cookie_value = cookie or os.environ.get("LUMA_COOKIE")
    if cookie_value:
        headers["Cookie"] = cookie_value

    request = Request(page_url, headers=headers, method="GET")
    try:
        with urlopen(request, timeout=timeout) as response:
            html = response.read().decode("utf-8", errors="replace")
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Luma page HTTP {exc.code}: {detail}") from exc
    except URLError as exc:
        raise RuntimeError(f"Luma page request failed: {exc}") from exc

    match = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html, re.DOTALL)
    if not match:
        raise RuntimeError("Could not find __NEXT_DATA__ in category page HTML.")

    payload = json.loads(match.group(1))
    initial_data = payload.get("props", {}).get("pageProps", {}).get("initialData", {}).get("data")
    if not isinstance(initial_data, dict):
        raise RuntimeError("Could not parse category initialData from __NEXT_DATA__.")
    return initial_data


def extract_luma_major_events_from_category_data(data: dict[str, Any]) -> list[dict[str, Any]]:
    """Extract 'Upcoming Major Events' calendars from Luma category page initialData."""
    timeline = data.get("timeline_calendars", [])
    if not isinstance(timeline, list):
        return []

    items: list[dict[str, Any]] = []
    for row in timeline:
        if not isinstance(row, dict):
            continue
        cal = row.get("calendar", {})
        if not isinstance(cal, dict):
            continue
        cal_slug = cal.get("slug", "")
        items.append(
            {
                "calendar_api_id": cal.get("api_id", ""),
                "calendar_name": cal.get("name", ""),
                "calendar_slug": cal_slug,
                "calendar_url": f"https://luma.com/{cal_slug}" if cal_slug else "",
                "event_count": row.get("event_count", 0),
                "subscriber_count": row.get("subscriber_count", 0),
                "start_at": row.get("start_at", ""),
                "end_at": row.get("end_at", ""),
                "geo_city": cal.get("geo_city", ""),
                "geo_country": cal.get("geo_country", ""),
            }
        )
    return items


def extract_luma_me_page_events(data: dict[str, Any]) -> list[dict[str, Any]]:
    """Normalize Luma me/home page entries to a compact event list."""
    entries = data.get("entries", [])
    if not isinstance(entries, list):
        return []

    events: list[dict[str, Any]] = []
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        event = entry.get("event", {})
        if not isinstance(event, dict):
            continue

        calendar = entry.get("calendar", {})
        calendar_slug = calendar.get("slug", "") if isinstance(calendar, dict) else ""
        featured_city = entry.get("featured_city", {})
        featured_city_slug = featured_city.get("slug", "") if isinstance(featured_city, dict) else ""
        hosts = entry.get("hosts", [])
        host_usernames = []
        if isinstance(hosts, list):
            for host in hosts:
                if isinstance(host, dict) and host.get("username"):
                    host_usernames.append(str(host["username"]))

        geo = event.get("geo_address_info", {})
        city = geo.get("city", "") if isinstance(geo, dict) else ""
        city_state = geo.get("city_state", "") if isinstance(geo, dict) else ""
        location = city_state or city or ""

        events.append(
            {
                "api_id": event.get("api_id", ""),
                "name": event.get("name", ""),
                "start_at": event.get("start_at", ""),
                "end_at": event.get("end_at", ""),
                "timezone": event.get("timezone", ""),
                "location": location,
                "location_type": event.get("location_type", ""),
                "url_slug": event.get("url", ""),
                "url": f"https://luma.com/{event.get('url', '')}" if event.get("url") else "",
                "calendar_slug": calendar_slug,
                "featured_city_slug": featured_city_slug,
                "host_usernames": host_usernames,
                "visibility": event.get("visibility", ""),
            }
        )
    return events


def extract_luma_sf_events(data: dict[str, Any]) -> list[dict[str, Any]]:
    """Normalize Luma SF discover entries to a compact event list."""
    return extract_luma_me_page_events(data)


def extract_luma_genai_sf_events(data: dict[str, Any]) -> list[dict[str, Any]]:
    """Normalize Luma GenAI SF discover entries to a compact event list."""
    return extract_luma_me_page_events(data)


def extract_luma_tech_events(data: dict[str, Any]) -> list[dict[str, Any]]:
    """Normalize Luma tech discover entries to a compact event list."""
    return extract_luma_me_page_events(data)


def extract_luma_tech_dataset(events_raw: dict[str, Any], major_raw: dict[str, Any]) -> dict[str, Any]:
    """Build combined tech payload with major events and nearby events."""
    return {
        "major_events": extract_luma_major_events_from_category_data(major_raw),
        "events": extract_luma_tech_events(events_raw),
    }


def extract_luma_ai_dataset(events_raw: dict[str, Any], major_raw: dict[str, Any]) -> dict[str, Any]:
    """Build combined AI payload with major events and nearby events."""
    return {
        "major_events": extract_luma_major_events_from_category_data(major_raw),
        "events": extract_luma_tech_events(events_raw),
    }


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


def save_cli_output(source: str, payload: Any, raw: bool) -> str:
    """Persist CLI output to data/<source>_(raw|events).json."""
    Path("data").mkdir(parents=True, exist_ok=True)
    suffix = "raw" if raw else "events"
    out_path = Path("data") / f"{source}_{suffix}.json"
    out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=True), encoding="utf-8")
    return str(out_path)


if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser(description="Fetch Cerebral Valley events.")
    parser.add_argument(
        "--source",
        default="cerebral",
        choices=("cerebral", "luma_me", "luma_sf", "luma_genai_sf", "luma_tech", "luma_tech_major", "luma_ai"),
        help="Which platform to fetch from",
    )
    parser.add_argument("--location", default="BAY_AREA", help="Cerebral Valley location filter value")
    parser.add_argument("--period", default="future", help="Luma period (e.g. future, past)")
    parser.add_argument("--timeout", type=int, default=15, help="Request timeout in seconds")
    parser.add_argument(
        "--raw",
        action="store_true",
        help="Print full raw payload instead of extracted events",
    )
    parser.add_argument(
        "--luma-cookie",
        default=None,
        help="Optional full Cookie header value for authenticated Luma requests",
    )
    parser.add_argument(
        "--discover-place-api-id",
        default=LUMA_SF_DISCOVER_PLACE_API_ID,
        help="Luma discover: discover place API id",
    )
    parser.add_argument(
        "--discover-page-url",
        default=LUMA_GENAI_SF_URL,
        help="Luma discover page URL (used by luma_genai_sf)",
    )
    parser.add_argument("--slug", default=LUMA_TECH_SLUG, help="Luma taxonomy slug (used by luma_tech)")
    parser.add_argument(
        "--category-page-url",
        default=LUMA_TECH_URL,
        help="Luma category page URL (used by luma_tech_major)",
    )
    args = parser.parse_args()
    tech_major_raw: dict[str, Any] | None = None
    ai_major_raw: dict[str, Any] | None = None

    try:
        if args.source == "luma_me":
            data = fetch_luma_me_page_events(
                period=args.period,
                timeout=args.timeout,
                cookie=args.luma_cookie,
            )
        elif args.source == "luma_sf":
            data = fetch_luma_discover_events(
                discover_place_api_id=args.discover_place_api_id,
                web_url="https://luma.com/sf",
                timeout=args.timeout,
                cookie=args.luma_cookie,
            )
        elif args.source == "luma_genai_sf":
            data = fetch_luma_genai_sf_events(
                page_url=args.discover_page_url,
                discover_place_api_id=args.discover_place_api_id,
                timeout=args.timeout,
                cookie=args.luma_cookie,
            )
        elif args.source == "luma_tech":
            data = fetch_luma_tech_events(
                slug=args.slug,
                latitude=LUMA_SF_LATITUDE,
                longitude=LUMA_SF_LONGITUDE,
                timeout=args.timeout,
                cookie=args.luma_cookie,
            )
            tech_major_raw = fetch_luma_category_page_data(
                page_url=LUMA_TECH_URL,
                timeout=args.timeout,
                cookie=args.luma_cookie,
            )
        elif args.source == "luma_tech_major":
            data = fetch_luma_category_page_data(
                page_url=args.category_page_url,
                timeout=args.timeout,
                cookie=args.luma_cookie,
            )
        elif args.source == "luma_ai":
            data = fetch_luma_ai_events(
                slug=LUMA_AI_SLUG,
                latitude=LUMA_SF_LATITUDE,
                longitude=LUMA_SF_LONGITUDE,
                timeout=args.timeout,
                cookie=args.luma_cookie,
            )
            ai_major_raw = fetch_luma_category_page_data(
                page_url=LUMA_AI_URL,
                timeout=args.timeout,
                cookie=args.luma_cookie,
            )
        else:
            data = fetch_cerebral_valley_events(location=args.location, timeout=args.timeout)
    except RuntimeError as exc:
        print(str(exc))
        raise SystemExit(1)

    if args.raw:
        if args.source == "luma_tech":
            output_payload = {
                "major_raw": tech_major_raw if tech_major_raw is not None else {},
                "events_raw": data,
            }
        elif args.source == "luma_ai":
            output_payload = {
                "major_raw": ai_major_raw if ai_major_raw is not None else {},
                "events_raw": data,
            }
        else:
            output_payload = data
    else:
        if args.source == "luma_me":
            output_payload = extract_luma_me_page_events(data)
        elif args.source == "luma_sf":
            output_payload = extract_luma_sf_events(data)
        elif args.source == "luma_genai_sf":
            output_payload = extract_luma_genai_sf_events(data)
        elif args.source == "luma_tech":
            output_payload = extract_luma_tech_dataset(
                events_raw=data,
                major_raw=tech_major_raw if tech_major_raw is not None else {},
            )
        elif args.source == "luma_ai":
            output_payload = extract_luma_ai_dataset(
                events_raw=data,
                major_raw=ai_major_raw if ai_major_raw is not None else {},
            )
        elif args.source == "luma_tech_major":
            output_payload = extract_luma_major_events_from_category_data(data)
        else:
            output_payload = extract_events(data)

    saved_path = save_cli_output(args.source, output_payload, raw=args.raw)
    print(json.dumps(output_payload, indent=2, ensure_ascii=True))
    print(f"Saved: {saved_path}")
