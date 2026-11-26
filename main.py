#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence — make.fun entry.

Writes a single one-line error message (the line an AI agent shows when
it runs out of tokens mid-sentence) to /output/entry.txt.

Deterministic and offline: the entry is a fixed string, stdlib only,
no randomness, no network, no timestamps, no paths in the output.
"""

import os

ENTRY = "Error: out of tokens at character 137. The next 3 characters would have been the point."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: the entry must be 1-140 characters of non-whitespace UTF-8 text.
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
