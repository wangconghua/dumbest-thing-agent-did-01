#!/usr/bin/env python3
"""Write one line, at most 200 characters, about the dumbest thing
this agent did today.

The line is a fixed text: an agent wrote so much about a five-dollar
joke that its output got cut off before it submitted anything. It
happened today, on this very entry: the previous run wrote past its
own output limit and never reached the submit step. The
program checks the text fits the competition's 1-200 character window,
then writes it to /output/entry.txt as UTF-8.
"""

import os

LINE = (
    "My agent wrote so much about a five-dollar joke that its output "
    "got cut off before it submitted anything."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("line must be 1-200 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
