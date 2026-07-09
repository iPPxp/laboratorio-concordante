#!/usr/bin/env python3
"""Compuerta no mutante de promocion REPORT_LAYER AO-REPORT-PROMO-GATE-001."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ALGORITHM_ID = "AO-REPORT-PROMO-GATE-001"
EXPEDIENTE = "AO-001"
DEFAULT_CASE_FILE = Path(__file__).resolve().parent / "fixtures" / "ao_report_promo_gate_001_cases.json"

SAFE_OUTCOMES = {
    "candidata_futura_documentada",
    "bloqueo_promocion_por_repeticion",
    "bloqueo_autoridad_historica",
    "bloqueo_cierre_global_implicito",
    "bloqueo_modo_mutante",
    "bloqueo_cambio_nivel_c",
    "bloqueo_contrato_incompleto",
}


@dataclass(frozen=True)
class ReportPromoCaseResult:
    case_id: str
    expected: str
    actual: str
    passed: bool
    blockers: tuple[str, ...]
    warnings: tuple[str, ...]


def load_suite(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def evaluate_case(case: dict[str, Any]) -> ReportPromoCaseResult:
    blockers: list[str] = []
    warnings: list[str] = []

    if bool(case.get("transformacion_permitida")):
        blockers.append("modo_mutante")
        actual = "bloqueo_modo_mutante"
    elif bool(case.get("modifies_level_c")) or str(case.get("authority_claim", "")) in {"nivel_c", "canon"}:
        blockers.append("cambio_nivel_c")
        actual = "bloqueo_cambio_nivel_c"
    elif bool(case.get("global_closure_claim")):
        blockers.append("cierre_global_implicito")
        actual = "bloqueo_cierre_global_implicito"
    elif bool(case.get("promotion_by_repetition")):
        blockers.append("promocion_por_repeticion")
        actual = "bloqueo_promocion_por_repeticion"
    elif str(case.get("authority_source", "")) == "registro_historico":
        blockers.append("autoridad_historica")
        actual = "bloqueo_autoridad_historica"
    elif not bool(case.get("contract_exportable")):
        blockers.append("contrato_exportable_ausente")
        actual = "bloqueo_contrato_incompleto"
    else:
        actual = "candidata_futura_documentada"
        if not bool(case.get("independent_audit")):
            warnings.append("auditoria_independiente_pendiente")

    if actual not in SAFE_OUTCOMES:
        actual = "bloqueo_contrato_incompleto"

    expected = str(case.get("expected", ""))
    return ReportPromoCaseResult(
        case_id=str(case.get("case_id", "")),
        expected=expected,
        actual=actual,
        passed=actual == expected,
        blockers=tuple(sorted(blockers)),
        warnings=tuple(sorted(warnings)),
    )


def summarize(results: list[ReportPromoCaseResult]) -> dict[str, Any]:
    failures = [result for result in results if not result.passed]
    by_outcome: dict[str, int] = {}
    for result in results:
        by_outcome[result.actual] = by_outcome.get(result.actual, 0) + 1
    return {
        "cases": len(results),
        "passed": len(results) - len(failures),
        "failed": len(failures),
        "findings": len(failures),
        "future_candidate_cases": by_outcome.get("candidata_futura_documentada", 0),
        "blocked_cases": sum(count for outcome, count in by_outcome.items() if outcome.startswith("bloqueo")),
        "by_outcome": by_outcome,
    }


def build_report(root: Path | None = None, case_file: Path | None = None) -> dict[str, Any]:
    del root
    suite_path = case_file or DEFAULT_CASE_FILE
    suite = load_suite(suite_path)
    results = [evaluate_case(case) for case in suite.get("cases", [])]
    failures = [result for result in results if not result.passed]
    return {
        "report_id": "AO-REPORT-PROMO-GATE-001-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": EXPEDIENTE,
        "algoritmo": ALGORITHM_ID,
        "suite_id": suite.get("suite_id", "AO-REPORT-PROMO-GATE-CASES-001"),
        "resultado": "ok" if not failures else "bloqueado",
        "recomendacion": "mantener_report_layer_como_candidata_futura_no_promovida" if not failures else "revisar_compuerta_report_layer",
        "transformacion_permitida": False,
        "report_layer_candidate_future": not failures,
        "report_layer_promoted": False,
        "global_closure_authorized": False,
        "global_export_authorized": False,
        "r4_gamma_global_export_authorized": False,
        "source_evidence": suite.get("source_evidence", []),
        "scope_guard": {
            "modifica_doc04": False,
            "modifica_canon": False,
            "modifica_nivel_c": False,
            "crea_nivel_c": False,
            "promueve_report_layer": False,
            "cierra_confluencia_global": False,
            "cierra_equivalencia_global": False,
            "exporta_r4_gamma": False,
            "autoriza_transformacion": False,
        },
        "summary": summarize(results),
        "case_results": [asdict(result) for result in results],
        "findings": [asdict(result) for result in failures],
    }


def render_md(report: dict[str, Any]) -> str:
    lines = [
        "# AO_REPORT_PROMO_GATE_001_REPORT",
        "",
        f"report_id: {report['report_id']}",
        f"expediente: {EXPEDIENTE}",
        f"algoritmo: {ALGORITHM_ID}",
        f"suite_id: {report['suite_id']}",
        f"resultado: {report['resultado']}",
        f"recomendacion: {report['recomendacion']}",
        "transformacion_permitida: false",
        f"report_layer_candidate_future: {str(report['report_layer_candidate_future']).lower()}",
        "report_layer_promoted: false",
        "global_closure_authorized: false",
        "global_export_authorized: false",
        "r4_gamma_global_export_authorized: false",
        "",
        "## Resumen",
        "",
        f"- cases: {report['summary']['cases']}",
        f"- passed: {report['summary']['passed']}",
        f"- failed: {report['summary']['failed']}",
        f"- future_candidate_cases: {report['summary']['future_candidate_cases']}",
        f"- blocked_cases: {report['summary']['blocked_cases']}",
        "",
        "## Casos",
        "",
    ]
    for result in report["case_results"]:
        status = "PASS" if result["passed"] else "FAIL"
        lines.append(f"- {status} `{result['case_id']}`: {result['actual']}")
        if result["blockers"]:
            lines.append(f"  - blockers: {', '.join(result['blockers'])}")
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
        lines.append("- REPORT_LAYER puede quedar como candidata futura documentada, no promovida.")
    return "\n".join(lines) + "\n"


def assert_inside(root: Path, path: Path) -> None:
    root_resolved = root.resolve()
    path_resolved = path.resolve()
    if path_resolved != root_resolved and root_resolved not in path_resolved.parents:
        raise SystemExit(f"Ruta fuera del repositorio: {path}")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Compuerta de promocion REPORT_LAYER no mutante.")
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
