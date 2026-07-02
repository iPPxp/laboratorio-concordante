#!/usr/bin/env python3
"""Reporte combinado no mutante de continuidad del Laboratorio Concordante."""

from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

MODULE_DIR = Path(__file__).resolve().parent

DEFAULT_KEY_TARGETS = [
    "CURRENT_STATE.md",
    "05_Estado_Proyecto/ESTADO_ACTUAL.md",
    "03_Expedientes/AUT-001.md",
    "02_Documentos/C-001_Especificacion_Tecnica_Auditor.md",
]

EXPECTED_AUTOMATION = [
    "06_Automatizacion/do_check_min.py",
    "06_Automatizacion/do_check_med.py",
    "06_Automatizacion/lab_status_board.py",
    "06_Automatizacion/lab_continuity_report.py",
    "06_Automatizacion/lab_risk_classifier.py",
    "06_Automatizacion/lab_executive_summary.py",
    "06_Automatizacion/lab_run.py",
]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"No se pudo cargar modulo: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_components():
    board = load_module("lab_status_board_component", MODULE_DIR / "lab_status_board.py")
    med = load_module("do_check_med_component", MODULE_DIR / "do_check_med.py")
    return board, med


def collect_med_targets(root: Path, med, scope: str) -> list[Path]:
    if scope == "repo":
        return list(med.iter_md(root))
    targets: list[Path] = []
    for rel_name in DEFAULT_KEY_TARGETS:
        path = (root / rel_name).resolve()
        if path.exists() and path.suffix.lower() == ".md":
            targets.append(path)
    return sorted(set(targets))


def build_med_report(root: Path, med, scope: str) -> dict[str, Any]:
    existing = {med.rel(path, root) for path in med.iter_files(root, med.EXCLUDED_INDEX_DIRS)}
    context = med.build_project_context(root)
    targets = collect_med_targets(root, med, scope)
    checked = [med.check_file(path, root, existing, context) for path in targets]
    findings = [finding for item in checked for finding in item["findings"]]
    findings.extend(med.repository_checks(root, context, existing))

    resultado, recomendacion, estado_aau_local = med.result_for(findings)
    return {
        "report_id": "DO-CHECK-MED-LIVE-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": "AUT-001",
        "algoritmo": "DO-CHECK-MED-001",
        "resultado": resultado,
        "recomendacion": recomendacion,
        "estado_aau_local": estado_aau_local,
        "transformacion_permitida": False,
        "scope": scope,
        "summary": {
            "files_checked": len(checked),
            "findings": len(findings),
            "by_severity": dict(Counter(item["severity"] for item in findings)),
            "by_check": dict(Counter(item["check_id"] for item in findings)),
        },
        "targets": checked,
        "findings": findings,
    }


def normalize_finding(source: str, item: dict[str, Any]) -> dict[str, Any]:
    return {
        "source": source,
        "severity": item.get("severity", "info"),
        "check_id": item.get("check_id", source),
        "kind": item.get("kind", "hallazgo"),
        "file": item.get("file", "no_detectado"),
        "detail": item.get("detail", ""),
        "evidence": item.get("evidence", ""),
    }


def combined_result(board_report: dict[str, Any], med_report: dict[str, Any], findings: list[dict[str, Any]]) -> tuple[str, str]:
    severities = {item["severity"] for item in findings}
    results = {board_report.get("resultado"), med_report.get("resultado")}
    if "block" in severities or "bloqueado" in results:
        return "bloqueado", "bloquear"
    if "warning" in severities or "advertencia" in results:
        return "advertencia", "continuar_sin_transformar"
    return "ok", "aprobar_lectura"


def build_report(root: Path, scope: str = "repo") -> dict[str, Any]:
    board, med = load_components()
    board_report = board.build_report(root)
    med_report = build_med_report(root, med, scope)

    findings = []
    findings.extend(normalize_finding("DO-STATE-BOARD-001", item) for item in board_report.get("findings", []))
    findings.extend(normalize_finding("DO-CHECK-MED-001", item) for item in med_report.get("findings", []))

    resultado, recomendacion = combined_result(board_report, med_report, findings)
    automation = board_report.get("state", {}).get("automatizacion", [])
    present = sum(1 for item in automation if item.get("exists"))

    return {
        "report_id": "DO-LAB-CONTINUITY-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": "AUT-001",
        "algoritmo": "DO-LAB-CONTINUITY-001",
        "resultado": resultado,
        "recomendacion": recomendacion,
        "transformacion_permitida": False,
        "scope": scope,
        "sources": {
            "tablero": board_report["report_id"],
            "chequeo_medio": med_report["report_id"],
        },
        "summary": {
            "board_resultado": board_report.get("resultado"),
            "board_findings": len(board_report.get("findings", [])),
            "med_resultado": med_report.get("resultado"),
            "med_files_checked": med_report.get("summary", {}).get("files_checked", 0),
            "med_findings": len(med_report.get("findings", [])),
            "combined_findings": len(findings),
            "automation_present": present,
            "automation_expected": len(EXPECTED_AUTOMATION),
            "by_severity": dict(Counter(item["severity"] for item in findings)),
        },
        "state": board_report.get("state", {}),
        "next_actions": [
            "Separar advertencias heredadas de riesgos operativos nuevos.",
            "Separar advertencias historicas conocidas de riesgos operativos nuevos.",
            "Mantener transformacion_permitida en false hasta decision explicita.",
        ],
        "component_reports": {
            "tablero": board_report,
            "chequeo_medio": med_report,
        },
        "findings": findings,
    }


def render_md(report: dict[str, Any]) -> str:
    state = report.get("state", {})
    summary = report.get("summary", {})
    lines = [
        "# LAB_CONTINUITY_REPORT",
        "",
        f"report_id: {report['report_id']}",
        "expediente: AUT-001",
        "algoritmo: DO-LAB-CONTINUITY-001",
        f"resultado: {report['resultado']}",
        f"recomendacion: {report['recomendacion']}",
        "transformacion_permitida: false",
        f"scope: {report['scope']}",
        "",
        "## Estado operativo",
        "",
        f"- expediente activo inmediato: {state.get('expediente_activo_inmediato') or 'no_detectado'}",
        f"- proximo objetivo: {state.get('proximo_objetivo') or 'no_detectado'}",
        f"- ultima decision operativa: {state.get('ultima_decision_operativa') or 'no_detectada'}",
        "",
        "## Cobertura integrada",
        "",
        f"- tablero: {summary.get('board_resultado')} ({summary.get('board_findings')} hallazgos)",
        f"- chequeo medio: {summary.get('med_resultado')} ({summary.get('med_files_checked')} archivos, {summary.get('med_findings')} hallazgos)",
        f"- automatizaciones presentes: {summary.get('automation_present')}/{summary.get('automation_expected')}",
        f"- hallazgos combinados: {summary.get('combined_findings')}",
        "",
        "## Riesgos",
        "",
    ]
    if not report["findings"]:
        lines.append("- Sin hallazgos.")
    else:
        for item in report["findings"][:40]:
            line = f"- [{item['severity']}] {item['source']} {item['file']} - {item['kind']}: {item['detail']}"
            if item.get("evidence"):
                line += f" | evidencia: {item['evidence']}"
            lines.append(line)
        remaining = len(report["findings"]) - 40
        if remaining > 0:
            lines.append(f"- ... {remaining} hallazgos adicionales en JSON.")
    lines.extend(["", "## Siguientes acciones", ""])
    lines.extend(f"- {item}" for item in report["next_actions"])
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Reporte combinado no mutante de continuidad del Laboratorio.")
    parser.add_argument("--scope", choices=("repo", "claves"), default="repo")
    parser.add_argument("--format", choices=("json", "md"), default="json")
    parser.add_argument("--output", help="Ruta de salida del reporte.")
    args = parser.parse_args(argv)

    root = Path.cwd()
    report = build_report(root, args.scope)
    output = json.dumps(report, ensure_ascii=True, indent=2) + "\n"
    if args.format == "md":
        output = render_md(report)

    if args.output:
        out_path = (root / args.output).resolve()
        if root.resolve() not in out_path.parents and out_path != root.resolve():
            raise SystemExit(f"Salida fuera del repositorio: {args.output}")
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output, encoding="utf-8")
    else:
        sys.stdout.write(output)
    return 0 if report["resultado"] in {"ok", "advertencia"} else 2


if __name__ == "__main__":
    raise SystemExit(main())
