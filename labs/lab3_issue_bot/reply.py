"""Lab 3: build the bot's reply to a new GitHub issue.

    python labs/lab3_issue_bot/reply.py --event labs/lab3_issue_bot/sample_event.json --out reply.md

The workflow gives this script the path of the event file (GITHUB_EVENT_PATH). We read the title
from that JSON file. We never paste the title into a shell command, because an issue title is typed
by a stranger and could contain shell code.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

ZWSP = "​"  # zero width space: stops "@name" from pinging real people

# TODO (Stretch 1): add a rule of your own. The first keyword found in the title wins.
RULES = [
    ("help", "It sounds like you need help. Say what you tried and what you expected to happen."),
    ("bug", "A bug report! Please add the steps to reproduce it and what you saw instead."),
    ("idea", "An idea! Describe who it helps and what the smallest first version could be."),
]
DEFAULT_RULE = "Thanks for the note. A maintainer will take a look."

HAIKUS = [
    "Green check, quiet room,\nthe robot finished its work\nbefore I looked up.",
    "Red cross on the screen,\nread the log, then read it twice,\nthe fix is a line.",
    "Midnight scheduler\nwakes the sleeping repository,\ncommits, and sleeps again.",
    "Small tests, one by one,\nturning from red into green,\nlike a morning field.",
]

_LOGIN = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,38})$")


def neutralize(text: str, limit: int = 80) -> str:
    """Make untrusted text safe to quote: no @mentions, no backticks, no line breaks, short."""
    text = re.sub(r"\s+", " ", text or "").strip()
    text = text.replace("`", "'").replace("@", "@" + ZWSP)
    return text[:limit] + ("..." if len(text) > limit else "")


def pick_haiku(title: str) -> str:
    index = int(hashlib.sha256((title or "").encode()).hexdigest(), 16) % len(HAIKUS)
    return HAIKUS[index]


def pick_rule(title: str) -> str:
    lowered = (title or "").lower()
    for keyword, message in RULES:
        if keyword in lowered:
            return message
    return DEFAULT_RULE


def build_reply(title: str, author: str) -> str:
    who = f"@{author}" if _LOGIN.match(author or "") else "friend"
    words = len(re.findall(r"\w+", title or ""))
    quote = neutralize(title) or "(no title)"
    haiku = "\n".join(f"> {line}" for line in pick_haiku(title).splitlines())
    return (
        f"Thanks for opening this issue, {who}!\n\n"
        f"You wrote: `{quote}` ({words} word{'s' if words != 1 else ''}).\n\n"
        f"{pick_rule(title)}\n\n"
        f"A haiku for your trouble:\n\n{haiku}\n\n"
        "_I am a bot made with GitHub Actions._\n"
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--event", required=True, help="path to the GitHub event JSON file")
    parser.add_argument("--out", default="reply.md")
    args = parser.parse_args(argv)
    event = json.loads(Path(args.event).read_text(encoding="utf-8"))
    issue = event.get("issue") or {}
    reply = build_reply(str(issue.get("title", "")), str((issue.get("user") or {}).get("login", "")))
    Path(args.out).write_text(reply, encoding="utf-8")
    print(f"wrote {args.out} ({len(reply)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
