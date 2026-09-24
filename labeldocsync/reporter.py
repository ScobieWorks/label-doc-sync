import json
from typing import Iterable

def report_diff(doc_labels: set[str], live_labels: set[str], output_format: str = "markdown") -> str:
    missing = sorted(doc_labels - live_labels)
    extra = sorted(live_labels - doc_labels)
    if output_format == "json":
        return json.dumps({"missing": missing, "extra": extra}, indent=2)
    # markdown
    lines = ["# Label Sync Report", ""]
    lines.append(f"**Missing ({len(missing)})**")
    for l in missing:
        lines.append(f"- {l}")
    lines.append("")
    lines.append(f"**Extra ({len(extra)})**")
    for l in extra:
        lines.append(f"- {l}")
    return "\n".join(lines)
