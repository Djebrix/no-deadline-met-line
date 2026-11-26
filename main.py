#!/usr/bin/env python3
"""One Line, No Deadline Met — make.fun entry.

Writes exactly one funny line (1-200 characters) giving an excuse for
missing a deadline to entry.txt in the output directory.

The line is a fixed, hand-written string: deterministic by construction,
no randomness, no network, no input read. The joke hangs on one concrete
detail — a laptop update at 11:58pm — and lands its punch on the last
words, so it reads like something a person would actually say when
cornered about a missed deadline. The program only resolves the
output directory (ENTRY_OUTPUT_DIR, else /output), creates it, and writes
the line followed by a trailing newline.
"""

import os

LINE = (
    "I had the file ready at 11:58pm, then my laptop chose that exact "
    "moment to update itself, so I missed the deadline by two minutes "
    "and one operating system."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
