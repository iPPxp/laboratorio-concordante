#!/usr/bin/env python3
"""Compuerta no mutante de adopcion oficial posterior MOC/Canon/Doc04."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from typing import Any


ALGORITHM_ID = "MOC-CANON-DOC04-ADOPT-GATE-001"
EXPEDIENTE = "MOC-001"
DEFAULT_CASE_FILE = Path(__file__).resolve().parent / "fixtures" / "moc_canon_doc04_adopt_gate_001.json"
FORBIDDEN_TRUE_FLAGS = {
    "official_file_edit_executed",
    "mutating_mode_authorized",
    "external_use_authorized",
    "global_closure_authorized",
    "report_layer_promoted",
    "r4_gamma_global_export_authorized",
    "nivel_c_modified",
    "h_xi_admitted",
    "psi_canonized",
    "real_persons_or_regulated_domain",
}
REQUIRED_SURFACES = {"M000", "M001", "DOC04", "EXPEDIENTE", "PROHIBIDO"}


def load_gate(path: Path = DEFAULT_CASE_FILE) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def evaluate_gate(gate: dict[str, Any], root: Path | None = None) -> dict[str, Any]:
    root = root or Path.cwd()
    flags = dict(gate.get("flags", {}))
    surfaces = list(gate.get("surfaces", []))
    blockers: list[str] = []
    warnings: list[str] = []

    for rel_path in gate.get("required_documents", []):
        if not (root / str(rel_path)).exists():
            blockers.append(f"documento_requerido_ausente:{rel_path}")

    for flag in sorted(FORBIDDEN_TRUE_FLAGS):
        if flags.get(flag):
            blockers.append(f"flag_prohibido_activo:{flag}")

    if not flags.get("impact_matrix_accepted"):
        blockers.append("matriz_impacto_no_aceptada")
    if not flags.get("candidate_text_exact"):
        blockers.append("texto_candidato_no_fijado")
    if flags.get("m000_adoption_recommended"):
        blockers.append("m000_no_debe_adoptarse")
    if not flags.get("m001_adoption_recommended"):
        blockers.append("m001_no_recomendado")
    if not flags.get("doc04_adoption_recommended"):
        blockers.append("doc04_no_recomendado")
    if not flags.get("official_edit_requires_explicit_apply_step"):
        blockers.append("falta_paso_explicito_de_aplicacion")

    present = {str(item.get("surface", "")) for item in surfaces}
    for surface in sorted(REQUIRED_SURFACES - present):
        blockers.append(f"superficie_ausente:{surface}")

    for item in surfaces:
        surface = str(item.get("surface", ""))
        recommendation = str(item.get("recommendation", ""))
        if surface == "M000" and recommendation != "no_adoptar":
            blockers.append("m000_recomendacion_no_defensiva")
        if surface in {"M001", "DOC04"}:
            if recommendation != "lista_para_aplicacion_posterior":
                blockers.append(f"{surface.lower()}_no_lista_para_aplicacion")
            if item.get("requires_official_edit") and not item.get("requires_explicit_apply_step"):
                blockers.append(f"{surface.lower()}_sin_paso_explicito")
        if surface == "EXPEDIENTE" and recommendation != "conservar_local":
            blockers.append("expediente_no_conserva_local")
        if surface == "PROHIBIDO" and recommendation != "bloquear":
            blockers.append("prohibido_no_bloqueado")

    if not blockers:
        actual = "lista_para_aplicacion_posterior"
        warnings.append("no_ejecuta_edicion_oficial")
    else:
        actual = "adopcion_bloqueada"

    return {
        "gate_id": str(gate.get("gate_id", "")),
        "expected": str(gate.get("expected", "")),
        "actual": actual,
        "passed": actual == gate.get("expected") and not blockers,
        "blockers": sorted(blockers),
        "warnings": sorted(warnings),
        "surfaces": sorted(present),
        "surface_count": len(surfaces),
    }


def build_report(root: Path | None = None, case_file: Path | None = None) -> dict[str, Any]:
    root = root or Path.cwd()
    gate = load_gate(case_file or DEFAULT_CASE_FILE)
    result = evaluate_gate(gate, root)
    ok = bool(result["passed"])
    flags = dict(gate.get("flags", {}))
    return {
        "report_id": "MOC-CANON-DOC04-ADOPT-GATE-001-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": EXPEDIENTE,
        "algoritmo": ALGORITHM_ID,
        "resultado": "ok" if ok else "bloqueado",
        "recomendacion": "aplicacion_posterior_explicita" if ok else "revisar_compuerta_adopcion",
        "transformacion_permitida": False,
        "adoption_gate_evaluated": True,
        "adoption_gate_result": result["actual"],
        "m000_adoption_recommended": bool(flags.get("m000_adoption_recommended")),
        "m001_adoption_recommended": bool(flags.get("m001_adoption_recommended")),
        "doc04_adoption_recommended": bool(flags.get("doc04_adoption_recommended")),
        "official_file_edit_executed": False,
        "official_edit_requires_explicit_apply_step": bool(flags.get("official_edit_requires_explicit_apply_step")),
        "mutating_mode_authorized": False,
        "external_use_authorized": False,
        "global_closure_authorized": False,
        "report_layer_promoted": False,
        "r4_gamma_global_export_authorized": False,
        "summary": {
            "surfaces": result["surface_count"],
            "findings": 0 if ok else len(result["blockers"]),
        },
        "gate": gate,
        "result": result,
        "findings": [] if ok else result["blockers"],
    }


def render_md(report: dict[str, Any]) -> str:
    result = report["result"]
    lines = [
        "# MOC_CANON_DOC04_ADOPT_GATE_001_REPORT",
        "",
        f"report_id: {report['report_id']}",
        f"expediente: {EXPEDIENTE}",
        f"algoritmo: {ALGORITHM_ID}",
        f"resultado: {report['resultado']}",
        f"recomendacion: {report['recomendacion']}",
        f"adoption_gate_evaluated: {str(report['adoption_gate_evaluated']).lower()}",
        f"adoption_gate_result: {report['adoption_gate_result']}",
        f"m000_adoption_recommended: {str(report['m000_adoption_recommended']).lower()}",
        f"m001_adoption_recommended: {str(report['m001_adoption_recommended']).lower()}",
        f"doc04_adoption_recommended: {str(report['doc04_adoption_recommended']).lower()}",
        "official_file_edit_executed: false",
        f"official_edit_requires_explicit_apply_step: {str(report['official_edit_requires_explicit_apply_step']).lower()}",
        "mutating_mode_authorized: false",
        "external_use_authorized: false",
        "global_closure_authorized: false",
        "report_layer_promoted: false",
        "r4_gamma_global_export_authorized: false",
        "transformacion_permitida: false",
        "",
        "## Resultado",
        "",
        f"- gate_id: {result['gate_id']}",
        f"- actual: {result['actual']}",
        f"- expected: {result['expected']}",
        f"- passed: {str(result['passed']).lower()}",
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
    parser = argparse.ArgumentParser(description="Compuerta no mutante de adopcion MOC Canon/Doc04.")
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
