import json
import urllib.request
from urllib.error import HTTPError

GITHUB_API_URL = "https://api.github.com"

def fetch_labels(repo: str, token: str | None = None) -> set[str]:
    """Return the set of label names for the given GitHub repository.

    Parameters
    ----------
    repo: str
        Repository in the form ``owner/repo``.
    token: str | None
        Optional GitHub personal access token. If provided, it is sent as
        an ``Authorization: token <token>`` header.
    """
    url = f"{GITHUB_API_URL}/repos/{repo}/labels"
    req = urllib.request.Request(url)
    if token:
        req.add_header("Authorization", f"token {token}")
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except HTTPError as e:
        raise RuntimeError(f"Failed to fetch labels: {e.code} {e.reason}") from e
    return {item["name"] for item in data}
