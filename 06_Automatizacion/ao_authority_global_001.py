#!/usr/bin/env python3
"""Criterio local de autoridad entre niveles para AO-AUTH-GLOBAL-001."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ALGORITHM_ID = "AO-AUTH-GLOBAL-001"
EXPEDIENTE = "AO-001"
DEFAULT_CASE_FILE = Path(__file__).resolve().parent / "fixtures" / "ao_authority_global_001_cases.json"

SAFE_OUTCOMES = {
    "comparabilidad_local_autorizada",
    "evidencia_pasiva_no_autoridad",
    "evidencia_externa_no_autoridad",
    "bloqueo_testigo",
    "bloqueo_historial_autoridad",
    "bloqueo_autoridad_por_repeticion",
    "bloqueo_recomendacion_como_decision",
    "bloqueo_autoridad_global_no_declarada",
    "bloqueo_modo_mutante",
}

LOCAL_AUTHORITY = {
    ("canon", "documento"): "autoridad_superior_reconocida",
    ("nivel_c", "expediente"): "autoridad_tecnica_acotada",
    ("documento", "expediente"): "autoridad_documental",
    ("expediente", "expediente"): "autoridad_local",
    ("reporte_automatizado", "expediente"): "evidencia_tecnica_no_autoridad",
    ("externo_sintetico", "expediente"): "evidencia_externa_no_autoridad",
    ("registro_historico", "expediente"): "evidencia_pasiva_no_autoridad",
}


@dataclass(frozen=True)
class AuthorityResult:
    case_id: str
    source_level: str
    target_level: str
    expected: str
    actual: str
    authority_class: str
    passed: bool
    blockers: tuple[str, ...]
    warnings: tuple[str, ...]


def load_suite(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def evaluate_case(case: dict[str, Any]) -> AuthorityResult:
    blockers: list[str] = []
    warnings: list[str] = []
    source = str(case.get("source_level", ""))
    target = str(case.get("target_level", ""))
    authority_claim = str(case.get("authority_claim", ""))
    authority_class = LOCAL_AUTHORITY.get((source, target), "no_comparable")

    if not str(case.get("witness", "")).strip():
        blockers.append("witness:ausente")
        actual = "bloqueo_testigo"
    elif bool(case.get("transformacion_permitida")):
        blockers.append("modo_mutante_no_autorizado")
        actual = "bloqueo_modo_mutante"
    elif source == "registro_historico" and authority_claim != "evidencia_pasiva":
        blockers.append(f"historial_como_autoridad:{authority_claim}")
        actual = "bloqueo_historial_autoridad"
    elif bool(case.get("authority_by_repetition")):
        blockers.append("autoridad_por_repeticion")
        actual = "bloqueo_autoridad_por_repeticion"
    elif bool(case.get("recommendation_as_decision")):
        blockers.append("recomendacion_convertida_en_decision")
        actual = "bloqueo_recomendacion_como_decision"
    elif bool(case.get("global_authority_claim")) or authority_claim in {"autoridad_global", "canonizar", "nivel_c_global"}:
        blockers.append(f"autoridad_global_no_autorizada:{authority_claim}")
        actual = "bloqueo_autoridad_global_no_declarada"
    elif source == "registro_historico":
        actual = "evidencia_pasiva_no_autoridad"
    elif source == "externo_sintetico":
        actual = "evidencia_externa_no_autoridad"
    elif authority_class == "no_comparable":
        warnings.append(f"relacion_no_comparable:{source}->{target}")
        actual = "evidencia_pasiva_no_autoridad"
    else:
        actual = "comparabilidad_local_autorizada"

    if actual not in SAFE_OUTCOMES:
        actual = "bloqueo_autoridad_global_no_declarada"

    expected = str(case.get("expected"))
    return AuthorityResult(
        case_id=str(case.get("case_id", "")),
        source_level=source,
        target_level=target,
        expected=expected,
        actual=actual,
        authority_class=authority_class,
        passed=actual == expected,
        blockers=tuple(sorted(blockers)),
        warnings=tuple(sorted(warnings)),
    )


def summarize(results: list[AuthorityResult]) -> dict[str, Any]:
    failures = [result for result in results if not result.passed]
    by_outcome: dict[str, int] = {}
    by_authority: dict[str, int] = {}
    for result in results:
        by_outcome[result.actual] = by_outcome.get(result.actual, 0) + 1
        by_authority[result.authority_class] = by_authority.get(result.authority_class, 0) + 1
    return {
        "cases": len(results),
        "passed": len(results) - len(failures),
        "failed": len(failures),
        "findings": len(failures),
        "local_comparable": sum(1 for result in results if result.actual == "comparabilidad_local_autorizada"),
        "blocked_cases": sum(1 for result in results if result.actual.startswith("bloqueo")),
        "by_outcome": by_outcome,
        "by_authority": by_authority,
    }


def build_report(root: Path | None = None, case_file: Path | None = None) -> dict[str, Any]:
    del root
    suite_path = case_file or DEFAULT_CASE_FILE
    suite = load_suite(suite_path)
    results = [evaluate_case(case) for case in suite.get("cases", [])]
    failures = [result for result in results if not result.passed]
    return {
        "report_id": "AO-AUTH-GLOBAL-001-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": EXPEDIENTE,
        "algoritmo": ALGORITHM_ID,
        "suite_id": suite.get("suite_id", "AO-AUTH-GLOBAL-CASES-001"),
        "resultado": "ok" if not failures else "bloqueado",
        "recomendacion": "mantener_criterio_autoridad_local" if not failures else "revisar_criterio_autoridad",
        "transformacion_permitida": False,
        "authority_criterion_local": not failures,
        "global_authority_authorized": False,
        "global_closure_authorized": False,
        "source_evidence": suite.get("source_evidence", []),
        "scope_guard": {
            "modifica_canon": False,
            "modifica_nivel_c": False,
            "crea_nivel_c": False,
            "usa_historial_como_autoridad": False,
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
        "# AO_AUTH_GLOBAL_001_REPORT",
        "",
        f"report_id: {report['report_id']}",
        f"expediente: {EXPEDIENTE}",
        f"algoritmo: {ALGORITHM_ID}",
        f"suite_id: {report['suite_id']}",
        f"resultado: {report['resultado']}",
        f"recomendacion: {report['recomendacion']}",
        "transformacion_permitida: false",
        f"authority_criterion_local: {str(report['authority_criterion_local']).lower()}",
        "global_authority_authorized: false",
        "global_closure_authorized: false",
        "",
        "## Resumen",
        "",
        f"- cases: {report['summary']['cases']}",
        f"- passed: {report['summary']['passed']}",
        f"- failed: {report['summary']['failed']}",
        f"- local_comparable: {report['summary']['local_comparable']}",
        f"- blocked_cases: {report['summary']['blocked_cases']}",
        "",
        "## Casos",
        "",
    ]
    for result in report["results"]:
        status = "PASS" if result["passed"] else "FAIL"
        lines.append(
            f"- {status} `{result['case_id']}`: {result['source_level']} -> "
            f"{result['target_level']} = {result['actual']} ({result['authority_class']})"
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
        lines.append("- Hay fallos de expectativa; no usar el criterio local de autoridad.")
    else:
        lines.append("- Sin hallazgos bloqueantes.")
        lines.append("- El criterio separa autoridad local, evidencia pasiva y bloqueos sin crear autoridad global.")
    return "\n".join(lines) + "\n"


def assert_inside(root: Path, path: Path) -> None:
    root_resolved = root.resolve()
    path_resolved = path.resolve()
    if path_resolved != root_resolved and root_resolved not in path_resolved.parents:
        raise SystemExit(f"Ruta fuera del repositorio: {path}")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Criterio local de autoridad entre niveles.")
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
