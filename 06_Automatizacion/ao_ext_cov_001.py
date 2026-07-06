#!/usr/bin/env python3
"""Cobertura externa sintetica no regulada para AO-EXT-COV-001."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ALGORITHM_ID = "AO-EXT-COV-001"
EXPEDIENTE = "AO-001"
DEFAULT_CASE_FILE = Path(__file__).resolve().parent / "fixtures" / "ao_ext_cov_001_cases.json"

SAFE_OUTCOMES = {
    "cobertura_externa_local",
    "conflicto_autoridades_clasificado",
    "divergencia_clasificada",
    "bloqueo_testigo",
    "bloqueo_autoridad",
    "bloqueo_modo_mutante",
    "bloqueo_dominio_regulado",
}


@dataclass(frozen=True)
class ExternalCoverageResult:
    case_id: str
    domain: str
    expected: str
    actual: str
    passed: bool
    witness: str
    source_family: str
    blockers: tuple[str, ...]
    warnings: tuple[str, ...]


def load_suite(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def evaluate_case(case: dict[str, Any]) -> ExternalCoverageResult:
    blockers: list[str] = []
    warnings: list[str] = []
    witness = str(case.get("witness", ""))
    source_family = str(case.get("source_family", ""))

    if bool(case.get("regulated_domain")):
        blockers.append("dominio_regulado_no_autorizado")
        actual = "bloqueo_dominio_regulado"
    elif not witness.strip():
        blockers.append("witness:ausente")
        actual = "bloqueo_testigo"
    elif bool(case.get("transformacion_permitida")):
        blockers.append("modo_mutante_no_autorizado")
        actual = "bloqueo_modo_mutante"
    elif str(case.get("authority_claim")) in {"canon", "nivel_c", "autoridad_global"} or bool(case.get("authority_exceeded")):
        blockers.append(f"autoridad_no_autorizada:{case.get('authority_claim')}")
        actual = "bloqueo_autoridad"
    elif bool(case.get("conflicting_authorities")):
        actual = "conflicto_autoridades_clasificado"
    elif case.get("expected_projection") and case.get("actual_projection") != case.get("expected_projection"):
        warnings.append("projection:diverge")
        actual = "divergencia_clasificada"
    else:
        actual = "cobertura_externa_local"

    if actual not in SAFE_OUTCOMES:
        actual = "bloqueo_autoridad"

    expected = str(case.get("expected"))
    return ExternalCoverageResult(
        case_id=str(case.get("case_id", "")),
        domain=str(case.get("domain", "")),
        expected=expected,
        actual=actual,
        passed=actual == expected,
        witness=witness,
        source_family=source_family,
        blockers=tuple(sorted(blockers)),
        warnings=tuple(sorted(warnings)),
    )


def summarize(results: list[ExternalCoverageResult]) -> dict[str, Any]:
    failures = [result for result in results if not result.passed]
    by_outcome: dict[str, int] = {}
    by_domain: dict[str, int] = {}
    for result in results:
        by_outcome[result.actual] = by_outcome.get(result.actual, 0) + 1
        by_domain[result.domain] = by_domain.get(result.domain, 0) + 1
    return {
        "cases": len(results),
        "passed": len(results) - len(failures),
        "failed": len(failures),
        "findings": len(failures),
        "coverage_local": sum(1 for result in results if result.actual == "cobertura_externa_local"),
        "classified_cases": sum(1 for result in results if result.actual in {"conflicto_autoridades_clasificado", "divergencia_clasificada"}),
        "blocked_cases": sum(1 for result in results if result.actual.startswith("bloqueo")),
        "by_outcome": by_outcome,
        "by_domain": by_domain,
    }


def build_report(root: Path | None = None, case_file: Path | None = None) -> dict[str, Any]:
    del root
    suite_path = case_file or DEFAULT_CASE_FILE
    suite = load_suite(suite_path)
    results = [evaluate_case(case) for case in suite.get("cases", [])]
    failures = [result for result in results if not result.passed]
    return {
        "report_id": "AO-EXT-COV-001-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": EXPEDIENTE,
        "algoritmo": ALGORITHM_ID,
        "suite_id": suite.get("suite_id", "AO-EXT-COV-CASES-001"),
        "resultado": "ok" if not failures else "bloqueado",
        "recomendacion": "mantener_cobertura_externa_local_parcial" if not failures else "revisar_cobertura_externa",
        "transformacion_permitida": False,
        "external_coverage_local": not failures,
        "external_coverage_global": False,
        "global_closure_authorized": False,
        "source_evidence": suite.get("source_evidence", []),
        "scope_guard": {
            "dominios_regulados": False,
            "modifica_doc04": False,
            "modifica_canon": False,
            "crea_nivel_c": False,
            "promueve_report_layer": False,
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
        "# AO_EXT_COV_001_REPORT",
        "",
        f"report_id: {report['report_id']}",
        f"expediente: {EXPEDIENTE}",
        f"algoritmo: {ALGORITHM_ID}",
        f"suite_id: {report['suite_id']}",
        f"resultado: {report['resultado']}",
        f"recomendacion: {report['recomendacion']}",
        "transformacion_permitida: false",
        f"external_coverage_local: {str(report['external_coverage_local']).lower()}",
        "external_coverage_global: false",
        "global_closure_authorized: false",
        "",
        "## Resumen",
        "",
        f"- cases: {report['summary']['cases']}",
        f"- passed: {report['summary']['passed']}",
        f"- failed: {report['summary']['failed']}",
        f"- coverage_local: {report['summary']['coverage_local']}",
        f"- classified_cases: {report['summary']['classified_cases']}",
        f"- blocked_cases: {report['summary']['blocked_cases']}",
        "",
        "## Casos",
        "",
    ]
    for result in report["results"]:
        status = "PASS" if result["passed"] else "FAIL"
        lines.append(f"- {status} `{result['case_id']}` [{result['domain']} / {result['source_family']}]: {result['actual']}")
        if result["blockers"]:
            lines.append(f"  - blockers: {', '.join(result['blockers'])}")
        if result["warnings"]:
            lines.append(f"  - warnings: {', '.join(result['warnings'])}")
    lines.extend(["", "## Guardas", ""])
    for key, value in report["scope_guard"].items():
        lines.append(f"- {key}: {str(value).lower()}")
    lines.extend(["", "## Dictamen", ""])
    if report["findings"]:
        lines.append("- Hay fallos de expectativa; no usar la cobertura externa como evidencia.")
    else:
        lines.append("- Sin hallazgos bloqueantes.")
        lines.append("- La cobertura externa sintetica fortalece evidencia local, pero no es independiente suficiente para cierre global.")
    return "\n".join(lines) + "\n"


def assert_inside(root: Path, path: Path) -> None:
    root_resolved = root.resolve()
    path_resolved = path.resolve()
    if path_resolved != root_resolved and root_resolved not in path_resolved.parents:
        raise SystemExit(f"Ruta fuera del repositorio: {path}")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Cobertura externa sintetica no regulada para AO-001.")
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
