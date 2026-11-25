#!/usr/bin/env python3
"""Describe Your Ex in One Word — make.fun entry.

Writes a single word to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Gate: UTF-8 text, 1-111 chars, exactly one word, no punctuation tricks.
"""

import os
import sys

WORD = "Unsubscribe"  # one word, 11 bytes: short text wins exact-tie breaks


def main() -> int:
    word = WORD.strip()
    if not word:
        print("error: entry word is empty", file=sys.stderr)
        return 1
    if len(word) > 111:
        print("error: entry exceeds 111 characters", file=sys.stderr)
        return 1
    if len(word.split()) != 1:
        print("error: entry must be exactly one word", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(word)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
