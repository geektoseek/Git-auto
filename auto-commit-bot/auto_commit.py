#!/usr/bin/env python3
"""
auto_commit.py — Makes a random commit to the current repo and pushes it.
Designed to be run by GitHub Actions on a cron schedule.
"""

import random
import subprocess
import sys
from datetime import datetime, timezone

COMMIT_TEMPLATES = {
    "feat": [
        "feat: add responsive layout improvements",
        "feat: enhance UI component structure",
        "feat: implement dynamic content loading",
        "feat: add new section styles",
        "feat: improve mobile navigation flow",
        "feat: add hover animation effects",
        "feat: enhance card component design",
        "feat: add footer link updates",
        "feat: improve hero section visuals",
        "feat: add smooth scroll behavior",
    ],
    "fix": [
        "fix: resolve alignment issue on mobile",
        "fix: correct broken link in navigation",
        "fix: patch overflow on small screens",
        "fix: fix font loading fallback",
        "fix: resolve button hover state bug",
        "fix: correct z-index layering issue",
        "fix: fix image aspect ratio on Safari",
        "fix: resolve CSS specificity conflict",
        "fix: patch scroll position reset",
        "fix: fix transition timing mismatch",
    ],
    "docs": [
        "docs: update README with setup steps",
        "docs: add inline code comments",
        "docs: improve component documentation",
        "docs: update deployment notes",
        "docs: clarify installation instructions",
        "docs: add project structure notes",
        "docs: update contact information",
        "docs: improve changelog entries",
        "docs: add usage examples",
        "docs: update tech stack references",
    ],
    "style": [
        "style: format code with consistent spacing",
        "style: clean up trailing whitespace",
        "style: reorganize import order",
        "style: apply consistent naming convention",
        "style: reformat CSS variables section",
        "style: adjust line breaks in components",
        "style: clean up unused class names",
        "style: normalize quote style",
        "style: improve code readability",
        "style: align table formatting in docs",
    ],
    "refactor": [
        "refactor: simplify component logic",
        "refactor: extract reusable utility",
        "refactor: consolidate repeated styles",
        "refactor: improve variable naming",
        "refactor: restructure section layout",
        "refactor: reduce component nesting",
        "refactor: optimize asset references",
        "refactor: clean up legacy code",
        "refactor: split large component into smaller parts",
        "refactor: move constants to config file",
    ],
    "chore": [
        "chore: update dependencies",
        "chore: clean up build artifacts",
        "chore: reorganize folder structure",
        "chore: update .gitignore entries",
        "chore: bump package version",
        "chore: remove unused imports",
        "chore: sync lockfile",
        "chore: add editor config settings",
        "chore: update CI pipeline notes",
        "chore: refresh environment config",
    ],
    "perf": [
        "perf: optimize image loading strategy",
        "perf: reduce bundle size",
        "perf: lazy load below-fold sections",
        "perf: preload critical fonts",
        "perf: minify inline SVGs",
        "perf: reduce animation repaints",
        "perf: improve scroll event throttling",
        "perf: cache static asset headers",
        "perf: compress background assets",
        "perf: defer non-critical scripts",
    ],
}

LOG_FILE = "activity_log.txt"


def run(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, check=check, capture_output=True, text=True)


def configure_git() -> None:
    run(["git", "config", "user.name", "github-actions[bot]"])
    run(["git", "config", "user.email", "github-actions[bot]@users.noreply.github.com"])


def pick_commit_message() -> str:
    commit_type = random.choice(list(COMMIT_TEMPLATES.keys()))
    return random.choice(COMMIT_TEMPLATES[commit_type])


def update_log(message: str) -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{now}] {message}\n")


def commit_and_push(message: str) -> None:
    run(["git", "add", LOG_FILE])

    result = run(["git", "diff", "--cached", "--quiet"], check=False)
    if result.returncode == 0:
        print("Nothing to commit — log file unchanged.")
        sys.exit(0)

    run(["git", "commit", "-m", message])
    run(["git", "push"])
    print(f"Pushed: {message}")


def main() -> None:
    configure_git()
    message = pick_commit_message()
    update_log(message)
    commit_and_push(message)


if __name__ == "__main__":
    main()
