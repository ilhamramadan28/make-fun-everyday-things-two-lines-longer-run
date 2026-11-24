#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run - write entry.txt to /output/entry.txt."""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.txt")
OUT = "/output/entry.txt"


def main() -> int:
    with open(SRC, "r", encoding="utf-8") as f:
        text = f.read()
    # Gate: 1-400 chars of UTF-8, not only whitespace, exactly two lines.
    stripped = text.strip()
    lines = stripped.split("\n")
    has_control = any(ord(c) < 32 and c != "\n" for c in stripped)
    if not 1 <= len(text) <= 400 or not stripped or len(lines) != 2 or has_control:
        print("entry fails gate: must be 1-400 chars, not only whitespace, exactly two lines, no control characters",
              file=sys.stderr)
        return 1
    if any(not line.strip() for line in lines):
        print("entry fails gate: each line must have text", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    shutil.copyfile(SRC, OUT)
    os.chmod(OUT, 0o644)
    with open(SRC, "rb") as a, open(OUT, "rb") as b:
        if a.read() != b.read():
            print("byte-verify failed", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
