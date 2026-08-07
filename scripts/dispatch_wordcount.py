#!/usr/bin/env python3
"""Report the body word count of a dispatch.

The platform limit applies to the article itself, so this counts from the
end of the byline block to the start of the closing comment prompt. The
sign-off and bio block are boilerplate and do not count against the cap.

Usage:
    python3 scripts/dispatch_wordcount.py content/substack/<slug>.md [--cap 1400]
"""

import argparse
import re
import sys
from pathlib import Path

COLUMN_TAG = "*Surviving the Feds: Dispatches from the Inside*"
SIGN_OFF = "Be Well, Stay Safe, and Survive the Feds,"


def body_of(text):
    """Return the article body: after the column tag, before the comment prompt."""
    if COLUMN_TAG not in text:
        sys.exit(f"error: column tag not found -- expected a line reading {COLUMN_TAG!r}")
    body = text.split(COLUMN_TAG, 1)[1]

    # The comment prompt is the last italic-only line before the sign-off.
    head = body.split(SIGN_OFF, 1)[0] if SIGN_OFF in body else body
    lines = head.rstrip().splitlines()
    while lines and (not lines[-1].strip() or lines[-1].strip() == "---"):
        lines.pop()
    if lines and lines[-1].strip().startswith("*") and lines[-1].strip().endswith("*"):
        lines.pop()

    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--cap", type=int, default=1400)
    args = ap.parse_args()

    path = Path(args.path)
    if not path.exists():
        sys.exit(f"error: {path} not found")

    body = body_of(path.read_text())
    words = len(re.sub(r"[*#_>-]", "", body).split())

    print(f"body words : {words}")
    print(f"cap        : {args.cap}")
    if words > args.cap:
        print(f"OVER by {words - args.cap}")
        sys.exit(1)
    print(f"PASS ({args.cap - words} to spare)")


if __name__ == "__main__":
    main()
