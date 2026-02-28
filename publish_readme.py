#!/usr/bin/env python3
"""Publish README to awesome-sf-events from locally built README."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

from build_readme import LOCAL_PREVIEW_README


PROJECT_ROOT = Path(__file__).resolve().parent
DEFAULT_AWESOME_REPO_DIR = PROJECT_ROOT.parent / "awesome-sf-events"
DEFAULT_AWESOME_REPO_URL = "git@github.com:kaarelkaarelson/awesome-sf-events.git"


def ensure_repo(repo_dir: Path, repo_url: str) -> None:
    if repo_dir.exists():
        return
    repo_dir.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["git", "clone", repo_url, str(repo_dir)], check=True)


def commit_and_maybe_push(repo_dir: Path, readme_path: Path, push: bool) -> None:
    subprocess.run(["git", "-C", str(repo_dir), "add", str(readme_path)], check=True)
    status = subprocess.run(
        ["git", "-C", str(repo_dir), "status", "--porcelain"],
        check=True,
        capture_output=True,
        text=True,
    )
    if not status.stdout.strip():
        print("No README changes to commit.")
        return

    message = "Update weekly SF events README"
    subprocess.run(["git", "-C", str(repo_dir), "commit", "-m", message], check=True)
    print(f"Committed: {message}")
    if push:
        subprocess.run(["git", "-C", str(repo_dir), "push", "origin", "HEAD"], check=True)
        print("Pushed to origin.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Publish local awesome README to awesome-sf-events repo.")
    parser.add_argument(
        "--local-readme",
        default=str(LOCAL_PREVIEW_README),
        help="Path to local README built by build_readme.py",
    )
    parser.add_argument(
        "--awesome-repo-dir",
        default=str(DEFAULT_AWESOME_REPO_DIR),
        help="Path to awesome-sf-events local repo",
    )
    parser.add_argument(
        "--awesome-repo-url",
        default=DEFAULT_AWESOME_REPO_URL,
        help="Git URL used if repo is missing locally",
    )
    parser.add_argument("--commit", action="store_true", help="Commit README update in awesome repo")
    parser.add_argument("--push", action="store_true", help="Push commit to origin (implies --commit)")
    args = parser.parse_args()

    local_readme = Path(args.local_readme).expanduser().resolve()
    if not local_readme.exists():
        raise RuntimeError(f"Missing local README. Build first: {local_readme}")

    repo_dir = Path(args.awesome_repo_dir).expanduser().resolve()
    ensure_repo(repo_dir=repo_dir, repo_url=args.awesome_repo_url)
    readme_path = repo_dir / "README.md"
    readme_path.write_text(local_readme.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"Published README: {readme_path}")

    if args.commit or args.push:
        commit_and_maybe_push(repo_dir=repo_dir, readme_path=readme_path, push=args.push)


if __name__ == "__main__":
    main()

