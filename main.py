#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one original dad joke (at most 200 characters) to entry.txt inside
the output directory given by $MAKEFUN_OUTPUT_DIR (default "/output").
Deterministic, standard library only, no network, no API keys.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

JOKE = (
    "My son asked why I carry a pen everywhere. "
    "I said, 'In case I need to draw a conclusion \u2014 "
    "and mine are always sketchy.'"
)


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
