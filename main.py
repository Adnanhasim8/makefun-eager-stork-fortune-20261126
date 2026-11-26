#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers.

Writes one fortune cookie message for a software engineer to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt, or --out <path>).
Python 3.13 standard library only, no network at run time.
"""

import os
import sys

FORTUNE = "Yesterday you deleted one line of code. It was holding up production."


def main() -> None:
    out_dir = None
    args = sys.argv[1:]
    if "--out" in args:
        out_path = args[args.index("--out") + 1]
    else:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
        out_path = os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    # Gate assertions: exactly one line, 1-120 characters, non-empty.
    line = FORTUNE.strip()
    assert line, "fortune must not be empty"
    assert "\n" not in line, "fortune must be a single line"
    assert 1 <= len(line) <= 120, f"fortune is {len(line)} chars, must be 1-120"
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(FORTUNE + "\n")
    # Verify what was written round-trips through the gate.
    with open(out_path, encoding="utf-8") as f:
        written = f.read()
    assert written.strip() == line, "written output differs from fortune"
    assert 1 <= len(written.strip()) <= 120, "written output fails length gate"


if __name__ == "__main__":
    main()
