import unittest
from pathlib import Path
from labeldocsync.parser import parse_contributing

class TestParser(unittest.TestCase):

    def setUp(self):
        from tempfile import TemporaryDirectory as _orion_scratch_directory
        self._orion_scratch = _orion_scratch_directory(prefix='orion-test-')
        self.addCleanup(self._orion_scratch.cleanup)
        self.md = Path(self._orion_scratch.name) / 'sample_contributing.md'
        self.md.write_text('# Contributing\n\n## Labels\n\n| Label | Description |\n|-------|--------------|\n| bug | Something is broken |\n| enhancement | New feature |\n| question | Need help |\n\nOther content\n')

    def test_parse(self):
        labels = parse_contributing(self.md)
        self.assertEqual(labels, {'bug', 'enhancement', 'question'})

    def tearDown(self):
        self.md.unlink()
