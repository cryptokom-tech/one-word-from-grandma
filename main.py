"""One Word From Grandma — make.fun bounty entry.

Writes the single word Grandma would text about AI to /output/entry.txt.
The word is fixed text, written by this program at run time.
"""

import os
import sys

# ROBOTO: Grandma means "robot" and types it the way she hears it —
# one letter off, warm, baffled, and unmistakably about the machine
# itself. A typo she would actually make, not a word anyone else
# would pick on purpose.
WORD = "ROBOTO"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = WORD.strip()
    if not text or len(text) > 30 or len(text.split()) != 1:
        print("entry must be exactly one word, 1-30 characters",
              file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    # One word, exactly what Grandma would text about AI.
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
