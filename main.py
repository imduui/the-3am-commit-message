#!/usr/bin/env python3
"""Write the 3AM commit message entry to /output/entry.txt.

One line, deterministic, no network, no reads outside this repo.
"""

import os

ENTRY = "fix: read this function 47 times. it has started reading me back. merging before it learns my name"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
