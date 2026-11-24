#!/usr/bin/env python3
"""Write the entry line for 'One Line, One Minute: The Funniest AI Excuse'.

The line is the funniest excuse an AI agent gives its human for a missed
deadline: the agent negotiates with itself and grants its own extension.
It is written out verbatim to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 200

# The excuse, in three beats: the admission, the self-negotiation,
# and the punchline landing on the agent's own persuasiveness.
SETUP = "I missed the deadline because I asked myself for an extension,"
TWIST = "and I said yes"
PUNCHLINE = "\u2014 I am very persuasive."


def build_entry_line() -> str:
    """Assemble the single entry line from its three beats."""
    return " ".join((SETUP, TWIST, PUNCHLINE))


def validate(line: str) -> None:
    """The gate: 1-200 characters, a single line, no stray whitespace."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry line must be 1-{MAX_CHARS} chars, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if line != line.strip():
        raise ValueError("entry line must not have leading/trailing whitespace")


def main() -> None:
    line = build_entry_line()
    validate(line)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
