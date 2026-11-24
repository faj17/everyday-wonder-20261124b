#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line entry.

Writes one original sentence about a small moment of wonder in
everyday life to /output/entry.txt (1-200 characters, UTF-8, a single
line). Standard library only, no network, no input.

The line is built from two fragments: a setup (the phone's autocorrect
swaps one ordinary word for another — a small, real, everyday machine
act) and a punch (the turn: the thumb, not the mind, "had written the
sea", so a typo becomes a moment of wonder and the surprise lands in
the last words).
``assemble`` joins them into the single sentence; ``validate`` checks
the entry gate before anything is written.
"""

from pathlib import Path

SETUP = "My phone's autocorrect turned 'tired' into 'tide',"
PUNCH = "and for a moment my thumb had written the sea."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, punch: str) -> str:
    """Join the setup and punch fragments into one sentence."""
    return f"{setup} {punch}"


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-200 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(SETUP, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
