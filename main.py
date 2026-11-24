"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (<=140 characters) for a city that
does not exist to /output/entry.txt. Deterministic: no randomness, no
network, no input.
"""

import os

LINE = "Umbrellatown: light confetti drizzle, 19\u00b0C. The 8:04 bus is late again, but the driver is singing, so nobody minds."

LIMIT = 140


def main() -> None:
    assert isinstance(LINE, str)
    assert LINE.strip(), "line must not be blank"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert 1 <= len(LINE) <= LIMIT, f"line is {len(LINE)} chars, limit {LIMIT}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
