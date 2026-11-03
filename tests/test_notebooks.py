import unittest
from pathlib import Path
import importlib.util

FILE = Path(__file__).resolve().parents[1] / 'scripts' / 'check_notebooks.py'
SPEC = importlib.util.spec_from_file_location('check_notebooks', FILE)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class NotebookTests(unittest.TestCase):
    def test_v1_structure(self):
        self.assertEqual(MODULE.validate(MODULE.ROOT / 'notebooks/phase2_version1.ipynb'), 63)

    def test_v2_structure(self):
        self.assertEqual(MODULE.validate(MODULE.ROOT / 'notebooks/phase2_version2.ipynb'), 64)


if __name__ == '__main__':
    unittest.main()
