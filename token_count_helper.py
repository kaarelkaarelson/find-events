#!/usr/bin/env python3
"""Estimate token usage for files in ./data."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"
SKIP_SUFFIXES = {".py"}
SKIP_NAMES = {"evaluate_events_prompt.txt"}


def estimate_tokens(text: str) -> int:
    """Use tiktoken when available, else a conservative chars/4 estimate."""
    try:
        import tiktoken  # type: ignore

        enc = tiktoken.get_encoding("cl100k_base")
        return len(enc.encode(text))
    except Exception:
        return max(1, len(text) // 4)


@dataclass
class FileUsage:
    path: Path
    chars: int
    est_tokens: int


def gather_usage() -> list[FileUsage]:
    rows: list[FileUsage] = []
    for path in sorted(DATA_DIR.iterdir()):
        if not path.is_file():
            continue
        if path.suffix in SKIP_SUFFIXES:
            continue
        if path.name in SKIP_NAMES:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        rows.append(FileUsage(path=path, chars=len(text), est_tokens=estimate_tokens(text)))
    return rows


def main() -> None:
    rows = gather_usage()
    if not rows:
        print("No files found.")
        return

    total_tokens = sum(r.est_tokens for r in rows)
    max_row = max(rows, key=lambda r: r.est_tokens)

    print(f"Files scanned: {len(rows)}")
    print(f"Estimated total tokens: {total_tokens}")
    print(
        f"Largest file: {max_row.path.name} "
        f"(~{max_row.est_tokens} tokens, {max_row.chars} chars)"
    )
    print("")
    print("Per-file estimate:")
    for r in sorted(rows, key=lambda x: x.est_tokens, reverse=True):
        print(f"- {r.path.name}: ~{r.est_tokens} tokens ({r.chars} chars)")


if __name__ == "__main__":
    main()
