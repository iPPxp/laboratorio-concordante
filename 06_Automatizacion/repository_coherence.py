#!/usr/bin/env python3
"""Verificador no mutante del corte de coherencia del repositorio."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from functools import lru_cache
from pathlib import Path
from typing import Any

MODULE_DIR = Path(__file__).resolve().parent
ROOT = MODULE_DIR.parent

RESEARCH_BASE_MANIFEST = ROOT / "03_Expedientes" / "LAB-RESEARCH-PROVENANCE-001_SHA256SUMS.txt"
RESEARCH_BASE_PATHS = ROOT / "03_Expedientes" / "LAB-RESEARCH-PROVENANCE-001_PATHS.txt"
RESEARCH_BASE_SNAPSHOT = "2c3264c473c865835571a1df4b28e1a022790695"
RESEARCH_EXTENSION_MANIFEST = ROOT / "03_Expedientes" / "LAB-RESEARCH-PROVENANCE-002_SHA256SUMS.txt"
RESEARCH_EXTENSION_PATHS = ROOT / "03_Expedientes" / "LAB-RESEARCH-PROVENANCE-002_PATHS.txt"
RESEARCH_EXTENSION_SNAPSHOT = "8b7ad0e02ca231a0f35ddd2ccff7c4d2d18ef2db"
RESEARCH_EXTENSION_PATHS_SHA256 = "734fc7060f2798bd8b21fd8b96c7847faa5b9c480a89038bec9d686bbd987335"
RESEARCH_EXTENSION_MANIFEST_SHA256 = "465ad0d0fa8c19b426c949f0f0f73da2343756ce9fd719abfff59e278aaeaeb0"
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


def sha256_canonical_lf(path: Path) -> str:
    """Hash a UTF-8 manifest using LF so checkout EOL policy cannot change identity."""
    return hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


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


def parse_sha256_manifest(manifest: Path) -> tuple[dict[str, str], list[str]]:
    entries: dict[str, str] = {}
    errors: list[str] = []
    if not manifest.is_file():
        return entries, [f"manifest_missing:{manifest.name}"]
    for line_no, raw in enumerate(manifest.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        if "  " not in raw:
            errors.append(f"manifest_format:{manifest.name}:{line_no}")
            continue
        expected, rel_path = raw.split("  ", 1)
        rel = Path(rel_path)
        if not re.fullmatch(r"[0-9a-f]{64}", expected):
            errors.append(f"manifest_hash:{manifest.name}:{line_no}")
            continue
        if rel.is_absolute() or ".." in rel.parts or not rel_path:
            errors.append(f"manifest_path:{manifest.name}:{line_no}")
            continue
        if rel_path in entries:
            errors.append(f"manifest_duplicate:{manifest.name}:{rel_path}")
            continue
        entries[rel_path] = expected
    return entries, errors


def verify_path_list(path_list: Path, entries: dict[str, str]) -> list[str]:
    if not path_list.is_file():
        return [f"path_list_missing:{path_list.name}"]
    paths = [line for line in path_list.read_text(encoding="utf-8").splitlines() if line]
    errors: list[str] = []
    if len(paths) != len(set(paths)):
        errors.append(f"path_list_duplicate:{path_list.name}")
    missing = sorted(set(entries) - set(paths))
    extra = sorted(set(paths) - set(entries))
    errors.extend(f"path_list_missing_entry:{item}" for item in missing)
    errors.extend(f"path_list_extra_entry:{item}" for item in extra)
    return errors


def verify_worktree_entries(entries: dict[str, str], root: Path = ROOT) -> tuple[int, list[str]]:
    verified = 0
    errors: list[str] = []
    for rel_path, expected in entries.items():
        path = root / rel_path
        if not path.is_file():
            errors.append(f"worktree_missing:{rel_path}")
        elif sha256(path) != expected:
            errors.append(f"worktree_sha256:{rel_path}")
        else:
            verified += 1
    return verified, errors


@lru_cache(maxsize=256)
def _git_filtered_sha256_cached(
    commit: str, rel_path: str, root_text: str
) -> tuple[str | None, str | None]:
    root = Path(root_text)
    try:
        probe = subprocess.run(
            [
                "git",
                "cat-file",
                "--filters",
                f"--path={rel_path}",
                f"{commit}:{rel_path}",
            ],
            cwd=root,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=False,
        )
    except OSError:
        return None, f"git_unavailable:{commit}:{rel_path}"
    if probe.returncode != 0:
        return None, f"snapshot_missing:{commit}:{rel_path}"
    return hashlib.sha256(probe.stdout).hexdigest(), None


def git_filtered_sha256(commit: str, rel_path: str, root: Path = ROOT) -> tuple[str | None, str | None]:
    """Hash the exact historical checkout bytes produced by Git filters.

    Batch mode is deliberately not used: on the supported Windows Git version,
    ``cat-file --batch --filters`` reports the LF blob rather than the CRLF
    checkout representation pinned by LAB-RESEARCH-PROVENANCE-001.
    """
    return _git_filtered_sha256_cached(commit, rel_path, str(root.resolve()))


def verify_snapshot_entries(
    entries: dict[str, str], commit: str, root: Path = ROOT
) -> tuple[int, list[str]]:
    verified = 0
    errors: list[str] = []
    for rel_path, expected in entries.items():
        actual, error = git_filtered_sha256(commit, rel_path, root)
        if error:
            errors.append(error)
        elif actual != expected:
            errors.append(f"snapshot_sha256:{commit}:{rel_path}")
        else:
            verified += 1
    return verified, errors


def overlay_summary(base: dict[str, str], extension: dict[str, str]) -> dict[str, Any]:
    overlap = set(base) & set(extension)
    additions = set(extension) - set(base)
    base_only = set(base) - set(extension)
    live = dict(base)
    live.update(extension)
    return {
        "overlap": overlap,
        "additions": additions,
        "base_only": base_only,
        "live": live,
    }


def verify_research_manifests() -> dict[str, Any]:
    base, base_parse_errors = parse_sha256_manifest(RESEARCH_BASE_MANIFEST)
    extension, extension_parse_errors = parse_sha256_manifest(RESEARCH_EXTENSION_MANIFEST)
    overlay = overlay_summary(base, extension)

    base_snapshot_verified, base_snapshot_errors = verify_snapshot_entries(
        base, RESEARCH_BASE_SNAPSHOT
    )
    extension_snapshot_verified, extension_snapshot_errors = verify_snapshot_entries(
        extension, RESEARCH_EXTENSION_SNAPSHOT
    )
    extension_worktree_verified, extension_worktree_errors = verify_worktree_entries(extension)
    live_worktree_verified, live_worktree_errors = verify_worktree_entries(overlay["live"])
    extension_snapshot_reachable = git_ancestor(RESEARCH_EXTENSION_SNAPSHOT)
    paths_file_sha256 = (
        sha256_canonical_lf(RESEARCH_EXTENSION_PATHS)
        if RESEARCH_EXTENSION_PATHS.is_file()
        else None
    )
    manifest_file_sha256 = (
        sha256_canonical_lf(RESEARCH_EXTENSION_MANIFEST)
        if RESEARCH_EXTENSION_MANIFEST.is_file()
        else None
    )

    errors = (
        base_parse_errors
        + extension_parse_errors
        + verify_path_list(RESEARCH_BASE_PATHS, base)
        + verify_path_list(RESEARCH_EXTENSION_PATHS, extension)
        + base_snapshot_errors
        + extension_snapshot_errors
        + extension_worktree_errors
        + live_worktree_errors
    )
    if paths_file_sha256 != RESEARCH_EXTENSION_PATHS_SHA256:
        errors.append(f"paths_file_sha256:{paths_file_sha256}")
    if manifest_file_sha256 != RESEARCH_EXTENSION_MANIFEST_SHA256:
        errors.append(f"manifest_file_sha256:{manifest_file_sha256}")
    if len(base) != 39:
        errors.append(f"base_count:{len(base)}")
    if len(extension) != 37:
        errors.append(f"extension_count:{len(extension)}")
    if len(overlay["overlap"]) != 20:
        errors.append(f"overlay_overlap:{len(overlay['overlap'])}")
    if len(overlay["additions"]) != 17:
        errors.append(f"overlay_additions:{len(overlay['additions'])}")
    if len(overlay["base_only"]) != 19:
        errors.append(f"overlay_base_only:{len(overlay['base_only'])}")
    if len(overlay["live"]) != 56:
        errors.append(f"overlay_live:{len(overlay['live'])}")

    return {
        "base_entries": len(base),
        "extension_entries": len(extension),
        "overlap": len(overlay["overlap"]),
        "additions": len(overlay["additions"]),
        "base_only": len(overlay["base_only"]),
        "live_entries": len(overlay["live"]),
        "base_snapshot_verified": base_snapshot_verified,
        "extension_snapshot_verified": extension_snapshot_verified,
        "extension_worktree_verified": extension_worktree_verified,
        "live_worktree_verified": live_worktree_verified,
        "extension_snapshot_reachable_from_head": extension_snapshot_reachable,
        "paths_file_sha256": paths_file_sha256,
        "manifest_file_sha256": manifest_file_sha256,
        "errors": errors,
    }


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
    extension_canon = (
        ROOT / "01_Canon" / "LAB-RESEARCH-PROVENANCE-002_Extension_4D_Corpus_Canonico.md"
    ).read_text(encoding="utf-8")
    registry = (ROOT / "03_Expedientes" / "LAB-RESEARCH-PROVENANCE-001.md").read_text(encoding="utf-8")
    extension_registry = (
        ROOT / "03_Expedientes" / "LAB-RESEARCH-PROVENANCE-002.md"
    ).read_text(encoding="utf-8")
    psi_bridge = (
        ROOT / "03_Expedientes" / "MOC-PSI-GEO-BRIDGE-001_Puente_4Simplex_24Cell.md"
    ).read_text(encoding="utf-8")
    current = (ROOT / "CURRENT_STATE.md").read_text(encoding="utf-8")
    state = (ROOT / "05_Estado_Proyecto" / "ESTADO_ACTUAL.md").read_text(encoding="utf-8")
    revision = (ROOT / "05_Estado_Proyecto" / "REVISION_FORMALIZACION_PENDIENTE.md").read_text(encoding="utf-8")

    research = verify_research_manifests()
    research_errors = research["errors"]
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
    extension_map = next(
        item
        for item in map_data["research_corpus_extensions"]
        if item["id"] == "LAB-RESEARCH-PROVENANCE-002"
    )
    resolved_psi_source = next(
        item
        for item in map_data["resolved_debts"]
        if item["id"] == "EXTERNAL_PSI_CANON_SOURCE_RECOVERY"
    )
    checks = [
        check(map_data["status"] == "REPOSITORY_COHERENT_WITH_EXPLICIT_OPEN_DEBTS", "COH-001", "map status"),
        check(open_ids == {"MOC-001", "AO-001", "TCS-001"}, "COH-002", "open expediente set"),
        check("GIT_GOVERNANCE_RECORD=MATERIALIZED_IN_ORIGIN_MAIN" in canon, "COH-003", "canonical Git record materialized"),
        check("INCORPORATED_IN_ORIGIN_MAIN=YES" in registry, "COH-004", "research registry incorporated"),
        check("MAPA_COHERENCIA_2026-09-12.md" in current, "COH-005", "current state routes to coherence map"),
        check("`RH-003`" in state, "COH-006", "historical processing close visible"),
        check((ROOT / "03_Expedientes" / "TCS-001.md").is_file(), "COH-007", "TCS parent index exists"),
        check("No hay otra adopción oficial pendiente" in revision, "COH-008", "MOC apply is not presented as future route"),
        check(
            research["base_snapshot_verified"] == 39 and not research_errors,
            "COH-009",
            f"historical research snapshot {research['base_snapshot_verified']}/39",
        ),
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
        check(
            research["extension_snapshot_verified"] == 37
            and research["extension_worktree_verified"] == 37,
            "COH-020",
            "4D extension snapshot and worktree 37/37",
        ),
        check(
            research["overlap"] == 20
            and research["additions"] == 17
            and research["base_only"] == 19
            and research["live_entries"] == 56,
            "COH-021",
            "manifest overlay 20 revised, 17 added, 19 inherited",
        ),
        check(
            research["live_worktree_verified"] == 56,
            "COH-022",
            "live overlay verifies all 56 research paths",
        ),
        check(
            research["extension_snapshot_reachable_from_head"] is not False,
            "COH-023",
            "4D payload integration head is an ancestor when Git is available",
        ),
        check(
            research["paths_file_sha256"] == RESEARCH_EXTENSION_PATHS_SHA256
            and research["manifest_file_sha256"] == RESEARCH_EXTENSION_MANIFEST_SHA256,
            "COH-024",
            "4D path list and manifest files match their anchored hashes",
        ),
        check(
            "DELTA_ROUTE_COUNT=37" in extension_canon
            and "DELTA_IDENTITY_CANONICAL=YES" in extension_canon
            and "SCIENTIFIC_CLAIMS_CANONIZED_AS_TRUE=NO" in extension_canon
            and "RESEARCH_STATUS=ACTIVE_RESEARCH_MATERIAL" in extension_registry,
            "COH-025",
            "4D extension canonizes identity and research status, not claims",
        ),
        check(
            extension_map["delta_routes"] == 37
            and extension_map["added_routes"] == 17
            and extension_map["revised_routes"] == 20
            and extension_map["scientific_claims_canonical_as_true"] is False,
            "COH-026",
            "structured 4D extension status matches manifests",
        ),
        check(
            "COMMIT=f068faf9dca98408b1a3b93b43f97401f8768795" in psi_bridge
            and "PSI_24CELL_STATUS=RESEARCH" in psi_bridge
            and "K6_COMPLETE_EQUALS_C6_CYCLE=NO" in psi_bridge
            and "A4_D4_CANONICAL_BIJECTION=NO" in psi_bridge
            and resolved_psi_source["status"] == "RESOLVED_BY_PINNED_EXTERNAL_AUTHORITY"
            and resolved_psi_source["commit"]
            == "f068faf9dca98408b1a3b93b43f97401f8768795"
            and resolved_psi_source["imports_psi_canon_into_lab"] is False
            and resolved_psi_source["reopens_psi_001"] is False,
            "COH-027",
            "PSI bridge pins authority and preserves open semantic boundaries",
        ),
    ]
    failures = [item for item in checks if not item["pass"]]
    return {
        "report_id": "REPOSITORY-COHERENCE-2026-09-12",
        "resultado": "ok" if not failures else "bloqueado",
        "transformacion_permitida": False,
        "summary": {"checks": len(checks), "passed": len(checks) - len(failures), "failed": len(failures)},
        "research_manifest_errors": research_errors,
        "research_manifests": research,
        "recovery_manifest_errors": recovery_errors,
        "checks": checks,
    }


def main() -> int:
    report = build_report()
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["resultado"] == "ok" else 1


if __name__ == "__main__":
    raise SystemExit(main())
