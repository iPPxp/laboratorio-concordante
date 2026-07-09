import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ao_protocol_independent_001


class AOProtocolIndependent001Tests(unittest.TestCase):
    def test_protocol_accepts_reproducible_cases(self):
        report = ao_protocol_independent_001.build_report()

        self.assertEqual(report["resultado"], "ok")
        self.assertTrue(report["independent_protocol_accepted"])
        self.assertFalse(report["transformacion_permitida"])
        self.assertFalse(report["global_closure_authorized"])
        self.assertFalse(report["report_layer_promoted"])
        self.assertEqual(report["summary"]["cases"], 4)
        self.assertEqual(report["summary"]["failed"], 0)

    def test_classifies_without_forcing_unanimity(self):
        report = ao_protocol_independent_001.build_report()

        self.assertEqual(report["summary"]["exact"], 2)
        self.assertEqual(report["summary"]["family"], 1)
        self.assertEqual(report["summary"]["justified_disagreement"], 1)
        self.assertFalse(report["scope_guard"]["fuerza_unanimidad"])


if __name__ == "__main__":
    unittest.main()
