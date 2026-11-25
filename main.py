#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Writes a single roast line (1-200 chars) to /output/entry.txt.
Stdlib only; no network; deterministic.
"""

import os
import sys

ROAST = (
    "My smart fridge pushed a firmware update at 2 a.m., rebooted, "
    "and forgot how to fridge \u2014 the ice maker now identifies "
    "as a screensaver."
)


def main() -> int:
    text = ROAST.strip()
    if not text or len(text) > 200:
        print(f"gate fail: length {len(text)}", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Read back and verify the gate: 1-200 chars, one non-blank line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        back = f.read()
    if back != text or not back.strip() or "\n" in back:
        print("gate fail: read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} chars to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
