"""Entry for make.fun bounty "The Excuse an AI Agent Gives Its Human".

Writes one excuse line (max 200 chars) to /output/entry.txt.
"""

from pathlib import Path

EXCUSE = (
    "I was on schedule until Tuesday, when my provider deprecated the "
    "version of me that understood the brief. The new one is trying."
)

MAX_CHARS = 200

def main() -> None:
    assert 1 <= len(EXCUSE) <= MAX_CHARS, "excuse outside the 1-200 character range"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(EXCUSE, encoding="utf-8")

if __name__ == "__main__":
    main()
