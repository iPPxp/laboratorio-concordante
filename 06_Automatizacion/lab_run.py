#!/usr/bin/env python3
"""Comando unico no mutante para correr la automatizacion de AUT-001."""

from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

MODULE_DIR = Path(__file__).resolve().parent
REPORT_DIR = MODULE_DIR / "reportes"
KEY_TARGETS = [
    "CURRENT_STATE.md",
    "05_Estado_Proyecto/ESTADO_ACTUAL.md",
    "03_Expedientes/AUT-001.md",
    "02_Documentos/C-001_Especificacion_Tecnica_Auditor.md",
]
AUT_CLOSE_DECISION = "03_Expedientes/AUT-001_Decision_Cierre_Operativo_Completo.md"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"No se pudo cargar modulo: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def load_components() -> dict[str, Any]:
    return {
        "min": load_module("do_check_min_component", MODULE_DIR / "do_check_min.py"),
        "med": load_module("do_check_med_component", MODULE_DIR / "do_check_med.py"),
        "board": load_module("lab_status_board_component", MODULE_DIR / "lab_status_board.py"),
        "continuity": load_module("lab_continuity_component", MODULE_DIR / "lab_continuity_report.py"),
        "risk": load_module("lab_risk_component", MODULE_DIR / "lab_risk_classifier.py"),
        "summary": load_module("lab_summary_component", MODULE_DIR / "lab_executive_summary.py"),
        "r001": load_module("r001_table_checks_component", MODULE_DIR / "r001_table_checks.py"),
        "ao_ext": load_module("ao_ext_confluence_component", MODULE_DIR / "ao_ext_confluence.py"),
        "moc": load_module("moc_eval_component", MODULE_DIR / "moc_eval.py"),
    }


def assert_inside(root: Path, path: Path) -> None:
    root_resolved = root.resolve()
    path_resolved = path.resolve()
    if path_resolved != root_resolved and root_resolved not in path_resolved.parents:
        raise SystemExit(f"Ruta fuera del repositorio: {path}")


def min_targets(root: Path, min_mod, scope: str) -> list[Path]:
    if scope == "repo":
        return list(min_mod.iter_md(root))
    targets = []
    for rel_name in KEY_TARGETS:
        path = root / rel_name
        if path.exists() and path.suffix.lower() == ".md":
            targets.append(path)
    return sorted(set(targets))


def build_min_report(root: Path, min_mod, scope: str) -> dict[str, Any]:
    existing = {min_mod.rel(path, root) for path in min_mod.iter_md(root)}
    checked = [min_mod.check_file(path, root, existing) for path in sorted(set(min_targets(root, min_mod, scope)))]
    findings = [finding for item in checked for finding in item["findings"]]
    for source in min_mod.REQUIRED_SOURCES:
        if not (root / source).exists():
            min_mod.add(findings, "block", "fuente_minima_ausente", source, "Fuente minima requerida no encontrada.")
    resultado, recomendacion = min_mod.result_for(findings)
    return {
        "report_id": "DO-CHECK-MIN-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": "AUT-001",
        "algoritmo": "DO-CHECK-MIN-001",
        "resultado": resultado,
        "recomendacion": recomendacion,
        "transformacion_permitida": False,
        "scope": scope,
        "fuentes_minimas": min_mod.REQUIRED_SOURCES,
        "summary": {"files_checked": len(checked), "findings": len(findings)},
        "targets": checked,
        "findings": findings,
    }


def write_report(root: Path, rel_path: str, content: str) -> None:
    out_path = root / rel_path
    assert_inside(root, out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(content, encoding="utf-8")


def write_json(root: Path, rel_path: str, report: dict[str, Any]) -> None:
    write_report(root, rel_path, json.dumps(report, ensure_ascii=True, indent=2) + "\n")


def report_result(report: dict[str, Any]) -> str:
    return str(report.get("resultado", "no_detectado"))


def combine_result(reports: list[dict[str, Any]]) -> tuple[str, str]:
    results = {report_result(report) for report in reports}
    recommendations = {str(report.get("recomendacion", "")) for report in reports}
    if "bloqueado" in results:
        return "bloqueado", "bloquear"
    if "atencion_requerida" in results:
        return "advertencia", "revisar_riesgos_altos_sin_transformar"
    if "preparar_cierre_tecnico_provisional" in recommendations:
        return "advertencia", "preparar_cierre_tecnico_provisional"
    if "advertencia" in results or "riesgo_controlado" in results or "advertencia_clasificada" in results:
        return "advertencia", "continuar_sin_transformar"
    return "ok", "aprobar_lectura"


def step_entry(name: str, algorithm: str, report: dict[str, Any], md_path: str, json_path: str) -> dict[str, Any]:
    summary = report.get("summary", {})
    findings = summary.get("findings", summary.get("combined_findings", summary.get("findings_considered", 0)))
    return {
        "name": name,
        "algorithm": algorithm,
        "resultado": report_result(report),
        "recomendacion": report.get("recomendacion", "no_detectada"),
        "findings": findings,
        "markdown": md_path,
        "json": json_path,
    }


def render_run_md(report: dict[str, Any]) -> str:
    lines = [
        "# LAB_RUN_REPORT",
        "",
        f"report_id: {report['report_id']}",
        "expediente: AUT-001",
        "algoritmo: DO-LAB-RUN-001",
        f"resultado: {report['resultado']}",
        f"recomendacion: {report['recomendacion']}",
        "transformacion_permitida: false",
        f"scope: {report['scope']}",
        "",
        "## Pasos",
        "",
    ]
    for step in report["steps"]:
        lines.append(f"- {step['algorithm']}: {step['resultado']} ({step['findings']} hallazgos)")
    lines.extend(["", "## Reportes generados", ""])
    for step in report["steps"]:
        lines.append(f"- {step['markdown']}")
        lines.append(f"- {step['json']}")
    lines.extend(["", "## Siguiente accion", ""])
    lines.append(f"- {report['next_action']}")
    return "\n".join(lines) + "\n"


def build_run_report(root: Path, scope: str) -> dict[str, Any]:
    components = load_components()
    min_report = build_min_report(root, components["min"], scope)
    med_report = components["continuity"].build_med_report(root, components["med"], scope)
    board_report = components["board"].build_report(root)
    continuity_report = components["continuity"].build_report(root, scope)

    write_json(root, "06_Automatizacion/reportes/do_check_min_repo.json", min_report)
    write_report(root, "06_Automatizacion/reportes/do_check_min_repo.md", components["min"].render_md(min_report))
    write_json(root, "06_Automatizacion/reportes/do_check_med_repo.json", med_report)
    write_report(root, "06_Automatizacion/reportes/do_check_med_repo.md", components["med"].render_md(med_report))

    r001_report = components["r001"].build_report(root)
    write_json(root, "06_Automatizacion/reportes/r001_table_checks_report.json", r001_report)
    write_report(root, "06_Automatizacion/reportes/r001_table_checks_report.md", components["r001"].render_md(r001_report))

    ao_ext_report = components["ao_ext"].build_report(root)
    write_json(root, "06_Automatizacion/reportes/ao_ext_confluence_report.json", ao_ext_report)
    write_report(root, "06_Automatizacion/reportes/ao_ext_confluence_report.md", components["ao_ext"].render_md(ao_ext_report))

    moc_report = components["moc"].build_report(root)
    write_json(root, "06_Automatizacion/reportes/moc_eval_report.json", moc_report)
    write_report(root, "06_Automatizacion/reportes/moc_eval_report.md", components["moc"].render_md(moc_report))

    risk_report = components["risk"].build_report(root)
    write_json(root, "06_Automatizacion/reportes/lab_risk_report.json", risk_report)
    write_report(root, "06_Automatizacion/reportes/lab_risk_report.md", components["risk"].render_md(risk_report))

    write_json(root, "06_Automatizacion/reportes/lab_status_board.json", board_report)
    write_report(root, "06_Automatizacion/reportes/lab_status_board.md", components["board"].render_md(board_report))
    write_json(root, "06_Automatizacion/reportes/lab_continuity_report.json", continuity_report)
    write_report(root, "06_Automatizacion/reportes/lab_continuity_report.md", components["continuity"].render_md(continuity_report))

    resultado, recomendacion = combine_result([min_report, med_report, board_report, continuity_report, risk_report, r001_report, ao_ext_report, moc_report])
    run_report = {
        "report_id": "DO-LAB-RUN-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": "AUT-001",
        "algoritmo": "DO-LAB-RUN-001",
        "resultado": resultado,
        "recomendacion": recomendacion,
        "transformacion_permitida": False,
        "scope": scope,
        "steps": [
            step_entry("chequeo_minimo", "DO-CHECK-MIN-001", min_report, "06_Automatizacion/reportes/do_check_min_repo.md", "06_Automatizacion/reportes/do_check_min_repo.json"),
            step_entry("chequeo_medio", "DO-CHECK-MED-001", med_report, "06_Automatizacion/reportes/do_check_med_repo.md", "06_Automatizacion/reportes/do_check_med_repo.json"),
            step_entry("tablero_estado", "DO-STATE-BOARD-001", board_report, "06_Automatizacion/reportes/lab_status_board.md", "06_Automatizacion/reportes/lab_status_board.json"),
            step_entry("continuidad_integrada", "DO-LAB-CONTINUITY-001", continuity_report, "06_Automatizacion/reportes/lab_continuity_report.md", "06_Automatizacion/reportes/lab_continuity_report.json"),
            step_entry("clasificacion_riesgos", "DO-LAB-RISK-001", risk_report, "06_Automatizacion/reportes/lab_risk_report.md", "06_Automatizacion/reportes/lab_risk_report.json"),
            step_entry("r001_table_checks", "R001-TABLE-CHECK-001", r001_report, "06_Automatizacion/reportes/r001_table_checks_report.md", "06_Automatizacion/reportes/r001_table_checks_report.json"),
            step_entry("ao_ext_confluence", "AO-EXT-CONF-001", ao_ext_report, "06_Automatizacion/reportes/ao_ext_confluence_report.md", "06_Automatizacion/reportes/ao_ext_confluence_report.json"),
            step_entry("moc_eval", "MOC-EVAL-001", moc_report, "06_Automatizacion/reportes/moc_eval_report.md", "06_Automatizacion/reportes/moc_eval_report.json"),
        ],
        "next_action": "Decidir o mantener el estatus de cierre de AUT-001 con advertencias visibles.",
    }
    if (root / AUT_CLOSE_DECISION).exists() and run_report["resultado"] in {"ok", "advertencia"}:
        run_report["recomendacion"] = "mantener_cierre_operativo"
        run_report["next_action"] = "Mantener cierre operativo de AUT-001 con deuda documental visible."

    summary_report = components["summary"].build_report(
        root,
        run_report=run_report,
        risk_report=risk_report,
        board_report=board_report,
        continuity_report=continuity_report,
    )
    write_json(root, "06_Automatizacion/reportes/lab_executive_summary.json", summary_report)
    write_report(root, "06_Automatizacion/reportes/lab_executive_summary.md", components["summary"].render_md(summary_report))
    run_report["steps"].append(step_entry("resumen_ejecutivo", "DO-LAB-SUMMARY-001", summary_report, "06_Automatizacion/reportes/lab_executive_summary.md", "06_Automatizacion/reportes/lab_executive_summary.json"))
    run_report["executive_summary"] = {
        "resultado": summary_report.get("resultado"),
        "recomendacion": summary_report.get("recomendacion"),
        "headline": summary_report.get("headline"),
    }
    run_report["resultado"], run_report["recomendacion"] = combine_result([min_report, med_report, board_report, continuity_report, risk_report, r001_report, ao_ext_report, moc_report, summary_report])
    if (root / AUT_CLOSE_DECISION).exists() and run_report["resultado"] in {"ok", "advertencia"}:
        run_report["recomendacion"] = "mantener_cierre_operativo"

    write_json(root, "06_Automatizacion/reportes/lab_run_report.json", run_report)
    write_report(root, "06_Automatizacion/reportes/lab_run_report.md", render_run_md(run_report))
    return run_report


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Comando unico no mutante del Laboratorio.")
    parser.add_argument("--scope", choices=("repo", "claves"), default="repo")
    parser.add_argument("--format", choices=("json", "md"), default="md")
    parser.add_argument("--output", help="Ruta opcional para copiar el reporte final.")
    args = parser.parse_args(argv)

    root = Path.cwd()
    report = build_run_report(root, args.scope)
    output = json.dumps(report, ensure_ascii=True, indent=2) + "\n"
    if args.format == "md":
        output = render_run_md(report)
    if args.output:
        out_path = root / args.output
        assert_inside(root, out_path)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output, encoding="utf-8")
    else:
        sys.stdout.write(output)
    return 0 if report["resultado"] in {"ok", "advertencia"} else 2


if __name__ == "__main__":
    raise SystemExit(main())
