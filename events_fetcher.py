"""Simple helper for fetching Cerebral Valley event data."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import threading
import time
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
STANFORD_API_EVENTS_URL = "https://events.stanford.edu/api/2/events"
STANFORD_HAI_EVENTS_URL = "https://hai.stanford.edu/events"
STANFORD_MLSYS_URL = "https://mlsys.stanford.edu/"
PARTIFUL_DISCOVER_EVENTS_URL = "https://api.partiful.com/getDiscoverableEvents"
REQUEST_TIMEOUT_SECONDS = 15
STANFORD_DEFAULT_EXPERIENCE = "inperson"
STANFORD_DEFAULT_ORDER = "date"
STANFORD_DEFAULT_PP = 100
STANFORD_DEFAULT_EVENT_TYPE_IDS = [
    37952570034524,
    37952570044769,
    37952570025304,
    38406833071942,
    37952570040671,
    37952570047842,
    37952570036573,
    37952570042720,
    37952570027353,
    40864883971398,
    40490468118962,
]


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


def fetch_stanford_events(
    event_type_ids: list[int] | None = None,
    experience: str = STANFORD_DEFAULT_EXPERIENCE,
    order: str = STANFORD_DEFAULT_ORDER,
    timeout: int = 20,
) -> dict[str, Any]:
    """Fetch Stanford events from Localist API with automatic pagination."""
    ids = event_type_ids if event_type_ids is not None else STANFORD_DEFAULT_EVENT_TYPE_IDS
    headers = {"Accept": "application/json", "User-Agent": "Mozilla/5.0"}

    all_events: list[Any] = []
    page = 1
    total_pages = 1

    while page <= total_pages:
        params: dict[str, Any] = {
            "experience": experience,
            "order": order,
            "pp": STANFORD_DEFAULT_PP,
            "page": page,
            "event_types[]": ids,
        }
        url = f"{STANFORD_API_EVENTS_URL}?{urlencode(params, doseq=True)}"
        request = Request(url, headers=headers, method="GET")
        try:
            with urlopen(request, timeout=timeout) as response:
                body = response.read().decode("utf-8", errors="replace")
        except HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Stanford HTTP {exc.code}: {detail}") from exc
        except URLError as exc:
            raise RuntimeError(f"Stanford request failed: {exc}") from exc

        data = json.loads(body)
        if not isinstance(data, dict):
            raise RuntimeError("Unexpected Stanford response format: expected JSON object.")

        page_info = data.get("page", {})
        if not isinstance(page_info, dict):
            raise RuntimeError("Unexpected Stanford response: missing page metadata.")

        events = data.get("events", [])
        if not isinstance(events, list):
            raise RuntimeError("Unexpected Stanford response: events is not a list.")
        all_events.extend(events)

        total_pages = int(page_info.get("total", 1) or 1)
        page += 1

    return {
        "events": all_events,
        "page": {"current": 1, "size": STANFORD_DEFAULT_PP, "total": total_pages},
        "meta": {
            "fetched_pages": total_pages,
            "experience": experience,
            "order": order,
            "event_type_ids": ids,
        },
    }


def fetch_page_markdown_with_firecrawl(url: str, timeout: int = 30) -> str:
    """Fetch a page as markdown using Firecrawl v2 scrape API."""
    api_key = os.environ.get("FIRECRAWL_API_KEY")
    if not api_key:
        raise RuntimeError("Missing FIRECRAWL_API_KEY in environment/.env.")

    body = json.dumps({"url": url, "formats": ["markdown"]}).encode("utf-8")
    request = Request(
        "https://api.firecrawl.dev/v2/scrape",
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0",
        },
        method="POST",
    )
    try:
        with urlopen(request, timeout=timeout) as response:
            raw = response.read().decode("utf-8", errors="replace")
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Firecrawl HTTP {exc.code}: {detail}") from exc
    except URLError as exc:
        raise RuntimeError(f"Firecrawl request failed: {exc}") from exc

    data = json.loads(raw)
    if not isinstance(data, dict):
        raise RuntimeError("Unexpected Firecrawl response format: expected JSON object.")

    payload = data.get("data", {})
    if isinstance(payload, dict):
        markdown = payload.get("markdown")
        if isinstance(markdown, str) and markdown.strip():
            return markdown

    markdown = data.get("markdown")
    if isinstance(markdown, str) and markdown.strip():
        return markdown

    raise RuntimeError("Firecrawl response did not include markdown content.")


def _load_json_env(key: str, default: dict[str, Any]) -> dict[str, Any]:
    """Load a JSON object from environment variable or return default."""
    raw = os.environ.get(key)
    if not raw:
        return dict(default)
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid JSON in {key}: {exc}") from exc
    if not isinstance(parsed, dict):
        raise RuntimeError(f"{key} must be a JSON object.")
    return parsed


def fetch_partiful_discoverable_events(
    timeout: int = REQUEST_TIMEOUT_SECONDS,
    bearer_token: str | None = None,
    request_body: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Fetch discoverable events from Partiful API with optional pagination."""
    token = (
        bearer_token
        or os.environ.get("PARTIFUL_BEARER_TOKEN")
        or os.environ.get("PARTIFUL_AUTH_TOKEN")
    )
    if not token:
        raise RuntimeError("Missing PARTIFUL_BEARER_TOKEN (or PARTIFUL_AUTH_TOKEN) in environment/.env.")

    base_payload = request_body if request_body is not None else _load_json_env("PARTIFUL_DISCOVER_BODY", {})
    if not isinstance(base_payload, dict):
        raise RuntimeError("Partiful request body must be a JSON object.")

    headers = {
        "Accept": "*/*",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
        "Origin": "https://partiful.com",
        "Referer": "https://partiful.com/",
        "User-Agent": "Mozilla/5.0",
    }

    cursor_keys = ("cursor", "next_cursor", "nextCursor", "pagination_cursor", "paginationCursor")

    def find_next_cursor(payload: dict[str, Any]) -> str | None:
        for key in ("next_cursor", "nextCursor", "cursor", "pagination_cursor", "paginationCursor"):
            value = payload.get(key)
            if isinstance(value, str) and value:
                return value
        page = payload.get("page")
        if isinstance(page, dict):
            for key in ("next_cursor", "nextCursor", "cursor"):
                value = page.get(key)
                if isinstance(value, str) and value:
                    return value
        return None

    def find_has_more(payload: dict[str, Any], next_cursor: str | None) -> bool:
        for key in ("has_more", "hasMore"):
            value = payload.get(key)
            if isinstance(value, bool):
                return value
        if isinstance(payload.get("page"), dict):
            page = payload["page"]
            for key in ("has_more", "hasMore"):
                value = page.get(key)
                if isinstance(value, bool):
                    return value
        return bool(next_cursor)

    entries: list[Any] = []
    pages = 0
    cursor: str | None = None
    seen_cursors: set[str] = set()
    last_response: dict[str, Any] | None = None

    while True:
        payload = dict(base_payload)
        if cursor:
            chosen_key = next((k for k in cursor_keys if k in payload), "cursor")
            payload[chosen_key] = cursor

        body = json.dumps(payload).encode("utf-8")
        request = Request(PARTIFUL_DISCOVER_EVENTS_URL, data=body, headers=headers, method="POST")
        try:
            with urlopen(request, timeout=timeout) as response:
                raw = response.read().decode("utf-8", errors="replace")
        except HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Partiful HTTP {exc.code}: {detail}") from exc
        except URLError as exc:
            raise RuntimeError(f"Partiful request failed: {exc}") from exc

        data = json.loads(raw)
        if not isinstance(data, dict):
            raise RuntimeError("Unexpected Partiful response format: expected JSON object.")

        last_response = data
        page_entries = extract_events(data)
        entries.extend(page_entries)
        pages += 1

        next_cursor = find_next_cursor(data)
        has_more = find_has_more(data, next_cursor)
        if not has_more or not next_cursor:
            break
        if next_cursor in seen_cursors:
            break
        seen_cursors.add(next_cursor)
        cursor = next_cursor

    return {
        "events": entries,
        "meta": {
            "pages_fetched": pages,
            "response_has_more": find_has_more(last_response or {}, find_next_cursor(last_response or {})),
            "next_cursor": find_next_cursor(last_response or {}),
        },
        "raw": last_response if isinstance(last_response, dict) else {},
    }


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


def extract_stanford_events(data: dict[str, Any]) -> list[dict[str, Any]]:
    """Normalize Stanford Localist API events to a compact event list."""
    rows = data.get("events", [])
    if not isinstance(rows, list):
        return []

    items: list[dict[str, Any]] = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        event = row.get("event", {})
        if not isinstance(event, dict):
            continue

        instances = event.get("event_instances", [])
        start_at = ""
        end_at = ""
        all_day = False
        if isinstance(instances, list) and instances:
            first = instances[0].get("event_instance", {}) if isinstance(instances[0], dict) else {}
            if isinstance(first, dict):
                start_at = first.get("start", "") or ""
                end_at = first.get("end", "") or ""
                all_day = bool(first.get("all_day", False))

        geo = event.get("geo", {})
        city = geo.get("city", "") if isinstance(geo, dict) else ""
        state = geo.get("state", "") if isinstance(geo, dict) else ""
        country = geo.get("country", "") if isinstance(geo, dict) else ""
        location_parts = [p for p in [city, state, country] if p]

        items.append(
            {
                "id": event.get("id", ""),
                "title": event.get("title", ""),
                "start_at": start_at,
                "end_at": end_at,
                "all_day": all_day,
                "experience": event.get("experience", ""),
                "event_types": [
                    t.get("name", "")
                    for t in event.get("filters", {}).get("event_types", [])
                    if isinstance(t, dict)
                ]
                if isinstance(event.get("filters", {}), dict)
                else [],
                "location_name": event.get("location_name", "") or event.get("location", ""),
                "location": ", ".join(location_parts),
                "url": event.get("localist_url", ""),
                "url_slug": event.get("urlname", ""),
                "departments": [
                    d.get("name", "") for d in event.get("departments", []) if isinstance(d, dict)
                ],
            }
        )
    return items


def extract_partiful_events(data: dict[str, Any]) -> list[dict[str, Any]]:
    """Normalize Partiful API events to a compact event list."""
    rows = data.get("events", [])
    if not isinstance(rows, list):
        return []

    items: list[dict[str, Any]] = []
    for event in rows:
        if not isinstance(event, dict):
            continue
        event_id = event.get("id", "") or ""
        items.append(
            {
                "id": event_id,
                "title": event.get("title", "") or "",
                "start_at": event.get("startDate", "") or "",
                "end_at": event.get("endDate", "") or "",
                "timezone": event.get("timezone", "") or "",
                "status": event.get("status", "") or "",
                # Partiful discover payload does not always include canonical URL.
                "url": f"https://partiful.com/e/{event_id}" if event_id else "",
            }
        )
    return items


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


def save_cli_output(source: str, payload: Any, raw: bool) -> str | None:
    """Persist non-raw CLI output to data/. Raw mode does not write files."""
    if raw:
        return None

    Path("data").mkdir(parents=True, exist_ok=True)
    if isinstance(payload, str) and not raw:
        if source == "cv":
            out_path = Path("data") / "cv_events.md"
            out_path.write_text(payload, encoding="utf-8")
            return str(out_path)
        out_path = Path("data") / f"{source}_events.md"
        out_path.write_text(payload, encoding="utf-8")
        return str(out_path)

    suffix = "raw" if raw else "events"
    out_path = Path("data") / f"{source}_{suffix}.json"
    out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=True), encoding="utf-8")
    return str(out_path)


def run_with_spinner(label: str, fn: Any, enabled: bool = True) -> Any:
    """Run a blocking function while showing a simple CLI spinner."""
    if not enabled:
        return fn()

    frames = "|/-\\"
    stop = threading.Event()

    def spin() -> None:
        idx = 0
        while not stop.is_set():
            sys.stdout.write(f"\r[RUN] {label:<18} {frames[idx % len(frames)]}")
            sys.stdout.flush()
            idx += 1
            time.sleep(0.1)

    t = threading.Thread(target=spin, daemon=True)
    t.start()
    try:
        return fn()
    finally:
        stop.set()
        t.join(timeout=1.0)
        sys.stdout.write("\r")
        sys.stdout.flush()


if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser(description="Fetch Cerebral Valley events.")
    available_sources = (
        "cv",
        "partiful",
        "luma_me",
        "luma_sf",
        "luma_genai_sf",
        "luma_tech",
        "luma_tech_major",
        "luma_ai",
        "stanford",
        "stanford_mlsys",
        "stanford_hai",
    )
    parser.add_argument(
        "--source",
        default="all",
        choices=("all",) + available_sources,
        help="Which platform to fetch from; defaults to all",
    )
    parser.add_argument("--location", default="BAY_AREA", help="Cerebral Valley location filter value")
    parser.add_argument("--period", default="future", help="Luma period (e.g. future, past)")
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
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print full payload and detailed errors",
    )
    args = parser.parse_args()
    sources_to_run = available_sources if args.source == "all" else (args.source,)

    if args.source == "all":
        print("Sources:", ", ".join(sources_to_run))

    for source in sources_to_run:
        state: dict[str, Any] = {"tech_major_raw": None, "ai_major_raw": None}

        def fetch_for_source() -> Any:
            if source == "luma_me":
                return fetch_luma_me_page_events(
                    period=args.period,
                    timeout=REQUEST_TIMEOUT_SECONDS,
                    cookie=args.luma_cookie,
                )
            if source == "luma_sf":
                return fetch_luma_discover_events(
                    discover_place_api_id=args.discover_place_api_id,
                    web_url="https://luma.com/sf",
                    timeout=REQUEST_TIMEOUT_SECONDS,
                    cookie=args.luma_cookie,
                )
            if source == "luma_genai_sf":
                return fetch_luma_genai_sf_events(
                    page_url=args.discover_page_url,
                    discover_place_api_id=args.discover_place_api_id,
                    timeout=REQUEST_TIMEOUT_SECONDS,
                    cookie=args.luma_cookie,
                )
            if source == "luma_tech":
                events_data = fetch_luma_tech_events(
                    slug=args.slug,
                    latitude=LUMA_SF_LATITUDE,
                    longitude=LUMA_SF_LONGITUDE,
                    timeout=REQUEST_TIMEOUT_SECONDS,
                    cookie=args.luma_cookie,
                )
                state["tech_major_raw"] = fetch_luma_category_page_data(
                    page_url=LUMA_TECH_URL,
                    timeout=REQUEST_TIMEOUT_SECONDS,
                    cookie=args.luma_cookie,
                )
                return events_data
            if source == "luma_tech_major":
                return fetch_luma_category_page_data(
                    page_url=args.category_page_url,
                    timeout=REQUEST_TIMEOUT_SECONDS,
                    cookie=args.luma_cookie,
                )
            if source == "luma_ai":
                events_data = fetch_luma_ai_events(
                    slug=LUMA_AI_SLUG,
                    latitude=LUMA_SF_LATITUDE,
                    longitude=LUMA_SF_LONGITUDE,
                    timeout=REQUEST_TIMEOUT_SECONDS,
                    cookie=args.luma_cookie,
                )
                state["ai_major_raw"] = fetch_luma_category_page_data(
                    page_url=LUMA_AI_URL,
                    timeout=REQUEST_TIMEOUT_SECONDS,
                    cookie=args.luma_cookie,
                )
                return events_data
            if source == "stanford":
                return fetch_stanford_events(timeout=REQUEST_TIMEOUT_SECONDS)
            if source == "stanford_mlsys":
                return fetch_page_markdown_with_firecrawl(
                    url=STANFORD_MLSYS_URL, timeout=REQUEST_TIMEOUT_SECONDS
                )
            if source == "stanford_hai":
                return fetch_page_markdown_with_firecrawl(
                    url=STANFORD_HAI_EVENTS_URL, timeout=REQUEST_TIMEOUT_SECONDS
                )
            if source == "partiful":
                return fetch_partiful_discoverable_events(
                    timeout=REQUEST_TIMEOUT_SECONDS,
                )
            if args.raw:
                return fetch_cerebral_valley_events(
                    location=args.location, timeout=REQUEST_TIMEOUT_SECONDS
                )
            cerebral_url = f"{BASE_URL}?{urlencode({'locations': args.location})}"
            return fetch_page_markdown_with_firecrawl(
                url=cerebral_url, timeout=REQUEST_TIMEOUT_SECONDS
            )

        try:
            data = run_with_spinner(source, fetch_for_source, enabled=not args.verbose)
        except RuntimeError as exc:
            print(f"[ERR] {source}: {exc}")
            if args.source != "all":
                raise SystemExit(1)
            continue

        if args.raw:
            if source == "luma_tech":
                output_payload = {
                    "major_raw": state["tech_major_raw"] if state["tech_major_raw"] is not None else {},
                    "events_raw": data,
                }
            elif source == "luma_ai":
                output_payload = {
                    "major_raw": state["ai_major_raw"] if state["ai_major_raw"] is not None else {},
                    "events_raw": data,
                }
            else:
                output_payload = data
        else:
            if source == "luma_me":
                output_payload = extract_luma_me_page_events(data)
            elif source == "luma_sf":
                output_payload = extract_luma_sf_events(data)
            elif source == "luma_genai_sf":
                output_payload = extract_luma_genai_sf_events(data)
            elif source == "luma_tech":
                output_payload = extract_luma_tech_dataset(
                    events_raw=data,
                    major_raw=state["tech_major_raw"] if state["tech_major_raw"] is not None else {},
                )
            elif source == "luma_ai":
                output_payload = extract_luma_ai_dataset(
                    events_raw=data,
                    major_raw=state["ai_major_raw"] if state["ai_major_raw"] is not None else {},
                )
            elif source == "stanford":
                output_payload = extract_stanford_events(data)
            elif source in ("stanford_mlsys", "stanford_hai"):
                output_payload = data
            elif source == "partiful":
                output_payload = extract_partiful_events(data) if isinstance(data, dict) else []
            elif source == "luma_tech_major":
                output_payload = extract_luma_major_events_from_category_data(data)
            elif source == "cv" and isinstance(data, str):
                output_payload = data
            else:
                output_payload = extract_events(data)

        saved_path = save_cli_output(source, output_payload, raw=args.raw)
        if args.verbose:
            if isinstance(output_payload, str):
                print(output_payload)
            else:
                print(json.dumps(output_payload, indent=2, ensure_ascii=True))
        if saved_path is None:
            print(f"[OK ] {source}: raw mode (not saved)")
        else:
            print(f"[OK ] {source}: {saved_path}")
        if args.verbose:
            print("")
