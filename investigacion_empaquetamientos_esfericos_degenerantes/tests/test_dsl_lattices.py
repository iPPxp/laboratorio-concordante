import json
import sys
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from spherepack.dsl import validate_case
from spherepack.lattices import lattice_catalog


class DslAndLatticeTests(unittest.TestCase):
    def test_example_cases_are_structurally_valid(self):
        cases = json.loads((PROJECT / "examples" / "initial_cases.json").read_text(encoding="utf-8"))["cases"]
        self.assertTrue(cases)
        for case in cases:
            self.assertEqual(validate_case(case), [], case["case_id"])

    def test_hcp_is_not_labeled_simple_bravais(self):
        self.assertEqual(lattice_catalog()["HCP"]["kind"], "PERIODIC_LATTICE_WITH_BASIS_NOT_SIMPLE_BRAVAIS")

    def test_required_lattices_are_present(self):
        self.assertTrue({"SC", "FCC", "HCP", "BCC"}.issubset(lattice_catalog()))


if __name__ == "__main__":
    unittest.main()
