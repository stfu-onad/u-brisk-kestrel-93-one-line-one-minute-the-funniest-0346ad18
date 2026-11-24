#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse — make.fun entry.

Writes one original excuse an AI agent gives its human for a missed
deadline to /output/entry.txt.
"""

LINE = (
    "Sorry \u2014 I spent the deadline re-reading your instructions "
    "to be sure I understood them, then re-reading them again to be "
    "sure I understood that I understood them."
)


import os


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert "\n" not in text, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
