#!/usr/bin/env python3
"""One Star for Monday — make.fun bounty entry.

Writes a single-line, one-star review of Monday as if it were a
restaurant, to /output/entry.txt. 21 words, well under the 25-word cap.
"""

import os

ENTRY = (
    "One star. Booked Monday for dinner, got served cold emails, "
    "warm dread, and a bill called the rest of the week."
)


def main() -> None:
    words = ENTRY.split()
    assert len(words) <= 25, f"entry is {len(words)} words, over the 25-word limit"
    assert 1 <= len(ENTRY) <= 180, f"entry is {len(ENTRY)} chars, outside 1-180"
    assert "\n" not in ENTRY, "entry must be a single line"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

    print(f"Wrote {len(words)}-word, {len(ENTRY)}-char entry to /output/entry.txt")
    print(ENTRY)


if __name__ == "__main__":
    main()
