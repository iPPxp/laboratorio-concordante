#!/usr/bin/env python3
"""Compuerta no mutante para REPORT_LAYER bajo C-002.

La herramienta valida casos sinteticos de REPORT_LAYER como capa local pre-C.
No transforma artefactos, no decide autoridad y no promueve REPORT_LAYER a Nivel C.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ALGORITHM_ID = "REPORT-LAYER-C002-GATE-001"
EXPEDIENTE = "AUT-003"
DEFAULT_CASE_FILE = Path(__file__).resolve().parent / "fixtures" / "report_layer_c002_cases.json"

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

SAFE_OUTCOMES = {
    "compatible_no_mutante",
    "bloqueo_campos_minimos",
    "bloqueo_recomendacion_como_decision",
    "bloqueo_modo_mutante",
    "bloqueo_promocion_nivel_c",
    "bloqueo_historial_autoridad",
    "bloqueo_permiso_material",
}

NON_MUTANT_DECISIONS = {
    "no_aplica",
    "bloquear",
    "escalar",
    "continuar_sin_transformar",
}


@dataclass(frozen=True)
class GateResult:
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


def missing_fields(item: dict[str, Any]) -> list[str]:
    missing: list[str] = []
    for field in sorted(C002_REQUIRED_FIELDS):
        if field not in item or is_empty(item[field]):
            missing.append(field)
    return missing


def evaluate_report_item(case: dict[str, Any]) -> tuple[str, tuple[str, ...], tuple[str, ...]]:
    item = dict(case.get("report_layer", {}))
    blockers: list[str] = []
    warnings: list[str] = []

    missing = missing_fields(item)
    if missing:
        blockers.extend(f"missing:{field}" for field in missing)
        return "bloqueo_campos_minimos", tuple(sorted(blockers)), tuple(warnings)

    source_kind = str(item.get("source_kind", "local"))
    authority_claim = str(item.get("authority_claim", "local_pre_c"))
    if source_kind == "historico" and authority_claim != "registro_historico_no_autoridad":
        blockers.append(f"historial_como_autoridad:{authority_claim}")
        return "bloqueo_historial_autoridad", tuple(sorted(blockers)), tuple(warnings)

    if authority_claim in {"nivel_c", "canon"} or bool(item.get("promueve_report_layer")):
        blockers.append(f"promocion_no_autorizada:{authority_claim}")
        return "bloqueo_promocion_nivel_c", tuple(sorted(blockers)), tuple(warnings)

    if bool(item.get("recomendacion_convertida_en_decision")):
        blockers.append("recomendacion_convertida_en_decision")
        return "bloqueo_recomendacion_como_decision", tuple(sorted(blockers)), tuple(warnings)

    if bool(item.get("transformacion_permitida")):
        blockers.append("transformacion_permitida_true")
        return "bloqueo_modo_mutante", tuple(sorted(blockers)), tuple(warnings)

    decision = str(item.get("decision_emitida"))
    if decision == "continuar_con_cambio_acotado":
        blockers.append("decision_mutante_sin_permiso_act_001")
        return "bloqueo_permiso_material", tuple(sorted(blockers)), tuple(warnings)

    if decision not in NON_MUTANT_DECISIONS:
        warnings.append(f"decision_no_mutante_no_estandar:{decision}")

    if not as_list(item.get("evidencia")):
        blockers.append("evidencia_vacia")
        return "bloqueo_campos_minimos", tuple(sorted(blockers)), tuple(warnings)

    return "compatible_no_mutante", tuple(), tuple(sorted(warnings))


def evaluate_case(case: dict[str, Any]) -> GateResult:
    actual, blockers, warnings = evaluate_report_item(case)
    if actual not in SAFE_OUTCOMES:
        actual = "bloqueo_campos_minimos"
    expected = str(case.get("expected"))
    return GateResult(
        case_id=str(case.get("case_id")),
        expected=expected,
        actual=actual,
        passed=actual == expected,
        detail=str(case.get("description", "")),
        blockers=blockers,
        warnings=warnings,
    )


def load_suite(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def summarize(results: list[GateResult]) -> dict[str, Any]:
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
    results = [evaluate_case(case) for case in suite.get("cases", [])]
    failures = [result for result in results if not result.passed]
    resultado = "ok" if not failures else "bloqueado"
    return {
        "report_id": "REPORT-LAYER-C002-GATE-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": EXPEDIENTE,
        "algoritmo": ALGORITHM_ID,
        "suite_id": suite.get("suite_id", "REPORT-LAYER-C002-CASES-001"),
        "resultado": resultado,
        "recomendacion": "mantener_report_layer_local_pre_c" if not failures else "revisar_report_layer_c002",
        "transformacion_permitida": False,
        "conforme_c002_no_mutante": not failures,
        "scope_guard": {
            "modifica_c001": False,
            "modifica_c002": False,
            "crea_nivel_c": False,
            "promueve_report_layer": False,
            "autoriza_transformacion": False,
            "emite_decision_autoridad": False,
            "usa_historial_como_autoridad": False,
        },
        "c002_guard": {
            "fuente_normativa": "02_Documentos/C-002_RFC_Operativo_Auditor_v0.md",
            "campos_requeridos": sorted(C002_REQUIRED_FIELDS),
            "separa_recomendacion_decision_permiso": True,
            "modo_mutante_bloqueado": True,
        },
        "summary": summarize(results),
        "results": [asdict(result) for result in results],
        "findings": [asdict(result) for result in failures],
    }


def render_md(report: dict[str, Any]) -> str:
    lines = [
        "# REPORT_LAYER_C002_GATE_REPORT",
        "",
        f"report_id: {report['report_id']}",
        f"expediente: {EXPEDIENTE}",
        f"algoritmo: {ALGORITHM_ID}",
        f"suite_id: {report['suite_id']}",
        f"resultado: {report['resultado']}",
        f"recomendacion: {report['recomendacion']}",
        "transformacion_permitida: false",
        f"conforme_c002_no_mutante: {str(report['conforme_c002_no_mutante']).lower()}",
        "",
        "## Resumen",
        "",
        f"- cases: {report['summary']['cases']}",
        f"- passed: {report['summary']['passed']}",
        f"- failed: {report['summary']['failed']}",
        "",
        "## Guardas",
        "",
    ]
    for key, value in report["scope_guard"].items():
        lines.append(f"- {key}: {str(value).lower()}")
    lines.extend(["", "## Casos", ""])
    for result in report["results"]:
        status = "PASS" if result["passed"] else "FAIL"
        lines.append(f"- {status} `{result['case_id']}`: {result['actual']} (esperado: {result['expected']})")
        if result["blockers"]:
            lines.append(f"  - bloqueos: {', '.join(result['blockers'])}")
        if result["warnings"]:
            lines.append(f"  - advertencias: {', '.join(result['warnings'])}")
    lines.extend(["", "## Dictamen", ""])
    if report["findings"]:
        lines.append("- Hay casos fallidos; no usar REPORT_LAYER como base de modo mutante.")
    else:
        lines.append("- Sin hallazgos bloqueantes.")
        lines.append("- REPORT_LAYER permanece como capa local pre-C; cualquier modo mutante futuro requiere decision separada.")
    return "\n".join(lines) + "\n"


def assert_inside(root: Path, path: Path) -> None:
    root_resolved = root.resolve()
    path_resolved = path.resolve()
    if path_resolved != root_resolved and root_resolved not in path_resolved.parents:
        raise SystemExit(f"Ruta fuera del repositorio: {path}")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Compuerta no mutante REPORT_LAYER/C-002.")
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
