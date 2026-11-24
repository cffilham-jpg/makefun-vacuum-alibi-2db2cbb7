"""The Vacuum's Alibi - one-line excuse entry.

Writes the funniest one-line excuse a robot vacuum gives for missing
a spot to $MAKEFUN_OUTPUT_DIR/entry.txt (default "out").
Python standard library only.
"""

import os

LINE = (
    "I circled that spot three times on 4% battery, ran a full diagnostic, "
    "and concluded the crumbs were union reps. I never cross a picket line."
)


def validate(line: str) -> bool:
    """The gate: 1-200 characters, not only whitespace."""
    return 1 <= len(line) <= 200 and line.strip() != ""


def main() -> None:
    if not validate(LINE):
        raise ValueError("entry line failed validation")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
