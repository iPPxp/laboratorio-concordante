#!/usr/bin/env python3
"""Protocolo reproducible independiente AO-PROTO-INDEP-001."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ALGORITHM_ID = "AO-PROTO-INDEP-001"
EXPEDIENTE = "AO-001"
DEFAULT_CASE_FILE = Path(__file__).resolve().parent / "fixtures" / "ao_protocol_independent_001_cases.json"

VALID_OUTCOMES = {
    "coincidencia_exacta",
    "coincidencia_familia",
    "desacuerdo_justificado",
    "bloqueo_protocolo",
}


@dataclass(frozen=True)
class ProtocolCaseResult:
    case_id: str
    expected: str
    actual: str
    evaluator_count: int
    states: tuple[str, ...]
    families: tuple[str, ...]
    debts: tuple[str, ...]
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


def evaluate_case(case: dict[str, Any]) -> ProtocolCaseResult:
    warnings: list[str] = []
    evaluators = [dict(item) for item in as_list(case.get("evaluators"))]
    states = tuple(str(item.get("state", "")) for item in evaluators)
    families = tuple(str(item.get("family", "")) for item in evaluators)
    debts = tuple(str(item.get("debt", "")) for item in evaluators if str(item.get("debt", "")).strip())
    justifications = tuple(str(item.get("justification", "")) for item in evaluators)

    if len(evaluators) < 3:
        warnings.append("evaluadores_insuficientes")
    if any(not state for state in states):
        warnings.append("estado_faltante")
    if any(not family for family in families):
        warnings.append("familia_faltante")
    if any(not text.strip() for text in justifications):
        warnings.append("justificacion_faltante")
    if bool(case.get("forces_unanimity")):
        warnings.append("unanimidad_forzada")
    if bool(case.get("global_claim")):
        warnings.append("cierre_global_implicito")

    if warnings:
        actual = "bloqueo_protocolo"
    elif len(set(states)) == 1:
        actual = "coincidencia_exacta"
    elif len(set(families)) == 1:
        actual = "coincidencia_familia"
    elif debts and len(debts) >= len(evaluators):
        actual = "desacuerdo_justificado"
    else:
        actual = "bloqueo_protocolo"

    if actual not in VALID_OUTCOMES:
        actual = "bloqueo_protocolo"

    expected = str(case.get("expected", ""))
    return ProtocolCaseResult(
        case_id=str(case.get("case_id", "")),
        expected=expected,
        actual=actual,
        evaluator_count=len(evaluators),
        states=states,
        families=families,
        debts=debts,
        passed=actual == expected,
        warnings=tuple(sorted(warnings)),
    )


def summarize(results: list[ProtocolCaseResult]) -> dict[str, Any]:
    failures = [result for result in results if not result.passed]
    by_outcome: dict[str, int] = {}
    for result in results:
        by_outcome[result.actual] = by_outcome.get(result.actual, 0) + 1
    return {
        "cases": len(results),
        "passed": len(results) - len(failures),
        "failed": len(failures),
        "findings": len(failures),
        "exact": by_outcome.get("coincidencia_exacta", 0),
        "family": by_outcome.get("coincidencia_familia", 0),
        "justified_disagreement": by_outcome.get("desacuerdo_justificado", 0),
        "blocked": by_outcome.get("bloqueo_protocolo", 0),
        "by_outcome": by_outcome,
    }


def build_report(root: Path | None = None, case_file: Path | None = None) -> dict[str, Any]:
    del root
    suite_path = case_file or DEFAULT_CASE_FILE
    suite = load_suite(suite_path)
    results = [evaluate_case(case) for case in suite.get("cases", [])]
    failures = [result for result in results if not result.passed]
    return {
        "report_id": "AO-PROTO-INDEP-001-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": EXPEDIENTE,
        "algoritmo": ALGORITHM_ID,
        "suite_id": suite.get("suite_id", "AO-PROTO-INDEP-CASES-001"),
        "resultado": "ok" if not failures else "bloqueado",
        "recomendacion": "aceptar_protocolo_reproducible_local" if not failures else "revisar_protocolo_independiente",
        "transformacion_permitida": False,
        "independent_protocol_accepted": not failures,
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
            "fuerza_unanimidad": False,
            "cierra_confluencia_global": False,
            "cierra_equivalencia_global": False,
            "promueve_report_layer": False,
            "exporta_r4_gamma": False,
            "autoriza_transformacion": False,
        },
        "summary": summarize(results),
        "case_results": [asdict(result) for result in results],
        "findings": [asdict(result) for result in failures],
    }


def render_md(report: dict[str, Any]) -> str:
    lines = [
        "# AO_PROTOCOL_INDEPENDENT_001_REPORT",
        "",
        f"report_id: {report['report_id']}",
        f"expediente: {EXPEDIENTE}",
        f"algoritmo: {ALGORITHM_ID}",
        f"suite_id: {report['suite_id']}",
        f"resultado: {report['resultado']}",
        f"recomendacion: {report['recomendacion']}",
        "transformacion_permitida: false",
        f"independent_protocol_accepted: {str(report['independent_protocol_accepted']).lower()}",
        "global_closure_authorized: false",
        "global_export_authorized: false",
        "report_layer_promoted: false",
        "r4_gamma_global_export_authorized: false",
        "",
        "## Resumen",
        "",
        f"- cases: {report['summary']['cases']}",
        f"- passed: {report['summary']['passed']}",
        f"- failed: {report['summary']['failed']}",
        f"- exact: {report['summary']['exact']}",
        f"- family: {report['summary']['family']}",
        f"- justified_disagreement: {report['summary']['justified_disagreement']}",
        "",
        "## Casos",
        "",
    ]
    for result in report["case_results"]:
        status = "PASS" if result["passed"] else "FAIL"
        lines.append(f"- {status} `{result['case_id']}`: {result['actual']}")
        lines.append(f"  - states: {', '.join(result['states'])}")
        lines.append(f"  - families: {', '.join(result['families'])}")
        if result["debts"]:
            lines.append(f"  - debts: {', '.join(result['debts'])}")
        if result["warnings"]:
            lines.append(f"  - warnings: {', '.join(result['warnings'])}")
    lines.extend(["", "## Guardas", ""])
    for key, value in report["scope_guard"].items():
        lines.append(f"- {key}: {str(value).lower()}")
    lines.extend(["", "## Dictamen", ""])
    if report["findings"]:
        lines.append("- Hay fallos de expectativa; no aceptar el protocolo independiente.")
    else:
        lines.append("- Sin hallazgos bloqueantes.")
        lines.append("- El protocolo clasifica coincidencias y desacuerdos justificados sin forzar unanimidad.")
        lines.append("- No autoriza cierre global ni promocion.")
    return "\n".join(lines) + "\n"


def assert_inside(root: Path, path: Path) -> None:
    root_resolved = root.resolve()
    path_resolved = path.resolve()
    if path_resolved != root_resolved and root_resolved not in path_resolved.parents:
        raise SystemExit(f"Ruta fuera del repositorio: {path}")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Protocolo independiente AO no mutante.")
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
