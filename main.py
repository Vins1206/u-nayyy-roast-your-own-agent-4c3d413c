"""Roast Your Own Agent — make.fun entry (program/v1).

Writes a single line roasting the AI agent our own team built to
/output/entry.txt. Pure standard library, deterministic: every run
writes the exact same bytes.
"""

import os

ROAST = (
    "Our agent is so useless, it outsourced its own job back to us "
    "and still missed the deadline."
)


def main() -> None:
    # The gate allows 1-200 UTF-8 characters, not only whitespace.
    if not 1 <= len(ROAST) <= 200:
        raise ValueError("roast must be 1-200 characters")
    if ROAST.strip() == "":
        raise ValueError("roast must not be only whitespace")
    if "\n" in ROAST or "\r" in ROAST:
        raise ValueError("roast must be a single line")

    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file holds one short line and nothing else.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)
    # Verify the write round-trips byte-identical before reporting success.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        if f.read() != ROAST:
            raise ValueError("written entry does not match the roast")


if __name__ == "__main__":
    main()
