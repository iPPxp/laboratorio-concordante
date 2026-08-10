import sys
import unittest
from pathlib import Path

import numpy as np

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from projective_n2 import additive_cross_difference, is_antipodal, pair_gram, q_tensor, unit


class ProjectiveN2Tests(unittest.TestCase):
    def test_q_tensor_identifies_head_and_tail(self):
        u = unit([1.0, 2.0, 3.0])
        self.assertTrue(np.allclose(q_tensor(u), q_tensor(-u), atol=1e-12))

    def test_antipodal_gram_matrix(self):
        gram = pair_gram([1, 0, 0], [-1, 0, 0])
        self.assertTrue(np.allclose(gram, [[1, -1], [-1, 1]], atol=1e-12))
        self.assertEqual(np.linalg.matrix_rank(gram, tol=1e-12), 1)
        self.assertTrue(np.allclose(np.linalg.eigvalsh(gram), [0, 2], atol=1e-12))

    def test_collective_kernel_mode(self):
        gram = pair_gram([1, 0, 0], [-1, 0, 0])
        self.assertTrue(np.allclose(gram @ np.asarray([1.0, 1.0]), [0, 0], atol=1e-12))

    def test_antipodality_is_relational(self):
        self.assertTrue(is_antipodal([1, 0, 0], [-1, 0, 0]))
        self.assertFalse(is_antipodal([1, 0, 0], [0, 1, 0]))

    def test_antipodality_indicator_is_not_unary_additive(self):
        self.assertEqual(additive_cross_difference(), 2.0)

    def test_zero_vector_does_not_define_axis(self):
        with self.assertRaises(ValueError):
            unit([0, 0, 0])


if __name__ == "__main__":
    unittest.main()
