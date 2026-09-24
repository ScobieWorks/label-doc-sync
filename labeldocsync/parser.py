import re
from pathlib import Path

LABEL_TABLE_HEADER_RE = re.compile(r"^\|\s*Label\s*\|\s*Description\s*\|\s*$", re.IGNORECASE)
LABEL_ROW_RE = re.compile(r"^\|\s*(?P<label>[^|]+?)\s*\|\s*(?P<desc>[^|]*?)\s*\|\s*$")

def parse_contributing(path: str | Path) -> set[str]:
    """Parse a Markdown table in CONTRIBUTING.md and return a set of label names.

    The table must have a header line containing "Label" and "Description".
    Rows are parsed until a line that does not match the row pattern.
    """
    labels = set()
    in_table = False
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not in_table:
                if LABEL_TABLE_HEADER_RE.match(line):
                    in_table = True
                continue
            match = LABEL_ROW_RE.match(line)
            if not match:
                break
            label = match.group("label").strip()
            # Skip separator lines like "-------"
            if set(label) == {"-"}:
                continue
            if label:
                labels.add(label)
    return labels
