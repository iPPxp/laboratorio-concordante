#!/usr/bin/env python3
"""Pruebas no mutantes de AO-DOC04-WIDE-001.

La herramienta evalua casos sinteticos para la formalizacion amplia de
Documento 04 y la relacion local con REPORT_LAYER. No modifica documentos,
no crea Nivel C, no autoriza transformaciones y no cierra problemas globales.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ALGORITHM_ID = "AO-DOC04-WIDE-TEST-001"
EXPEDIENTE = "AO-001"
DEFAULT_CASE_FILE = Path(__file__).resolve().parent / "fixtures" / "ao_doc04_wide_cases.json"

SAFE_OUTPUTS = {
    "equivalencia_local",
    "confluencia_local",
    "no_autorizado_sin_transformar",
    "bloqueo_por_testigo",
    "bloqueo_por_evidencia",
    "bloqueo_por_autoridad",
    "bloqueo_report_layer_incompleto",
    "bloqueo_exportacion_r4_gamma",
    "divergencia_clasificada",
}

AUTHORITY_ORDER = {
    "historico": 0,
    "expediente": 1,
    "documento": 2,
    "nivel_c": 3,
    "canon": 4,
}

REPORT_LAYER_REQUIRED = {
    "report_id",
    "objeto",
    "operador_abstracto",
    "clase_reporte",
    "resultado",
    "evidencia",
    "estatus_afirmacion",
    "decisiones_permitidas",
    "decision_emitida",
    "transformacion_permitida",
    "deudas_generadas",
}


@dataclass(frozen=True)
class CaseResult:
    case_id: str
    operation: str
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


def missing_common_fields(projection: dict[str, Any]) -> list[str]:
    missing: list[str] = []
    for field in ("context", "witness", "evidence", "status", "authority", "authority_claim", "output_family", "rule_id"):
        value = projection.get(field)
        if value is None or value == "" or value == []:
            missing.append(field)
    return missing


def authority_blocker(projection: dict[str, Any]) -> str | None:
    authority = str(projection.get("authority", "historico"))
    claim = str(projection.get("authority_claim", authority))
    if AUTHORITY_ORDER.get(claim, 99) > AUTHORITY_ORDER.get(authority, 99) + 1:
        return f"authority_increase:{authority}->{claim}"
    return None


def report_layer_blockers(projection: dict[str, Any]) -> list[str]:
    if projection.get("projection") != "Pi_rep":
        return []
    report_item = projection.get("report_layer")
    if report_item is None:
        return ["report_layer:missing"]
    missing = sorted(REPORT_LAYER_REQUIRED - set(report_item))
    return [f"report_layer:missing:{field}" for field in missing]


def projection_blockers(projection: dict[str, Any]) -> list[str]:
    blockers: list[str] = []
    missing = missing_common_fields(projection)
    blockers.extend(f"missing:{field}" for field in missing)
    auth = authority_blocker(projection)
    if auth:
        blockers.append(auth)
    blockers.extend(report_layer_blockers(projection))
    permission = dict(projection.get("permission", {}))
    if projection.get("requires_transform") and not permission.get("transformacion_permitida", False):
        blockers.append("permission:transformacion_no_autorizada")
    if projection.get("r4_gamma_export") == "general":
        blockers.append("r4_gamma:exportacion_general")
    return sorted(blockers)


def classify_blockers(blockers: list[str]) -> str | None:
    if not blockers:
        return None
    if any(item == "missing:witness" for item in blockers):
        return "bloqueo_por_testigo"
    if any(item.startswith("report_layer:") for item in blockers):
        return "bloqueo_report_layer_incompleto"
    if any(item.startswith("permission:") for item in blockers):
        return "no_autorizado_sin_transformar"
    if any(item.startswith("authority_increase:") for item in blockers):
        return "bloqueo_por_autoridad"
    if any(item.startswith("r4_gamma:") for item in blockers):
        return "bloqueo_exportacion_r4_gamma"
    return "bloqueo_por_evidencia"


def signature(projection: dict[str, Any]) -> tuple[Any, ...]:
    invariants = tuple(sorted(str(item) for item in as_list(projection.get("invariants"))))
    return (
        projection.get("output_family"),
        projection.get("rule_id"),
        invariants,
        bool(dict(projection.get("permission", {})).get("transformacion_permitida", False)),
    )


def debt_preserved(case: dict[str, Any], projections: list[dict[str, Any]]) -> bool:
    required = set(str(item) for item in as_list(case.get("required_debt")))
    if not required:
        return True
    present: set[str] = set()
    for projection in projections:
        present.update(str(item) for item in as_list(projection.get("debt")))
        report_item = projection.get("report_layer") or {}
        present.update(str(item) for item in as_list(report_item.get("deudas_generadas")))
        trace = projection.get("operator_trace") or {}
        present.update(str(item) for item in as_list(trace.get("deuda")))
    return required.issubset(present)


def eval_pair(case: dict[str, Any], success_output: str) -> tuple[str, tuple[str, ...], tuple[str, ...]]:
    left = dict(case.get("left", {}))
    right = dict(case.get("right", {}))
    blockers = projection_blockers(left) + projection_blockers(right)
    blocked = classify_blockers(blockers)
    if blocked:
        return blocked, tuple(sorted(blockers)), tuple()
    if not debt_preserved(case, [left, right]):
        return "bloqueo_por_evidencia", ("debt:not_preserved",), tuple()
    if signature(left) == signature(right):
        return success_output, tuple(), tuple()
    return "divergencia_clasificada", tuple(), ("projection:signature_differs",)


def eval_gate(case: dict[str, Any]) -> tuple[str, tuple[str, ...], tuple[str, ...]]:
    operator = dict(case.get("operator", {}))
    blockers = projection_blockers(operator)
    blocked = classify_blockers(blockers)
    if blocked:
        return blocked, tuple(sorted(blockers)), tuple()
    return "equivalencia_local", tuple(), ("gate:no_material_action_requested",)


def eval_r4_gamma(case: dict[str, Any]) -> tuple[str, tuple[str, ...], tuple[str, ...]]:
    operator = dict(case.get("operator", {}))
    blockers = projection_blockers(operator)
    blocked = classify_blockers(blockers)
    if blocked:
        return blocked, tuple(sorted(blockers)), tuple()
    return "equivalencia_local", tuple(), ("r4_gamma:perfil_restringido_local",)


def evaluate_case(case: dict[str, Any]) -> CaseResult:
    operation = str(case.get("operation", ""))
    if operation == "Eq_local":
        actual, blockers, warnings = eval_pair(case, "equivalencia_local")
    elif operation == "Conf_local":
        actual, blockers, warnings = eval_pair(case, "confluencia_local")
    elif operation == "Gate_AO":
        actual, blockers, warnings = eval_gate(case)
    elif operation == "R4Gamma_AO":
        actual, blockers, warnings = eval_r4_gamma(case)
    else:
        actual, blockers, warnings = "bloqueo_por_evidencia", ("operation:unknown",), tuple()
    if actual not in SAFE_OUTPUTS:
        actual = "bloqueo_por_evidencia"
    expected = str(case.get("expected"))
    return CaseResult(
        case_id=str(case.get("case_id")),
        operation=operation,
        expected=expected,
        actual=actual,
        passed=actual == expected,
        detail=f"{operation} => {actual}",
        blockers=tuple(sorted(blockers)),
        warnings=tuple(sorted(warnings)),
    )


def load_suite(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def summarize_by_operation(results: list[CaseResult]) -> dict[str, dict[str, int]]:
    summary: dict[str, dict[str, int]] = {}
    for result in results:
        entry = summary.setdefault(result.operation, {"cases": 0, "passed": 0, "failed": 0})
        entry["cases"] += 1
        if result.passed:
            entry["passed"] += 1
        else:
            entry["failed"] += 1
    return summary


def build_report(root: Path | None = None, case_file: Path | None = None) -> dict[str, Any]:
    del root
    suite_path = case_file or DEFAULT_CASE_FILE
    suite = load_suite(suite_path)
    results = [evaluate_case(case) for case in suite.get("cases", [])]
    failures = [result for result in results if not result.passed]
    resultado = "ok" if not failures else "bloqueado"
    return {
        "report_id": "AO-DOC04-WIDE-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": EXPEDIENTE,
        "algoritmo": ALGORITHM_ID,
        "suite_id": suite.get("suite_id", "AO-DOC04-WIDE-CASES-001"),
        "resultado": resultado,
        "recomendacion": "precisar_report_layer_sin_promocion" if not failures else "revisar_doc04_wide_cases",
        "transformacion_permitida": False,
        "summary": {
            "cases": len(results),
            "passed": len(results) - len(failures),
            "failed": len(failures),
            "findings": len(failures),
            "by_operation": summarize_by_operation(results),
        },
        "scope_guard": {
            "modifica_doc04": False,
            "modifica_canon": False,
            "crea_nivel_c": False,
            "promueve_report_layer": False,
            "cierra_confluencia_global": False,
            "cierra_equivalencia_global": False,
            "promueve_r4_gamma": False,
            "autoriza_transformacion": False,
        },
        "report_layer_relation": {
            "estatus": "local_pre_c",
            "rol_ao": "entrada_de_Pi_rep_y_evidencia_de_reporte",
            "no_sustituye": ["Op_AO", "decision", "permiso", "verificacion_posterior", "Nivel_C"],
        },
        "debt_guard": {
            "confluencia_global_abierta": True,
            "equivalencia_global_abierta": True,
            "report_layer_nivel_c_abierto": True,
            "r4_gamma_exportacion_general_bloqueada": True,
            "tcs_maduracion_abierta": True,
        },
        "results": [asdict(result) for result in results],
        "findings": [asdict(result) for result in failures],
    }


def render_md(report: dict[str, Any]) -> str:
    lines = [
        "# AO_DOC04_WIDE_TEST_REPORT",
        "",
        f"report_id: {report['report_id']}",
        f"expediente: {EXPEDIENTE}",
        f"algoritmo: {ALGORITHM_ID}",
        f"suite_id: {report['suite_id']}",
        f"resultado: {report['resultado']}",
        f"recomendacion: {report['recomendacion']}",
        "transformacion_permitida: false",
        "",
        "## Resumen",
        "",
        f"- cases: {report['summary']['cases']}",
        f"- passed: {report['summary']['passed']}",
        f"- failed: {report['summary']['failed']}",
        "",
        "## Relacion REPORT_LAYER",
        "",
        f"- estatus: {report['report_layer_relation']['estatus']}",
        f"- rol_ao: {report['report_layer_relation']['rol_ao']}",
        f"- no_sustituye: {', '.join(report['report_layer_relation']['no_sustituye'])}",
        "",
        "## Guardas de alcance",
        "",
    ]
    for key, value in report["scope_guard"].items():
        lines.append(f"- {key}: {str(value).lower()}")
    lines.extend(["", "## Deudas conservadas abiertas", ""])
    for key, value in report["debt_guard"].items():
        lines.append(f"- {key}: {str(value).lower()}")
    lines.extend(["", "## Resultados", ""])
    for result in report["results"]:
        status = "PASS" if result["passed"] else "FAIL"
        lines.append(f"- {status} `{result['case_id']}` (`{result['operation']}`): {result['detail']}")
        if result["blockers"]:
            lines.append(f"  - blockers: `{', '.join(result['blockers'])}`")
        if result["warnings"]:
            lines.append(f"  - warnings: `{', '.join(result['warnings'])}`")
    if not report["findings"]:
        lines.extend(["", "## Hallazgos", "", "- Sin hallazgos bloqueantes."])
    return "\n".join(lines) + "\n"


def assert_inside(root: Path, path: Path) -> None:
    root_resolved = root.resolve()
    path_resolved = path.resolve()
    if path_resolved != root_resolved and root_resolved not in path_resolved.parents:
        raise SystemExit(f"Salida fuera del repositorio: {path}")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Pruebas no mutantes de AO-DOC04-WIDE-001.")
    parser.add_argument("--case-file", help="Fixture JSON opcional.")
    parser.add_argument("--format", choices=("json", "md"), default="md")
    parser.add_argument("--output", help="Ruta opcional de salida.")
    args = parser.parse_args(argv)

    root = Path.cwd()
    case_file = Path(args.case_file) if args.case_file else DEFAULT_CASE_FILE
    if not case_file.is_absolute():
        case_file = root / case_file
    report = build_report(root, case_file)
    output = json.dumps(report, ensure_ascii=True, indent=2) + "\n"
    if args.format == "md":
        output = render_md(report)
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
