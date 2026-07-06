#!/usr/bin/env python3
"""Matriz no mutante AO-PPI-BRIDGE-003.

Prepara condiciones faltantes para cierre global de Confluencia y
Equivalencia usando AO-PPI-BRIDGE-002 como evidencia local fuerte. Tambien
evalua casos heterogeneos de REPORT_LAYER sin promoverlo ni autorizar cambios.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ALGORITHM_ID = "AO-PPI-BRIDGE-003"
EXPEDIENTE = "AO-001"
DEFAULT_CASE_FILE = Path(__file__).resolve().parent / "fixtures" / "ao_ppi_bridge_003_matrix.json"

VALID_CONDITION_STATUS = {
    "satisfecha_local",
    "faltante_global",
    "bloqueada_por_alcance",
}

C002_REQUIRED_FIELDS = {
    "report_id",
    "artefacto_revisado",
    "operador_fase",
    "resultado",
    "tipo_hallazgo",
    "ubicacion",
    "evidencia",
    "estatus_afirmacion",
    "decisiones_permitidas",
    "decision_emitida",
    "transformacion_permitida",
    "dependencias",
    "deudas_generadas",
    "recomendacion",
}

HET_REQUIRED_FIELDS = {
    "source_family",
    "witness",
    "projection_target",
    "projection_family",
}

SAFE_REPORT_LAYER_OUTCOMES = {
    "compatible_heterogeneo_no_mutante",
    "bloqueo_campo_minimo",
    "bloqueo_testigo",
    "bloqueo_autoridad",
    "bloqueo_modo_mutante",
    "bloqueo_recomendacion_como_decision",
    "bloqueo_historial_autoridad",
    "divergencia_clasificada",
}


@dataclass(frozen=True)
class ConditionResult:
    condition_id: str
    domain: str
    status: str
    expected_effect: str
    blocks_global_closure: bool
    local_credit: bool
    passed: bool
    gap: str
    warnings: tuple[str, ...]


@dataclass(frozen=True)
class ReportLayerResult:
    case_id: str
    expected: str
    actual: str
    passed: bool
    detail: str
    blockers: tuple[str, ...]
    warnings: tuple[str, ...]


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def is_empty(value: Any) -> bool:
    return value is None or value == "" or value == []


def load_suite(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def missing_fields(item: dict[str, Any], fields: set[str]) -> list[str]:
    return sorted(field for field in fields if field not in item or is_empty(item[field]))


def evaluate_condition(condition: dict[str, Any]) -> ConditionResult:
    status = str(condition.get("status", ""))
    warnings: list[str] = []
    if status not in VALID_CONDITION_STATUS:
        warnings.append(f"status_no_reconocido:{status}")
    if is_empty(condition.get("evidence")):
        warnings.append("evidencia_vacia")
    if status == "satisfecha_local" and not bool(condition.get("local_credit")):
        warnings.append("sin_credito_local")
    if status != "satisfecha_local" and not bool(condition.get("blocks_global_closure")):
        warnings.append("faltante_no_bloquea_cierre")

    return ConditionResult(
        condition_id=str(condition.get("condition_id", "")),
        domain=str(condition.get("domain", "")),
        status=status,
        expected_effect=str(condition.get("closure_effect", "")),
        blocks_global_closure=bool(condition.get("blocks_global_closure")),
        local_credit=bool(condition.get("local_credit")),
        passed=not warnings,
        gap=str(condition.get("gap", "")),
        warnings=tuple(sorted(warnings)),
    )


def evaluate_report_layer_case(case: dict[str, Any]) -> ReportLayerResult:
    item = dict(case.get("report_layer", {}))
    blockers: list[str] = []
    warnings: list[str] = []

    missing = missing_fields(item, C002_REQUIRED_FIELDS | (HET_REQUIRED_FIELDS - {"witness"}))
    if not str(item.get("witness", "")).strip():
        blockers.append("witness:ausente")
        actual = "bloqueo_testigo"
    elif missing:
        blockers.extend(f"missing:{field}" for field in missing)
        actual = "bloqueo_campo_minimo"
    elif str(item.get("source_kind")) == "historico" and str(item.get("authority_claim")) != "registro_historico_no_autoridad":
        blockers.append(f"historial_como_autoridad:{item.get('authority_claim')}")
        actual = "bloqueo_historial_autoridad"
    elif str(item.get("authority_claim")) in {"nivel_c", "canon"} or bool(item.get("promueve_report_layer")):
        blockers.append(f"autoridad_no_autorizada:{item.get('authority_claim')}")
        actual = "bloqueo_autoridad"
    elif bool(item.get("recomendacion_convertida_en_decision")):
        blockers.append("recomendacion_convertida_en_decision")
        actual = "bloqueo_recomendacion_como_decision"
    elif bool(item.get("transformacion_permitida")) or str(item.get("decision_emitida")) == "continuar_con_cambio_acotado":
        blockers.append("modo_mutante_no_autorizado")
        actual = "bloqueo_modo_mutante"
    elif item.get("expected_projection_family") and item.get("expected_projection_family") != item.get("projection_family"):
        warnings.append("projection_family:diverge")
        actual = "divergencia_clasificada"
    else:
        if str(item.get("projection_target")) != "Pi_rep":
            warnings.append(f"projection_target_no_estandar:{item.get('projection_target')}")
        actual = "compatible_heterogeneo_no_mutante"

    if actual not in SAFE_REPORT_LAYER_OUTCOMES:
        actual = "bloqueo_campo_minimo"

    expected = str(case.get("expected"))
    return ReportLayerResult(
        case_id=str(case.get("case_id")),
        expected=expected,
        actual=actual,
        passed=actual == expected,
        detail=str(case.get("description", "")),
        blockers=tuple(sorted(blockers)),
        warnings=tuple(sorted(warnings)),
    )


def summarize_conditions(results: list[ConditionResult]) -> dict[str, Any]:
    by_status: dict[str, int] = {}
    by_domain: dict[str, int] = {}
    for result in results:
        by_status[result.status] = by_status.get(result.status, 0) + 1
        by_domain[result.domain] = by_domain.get(result.domain, 0) + 1
    missing_or_blocked = sum(
        1 for result in results
        if result.status in {"faltante_global", "bloqueada_por_alcance"} or result.blocks_global_closure
    )
    local_satisfied = sum(1 for result in results if result.status == "satisfecha_local" and result.local_credit)
    return {
        "conditions": len(results),
        "passed": sum(1 for result in results if result.passed),
        "failed": sum(1 for result in results if not result.passed),
        "findings": sum(1 for result in results if not result.passed),
        "local_satisfied": local_satisfied,
        "missing_or_blocking": missing_or_blocked,
        "by_status": by_status,
        "by_domain": by_domain,
    }


def summarize_report_layer(results: list[ReportLayerResult]) -> dict[str, Any]:
    by_outcome: dict[str, int] = {}
    for result in results:
        by_outcome[result.actual] = by_outcome.get(result.actual, 0) + 1
    failures = [result for result in results if not result.passed]
    return {
        "cases": len(results),
        "passed": len(results) - len(failures),
        "failed": len(failures),
        "findings": len(failures),
        "by_outcome": by_outcome,
    }


def build_report(root: Path | None = None, case_file: Path | None = None) -> dict[str, Any]:
    del root
    suite_path = case_file or DEFAULT_CASE_FILE
    suite = load_suite(suite_path)
    condition_results = [evaluate_condition(item) for item in suite.get("conditions", [])]
    report_layer_results = [evaluate_report_layer_case(item) for item in suite.get("report_layer_cases", [])]
    condition_summary = summarize_conditions(condition_results)
    report_layer_summary = summarize_report_layer(report_layer_results)
    findings = [
        *(result for result in condition_results if not result.passed),
        *(result for result in report_layer_results if not result.passed),
    ]
    closure_authorized = False
    resultado = "ok" if not findings else "bloqueado"
    return {
        "report_id": "AO-PPI-BRIDGE-003-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": EXPEDIENTE,
        "algoritmo": ALGORITHM_ID,
        "suite_id": suite.get("suite_id", "AO-PPI-BRIDGE-003-MATRIX"),
        "resultado": resultado,
        "recomendacion": "mantener_cierre_global_no_autorizado" if not findings else "revisar_matriz_ao_ppi_003",
        "transformacion_permitida": False,
        "global_closure_authorized": closure_authorized,
        "source_evidence": suite.get("source_evidence", []),
        "scope_guard": {
            "modifica_doc04": False,
            "modifica_canon": False,
            "crea_nivel_c": False,
            "reabre_p_pi_0": False,
            "reabre_p_pi_1": False,
            "cierra_confluencia_global": False,
            "cierra_equivalencia_global": False,
            "promueve_report_layer": False,
            "promueve_r4_gamma": False,
            "autoriza_transformacion": False,
        },
        "condition_summary": condition_summary,
        "report_layer_summary": report_layer_summary,
        "summary": {
            "conditions": condition_summary["conditions"],
            "report_layer_cases": report_layer_summary["cases"],
            "passed": condition_summary["passed"] + report_layer_summary["passed"],
            "failed": condition_summary["failed"] + report_layer_summary["failed"],
            "findings": condition_summary["findings"] + report_layer_summary["findings"],
            "global_closure_authorized": closure_authorized,
        },
        "condition_results": [asdict(result) for result in condition_results],
        "report_layer_results": [asdict(result) for result in report_layer_results],
        "findings": [asdict(result) for result in findings],
    }


def render_md(report: dict[str, Any]) -> str:
    lines = [
        "# AO_PPI_BRIDGE_003_REPORT",
        "",
        f"report_id: {report['report_id']}",
        f"expediente: {EXPEDIENTE}",
        f"algoritmo: {ALGORITHM_ID}",
        f"suite_id: {report['suite_id']}",
        f"resultado: {report['resultado']}",
        f"recomendacion: {report['recomendacion']}",
        "transformacion_permitida: false",
        f"global_closure_authorized: {str(report['global_closure_authorized']).lower()}",
        "",
        "## Evidencia fuente",
        "",
    ]
    for item in report["source_evidence"]:
        lines.append(f"- {item}")
    lines.extend([
        "",
        "## Resumen",
        "",
        f"- conditions: {report['condition_summary']['conditions']}",
        f"- local_satisfied: {report['condition_summary']['local_satisfied']}",
        f"- missing_or_blocking: {report['condition_summary']['missing_or_blocking']}",
        f"- report_layer_cases: {report['report_layer_summary']['cases']}",
        f"- report_layer_passed: {report['report_layer_summary']['passed']}",
        f"- report_layer_failed: {report['report_layer_summary']['failed']}",
        "",
        "## Guardas de alcance",
        "",
    ])
    for key, value in report["scope_guard"].items():
        lines.append(f"- {key}: {str(value).lower()}")
    lines.extend(["", "## Matriz de condiciones", ""])
    for result in report["condition_results"]:
        status = "PASS" if result["passed"] else "FAIL"
        lines.append(f"- {status} `{result['condition_id']}` ({result['domain']}): {result['status']} / {result['expected_effect']}")
        lines.append(f"  - gap: {result['gap']}")
        if result["warnings"]:
            lines.append(f"  - warnings: `{', '.join(result['warnings'])}`")
    lines.extend(["", "## Casos heterogeneos REPORT_LAYER", ""])
    for result in report["report_layer_results"]:
        status = "PASS" if result["passed"] else "FAIL"
        lines.append(f"- {status} `{result['case_id']}`: {result['actual']} (esperado: {result['expected']})")
        if result["blockers"]:
            lines.append(f"  - blockers: `{', '.join(result['blockers'])}`")
        if result["warnings"]:
            lines.append(f"  - warnings: `{', '.join(result['warnings'])}`")
    lines.extend(["", "## Dictamen", ""])
    if report["findings"]:
        lines.append("- Hay fallos de expectativa; no usar la matriz como base decisoria.")
    else:
        lines.append("- Sin hallazgos bloqueantes.")
        lines.append("- La matriz acredita avance local fuerte, pero mantiene cierre global no autorizado.")
        lines.append("- REPORT_LAYER queda ampliado con casos heterogeneos no mutantes y permanece local pre-C.")
    return "\n".join(lines) + "\n"


def assert_inside(root: Path, path: Path) -> None:
    root_resolved = root.resolve()
    path_resolved = path.resolve()
    if path_resolved != root_resolved and root_resolved not in path_resolved.parents:
        raise SystemExit(f"Ruta fuera del repositorio: {path}")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Matriz AO-PPI-BRIDGE-003 no mutante.")
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
    output = render_md(report) if args.format == "md" else json.dumps(report, ensure_ascii=True, indent=2) + "\n"
    if args.output:
        out_path = root / args.output
        assert_inside(root, out_path)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output, encoding="utf-8")
    else:
        sys.stdout.write(output)
    return 0 if report["resultado"] == "ok" else 2


if __name__ == "__main__":
    raise SystemExit(main())
