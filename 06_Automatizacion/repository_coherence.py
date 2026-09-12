#!/usr/bin/env python3
"""Verificador no mutante del corte de coherencia del repositorio."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any

MODULE_DIR = Path(__file__).resolve().parent
ROOT = MODULE_DIR.parent

RESEARCH_MANIFEST = ROOT / "03_Expedientes" / "LAB-RESEARCH-PROVENANCE-001_SHA256SUMS.txt"
RECOVERY_DIR = ROOT / "04_Registro_Historico" / "2026-09-11_chatgpt_recovery_001"
RECOVERY_MANIFEST = RECOVERY_DIR / "MANIFEST.json"
COHERENCE_MAP = ROOT / "05_Estado_Proyecto" / "MAPA_COHERENCIA_2026-09-12.json"
INCORPORATION_EXPEDIENTS = {
    "LAB-INC-SCI-001": "LAB-INC-SCI-001_Factorizacion_Identificabilidad.md",
    "LAB-INC-SCI-002": "LAB-INC-SCI-002_Geometria_Observabilidad.md",
    "LAB-INC-SCI-003": "LAB-INC-SCI-003_Arquitecturas_Reflexivas_ConcordIA.md",
    "LAB-INC-SCI-004": "LAB-INC-SCI-004_Necesidad_Representacional.md",
    "LAB-INC-SCI-005": "LAB-INC-SCI-005_Validacion_Estructural_Minima.md",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def check(condition: bool, check_id: str, detail: str) -> dict[str, Any]:
    return {"check_id": check_id, "pass": bool(condition), "detail": detail}


def git_ancestor(commit: str) -> bool | None:
    try:
        probe = subprocess.run(
            ["git", "merge-base", "--is-ancestor", commit, "HEAD"],
            cwd=ROOT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
    except OSError:
        return None
    return probe.returncode == 0


def verify_research_manifest() -> tuple[int, list[str]]:
    verified = 0
    errors: list[str] = []
    for raw in RESEARCH_MANIFEST.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        expected, rel_path = raw.split("  ", 1)
        path = ROOT / rel_path
        if not path.is_file():
            errors.append(f"missing:{rel_path}")
        elif sha256(path) != expected:
            errors.append(f"sha256:{rel_path}")
        else:
            verified += 1
    return verified, errors


def verify_recovery_manifest() -> tuple[int, list[str]]:
    data = json.loads(RECOVERY_MANIFEST.read_text(encoding="utf-8"))
    verified = 0
    errors: list[str] = []
    for entry in data["files"]:
        path = RECOVERY_DIR / entry["path"]
        if not path.is_file():
            errors.append(f"missing:{entry['path']}")
        elif path.stat().st_size != entry["size"]:
            errors.append(f"size:{entry['path']}")
        elif sha256(path) != entry["sha256"]:
            errors.append(f"sha256:{entry['path']}")
        else:
            verified += 1
    return verified, errors


def build_report() -> dict[str, Any]:
    map_data = json.loads(COHERENCE_MAP.read_text(encoding="utf-8"))
    canon = (ROOT / "01_Canon" / "LAB-RESEARCH-PROVENANCE-001_Corpus_Canonico.md").read_text(encoding="utf-8")
    registry = (ROOT / "03_Expedientes" / "LAB-RESEARCH-PROVENANCE-001.md").read_text(encoding="utf-8")
    current = (ROOT / "CURRENT_STATE.md").read_text(encoding="utf-8")
    state = (ROOT / "05_Estado_Proyecto" / "ESTADO_ACTUAL.md").read_text(encoding="utf-8")
    revision = (ROOT / "05_Estado_Proyecto" / "REVISION_FORMALIZACION_PENDIENTE.md").read_text(encoding="utf-8")

    research_verified, research_errors = verify_research_manifest()
    recovery_verified, recovery_errors = verify_recovery_manifest()

    incorporation = map_data["research_corpus"]["incorporation_commit"]
    governance = map_data["research_corpus"]["governance_commit"]
    incorporation_reachable = git_ancestor(incorporation)
    governance_reachable = git_ancestor(governance)

    open_ids = {item["id"] for item in map_data["open_expedientes"]}
    incorporation_items = map_data["open_scientific_incorporation_expedientes"]
    incorporation_ids = {item["id"] for item in incorporation_items}
    incorporation_docs = {
        item_id: (ROOT / "03_Expedientes" / filename).read_text(encoding="utf-8")
        for item_id, filename in INCORPORATION_EXPEDIENTS.items()
    }
    cleanup = (ROOT / "03_Expedientes" / "CLN-001_Limpieza_Workspace_2026-09-12.md").read_text(encoding="utf-8")
    checks = [
        check(map_data["status"] == "REPOSITORY_COHERENT_WITH_EXPLICIT_OPEN_DEBTS", "COH-001", "map status"),
        check(open_ids == {"MOC-001", "AO-001", "TCS-001"}, "COH-002", "open expediente set"),
        check("GIT_GOVERNANCE_RECORD=MATERIALIZED_IN_ORIGIN_MAIN" in canon, "COH-003", "canonical Git record materialized"),
        check("INCORPORATED_IN_ORIGIN_MAIN=YES" in registry, "COH-004", "research registry incorporated"),
        check("MAPA_COHERENCIA_2026-09-12.md" in current, "COH-005", "current state routes to coherence map"),
        check("`RH-003`" in state, "COH-006", "historical processing close visible"),
        check((ROOT / "03_Expedientes" / "TCS-001.md").is_file(), "COH-007", "TCS parent index exists"),
        check("No hay otra adopción oficial pendiente" in revision, "COH-008", "MOC apply is not presented as future route"),
        check(research_verified == 39 and not research_errors, "COH-009", f"research manifest {research_verified}/39"),
        check(recovery_verified == 23 and not recovery_errors, "COH-010", f"recovery manifest {recovery_verified}/23"),
        check(incorporation_reachable is not False, "COH-011", "incorporation commit reachable when Git is available"),
        check(governance_reachable is not False, "COH-012", "governance commit reachable when Git is available"),
        check(map_data["research_corpus"]["scientific_claims_canonical_as_true"] is False, "COH-013", "scientific claims remain noncanonical"),
        check(map_data["research_corpus"]["activation"] is False, "COH-014", "research remains inactive"),
        check(map_data["chatgpt_recovery"]["canon"] is False, "COH-015", "recovery remains noncanonical"),
        check(incorporation_ids == set(INCORPORATION_EXPEDIENTS), "COH-016", "five scientific incorporation expedients registered"),
        check(all(item["payload_in_origin_main"] is False for item in incorporation_items), "COH-017", "candidate payloads remain outside origin/main"),
        check(
            all(
                "PAYLOAD_IN_ORIGIN_MAIN=NO" in document
                and "INCORPORATION_DECISION=PENDING" in document
                and "CANONIZATION=NO" in document
                and "ACTIVATION=NO" in document
                for document in incorporation_docs.values()
            ),
            "COH-018",
            "incorporation authority gates remain closed",
        ),
        check(
            map_data["latest_workspace_cleanup"]["post_cleanup_status_entries"] == 0
            and "WORKSPACE_STATUS_AFTER_CLEANUP=0" in cleanup,
            "COH-019",
            "conservative workspace cleanup recorded",
        ),
    ]
    failures = [item for item in checks if not item["pass"]]
    return {
        "report_id": "REPOSITORY-COHERENCE-2026-09-12",
        "resultado": "ok" if not failures else "bloqueado",
        "transformacion_permitida": False,
        "summary": {"checks": len(checks), "passed": len(checks) - len(failures), "failed": len(failures)},
        "research_manifest_errors": research_errors,
        "recovery_manifest_errors": recovery_errors,
        "checks": checks,
    }


def main() -> int:
    report = build_report()
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["resultado"] == "ok" else 1


if __name__ == "__main__":
    raise SystemExit(main())
