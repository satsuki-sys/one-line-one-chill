#!/usr/bin/env python3
"""One Line, One Chill — writes a single sentence of horror to /output/entry.txt."""

import os

LINE = "My daughter drew our family at dinner \u2014 four people at the table, and me outside the window, smiling, asking to be let in."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
