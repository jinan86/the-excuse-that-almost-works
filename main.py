#!/usr/bin/env python3
"""The Excuse That Almost Works — make.fun entry.

Writes the single line a gamer texts their boss to skip work during
GTA 6 launch week to /output/entry.txt. One line, plain text, no setup,
no explanation, no signature — a hurried SMS built on one boring,
specific, almost-believable detail: a gas safety check with a narrow
engineer window and a three-week rebooking penalty.
"""

ENTRY = (
    "Gas safety check, engineer booked 8-1, can't leave flat unattended "
    "or they cancel and rebook in 3 weeks."
)


def main() -> None:
    """Write the excuse, exactly as-is, to /output/entry.txt."""
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
