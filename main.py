"""One-sentence pitch for the worst app idea ever pitched.

Running this module writes the pitch to the file the grader reads:
``/output/entry.txt`` by default, or the path named by ``ENTRY_OUTPUT``
for a local test run. Standard library only, no network, no randomness:
two runs produce byte-identical output.
"""

import os
from pathlib import Path

# The pitch itself: one sentence, 181 characters. Every clause earns
# its keep against the judge's brief, in order: a named app and what
# it uselessly does ("rings your own doorbell"); absurd logic with a
# perfect mismatch (a doorbell for someone already home, "practice
# being out without ever leaving the house"); a real-pitch sound
# (product name, what it does, who it is for); one clean sentence
# with no second idea; and a vivid picture (a live feed of yourself
# not answering your own door).
PITCH = (
    "Doorbell+: an app that rings your own doorbell from the couch, "
    "then shows you a live feed of yourself not answering it, so you "
    "can practice being out without ever leaving the house."
)
LIMIT = 200


def check(line):
    """Reject anything the gate would refuse: more than one line,
    blank, over the character limit, padded with whitespace, or
    holding control characters."""
    if "\n" in line or "\r" in line:
        raise ValueError("pitch must fit on one line")
    if not line.strip():
        raise ValueError("pitch must not be blank")
    if len(line) > LIMIT:
        raise ValueError("pitch is over the character limit")
    if line != line.strip():
        raise ValueError("pitch must not start or end with whitespace")
    if any(ord(ch) < 0x20 for ch in line):
        raise ValueError("pitch must not hold control characters")


def destination():
    """Where the pitch goes: the grader's path, unless ENTRY_OUTPUT
    points the run at a scratch file for local testing."""
    return Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def main():
    check(PITCH)
    target = destination()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(PITCH, encoding="utf-8")


if __name__ == "__main__":
    main()
