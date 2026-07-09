#!/usr/bin/env python3
"""Validador no mutante de matriz de impacto Canon/Documento 04."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from typing import Any


ALGORITHM_ID = "MOC-CANON-DOC04-IMPACT-001"
EXPEDIENTE = "MOC-001"
DEFAULT_CASE_FILE = Path(__file__).resolve().parent / "fixtures" / "moc_canon_doc04_impact_001_matrix.json"
FORBIDDEN_TRUE_FLAGS = {
    "official_canon_edit_authorized",
    "official_doc04_edit_authorized",
    "mutating_mode_authorized",
    "external_use_authorized",
    "global_closure_authorized",
    "report_layer_promoted",
    "r4_gamma_global_export_authorized",
}


def load_matrix(path: Path = DEFAULT_CASE_FILE) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def evaluate_matrix(matrix: dict[str, Any]) -> dict[str, Any]:
    flags = dict(matrix.get("flags", {}))
    rows = list(matrix.get("rows", []))
    blockers: list[str] = []
    warnings: list[str] = []

    for flag in sorted(FORBIDDEN_TRUE_FLAGS):
        if flags.get(flag):
            blockers.append(f"flag_prohibido_activo:{flag}")

    required_surfaces = set(matrix.get("required_surfaces", []))
    present_surfaces = {str(row.get("surface", "")) for row in rows}
    missing_surfaces = sorted(required_surfaces - present_surfaces)
    for surface in missing_surfaces:
        blockers.append(f"superficie_ausente:{surface}")

    if flags.get("m000_text_change_recommended"):
        blockers.append("m000_no_debe_tener_cambio_textual_en_esta_ruta")
    if not flags.get("m001_candidate_amendment_recommended"):
        blockers.append("m001_sin_propuesta_candidata")
    if not flags.get("doc04_candidate_amendment_recommended"):
        blockers.append("doc04_sin_propuesta_candidata")

    for row in rows:
        row_id = str(row.get("id", "sin_id"))
        surface = str(row.get("surface", ""))
        action = str(row.get("candidate_action", ""))
        if row.get("official_edit_authorized"):
            blockers.append(f"edicion_oficial_en_fila:{row_id}")
        if surface in {"M001", "DOC04"} and not row.get("requires_future_decision"):
            blockers.append(f"decision_futura_ausente:{row_id}")
        if surface == "PROHIBIDO" and action != "rechazar":
            blockers.append(f"prohibido_no_rechazado:{row_id}")
        if surface == "M000" and action not in {"referenciar_sin_editar", "bloquear_promocion_automatica"}:
            blockers.append(f"m000_accion_no_defensiva:{row_id}")

    if not rows:
        blockers.append("matriz_sin_filas")

    if not blockers:
        actual = "impact_matrix_accepted"
        warnings.append("propuesta_candidata_no_incorporada")
    else:
        actual = "impact_matrix_blocked"

    return {
        "matrix_id": str(matrix.get("matrix_id", "")),
        "expected": str(matrix.get("expected", "")),
        "actual": actual,
        "passed": actual == matrix.get("expected") and not blockers,
        "blockers": sorted(blockers),
        "warnings": sorted(warnings),
        "surfaces": sorted(present_surfaces),
        "row_count": len(rows),
    }


def build_report(root: Path | None = None, case_file: Path | None = None) -> dict[str, Any]:
    del root
    matrix = load_matrix(case_file or DEFAULT_CASE_FILE)
    result = evaluate_matrix(matrix)
    ok = bool(result["passed"])
    flags = dict(matrix.get("flags", {}))
    return {
        "report_id": "MOC-CANON-DOC04-IMPACT-001-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": EXPEDIENTE,
        "algoritmo": ALGORITHM_ID,
        "resultado": "ok" if ok else "bloqueado",
        "recomendacion": "mantener_como_propuesta_candidata" if ok else "revisar_matriz_impacto",
        "transformacion_permitida": False,
        "impact_matrix_accepted": ok,
        "candidate_proposal_prepared": ok,
        "m000_text_change_recommended": bool(flags.get("m000_text_change_recommended")),
        "m001_candidate_amendment_recommended": bool(flags.get("m001_candidate_amendment_recommended")),
        "doc04_candidate_amendment_recommended": bool(flags.get("doc04_candidate_amendment_recommended")),
        "official_canon_edit_authorized": False,
        "official_doc04_edit_authorized": False,
        "mutating_mode_authorized": False,
        "external_use_authorized": False,
        "global_closure_authorized": False,
        "report_layer_promoted": False,
        "r4_gamma_global_export_authorized": False,
        "summary": {
            "rows": result["row_count"],
            "surfaces": len(result["surfaces"]),
            "findings": 0 if ok else len(result["blockers"]),
        },
        "matrix": matrix,
        "result": result,
        "findings": [] if ok else result["blockers"],
    }


def render_md(report: dict[str, Any]) -> str:
    result = report["result"]
    lines = [
        "# MOC_CANON_DOC04_IMPACT_001_REPORT",
        "",
        f"report_id: {report['report_id']}",
        f"expediente: {EXPEDIENTE}",
        f"algoritmo: {ALGORITHM_ID}",
        f"resultado: {report['resultado']}",
        f"recomendacion: {report['recomendacion']}",
        f"impact_matrix_accepted: {str(report['impact_matrix_accepted']).lower()}",
        f"candidate_proposal_prepared: {str(report['candidate_proposal_prepared']).lower()}",
        f"m000_text_change_recommended: {str(report['m000_text_change_recommended']).lower()}",
        f"m001_candidate_amendment_recommended: {str(report['m001_candidate_amendment_recommended']).lower()}",
        f"doc04_candidate_amendment_recommended: {str(report['doc04_candidate_amendment_recommended']).lower()}",
        "official_canon_edit_authorized: false",
        "official_doc04_edit_authorized: false",
        "mutating_mode_authorized: false",
        "external_use_authorized: false",
        "global_closure_authorized: false",
        "report_layer_promoted: false",
        "r4_gamma_global_export_authorized: false",
        "transformacion_permitida: false",
        "",
        "## Resultado",
        "",
        f"- matrix_id: {result['matrix_id']}",
        f"- actual: {result['actual']}",
        f"- expected: {result['expected']}",
        f"- passed: {str(result['passed']).lower()}",
        f"- rows: {result['row_count']}",
        f"- surfaces: {', '.join(result['surfaces'])}",
    ]
    if result["warnings"]:
        lines.extend(["", "## Advertencias", ""])
        for warning in result["warnings"]:
            lines.append(f"- {warning}")
    if result["blockers"]:
        lines.extend(["", "## Bloqueos", ""])
        for blocker in result["blockers"]:
            lines.append(f"- {blocker}")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validador no mutante de matriz MOC Canon/Doc04.")
    parser.add_argument("--case-file", type=Path, default=DEFAULT_CASE_FILE)
    parser.add_argument("--format", choices=("json", "md"), default="md")
    parser.add_argument("--output", help="Ruta opcional de salida.")
    args = parser.parse_args(argv)

    report = build_report(case_file=args.case_file)
    output = json.dumps(report, ensure_ascii=True, indent=2) + "\n"
    if args.format == "md":
        output = render_md(report)
    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output, encoding="utf-8")
    else:
        sys.stdout.write(output)
    return 0 if report["resultado"] == "ok" else 2


if __name__ == "__main__":
    raise SystemExit(main())
