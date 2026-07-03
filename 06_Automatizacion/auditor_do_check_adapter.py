#!/usr/bin/env python3
"""Adaptador no mutante de DO_CHECK_REPORT a REPORT_ITEM."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from typing import Any

EXPEDIENTE = "AUD-001"
ALGORITHM = "AUDITOR-DO-CHECK-ADAPTER-001"
REQUIRED_FIELDS = {"report_id", "resultado", "recomendacion", "transformacion_permitida"}


def assert_inside(root: Path, path: Path) -> None:
    root_resolved = root.resolve()
    path_resolved = path.resolve()
    if path_resolved != root_resolved and root_resolved not in path_resolved.parents:
        raise SystemExit(f"Ruta fuera del repositorio: {path}")


def source_errors(source: Any) -> list[str]:
    if not isinstance(source, dict):
        return ["DO_CHECK_REPORT debe ser objeto JSON"]
    errors: list[str] = []
    missing = sorted(REQUIRED_FIELDS - set(source))
    if missing:
        errors.append("campos faltantes: " + ", ".join(missing))
    if source.get("transformacion_permitida") is not False:
        errors.append("transformacion_permitida debe ser false")
    if not isinstance(source.get("findings", []), list):
        errors.append("findings debe ser lista")
    return errors


def decisions_for_recommendation(recommendation: str) -> list[str]:
    if recommendation == "aprobar_lectura":
        return ["aprobar_lectura", "continuar_sin_transformar"]
    if recommendation == "continuar_sin_transformar":
        return ["continuar_sin_transformar"]
    if recommendation == "bloquear":
        return ["bloquear"]
    return ["escalar", "continuar_sin_transformar"]


def item_from_finding(source: dict[str, Any], finding: dict[str, Any], index: int) -> dict[str, Any]:
    detail = str(finding.get("detail", "hallazgo sin detalle"))
    evidence = str(finding.get("evidence") or finding.get("detail") or "")
    return {
        "report_item_id": f"{ALGORITHM}-{source.get('report_id', 'DO-CHECK-SIN-ID')}-{index:03d}",
        "fuente_report_id": source.get("report_id", ""),
        "fuente_algoritmo": source.get("algoritmo", ""),
        "operador_abstracto": "calculo",
        "clase_reporte": "calculo_falla",
        "objeto": finding.get("file", ""),
        "resultado": finding.get("severity", source.get("resultado", "no_clasificado")),
        "tipo_hallazgo": finding.get("kind", "hallazgo_no_clasificado"),
        "ubicacion": finding.get("file", ""),
        "descripcion": detail,
        "evidencia": evidence,
        "estatus_afirmacion": "no_clasificado",
        "dependencias": source.get("fuentes_minimas", []),
        "deudas_generadas": [detail] if detail else [],
        "decisiones_permitidas": decisions_for_recommendation(str(source.get("recomendacion", ""))),
        "decision_emitida": "no_aplica",
        "transformacion_permitida": False,
    }


def item_without_findings(source: dict[str, Any]) -> dict[str, Any]:
    return {
        "report_item_id": f"{ALGORITHM}-{source.get('report_id', 'DO-CHECK-SIN-ID')}-000",
        "fuente_report_id": source.get("report_id", ""),
        "fuente_algoritmo": source.get("algoritmo", ""),
        "operador_abstracto": "calculo",
        "clase_reporte": "sin_hallazgo_bloqueante",
        "objeto": "DO_CHECK_REPORT",
        "resultado": source.get("resultado", "ok"),
        "tipo_hallazgo": "sin_hallazgo_bloqueante",
        "ubicacion": "reporte",
        "descripcion": "DO_CHECK_REPORT sin hallazgos proyectado como evidencia no mutante.",
        "evidencia": source.get("report_id", ""),
        "estatus_afirmacion": "no_clasificado",
        "dependencias": source.get("fuentes_minimas", []),
        "deudas_generadas": [],
        "decisiones_permitidas": decisions_for_recommendation(str(source.get("recomendacion", ""))),
        "decision_emitida": "no_aplica",
        "transformacion_permitida": False,
    }


def adapt_report(source: Any) -> dict[str, Any]:
    errors = source_errors(source)
    source_dict = source if isinstance(source, dict) else {}
    findings = source_dict.get("findings", []) if isinstance(source_dict.get("findings", []), list) else []
    items = [item_from_finding(source_dict, finding, index + 1) for index, finding in enumerate(findings)]
    if not items and not errors:
        items = [item_without_findings(source_dict)]
    return {
        "report_id": "AUDITOR-DO-CHECK-ADAPTER-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": EXPEDIENTE,
        "algoritmo": ALGORITHM,
        "modo": "no_mutante",
        "fuente_report_id": source_dict.get("report_id", ""),
        "fuente_algoritmo": source_dict.get("algoritmo", ""),
        "resultado_fuente": source_dict.get("resultado", "no_clasificado"),
        "recomendacion_fuente": source_dict.get("recomendacion", ""),
        "decision_emitida": "no_aplica",
        "transformacion_permitida": False,
        "conforme_c002": not errors and all(item["transformacion_permitida"] is False for item in items),
        "summary": {
            "source_findings": len(findings),
            "report_items": len(items),
            "adapter_errors": errors,
        },
        "report_items": items,
    }


def render_md(report: dict[str, Any]) -> str:
    summary = report["summary"]
    lines = [
        "# AUDITOR_DO_CHECK_ADAPTER_REPORT",
        "",
        f"report_id: {report['report_id']}",
        f"expediente: {report['expediente']}",
        f"algoritmo: {report['algoritmo']}",
        f"fuente_report_id: {report['fuente_report_id']}",
        f"fuente_algoritmo: {report['fuente_algoritmo']}",
        f"conforme_c002: {str(report['conforme_c002']).lower()}",
        "decision_emitida: no_aplica",
        "transformacion_permitida: false",
        "",
        "## Resumen",
        "",
        f"- hallazgos fuente: {summary['source_findings']}",
        f"- report_items: {summary['report_items']}",
        f"- errores adaptador: {len(summary['adapter_errors'])}",
        "",
        "## Report Items",
        "",
    ]
    if not report["report_items"]:
        lines.append("- Sin items proyectados.")
    for item in report["report_items"]:
        lines.append(
            "- "
            + f"{item['report_item_id']} / {item['clase_reporte']} / {item['resultado']}: "
            + f"{item['descripcion']} Decision: {item['decision_emitida']}. "
            + f"Transformacion: {str(item['transformacion_permitida']).lower()}."
        )
    if summary["adapter_errors"]:
        lines.extend(["", "## Errores", ""])
        lines.extend(f"- {error}" for error in summary["adapter_errors"])
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Adaptador no mutante DO_CHECK_REPORT -> REPORT_ITEM.")
    parser.add_argument("input", help="Ruta JSON de DO_CHECK_REPORT.")
    parser.add_argument("--format", choices=("json", "md"), default="md")
    parser.add_argument("--output", help="Ruta de salida del reporte adaptado.")
    args = parser.parse_args(argv)

    root = Path.cwd()
    in_path = root / args.input
    assert_inside(root, in_path)
    source = json.loads(in_path.read_text(encoding="utf-8"))
    report = adapt_report(source)
    output = render_md(report) if args.format == "md" else json.dumps(report, ensure_ascii=True, indent=2) + "\n"
    if args.output:
        out_path = root / args.output
        assert_inside(root, out_path)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output, encoding="utf-8")
    else:
        sys.stdout.write(output)
    return 0 if report["conforme_c002"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
