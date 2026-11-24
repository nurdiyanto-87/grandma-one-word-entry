"""One Word From Grandma — make.fun entry.

Writes the single word a grandma would text about AI to /output/entry.txt.
The word must pass a small gate (1–30 chars, a single token with no
whitespace) before it is written. Pure Python standard library only;
no third-party packages.
"""

import os

WORD = "robit"


def validate_word(word: str) -> str:
    """Check the entry word is a single 1–30 char token; raise otherwise."""
    if not isinstance(word, str) or not 1 <= len(word) <= 30:
        raise ValueError("entry word must be 1–30 characters long")
    if any(c.isspace() for c in word) or len(word.split()) != 1:
        raise ValueError("entry word must be a single token with no whitespace")
    return word


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(validate_word(WORD))


if __name__ == "__main__":
    main()
