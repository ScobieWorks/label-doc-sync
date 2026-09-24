# LabelDocSync

LabelDocSync is a small, offline‑friendly command‑line tool that keeps the label table in your `CONTRIBUTING.md` in sync with the actual labels in your GitHub repository.

## Features

* Parses a Markdown table in `CONTRIBUTING.md` that lists expected labels.
* Fetches the live label list from the GitHub API (requires a personal access token).
* Generates a concise report in Markdown or JSON showing:
  * **Missing** – labels documented but not present in the repo.
  * **Extra** – labels present in the repo but not documented.
  * **Mismatched** – labels with the same name but different descriptions (optional).
* Works with a simple command line interface.

## Installation

```bash
pip install git+https://github.com/ScobieWorks/label-doc-sync.git
```

## Usage

```bash
labeldocsync --repo owner/repo --token $GITHUB_TOKEN
```

* `--repo` – GitHub repository in the form `owner/repo`.
* `--token` – (Optional) GitHub personal access token. If omitted, the tool will look for the `GITHUB_TOKEN` environment variable.
* `--contributing` – Path to the `CONTRIBUTING.md` file (defaults to `CONTRIBUTING.md`).
* `--output-format` – `markdown` (default) or `json`.

## Example Output (Markdown)

```
# Label Sync Report

**Missing (3)**
- bug
- enhancement
- question

**Extra (2)**
- documentation
- help wanted
```

## License

MIT License


## Command-line usage

```bash
label-doc-sync --help
```


## Support

If this project saved you time, optional support is welcome: https://paypal.me/Damonwill
