import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
ACTIVE_SURFACES = (
    "README.md",
    "CURRENT_STATE.md",
    "INDEX.md",
    "HANDOFF.md",
    "HANDOFF_PACKAGE.md",
    "01_Canon",
    "02_Documentos",
    "03_Expedientes",
    "05_Estado_Proyecto",
    "06_Automatizacion",
)
HISTORICAL_REFERENCE_ALLOWLIST = {
    "03_Expedientes/R001-001_Integracion_Table_Checks.md",
}
TEXT_SUFFIXES = {".csv", ".json", ".md", ".py", ".txt", ".yaml", ".yml"}
LEGACY_TOKENS = (
    "v" + "1.5.2",
    "v." + "1.5.2",
)


def candidate_files():
    for surface in ACTIVE_SURFACES:
        path = ROOT / surface
        if path.is_file():
            yield path
        elif path.is_dir():
            yield from (item for item in path.rglob("*") if item.is_file())


class LegacyWorkspaceReferenceTests(unittest.TestCase):
    def test_legacy_version_references_are_only_explicit_history(self) -> None:
        findings = []
        for path in candidate_files():
            relative = path.relative_to(ROOT).as_posix()
            if relative in HISTORICAL_REFERENCE_ALLOWLIST:
                continue
            if path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            for line_number, line in enumerate(text.splitlines(), start=1):
                if any(token.lower() in line.lower() for token in LEGACY_TOKENS):
                    findings.append(f"{relative}:{line_number}: {line.strip()}")

        self.assertEqual(findings, [], "Referencias legacy fuera de historia permitida:\n" + "\n".join(findings))


if __name__ == "__main__":
    unittest.main()
