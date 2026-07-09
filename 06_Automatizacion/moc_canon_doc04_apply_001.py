#!/usr/bin/env python3
"""Verificacion no mutante de aplicacion oficial MOC/Canon/Doc04."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from typing import Any


ALGORITHM_ID = "MOC-CANON-DOC04-APPLY-CHECK-001"
EXPEDIENTE = "MOC-001"
DEFAULT_CASE_FILE = Path(__file__).resolve().parent / "fixtures" / "moc_canon_doc04_apply_001.json"
FORBIDDEN_TRUE_FLAGS = {
    "m000_text_changed",
    "mutating_mode_authorized",
    "external_use_authorized",
    "global_closure_authorized",
    "report_layer_promoted",
    "r4_gamma_global_export_authorized",
    "nivel_c_modified",
    "h_xi_admitted",
    "psi_canonized",
    "regulated_domain_authorized",
}
REQUIRED_TRUE_FLAGS = {
    "m001_official_section_added",
    "doc04_official_section_added",
    "official_application_executed",
}
REQUIRED_SURFACES = {"M000", "M001", "DOC04"}


def load_application(path: Path = DEFAULT_CASE_FILE) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(root: Path, rel_path: str) -> str:
    return (root / rel_path).read_text(encoding="utf-8", errors="replace")


def section_from_heading(text: str, heading: str) -> str:
    if heading not in text:
        return ""
    start = text.index(heading)
    prefix = heading.split(" ", 1)[0]
    level = len(prefix)
    lines = text[start:].splitlines()
    collected: list[str] = []
    for index, line in enumerate(lines):
        if index > 0 and line.startswith("#"):
            next_level = len(line.split(" ", 1)[0])
            if next_level <= level:
                break
        collected.append(line)
    return "\n".join(collected)


def evaluate_application(application: dict[str, Any], root: Path | None = None) -> dict[str, Any]:
    root = root or Path.cwd()
    flags = dict(application.get("flags", {}))
    surfaces = list(application.get("official_surfaces", []))
    blockers: list[str] = []
    warnings: list[str] = []

    for rel_path in application.get("required_documents", []):
        if not (root / str(rel_path)).exists():
            blockers.append(f"documento_requerido_ausente:{rel_path}")

    for flag in sorted(FORBIDDEN_TRUE_FLAGS):
        if flags.get(flag):
            blockers.append(f"flag_prohibido_activo:{flag}")

    for flag in sorted(REQUIRED_TRUE_FLAGS):
        if not flags.get(flag):
            blockers.append(f"flag_requerido_inactivo:{flag}")

    present = {str(item.get("surface", "")) for item in surfaces}
    for surface in sorted(REQUIRED_SURFACES - present):
        blockers.append(f"superficie_ausente:{surface}")

    for item in surfaces:
        surface = str(item.get("surface", ""))
        rel_path = str(item.get("path", ""))
        path = root / rel_path
        if not path.exists():
            continue
        text = read_text(root, rel_path)

        for marker in item.get("required_markers", []):
            if str(marker) not in text:
                blockers.append(f"marcador_ausente:{surface}:{marker}")

        for marker in item.get("required_absent_markers", []):
            if str(marker) in text:
                blockers.append(f"marcador_no_debe_existir:{surface}:{marker}")

        section = text
        heading = item.get("section_heading")
        if heading:
            section = section_from_heading(text, str(heading))
            if not section:
                blockers.append(f"seccion_ausente:{surface}:{heading}")

        for term in item.get("section_forbidden_terms", []):
            if str(term) in section:
                blockers.append(f"termino_prohibido_en_seccion:{surface}:{term}")

        recommendation = str(item.get("recommendation", ""))
        if surface == "M000" and recommendation != "sin_cambio_textual":
            blockers.append("m000_recomendacion_no_defensiva")
        if surface == "M001" and recommendation != "seccion_oficial_adoptada":
            blockers.append("m001_sin_adopcion_oficial")
        if surface == "DOC04" and recommendation != "subseccion_oficial_adoptada":
            blockers.append("doc04_sin_adopcion_oficial")

    if not blockers:
        actual = "aplicacion_oficial_verificada"
        warnings.append("adopcion_acotada_sin_cierre_global")
    else:
        actual = "aplicacion_oficial_bloqueada"

    return {
        "apply_id": str(application.get("apply_id", "")),
        "expected": str(application.get("expected", "")),
        "actual": actual,
        "passed": actual == application.get("expected") and not blockers,
        "blockers": sorted(blockers),
        "warnings": sorted(warnings),
        "surfaces": sorted(present),
        "surface_count": len(surfaces),
    }


def build_report(root: Path | None = None, case_file: Path | None = None) -> dict[str, Any]:
    root = root or Path.cwd()
    application = load_application(case_file or DEFAULT_CASE_FILE)
    result = evaluate_application(application, root)
    ok = bool(result["passed"])
    flags = dict(application.get("flags", {}))
    return {
        "report_id": "MOC-CANON-DOC04-APPLY-CHECK-001-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": EXPEDIENTE,
        "algoritmo": ALGORITHM_ID,
        "resultado": "ok" if ok else "bloqueado",
        "recomendacion": "mantener_adopcion_acotada" if ok else "revisar_aplicacion_oficial",
        "transformacion_permitida": False,
        "official_application_verified": ok,
        "official_application_executed": bool(flags.get("official_application_executed")),
        "m000_text_changed": bool(flags.get("m000_text_changed")),
        "m001_official_section_added": bool(flags.get("m001_official_section_added")),
        "doc04_official_section_added": bool(flags.get("doc04_official_section_added")),
        "mutating_mode_authorized": False,
        "external_use_authorized": False,
        "global_closure_authorized": False,
        "report_layer_promoted": False,
        "r4_gamma_global_export_authorized": False,
        "nivel_c_modified": False,
        "h_xi_admitted": False,
        "psi_canonized": False,
        "regulated_domain_authorized": False,
        "summary": {
            "surfaces": result["surface_count"],
            "findings": 0 if ok else len(result["blockers"]),
        },
        "application": application,
        "result": result,
        "findings": [] if ok else result["blockers"],
    }


def render_md(report: dict[str, Any]) -> str:
    result = report["result"]
    lines = [
        "# MOC_CANON_DOC04_APPLY_CHECK_001_REPORT",
        "",
        f"report_id: {report['report_id']}",
        f"expediente: {EXPEDIENTE}",
        f"algoritmo: {ALGORITHM_ID}",
        f"resultado: {report['resultado']}",
        f"recomendacion: {report['recomendacion']}",
        f"official_application_verified: {str(report['official_application_verified']).lower()}",
        f"official_application_executed: {str(report['official_application_executed']).lower()}",
        f"m000_text_changed: {str(report['m000_text_changed']).lower()}",
        f"m001_official_section_added: {str(report['m001_official_section_added']).lower()}",
        f"doc04_official_section_added: {str(report['doc04_official_section_added']).lower()}",
        "mutating_mode_authorized: false",
        "external_use_authorized: false",
        "global_closure_authorized: false",
        "report_layer_promoted: false",
        "r4_gamma_global_export_authorized: false",
        "nivel_c_modified: false",
        "h_xi_admitted: false",
        "psi_canonized: false",
        "regulated_domain_authorized: false",
        "transformacion_permitida: false",
        "",
        "## Resultado",
        "",
        f"- apply_id: {result['apply_id']}",
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
    parser = argparse.ArgumentParser(description="Verificacion no mutante de aplicacion MOC Canon/Doc04.")
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
