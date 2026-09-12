import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("repository_coherence.py")
SPEC = importlib.util.spec_from_file_location("repository_coherence", MODULE_PATH)
assert SPEC and SPEC.loader
coherence = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(coherence)


class RepositoryCoherenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = coherence.build_report()

    def test_all_coherence_checks_pass(self):
        self.assertEqual("ok", self.report["resultado"])
        self.assertEqual(0, self.report["summary"]["failed"])

    def test_research_manifest_is_complete(self):
        self.assertEqual([], self.report["research_manifest_errors"])
        item = next(check for check in self.report["checks"] if check["check_id"] == "COH-009")
        self.assertTrue(item["pass"])

    def test_recovery_manifest_is_complete(self):
        self.assertEqual([], self.report["recovery_manifest_errors"])
        item = next(check for check in self.report["checks"] if check["check_id"] == "COH-010")
        self.assertTrue(item["pass"])

    def test_authority_boundaries_remain_closed(self):
        for check_id in ("COH-013", "COH-014", "COH-015"):
            item = next(check for check in self.report["checks"] if check["check_id"] == check_id)
            self.assertTrue(item["pass"])

    def test_scientific_incorporation_expedients_remain_nonmutating(self):
        for check_id in ("COH-016", "COH-017", "COH-018"):
            item = next(check for check in self.report["checks"] if check["check_id"] == check_id)
            self.assertTrue(item["pass"])


if __name__ == "__main__":
    unittest.main()
