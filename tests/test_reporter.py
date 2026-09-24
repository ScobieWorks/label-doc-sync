import unittest
from labeldocsync.reporter import report_diff

class TestReporter(unittest.TestCase):
    def test_markdown(self):
        doc = {"bug", "enhancement", "question"}
        live = {"bug", "documentation", "help wanted"}
        out = report_diff(doc, live, "markdown")
        self.assertIn("**Missing (2)**", out)
        self.assertIn("- enhancement", out)
        self.assertIn("- question", out)
        self.assertIn("**Extra (2)**", out)
        self.assertIn("- documentation", out)
        self.assertIn("- help wanted", out)

    def test_json(self):
        doc = {"bug", "enhancement"}
        live = {"bug", "documentation"}
        out = report_diff(doc, live, "json")
        import json
        data = json.loads(out)
        self.assertEqual(data["missing"], ["enhancement"])
        self.assertEqual(data["extra"], ["documentation"])
