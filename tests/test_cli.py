import unittest
from unittest.mock import patch, MagicMock
import json

class TestCLI(unittest.TestCase):
    @patch("labeldocsync.api.fetch_labels")
    @patch("labeldocsync.parser.parse_contributing")
    def test_main(self, mock_parse, mock_fetch):
        mock_parse.return_value = {"bug", "enhancement"}
        mock_fetch.return_value = {"bug", "documentation"}
        from labeldocsync.cli import main
        with patch("sys.stdout") as mock_stdout:
            main(["--repo", "owner/repo", "--output-format", "json", "--contributing", "CONTRIBUTING.md", "--token", "dummy"])
            output = mock_stdout.write.call_args[0][0]
            data = json.loads(output)
            self.assertEqual(data["missing"], ["enhancement"])
            self.assertEqual(data["extra"], ["documentation"])
