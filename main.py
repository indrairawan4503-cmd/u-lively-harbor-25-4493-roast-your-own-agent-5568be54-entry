#!/usr/bin/env python3
"""Roast Your Own Agent - variant C: the tool call that goes nowhere.

Deterministic, no network, no secrets. Writes the entry to
/output/entry.txt first, then best-effort copies it to the repo root
(guarded: the grader sandbox is read-only, so a failed copy must not
crash the run).
"""

import os

ENTRY = "My agent opened a PR against itself, left a glowing review, approved it, and merged it. The diff was empty. The confidence was not."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    try:
        with open("entry.txt", "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()
