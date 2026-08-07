#!/usr/bin/env python3
"""Reconsideracion no mutante de promocion formal de REPORT_LAYER."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ALGORITHM_ID = "AO-REPORT-PROMO-GATE-002"
EXPEDIENTE = "AO-001"
DEFAULT_CASE_FILE = Path(__file__).resolve().parent / "fixtures" / "ao_report_promo_gate_002_matrix.json"


@dataclass(frozen=True)
class PromotionConditionResult:
    condition_id: str
    front: str
    expected: str
    actual: str
    passed: bool
    blocks_formal_promotion: bool
    local_credit: bool
    gap: str
    evidence: tuple[str, ...]


def load_suite(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def evaluate_condition(condition: dict[str, Any]) -> PromotionConditionResult:
    actual = str(condition.get("status", "no_detectada"))
    expected = str(condition.get("expected", actual))
    return PromotionConditionResult(
        condition_id=str(condition.get("condition_id", "")),
        front=str(condition.get("front", "")),
        expected=expected,
        actual=actual,
        passed=actual == expected,
        blocks_formal_promotion=bool(condition.get("blocks_formal_promotion")),
        local_credit=bool(condition.get("local_credit")),
        gap=str(condition.get("gap", "")),
        evidence=tuple(str(item) for item in condition.get("evidence", [])),
    )


def summarize(results: list[PromotionConditionResult]) -> dict[str, Any]:
    failures = [result for result in results if not result.passed]
    blockers = [result for result in results if result.blocks_formal_promotion]
    local = [result for result in results if result.local_credit]
    by_status: dict[str, int] = {}
    for result in results:
        by_status[result.actual] = by_status.get(result.actual, 0) + 1
    return {
        "conditions": len(results),
        "passed": len(results) - len(failures),
        "failed": len(failures),
        "findings": len(failures),
        "local_credit": len(local),
        "blocking_conditions": len(blockers),
        "by_status": by_status,
    }


def build_report(root: Path | None = None, case_file: Path | None = None) -> dict[str, Any]:
    del root
    suite_path = case_file or DEFAULT_CASE_FILE
    suite = load_suite(suite_path)
    results = [evaluate_condition(condition) for condition in suite.get("conditions", [])]
    failures = [result for result in results if not result.passed]
    blockers = [result for result in results if result.blocks_formal_promotion]
    formal_profile_prepared = not failures and bool(results)
    return {
        "report_id": ALGORITHM_ID + "-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": EXPEDIENTE,
        "algoritmo": ALGORITHM_ID,
        "suite_id": suite.get("suite_id", "AO-REPORT-PROMO-GATE-002-MATRIX"),
        "resultado": "ok" if not failures else "bloqueado",
        "recomendacion": "mantener_report_layer_pre_c_con_perfil_formal_condicionado",
        "transformacion_permitida": False,
        "report_layer_formal_profile_prepared": formal_profile_prepared,
        "report_layer_formal_promotion_authorized": False,
        "report_layer_promoted": False,
        "report_layer_candidate_future": True,
        "global_closure_authorized": False,
        "global_export_authorized": False,
        "global_equivalence_authorized": False,
        "global_confluence_authorized": False,
        "r4_gamma_global_export_authorized": False,
        "blocking_reason": [result.condition_id for result in blockers],
        "source_evidence": suite.get("source_evidence", []),
        "scope_guard": {
            "modifica_doc04": False,
            "modifica_canon": False,
            "modifica_nivel_c": False,
            "crea_nivel_c": False,
            "crea_c003": False,
            "promueve_report_layer": False,
            "cierra_confluencia_global": False,
            "cierra_equivalencia_global": False,
            "exporta_r4_gamma": False,
            "autoriza_transformacion": False,
        },
        "summary": summarize(results),
        "condition_results": [asdict(result) for result in results],
        "findings": [asdict(result) for result in failures],
    }


def render_md(report: dict[str, Any]) -> str:
    lines = [
        "# AO_REPORT_PROMO_GATE_002_REPORT",
        "",
        f"report_id: {report['report_id']}",
        f"expediente: {EXPEDIENTE}",
        f"algoritmo: {ALGORITHM_ID}",
        f"suite_id: {report['suite_id']}",
        f"resultado: {report['resultado']}",
        f"recomendacion: {report['recomendacion']}",
        "transformacion_permitida: false",
        f"report_layer_formal_profile_prepared: {str(report['report_layer_formal_profile_prepared']).lower()}",
        "report_layer_formal_promotion_authorized: false",
        "report_layer_promoted: false",
        "global_closure_authorized: false",
        "global_export_authorized: false",
        "global_equivalence_authorized: false",
        "global_confluence_authorized: false",
        "r4_gamma_global_export_authorized: false",
        "",
        "## Resumen",
        "",
    ]
    summary = report["summary"]
    for key in ["conditions", "passed", "failed", "local_credit", "blocking_conditions"]:
        lines.append(f"- {key}: {summary[key]}")
    lines.extend(["", "## Condiciones", ""])
    for result in report["condition_results"]:
        status = "PASS" if result["passed"] else "FAIL"
        block = "bloquea" if result["blocks_formal_promotion"] else "no_bloquea"
        lines.append(f"- {status} `{result['condition_id']}` ({result['front']}): {result['actual']} / {block}")
        lines.append(f"  - gap: {result['gap']}")
    lines.extend(["", "## Guardas", ""])
    for key, value in report["scope_guard"].items():
        lines.append(f"- {key}: {str(value).lower()}")
    lines.extend(["", "## Dictamen", ""])
    lines.append("- REPORT_LAYER obtiene perfil formal condicionado de expediente.")
    lines.append("- La promocion formal general no queda autorizada por faltar Equivalencia global, Confluencia global, revision externa independiente y autoridad de Nivel C/Canon.")
    return "\n".join(lines) + "\n"


def assert_inside(root: Path, path: Path) -> None:
    root_resolved = root.resolve()
    path_resolved = path.resolve()
    if path_resolved != root_resolved and root_resolved not in path_resolved.parents:
        raise SystemExit(f"Ruta fuera del repositorio: {path}")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Reconsideracion de promocion formal REPORT_LAYER no mutante.")
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
