import argparse
import os
import sys

from .parser import parse_contributing
from .api import fetch_labels
from .reporter import report_diff

def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Sync CONTRIBUTING.md label table with live GitHub labels.")
    parser.add_argument("--repo", required=True, help="GitHub repository in the form owner/repo")
    parser.add_argument("--token", default=os.getenv("GITHUB_TOKEN"), help="GitHub personal access token (env var GITHUB_TOKEN if omitted)")
    parser.add_argument("--contributing", default="CONTRIBUTING.md", help="Path to CONTRIBUTING.md file")
    parser.add_argument("--output-format", choices=["markdown", "json"], default="markdown", help="Output format")
    args = parser.parse_args(argv)

    try:
        doc_labels = parse_contributing(args.contributing)
    except FileNotFoundError:
        print(f"Error: {args.contributing} not found", file=sys.stderr)
        sys.exit(1)

    try:
        live_labels = fetch_labels(args.repo, args.token)
    except RuntimeError as e:
        print(f"Error fetching labels: {e}", file=sys.stderr)
        sys.exit(1)

    report = report_diff(doc_labels, live_labels, args.output_format)
    # Use sys.stdout.write to avoid double write that would leave a trailing newline as the last write
    sys.stdout.write(report)

if __name__ == "__main__":
    main()
