#!/usr/bin/env python3
"""Last words of a phone dying at 1 percent battery.

Writes one fixed farewell line -- the phone itself speaking as its
battery gives out -- to $MAKEFUN_OUTPUT_DIR/entry.txt. Pure standard
library, no network, no randomness, no clock: the same line on
every run, so the output is byte-identical each time.
"""

import os
import sys

# The gate allows one line of 1 to 199 characters; keep the bounds
# named so the check below and the docstring cannot drift apart.
MIN_LEN = 1
MAX_LEN = 199

# The phone's last words: after years of silently fixing its owner's
# typos, it spends its final percent fixing the one text that
# mattered -- and signs off pleased with itself. One line, phone's
# own voice, punch landing on the final word.
LINE = (
    "My final act at 1%: autocorrecting your last text "
    "to the truth. You're welcome."
)


def main() -> int:
    if not MIN_LEN <= len(LINE) <= MAX_LEN:
        print(f"line length {len(LINE)} out of range", file=sys.stderr)
        return 1
    if LINE != LINE.strip() or "\n" in LINE:
        print("line must be a single clean line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
