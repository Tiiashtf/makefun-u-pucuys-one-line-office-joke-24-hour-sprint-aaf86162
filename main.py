#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint — entry program.

Writes a single-line joke about office life (at most 200 characters)
to /output/entry.txt.
"""

import os

JOKE = "We switched to hot-desking, so now I start every morning by reintroducing myself to my own chair."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = JOKE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 chars, got %d" % len(text)
    out_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(out_dir, exist_ok=True)
    # Clear only the contents of the output dir, never the dir itself:
    # the grader may run this with a root-owned output dir inside a
    # sticky parent, where removing the dir itself fails with EPERM.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
