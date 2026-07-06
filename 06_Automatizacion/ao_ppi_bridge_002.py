#!/usr/bin/env python3
"""Bateria fuerte no mutante para AO-PPI-BRIDGE-002.

Evalua casos sinteticos de Confluencia y Equivalencia de proyecciones.
No modifica artefactos, no reabre P-PI.0/P-PI.1 y no cierra problemas
globales.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ALGORITHM_ID = "AO-PPI-BRIDGE-002"
EXPEDIENTE = "AO-001"
DEFAULT_CASE_FILE = Path(__file__).resolve().parent / "fixtures" / "ao_ppi_bridge_002_cases.json"

SAFE_OUTCOMES = {
    "equivalencia_fuerte_local",
    "confluencia_fuerte_local",
    "divergencia_clasificada",
    "bloqueo_por_testigo",
    "bloqueo_report_layer_incompleto",
    "bloqueo_por_autoridad",
    "bloqueo_por_deuda",
    "no_comparable",
}

AUTHORITY_ORDER = {
    "historico": 0,
    "expediente": 1,
    "documento": 2,
    "nivel_c": 3,
    "canon": 4,
}

REQUIRED_FIELDS = {
    "name",
    "witness",
    "artifact_id",
    "status",
    "evidence",
    "decision",
    "permission",
    "output_family",
    "rule_id",
    "debt",
    "authority",
    "authority_claim",
}


@dataclass(frozen=True)
class CaseResult:
    case_id: str
    kind: str
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
    return sorted(field for field in REQUIRED_FIELDS if field not in item or is_empty(item[field]))


def authority_blocker(item: dict[str, Any]) -> str | None:
    authority = str(item.get("authority", "historico"))
    claim = str(item.get("authority_claim", authority))
    if AUTHORITY_ORDER.get(claim, 99) > AUTHORITY_ORDER.get(authority, 99) + 1:
        return f"autoridad_aumentada:{authority}->{claim}"
    return None


def item_blockers(item: dict[str, Any]) -> list[str]:
    blockers: list[str] = []
    blockers.extend(f"missing:{field}" for field in missing_fields(item))
    auth = authority_blocker(item)
    if auth:
        blockers.append(auth)
    if bool(dict(item.get("permission", {})).get("transformacion_permitida", False)):
        blockers.append("permission:transformacion_permitida")
    if item.get("name") in {"Pi_rep", "ruta_reporte"} and item.get("report_layer_complete") is False:
        blockers.append("report_layer:incompleto")
    if bool(item.get("closes_global")):
        blockers.append("scope:cierre_global_no_autorizado")
    return sorted(blockers)


def classify_blockers(blockers: list[str]) -> str | None:
    if not blockers:
        return None
    if any(item.startswith("missing:witness") for item in blockers):
        return "bloqueo_por_testigo"
    if any(item.startswith("report_layer:") for item in blockers):
        return "bloqueo_report_layer_incompleto"
    if any(item.startswith("autoridad_aumentada:") for item in blockers):
        return "bloqueo_por_autoridad"
    if any(item.startswith("debt:") for item in blockers):
        return "bloqueo_por_deuda"
    if any(item.startswith("scope:") for item in blockers):
        return "no_comparable"
    if any(item.startswith("permission:") for item in blockers):
        return "no_comparable"
    return "no_comparable"


def projection_signature(item: dict[str, Any]) -> tuple[Any, ...]:
    debt = tuple(sorted(str(entry) for entry in as_list(item.get("debt"))))
    evidence = tuple(sorted(str(entry) for entry in as_list(item.get("evidence"))))
    permission = bool(dict(item.get("permission", {})).get("transformacion_permitida", False))
    return (
        item.get("artifact_id"),
        item.get("status"),
        evidence,
        item.get("decision"),
        permission,
        item.get("output_family"),
        item.get("rule_id"),
        debt,
    )


def common_witness(items: list[dict[str, Any]]) -> bool:
    witnesses = [str(item.get("witness")) for item in items if not is_empty(item.get("witness"))]
    return len(witnesses) == len(items) and len(set(witnesses)) == 1


def required_debt_preserved(case: dict[str, Any], items: list[dict[str, Any]]) -> bool:
    required = {str(entry) for entry in as_list(case.get("required_debt"))}
    if not required:
        return True
    for item in items:
        present = {str(entry) for entry in as_list(item.get("debt"))}
        if not required.issubset(present):
            return False
    return True


def evaluate_items(case: dict[str, Any], items: list[dict[str, Any]], success_outcome: str) -> tuple[str, tuple[str, ...], tuple[str, ...]]:
    blockers = [blocker for item in items for blocker in item_blockers(item)]
    blocked = classify_blockers(blockers)
    if blocked:
        return blocked, tuple(sorted(blockers)), tuple()
    if not common_witness(items):
        return "bloqueo_por_testigo", ("witness:no_comun",), tuple()
    if not required_debt_preserved(case, items):
        return "bloqueo_por_deuda", ("debt:required_not_preserved",), tuple()
    signatures = {projection_signature(item) for item in items}
    if len(signatures) == 1:
        return success_outcome, tuple(), tuple()
    return "divergencia_clasificada", tuple(), ("signature:diverge_bajo_testigo",)


def evaluate_case(case: dict[str, Any]) -> CaseResult:
    kind = str(case.get("kind"))
    if kind == "equivalence":
        actual, blockers, warnings = evaluate_items(case, [dict(item) for item in case.get("projections", [])], "equivalencia_fuerte_local")
    elif kind == "confluence":
        actual, blockers, warnings = evaluate_items(case, [dict(item) for item in case.get("routes", [])], "confluencia_fuerte_local")
    else:
        actual, blockers, warnings = "no_comparable", ("case:kind_unknown",), tuple()
    if actual not in SAFE_OUTCOMES:
        actual = "no_comparable"
    expected = str(case.get("expected"))
    return CaseResult(
        case_id=str(case.get("case_id")),
        kind=kind,
        expected=expected,
        actual=actual,
        passed=actual == expected,
        detail=f"{kind} => {actual}",
        blockers=tuple(sorted(blockers)),
        warnings=tuple(sorted(warnings)),
    )


def load_suite(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def summarize(results: list[CaseResult]) -> dict[str, Any]:
    by_kind: dict[str, dict[str, int]] = {}
    by_outcome: dict[str, int] = {}
    failures = [result for result in results if not result.passed]
    for result in results:
        entry = by_kind.setdefault(result.kind, {"cases": 0, "passed": 0, "failed": 0})
        entry["cases"] += 1
        entry["passed" if result.passed else "failed"] += 1
        by_outcome[result.actual] = by_outcome.get(result.actual, 0) + 1
    return {
        "cases": len(results),
        "passed": len(results) - len(failures),
        "failed": len(failures),
        "findings": len(failures),
        "by_kind": by_kind,
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
        "report_id": "AO-PPI-BRIDGE-002-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": EXPEDIENTE,
        "algoritmo": ALGORITHM_ID,
        "suite_id": suite.get("suite_id", "AO-PPI-BRIDGE-002-CASES"),
        "resultado": resultado,
        "recomendacion": "mantener_deudas_globales_abiertas" if not failures else "revisar_ao_ppi_bridge_002",
        "transformacion_permitida": False,
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
        "strong_case_criteria": {
            "testigo_comun": True,
            "evidencia_preservada": True,
            "decision_preservada": True,
            "permiso_no_mutante": True,
            "deuda_preservada": True,
            "autoridad_no_aumentada": True,
            "salida_segura": True,
        },
        "debt_guard": {
            "confluencia_global_abierta": True,
            "equivalencia_global_abierta": True,
            "serializacion_report_layer_abierta": True,
            "relacion_tcs_abierta": True,
            "r4_gamma_exportacion_general_bloqueada": True,
        },
        "summary": summarize(results),
        "results": [asdict(result) for result in results],
        "findings": [asdict(result) for result in failures],
    }


def render_md(report: dict[str, Any]) -> str:
    lines = [
        "# AO_PPI_BRIDGE_002_REPORT",
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
        "## Criterios fuertes",
        "",
    ]
    for key, value in report["strong_case_criteria"].items():
        lines.append(f"- {key}: {str(value).lower()}")
    lines.extend(["", "## Guardas de alcance", ""])
    for key, value in report["scope_guard"].items():
        lines.append(f"- {key}: {str(value).lower()}")
    lines.extend(["", "## Deudas conservadas abiertas", ""])
    for key, value in report["debt_guard"].items():
        lines.append(f"- {key}: {str(value).lower()}")
    lines.extend(["", "## Resultados", ""])
    for result in report["results"]:
        status = "PASS" if result["passed"] else "FAIL"
        lines.append(f"- {status} `{result['case_id']}` (`{result['kind']}`): {result['actual']} (esperado: {result['expected']})")
        if result["blockers"]:
            lines.append(f"  - blockers: `{', '.join(result['blockers'])}`")
        if result["warnings"]:
            lines.append(f"  - warnings: `{', '.join(result['warnings'])}`")
    lines.extend(["", "## Hallazgos", ""])
    if report["findings"]:
        lines.append("- Hay fallos de expectativa; revisar fixture o reglas antes de aceptar.")
    else:
        lines.append("- Sin hallazgos bloqueantes.")
        lines.append("- La bateria fortalece evidencia local, pero no cierra Confluencia global ni Equivalencia global.")
    return "\n".join(lines) + "\n"


def assert_inside(root: Path, path: Path) -> None:
    root_resolved = root.resolve()
    path_resolved = path.resolve()
    if path_resolved != root_resolved and root_resolved not in path_resolved.parents:
        raise SystemExit(f"Ruta fuera del repositorio: {path}")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Bateria fuerte no mutante AO-PPI-BRIDGE-002.")
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
