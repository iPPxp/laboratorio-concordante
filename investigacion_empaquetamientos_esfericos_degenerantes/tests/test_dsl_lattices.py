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

    def test_dsl_rejects_ragged_non_numeric_and_nonfinite_directions(self):
        base = {
            "case_id": "invalid-r4",
            "kind": "CENTERED_CONFIGURATION",
            "n": 2,
            "ambient_dimension": 4,
            "outer_radius": 1,
            "central_radius": 0.1,
            "directions": [[1, 0, 0, 0], [-1, 0, 0, 0]],
            "epistemic_status": "DEFINICION_PROPUESTA",
        }
        ragged = {**base, "directions": [[1, 0, 0, 0], [-1, 0, 0]]}
        text = {**base, "directions": [[1, 0, 0, 0], ["x", 0, 0, 0]]}
        infinite = {**base, "directions": [[1, 0, 0, 0], [float("inf"), 0, 0, 0]]}
        zero = {**base, "directions": [[1, 0, 0, 0], [0, 0, 0, 0]]}

        self.assertIn("directions_dimension_mismatch", validate_case(ragged))
        self.assertIn("directions_must_be_finite_numeric", validate_case(text))
        self.assertIn("directions_must_be_finite_numeric", validate_case(infinite))
        self.assertIn("directions_must_be_nonzero", validate_case(zero))

    def test_dsl_requires_declared_positive_dimension(self):
        case = {
            "case_id": "missing-dimension",
            "kind": "CENTERED_CONFIGURATION",
            "n": 2,
            "outer_radius": 1,
            "central_radius": 0.1,
            "directions": [[1, 0, 0], [-1, 0, 0]],
            "epistemic_status": "DEFINICION_PROPUESTA",
        }
        errors = validate_case(case)
        self.assertIn("missing_fields=['ambient_dimension']", errors)
        self.assertIn("invalid_ambient_dimension", errors)

    def test_hcp_is_not_labeled_simple_bravais(self):
        self.assertEqual(lattice_catalog()["HCP"]["kind"], "PERIODIC_LATTICE_WITH_BASIS_NOT_SIMPLE_BRAVAIS")

    def test_required_lattices_are_present(self):
        self.assertTrue({"SC", "FCC", "HCP", "BCC"}.issubset(lattice_catalog()))


if __name__ == "__main__":
    unittest.main()
