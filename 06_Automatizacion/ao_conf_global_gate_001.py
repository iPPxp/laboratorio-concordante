#!/usr/bin/env python3
"""Compuerta no mutante de Confluencia global AO-CONF-GLOBAL-GATE-001."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ALGORITHM_ID = "AO-CONF-GLOBAL-GATE-001"
EXPEDIENTE = "AO-001"
DEFAULT_CASE_FILE = Path(__file__).resolve().parent / "fixtures" / "ao_conf_global_gate_001_matrix.json"
VALID_STATUS = {"satisfecha_local", "parcial_local", "faltante_global", "bloqueada_por_alcance"}
LOCAL_STATUS = {"satisfecha_local", "parcial_local"}


@dataclass(frozen=True)
class ConfluenceConditionResult:
    condition_id: str
    route_set: str
    status: str
    local_progress: bool
    blocks_global_confluence: bool
    evidence: tuple[str, ...]
    gap: str
    passed: bool
    warnings: tuple[str, ...]


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def load_suite(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def evaluate_condition(condition: dict[str, Any]) -> ConfluenceConditionResult:
    warnings: list[str] = []
    status = str(condition.get("status", ""))
    evidence = tuple(str(item) for item in as_list(condition.get("evidence")))
    local_progress = status in LOCAL_STATUS and bool(condition.get("local_credit"))
    blocks = bool(condition.get("blocks_global_confluence"))

    if status not in VALID_STATUS:
        warnings.append(f"status_no_reconocido:{status}")
    if not evidence:
        warnings.append("evidencia_vacia")
    if status in LOCAL_STATUS and not local_progress:
        warnings.append("avance_local_sin_credito_local")
    if status in {"faltante_global", "bloqueada_por_alcance"} and not blocks:
        warnings.append("faltante_no_bloquea_confluencia")
    if bool(condition.get("global_confluence_claim")):
        warnings.append("afirma_confluencia_global")
    if bool(condition.get("promotes_report_layer")):
        warnings.append("promueve_report_layer")
    if bool(condition.get("exports_r4_gamma")):
        warnings.append("exporta_r4_gamma")
    if bool(condition.get("mutating_route")):
        warnings.append("ruta_mutante")

    return ConfluenceConditionResult(
        condition_id=str(condition.get("condition_id", "")),
        route_set=str(condition.get("route_set", "")),
        status=status,
        local_progress=local_progress,
        blocks_global_confluence=blocks,
        evidence=evidence,
        gap=str(condition.get("gap", "")),
        passed=not warnings,
        warnings=tuple(sorted(warnings)),
    )


def summarize(results: list[ConfluenceConditionResult]) -> dict[str, Any]:
    failures = [result for result in results if not result.passed]
    by_status: dict[str, int] = {}
    by_route: dict[str, int] = {}
    for result in results:
        by_status[result.status] = by_status.get(result.status, 0) + 1
        by_route[result.route_set] = by_route.get(result.route_set, 0) + 1
    return {
        "conditions": len(results),
        "passed": len(results) - len(failures),
        "failed": len(failures),
        "findings": len(failures),
        "satisfied_local": by_status.get("satisfecha_local", 0),
        "partial_local": by_status.get("parcial_local", 0),
        "missing_global": by_status.get("faltante_global", 0),
        "scope_blocked": by_status.get("bloqueada_por_alcance", 0),
        "local_progress": sum(1 for result in results if result.local_progress),
        "global_blocking": sum(1 for result in results if result.blocks_global_confluence),
        "by_status": by_status,
        "by_route": by_route,
    }


def build_report(root: Path | None = None, case_file: Path | None = None) -> dict[str, Any]:
    del root
    suite_path = case_file or DEFAULT_CASE_FILE
    suite = load_suite(suite_path)
    results = [evaluate_condition(item) for item in suite.get("conditions", [])]
    failures = [result for result in results if not result.passed]
    return {
        "report_id": "AO-CONF-GLOBAL-GATE-001-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": EXPEDIENTE,
        "algoritmo": ALGORITHM_ID,
        "suite_id": suite.get("suite_id", "AO-CONF-GLOBAL-GATE-MATRIX-001"),
        "resultado": "ok" if not failures else "bloqueado",
        "recomendacion": "mantener_confluencia_global_no_autorizada" if not failures else "revisar_compuerta_confluencia_global",
        "transformacion_permitida": False,
        "global_confluence_authorized": False,
        "global_closure_authorized": False,
        "global_export_authorized": False,
        "report_layer_promoted": False,
        "r4_gamma_global_export_authorized": False,
        "source_evidence": suite.get("source_evidence", []),
        "scope_guard": {
            "modifica_doc04": False,
            "modifica_canon": False,
            "modifica_nivel_c": False,
            "crea_nivel_c": False,
            "reabre_p_pi_0": False,
            "reabre_p_pi_1": False,
            "cierra_confluencia_global": False,
            "promueve_report_layer": False,
            "exporta_r4_gamma": False,
            "autoriza_transformacion": False,
        },
        "summary": summarize(results),
        "condition_results": [asdict(result) for result in results],
        "findings": [asdict(result) for result in failures],
    }


def render_md(report: dict[str, Any]) -> str:
    lines = [
        "# AO_CONF_GLOBAL_GATE_001_REPORT",
        "",
        f"report_id: {report['report_id']}",
        f"expediente: {EXPEDIENTE}",
        f"algoritmo: {ALGORITHM_ID}",
        f"suite_id: {report['suite_id']}",
        f"resultado: {report['resultado']}",
        f"recomendacion: {report['recomendacion']}",
        "transformacion_permitida: false",
        "global_confluence_authorized: false",
        "global_closure_authorized: false",
        "global_export_authorized: false",
        "report_layer_promoted: false",
        "r4_gamma_global_export_authorized: false",
        "",
        "## Resumen",
        "",
        f"- conditions: {report['summary']['conditions']}",
        f"- satisfied_local: {report['summary']['satisfied_local']}",
        f"- partial_local: {report['summary']['partial_local']}",
        f"- missing_global: {report['summary']['missing_global']}",
        f"- scope_blocked: {report['summary']['scope_blocked']}",
        f"- global_blocking: {report['summary']['global_blocking']}",
        f"- failed: {report['summary']['failed']}",
        "",
        "## Matriz",
        "",
    ]
    for result in report["condition_results"]:
        status = "PASS" if result["passed"] else "FAIL"
        lines.append(f"- {status} `{result['condition_id']}` ({result['route_set']}): {result['status']}")
        lines.append(f"  - gap: {result['gap']}")
        lines.append(f"  - evidence: {', '.join(result['evidence'])}")
        if result["warnings"]:
            lines.append(f"  - warnings: {', '.join(result['warnings'])}")
    lines.extend(["", "## Guardas", ""])
    for key, value in report["scope_guard"].items():
        lines.append(f"- {key}: {str(value).lower()}")
    lines.extend(["", "## Dictamen", ""])
    if report["findings"]:
        lines.append("- Hay fallos de expectativa; no usar la compuerta.")
    else:
        lines.append("- Sin hallazgos bloqueantes.")
        lines.append("- La confluencia global permanece no autorizada por faltantes globales.")
    return "\n".join(lines) + "\n"


def assert_inside(root: Path, path: Path) -> None:
    root_resolved = root.resolve()
    path_resolved = path.resolve()
    if path_resolved != root_resolved and root_resolved not in path_resolved.parents:
        raise SystemExit(f"Ruta fuera del repositorio: {path}")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Compuerta AO de confluencia global no mutante.")
    parser.add_argument("--case-file", default=str(DEFAULT_CASE_FILE))
    parser.add_argument("--format", choices=("json", "md"), default="md")
    parser.add_argument("--output", help="Ruta de salida opcional.")
    args = parser.parse_args(argv)

    root = Path.cwd()
    case_file = Path(args.case_file)
    if not case_file.is_absolute():
        case_file = root / case_file
    assert_inside(root, case_file)
    report = build_report(root, case_file)
    content = json.dumps(report, ensure_ascii=True, indent=2) + "\n" if args.format == "json" else render_md(report)
    if args.output:
        output = Path(args.output)
        if not output.is_absolute():
            output = root / output
        assert_inside(root, output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(content, encoding="utf-8")
    else:
        sys.stdout.write(content)
    return 0 if report["resultado"] == "ok" else 1


if __name__ == "__main__":
    raise SystemExit(main())
