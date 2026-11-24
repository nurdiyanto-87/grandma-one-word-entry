"""One Word From Grandma — make.fun entry.

Writes the single word a grandma would text about AI to /output/entry.txt.
Pure Python standard library only; no third-party packages.
"""

import os

WORD = "robit"


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
