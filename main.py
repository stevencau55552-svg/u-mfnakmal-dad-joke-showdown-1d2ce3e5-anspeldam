#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one original dad joke (at most 200 characters) to /output/entry.txt.
Deterministic, standard library only, no network, no API keys.
"""

import os

JOKE = (
    "My son asked why I carry a pen everywhere. "
    "I said, 'In case I need to draw a conclusion \u2014 "
    "and mine are always sketchy.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
