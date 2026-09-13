import importlib.util
import hashlib
import tempfile
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
        for check_id in (
            "COH-009",
            "COH-020",
            "COH-021",
            "COH-022",
            "COH-023",
            "COH-024",
            "COH-025",
            "COH-026",
            "COH-027",
        ):
            item = next(check for check in self.report["checks"] if check["check_id"] == check_id)
            self.assertTrue(item["pass"])
        manifests = self.report["research_manifests"]
        self.assertEqual(39, manifests["base_snapshot_verified"])
        self.assertEqual(37, manifests["extension_snapshot_verified"])
        self.assertEqual(56, manifests["live_worktree_verified"])
        self.assertTrue(manifests["extension_snapshot_reachable_from_head"])
        self.assertEqual(
            coherence.RESEARCH_EXTENSION_PATHS_SHA256,
            manifests["paths_file_sha256"],
        )
        self.assertEqual(
            coherence.RESEARCH_EXTENSION_MANIFEST_SHA256,
            manifests["manifest_file_sha256"],
        )
        base, errors = coherence.parse_sha256_manifest(coherence.RESEARCH_BASE_MANIFEST)
        self.assertEqual([], errors)
        rel_path = "investigacion_empaquetamientos_esfericos_degenerantes/README.md"
        actual, error = coherence.git_filtered_sha256(
            coherence.RESEARCH_BASE_SNAPSHOT,
            rel_path,
        )
        self.assertIsNone(error)
        self.assertEqual(base[rel_path], actual)

    def test_manifest_parser_rejects_duplicate_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            manifest = Path(tmp) / "manifest.txt"
            digest = "0" * 64
            manifest.write_text(
                f"{digest}  payload.txt\n{digest}  payload.txt\n",
                encoding="utf-8",
            )
            entries, errors = coherence.parse_sha256_manifest(manifest)
        self.assertEqual({"payload.txt": digest}, entries)
        self.assertTrue(any(error.startswith("manifest_duplicate:") for error in errors))

    def test_worktree_verifier_detects_tamper(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            payload = root / "payload.bin"
            original = b"original"
            payload.write_bytes(original)
            entries = {"payload.bin": hashlib.sha256(original).hexdigest()}
            verified, errors = coherence.verify_worktree_entries(entries, root)
            self.assertEqual((1, []), (verified, errors))
            payload.write_bytes(b"tampered")
            verified, errors = coherence.verify_worktree_entries(entries, root)
        self.assertEqual(0, verified)
        self.assertEqual(["worktree_sha256:payload.bin"], errors)

    def test_worktree_verifier_detects_missing_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            verified, errors = coherence.verify_worktree_entries(
                {"missing.bin": hashlib.sha256(b"missing").hexdigest()},
                Path(tmp),
            )
        self.assertEqual(0, verified)
        self.assertEqual(["worktree_missing:missing.bin"], errors)

    def test_manifest_overlay_contract_is_exact(self):
        base = {f"shared-{index}": "a" for index in range(20)}
        base.update({f"base-{index}": "b" for index in range(19)})
        extension = {f"shared-{index}": "c" for index in range(20)}
        extension.update({f"added-{index}": "d" for index in range(17)})
        summary = coherence.overlay_summary(base, extension)
        self.assertEqual(20, len(summary["overlap"]))
        self.assertEqual(17, len(summary["additions"]))
        self.assertEqual(19, len(summary["base_only"]))
        self.assertEqual(56, len(summary["live"]))
        self.assertTrue(all(summary["live"][f"shared-{index}"] == "c" for index in range(20)))

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
