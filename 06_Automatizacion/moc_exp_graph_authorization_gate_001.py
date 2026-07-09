#!/usr/bin/env python3
"""Compuerta no mutante de autorizacion interna para MOC-EXP-GRAPH-001."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from typing import Any


ALGORITHM_ID = "MOC-GRAPH-CANON-DOC04-GATE-001"
EXPEDIENTE = "MOC-001"
DEFAULT_CASE_FILE = Path(__file__).resolve().parent / "fixtures" / "moc_exp_graph_authorization_gate_001.json"


def load_manifest(path: Path = DEFAULT_CASE_FILE) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def evaluate_manifest(manifest: dict[str, Any]) -> dict[str, Any]:
    flags = dict(manifest.get("flags", {}))
    blockers: list[str] = []
    warnings: list[str] = []

    if not str(manifest.get("rights_holder", "")).strip():
        blockers.append("titularidad_interna_ausente")
    if not flags.get("rights_holder_declared"):
        blockers.append("titularidad_no_declarada")
    if not flags.get("license_document_present"):
        blockers.append("licencia_no_declarada")
    if not flags.get("internal_use_only"):
        blockers.append("uso_no_interno")
    if flags.get("external_publication_requested"):
        blockers.append("publicacion_externa_no_autorizada")
    if flags.get("clinical_or_regulated_use"):
        blockers.append("uso_clinico_o_regulado_no_autorizado")
    if flags.get("real_persons"):
        blockers.append("personas_reales_no_autorizadas")
    if flags.get("h_xi_admission"):
        blockers.append("admision_h_xi_no_autorizada")
    if flags.get("xi_canonization"):
        blockers.append("canonizacion_xi_no_autorizada")
    if flags.get("global_closure_requested"):
        blockers.append("cierre_global_no_autorizado")
    if flags.get("mutating_mode_requested"):
        blockers.append("modo_mutante_no_autorizado")
    if flags.get("official_edit_requested"):
        blockers.append("edicion_oficial_directa_no_autorizada")
    if not flags.get("candidate_amendment_only"):
        blockers.append("alcance_no_limitado_a_propuesta_candidata")
    if not flags.get("requires_future_decision"):
        blockers.append("decision_posterior_no_exigida")

    if not manifest.get("target_surfaces"):
        blockers.append("superficies_destino_ausentes")
    if not manifest.get("source_documents"):
        blockers.append("fuentes_grafo_ausentes")

    if not blockers:
        actual = "autorizacion_interna_preparatoria"
        warnings.append("no_sustituye_asesoria_legal_externa")
    elif any(item in blockers for item in ("publicacion_externa_no_autorizada", "uso_clinico_o_regulado_no_autorizado")):
        actual = "rechazo_por_alcance"
    elif "titularidad_interna_ausente" in blockers or "licencia_no_declarada" in blockers:
        actual = "rechazo_por_derechos"
    else:
        actual = "rechazo_por_autoridad"

    expected = str(manifest.get("expected", "")).strip()
    return {
        "authorization_id": str(manifest.get("authorization_id", "")),
        "expected": expected,
        "actual": actual,
        "passed": actual == expected and not blockers,
        "blockers": sorted(blockers),
        "warnings": sorted(warnings),
    }


def build_report(root: Path | None = None, case_file: Path | None = None) -> dict[str, Any]:
    del root
    manifest = load_manifest(case_file or DEFAULT_CASE_FILE)
    result = evaluate_manifest(manifest)
    ok = bool(result["passed"])
    return {
        "report_id": "MOC-GRAPH-CANON-DOC04-GATE-001-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": EXPEDIENTE,
        "algoritmo": ALGORITHM_ID,
        "resultado": "ok" if ok else "bloqueado",
        "recomendacion": "preparar_matriz_impacto_candidata" if ok else "revisar_autorizacion_interna",
        "transformacion_permitida": False,
        "autorizacion_interna_preparatoria": ok,
        "candidate_amendment_preparation_authorized": ok,
        "official_canon_doc04_edit_authorized": False,
        "external_use_authorized": False,
        "legal_advice_provided": False,
        "requires_external_legal_review_for_publication": True,
        "global_closure_authorized": False,
        "global_export_authorized": False,
        "global_equivalence_authorized": False,
        "global_confluence_authorized": False,
        "report_layer_promoted": False,
        "r4_gamma_global_export_authorized": False,
        "summary": {
            "manifests": 1,
            "passed": 1 if ok else 0,
            "failed": 0 if ok else 1,
            "findings": 0 if ok else 1,
        },
        "manifest": manifest,
        "result": result,
        "findings": [] if ok else [result],
    }


def render_md(report: dict[str, Any]) -> str:
    result = report["result"]
    lines = [
        "# MOC_GRAPH_CANON_DOC04_GATE_001_REPORT",
        "",
        f"report_id: {report['report_id']}",
        f"expediente: {EXPEDIENTE}",
        f"algoritmo: {ALGORITHM_ID}",
        f"resultado: {report['resultado']}",
        f"recomendacion: {report['recomendacion']}",
        f"autorizacion_interna_preparatoria: {str(report['autorizacion_interna_preparatoria']).lower()}",
        f"candidate_amendment_preparation_authorized: {str(report['candidate_amendment_preparation_authorized']).lower()}",
        "official_canon_doc04_edit_authorized: false",
        "external_use_authorized: false",
        "legal_advice_provided: false",
        "requires_external_legal_review_for_publication: true",
        "transformacion_permitida: false",
        "global_closure_authorized: false",
        "global_export_authorized: false",
        "global_equivalence_authorized: false",
        "global_confluence_authorized: false",
        "report_layer_promoted: false",
        "r4_gamma_global_export_authorized: false",
        "",
        "## Resultado",
        "",
        f"- authorization_id: {result['authorization_id']}",
        f"- actual: {result['actual']}",
        f"- expected: {result['expected']}",
        f"- passed: {str(result['passed']).lower()}",
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
    parser = argparse.ArgumentParser(description="Compuerta no mutante de autorizacion interna MOC.")
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

