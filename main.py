"""One-Liner Laugh Lab entry: the excuse a robot vacuum gives after
eating a sock. Standard library only; writes exactly one line to
/output/entry.txt, byte-exact, no trailing newline."""

import os

LINE = "It registered as dust. My sensors don't do fashion."
# 51 characters: inside the 1-200 character gate, one line, no newline.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
