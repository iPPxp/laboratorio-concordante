#!/usr/bin/env python3
"""Relacion local no mutante AO/TCS para AO-TCS-REL-001."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ALGORITHM_ID = "AO-TCS-REL-001"
EXPEDIENTE = "AO-001"
DEFAULT_CASE_FILE = Path(__file__).resolve().parent / "fixtures" / "ao_tcs_rel_001_cases.json"

AO_TO_TCS = {
    "falta_testigo": ("TCS-F1", "bloqueo_de_concordancia"),
    "aumento_autoridad": ("TCS-F2", "bloqueo_de_concordancia"),
    "autoridad_por_repeticion": ("TCS-F3", "bloqueo_de_concordancia"),
    "recomendacion_como_decision": ("TCS-F4", "bloqueo_de_concordancia"),
    "perdida_permiso": ("TCS-F5", "bloqueo_de_concordancia"),
    "historial_autoridad": ("TCS-F7", "bloqueo_de_concordancia"),
    "conflicto_autoridades": ("TCS-F9", "bloqueo_de_concordancia"),
    "divergencia_clasificada": ("TCS-F10", "discordancia_global_controlada"),
    "no_comparable": ("TCS-F10", "no_comparable"),
    "bloqueo_concordancia": ("TCS-F10", "bloqueo_de_concordancia"),
}

SAFE_OUTCOMES = {
    "relacion_ao_tcs_local",
    "no_comparable_clasificado",
    "bloqueo_mapeo_incompleto",
    "bloqueo_canonizacion_tcs",
    "bloqueo_cierre_global",
}


@dataclass(frozen=True)
class TCSRelationResult:
    case_id: str
    ao_signal: str
    expected_tcs_failure: str
    actual_tcs_failure: str
    expected_state: str
    actual_state: str
    expected: str
    actual: str
    passed: bool
    blockers: tuple[str, ...]
    warnings: tuple[str, ...]


def is_empty(value: Any) -> bool:
    return value is None or value == "" or value == []


def load_suite(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def evaluate_case(case: dict[str, Any]) -> TCSRelationResult:
    blockers: list[str] = []
    warnings: list[str] = []
    signal = str(case.get("ao_signal", ""))
    expected_tcs = str(case.get("expected_tcs_failure", ""))
    expected_state = str(case.get("expected_state", ""))

    if not str(case.get("witness", "")).strip():
        blockers.append("witness:ausente")
        actual_tcs = ""
        actual_state = "bloqueo_de_concordancia"
        actual = "bloqueo_mapeo_incompleto"
    elif bool(case.get("promotes_tcs")):
        blockers.append("canonizacion_tcs_no_autorizada")
        actual_tcs = ""
        actual_state = "bloqueo_de_concordancia"
        actual = "bloqueo_canonizacion_tcs"
    elif bool(case.get("closes_global")):
        blockers.append("cierre_global_no_autorizado")
        actual_tcs = ""
        actual_state = "bloqueo_de_concordancia"
        actual = "bloqueo_cierre_global"
    elif signal not in AO_TO_TCS:
        blockers.append(f"ao_signal_no_mapeado:{signal}")
        actual_tcs = ""
        actual_state = "bloqueo_de_concordancia"
        actual = "bloqueo_mapeo_incompleto"
    elif is_empty(case.get("local_evidence")):
        blockers.append("evidencia_local_ausente")
        actual_tcs = ""
        actual_state = "bloqueo_de_concordancia"
        actual = "bloqueo_mapeo_incompleto"
    else:
        actual_tcs, actual_state = AO_TO_TCS[signal]
        if actual_tcs != expected_tcs:
            warnings.append(f"tcs_esperado_diverge:{expected_tcs}")
        if actual_state != expected_state:
            warnings.append(f"estado_esperado_diverge:{expected_state}")
        actual = "no_comparable_clasificado" if signal == "no_comparable" else "relacion_ao_tcs_local"

    if actual not in SAFE_OUTCOMES:
        actual = "bloqueo_mapeo_incompleto"

    expected = str(case.get("expected"))
    return TCSRelationResult(
        case_id=str(case.get("case_id", "")),
        ao_signal=signal,
        expected_tcs_failure=expected_tcs,
        actual_tcs_failure=actual_tcs,
        expected_state=expected_state,
        actual_state=actual_state,
        expected=expected,
        actual=actual,
        passed=actual == expected and not warnings,
        blockers=tuple(sorted(blockers)),
        warnings=tuple(sorted(warnings)),
    )


def summarize(results: list[TCSRelationResult]) -> dict[str, Any]:
    failures = [result for result in results if not result.passed]
    by_failure: dict[str, int] = {}
    by_outcome: dict[str, int] = {}
    for result in results:
        by_failure[result.actual_tcs_failure] = by_failure.get(result.actual_tcs_failure, 0) + 1
        by_outcome[result.actual] = by_outcome.get(result.actual, 0) + 1
    return {
        "cases": len(results),
        "passed": len(results) - len(failures),
        "failed": len(failures),
        "findings": len(failures),
        "mapped_cases": sum(1 for result in results if result.actual_tcs_failure.startswith("TCS-")),
        "blocked_cases": sum(1 for result in results if result.actual.startswith("bloqueo")),
        "by_failure": by_failure,
        "by_outcome": by_outcome,
    }


def build_report(root: Path | None = None, case_file: Path | None = None) -> dict[str, Any]:
    del root
    suite_path = case_file or DEFAULT_CASE_FILE
    suite = load_suite(suite_path)
    results = [evaluate_case(case) for case in suite.get("cases", [])]
    failures = [result for result in results if not result.passed]
    return {
        "report_id": "AO-TCS-REL-001-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": EXPEDIENTE,
        "algoritmo": ALGORITHM_ID,
        "suite_id": suite.get("suite_id", "AO-TCS-REL-CASES-001"),
        "resultado": "ok" if not failures else "bloqueado",
        "recomendacion": "mantener_tcs_provisional_no_canonico" if not failures else "revisar_relacion_ao_tcs",
        "transformacion_permitida": False,
        "tcs_relation_local": not failures,
        "tcs_canonical": False,
        "global_closure_authorized": False,
        "source_evidence": suite.get("source_evidence", []),
        "scope_guard": {
            "modifica_doc04": False,
            "modifica_canon": False,
            "crea_nivel_c": False,
            "canoniza_tcs": False,
            "cierra_confluencia_global": False,
            "cierra_equivalencia_global": False,
            "autoriza_transformacion": False,
        },
        "summary": summarize(results),
        "results": [asdict(result) for result in results],
        "findings": [asdict(result) for result in failures],
    }


def render_md(report: dict[str, Any]) -> str:
    lines = [
        "# AO_TCS_REL_001_REPORT",
        "",
        f"report_id: {report['report_id']}",
        f"expediente: {EXPEDIENTE}",
        f"algoritmo: {ALGORITHM_ID}",
        f"suite_id: {report['suite_id']}",
        f"resultado: {report['resultado']}",
        f"recomendacion: {report['recomendacion']}",
        "transformacion_permitida: false",
        f"tcs_relation_local: {str(report['tcs_relation_local']).lower()}",
        "tcs_canonical: false",
        "global_closure_authorized: false",
        "",
        "## Resumen",
        "",
        f"- cases: {report['summary']['cases']}",
        f"- passed: {report['summary']['passed']}",
        f"- failed: {report['summary']['failed']}",
        f"- mapped_cases: {report['summary']['mapped_cases']}",
        f"- blocked_cases: {report['summary']['blocked_cases']}",
        "",
        "## Casos",
        "",
    ]
    for result in report["results"]:
        status = "PASS" if result["passed"] else "FAIL"
        lines.append(
            f"- {status} `{result['case_id']}`: {result['ao_signal']} -> "
            f"{result['actual_tcs_failure']} / {result['actual_state']} ({result['actual']})"
        )
        if result["blockers"]:
            lines.append(f"  - blockers: {', '.join(result['blockers'])}")
        if result["warnings"]:
            lines.append(f"  - warnings: {', '.join(result['warnings'])}")
    lines.extend(["", "## Guardas", ""])
    for key, value in report["scope_guard"].items():
        lines.append(f"- {key}: {str(value).lower()}")
    lines.extend(["", "## Dictamen", ""])
    if report["findings"]:
        lines.append("- Hay fallos de expectativa; no usar la relacion AO/TCS como evidencia.")
    else:
        lines.append("- Sin hallazgos bloqueantes.")
        lines.append("- TCS clasifica fallos AO en grado local provisional; no se canoniza TCS ni se cierra ningun problema global.")
    return "\n".join(lines) + "\n"


def assert_inside(root: Path, path: Path) -> None:
    root_resolved = root.resolve()
    path_resolved = path.resolve()
    if path_resolved != root_resolved and root_resolved not in path_resolved.parents:
        raise SystemExit(f"Ruta fuera del repositorio: {path}")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Relacion local no mutante AO/TCS.")
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
