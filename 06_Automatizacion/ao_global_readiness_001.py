#!/usr/bin/env python3
"""Matriz no mutante de readiness global AO-GLOBAL-READINESS-001."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ALGORITHM_ID = "AO-GLOBAL-READINESS-001"
EXPEDIENTE = "AO-001"
DEFAULT_CASE_FILE = Path(__file__).resolve().parent / "fixtures" / "ao_global_readiness_001_matrix.json"
VALID_STATUS = {
    "satisfecha_local",
    "parcial_local",
    "faltante_global",
    "bloqueada_por_alcance",
    "no_promocion",
    "no_exportacion",
}
LOCAL_PROGRESS_STATUS = {"satisfecha_local", "parcial_local", "no_promocion", "no_exportacion"}


@dataclass(frozen=True)
class ReadinessConditionResult:
    condition_id: str
    front: str
    status: str
    local_progress: bool
    blocks_global_readiness: bool
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


def evaluate_condition(condition: dict[str, Any]) -> ReadinessConditionResult:
    warnings: list[str] = []
    status = str(condition.get("status", ""))
    evidence = tuple(str(item) for item in as_list(condition.get("evidence")))
    local_progress = status in LOCAL_PROGRESS_STATUS and bool(condition.get("local_credit"))
    blocks = bool(condition.get("blocks_global_readiness"))

    if status not in VALID_STATUS:
        warnings.append(f"status_no_reconocido:{status}")
    if not evidence:
        warnings.append("evidencia_vacia")
    if status in LOCAL_PROGRESS_STATUS and not local_progress:
        warnings.append("avance_local_sin_credito_local")
    if status in {"faltante_global", "bloqueada_por_alcance", "no_promocion", "no_exportacion"} and not blocks:
        warnings.append("condicion_global_no_bloquea_readiness")
    if bool(condition.get("global_closure_claim")):
        warnings.append("afirma_cierre_global")
    if bool(condition.get("global_export_claim")):
        warnings.append("afirma_exportacion_global")
    if bool(condition.get("report_layer_promotion_claim")):
        warnings.append("afirma_promocion_report_layer")
    if bool(condition.get("r4_gamma_export_claim")):
        warnings.append("afirma_exportacion_r4_gamma")
    if bool(condition.get("modifies_level_c")):
        warnings.append("modifica_nivel_c")

    return ReadinessConditionResult(
        condition_id=str(condition.get("condition_id", "")),
        front=str(condition.get("front", "")),
        status=status,
        local_progress=local_progress,
        blocks_global_readiness=blocks,
        evidence=evidence,
        gap=str(condition.get("gap", "")),
        passed=not warnings,
        warnings=tuple(sorted(warnings)),
    )


def summarize(results: list[ReadinessConditionResult]) -> dict[str, Any]:
    failures = [result for result in results if not result.passed]
    by_status: dict[str, int] = {}
    by_front: dict[str, int] = {}
    for result in results:
        by_status[result.status] = by_status.get(result.status, 0) + 1
        by_front[result.front] = by_front.get(result.front, 0) + 1
    return {
        "conditions": len(results),
        "passed": len(results) - len(failures),
        "failed": len(failures),
        "findings": len(failures),
        "satisfied_local": by_status.get("satisfecha_local", 0),
        "partial_local": by_status.get("parcial_local", 0),
        "missing_global": by_status.get("faltante_global", 0),
        "scope_blocked": by_status.get("bloqueada_por_alcance", 0),
        "no_promotion": by_status.get("no_promocion", 0),
        "no_export": by_status.get("no_exportacion", 0),
        "local_progress": sum(1 for result in results if result.local_progress),
        "global_blocking": sum(1 for result in results if result.blocks_global_readiness),
        "by_status": by_status,
        "by_front": by_front,
    }


def readiness_result(summary: dict[str, Any]) -> str:
    if summary["failed"]:
        return "mantener_no_autorizado"
    if summary["global_blocking"]:
        return "mantener_no_autorizado"
    return "listo_para_decision_global_posterior"


def build_report(root: Path | None = None, case_file: Path | None = None) -> dict[str, Any]:
    del root
    suite_path = case_file or DEFAULT_CASE_FILE
    suite = load_suite(suite_path)
    results = [evaluate_condition(item) for item in suite.get("conditions", [])]
    summary = summarize(results)
    result = readiness_result(summary)
    failures = [condition for condition in results if not condition.passed]
    return {
        "report_id": "AO-GLOBAL-READINESS-001-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": EXPEDIENTE,
        "algoritmo": ALGORITHM_ID,
        "suite_id": suite.get("suite_id", "AO-GLOBAL-READINESS-MATRIX-001"),
        "resultado": "ok" if not failures else "bloqueado",
        "recomendacion": result,
        "readiness_result": result,
        "ready_for_global_decision": result == "listo_para_decision_global_posterior",
        "transformacion_permitida": False,
        "global_closure_authorized": False,
        "global_export_authorized": False,
        "global_equivalence_authorized": False,
        "global_confluence_authorized": False,
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
            "cierra_equivalencia_global": False,
            "promueve_report_layer": False,
            "exporta_r4_gamma": False,
            "autoriza_transformacion": False,
        },
        "summary": summary,
        "condition_results": [asdict(result_item) for result_item in results],
        "findings": [asdict(result_item) for result_item in failures],
    }


def render_md(report: dict[str, Any]) -> str:
    lines = [
        "# AO_GLOBAL_READINESS_001_REPORT",
        "",
        f"report_id: {report['report_id']}",
        f"expediente: {EXPEDIENTE}",
        f"algoritmo: {ALGORITHM_ID}",
        f"suite_id: {report['suite_id']}",
        f"resultado: {report['resultado']}",
        f"recomendacion: {report['recomendacion']}",
        f"readiness_result: {report['readiness_result']}",
        f"ready_for_global_decision: {str(report['ready_for_global_decision']).lower()}",
        "transformacion_permitida: false",
        "global_closure_authorized: false",
        "global_export_authorized: false",
        "global_equivalence_authorized: false",
        "global_confluence_authorized: false",
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
        f"- no_promotion: {report['summary']['no_promotion']}",
        f"- no_export: {report['summary']['no_export']}",
        f"- global_blocking: {report['summary']['global_blocking']}",
        f"- failed: {report['summary']['failed']}",
        "",
        "## Matriz",
        "",
    ]
    for result in report["condition_results"]:
        status = "PASS" if result["passed"] else "FAIL"
        lines.append(f"- {status} `{result['condition_id']}` ({result['front']}): {result['status']}")
        lines.append(f"  - gap: {result['gap']}")
        lines.append(f"  - evidence: {', '.join(result['evidence'])}")
        if result["warnings"]:
            lines.append(f"  - warnings: {', '.join(result['warnings'])}")
    lines.extend(["", "## Guardas", ""])
    for key, value in report["scope_guard"].items():
        lines.append(f"- {key}: {str(value).lower()}")
    lines.extend(["", "## Dictamen", ""])
    if report["findings"]:
        lines.append("- Hay fallos de expectativa; no usar la matriz.")
    elif report["readiness_result"] == "listo_para_decision_global_posterior":
        lines.append("- No se autoriza cierre automatico; solo queda lista una decision global posterior.")
    else:
        lines.append("- Resultado consolidado: mantener_no_autorizado.")
        lines.append("- AO-PPI-BRIDGE-004 conserva valor como estado actual local de deudas AO-PPI.")
    return "\n".join(lines) + "\n"


def assert_inside(root: Path, path: Path) -> None:
    root_resolved = root.resolve()
    path_resolved = path.resolve()
    if path_resolved != root_resolved and root_resolved not in path_resolved.parents:
        raise SystemExit(f"Ruta fuera del repositorio: {path}")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Matriz AO de readiness global no mutante.")
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
