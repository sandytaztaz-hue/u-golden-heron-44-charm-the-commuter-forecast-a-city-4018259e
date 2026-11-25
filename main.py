#!/usr/bin/env python3
"""Charm the Commuter — Round 2 entry.

Writes one line of weather forecast (at most 140 characters) for a city
that does not exist, to /output/entry.txt. Deterministic: the same line
every run, no randomness, no network, no input files.
"""

import os

LINE = (
    # Breathton is an invented city: it names the place, gives it weather
    # (minus 4, frost), and ends on the warm payoff for a bored commuter.
    "Breathton, minus 4\u00b0: frost on the platform, the bus is late \u2014 "
    "but the driver stopped at the bakery, and the whole bus smells of warm bread."
)


def main() -> None:
    assert len(LINE) <= 140, f"entry line is {len(LINE)} chars, over the 140 cap"
    assert "\n" not in LINE, "entry must be exactly one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
