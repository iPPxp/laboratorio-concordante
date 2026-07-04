#!/usr/bin/env python3
"""Clasificador no mutante de advertencias y riesgos de AUT-001."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

REPORT_INPUTS = {
    "minimo": "06_Automatizacion/reportes/do_check_min_repo.json",
    "medio": "06_Automatizacion/reportes/do_check_med_repo.json",
}
AUT_CLOSE_DECISION = "03_Expedientes/AUT-001_Decision_Cierre_Operativo_Completo.md"

DOCUMENTARY_KINDS = {
    "referencia_no_materializada",
    "estatus_ausente",
    "reporte_normalizado_incompleto",
}

HISTORICAL_KINDS = {
    "historial_como_autoridad",
    "historial_como_autoridad_posible",
}

ACTIVE_PREFIXES = (
    "CURRENT_STATE.md",
    "README.md",
    "HANDOFF.md",
    "HANDOFF_PACKAGE.md",
    "CHANGELOG.md",
    "01_Canon/",
    "02_Documentos/",
    "05_Estado_Proyecto/",
    "06_Automatizacion/",
    "03_Expedientes/AUT-001",
)

INHERITED_PREFIXES = (
    "03_Expedientes/AUD-001",
    "03_Expedientes/DO-001",
    "03_Expedientes/RH-",
    "03_Expedientes/REC-",
    "03_Expedientes/P-PI",
    "03_Expedientes/B-001.5",
    "04_Registro_Historico/",
)

CATEGORY_LABELS = {
    "riesgo_activo": "Riesgo activo",
    "deuda_documental": "Deuda documental",
    "advertencia_controlada": "Advertencia controlada",
    "advertencia_heredada": "Advertencia heredada",
    "observacion": "Observacion",
}

CONTROLLED_CONTEXT_CLASSES = {
    "guardrail",
    "decision_registrada",
    "bitacora_historica",
    "meta_check",
    "control_auditoria",
}

GUARDRAIL_MARKERS = (
    "no puede",
    "no permite",
    "no debe",
    "ningun ",
    "ninguna ",
    "fuera de alcance",
    "no cubre",
    "contenido prohibido",
    "no autoriza",
    "debe rechazarse",
    "debe rechazarse o bloquearse",
    "matriz minima de pruebas",
    "aud-t",
    "med-historial",
    "principio de autoridad",
    "orden local de autoridad",
    "puede proponer",
)


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def is_active_file(file_rel: str) -> bool:
    return any(file_rel == prefix or file_rel.startswith(prefix) for prefix in ACTIVE_PREFIXES)


def is_inherited_file(file_rel: str) -> bool:
    return any(file_rel.startswith(prefix) for prefix in INHERITED_PREFIXES)


def normalize(source: str, item: dict[str, Any]) -> dict[str, Any]:
    return {
        "source": source,
        "severity": item.get("severity", "warning"),
        "check_id": item.get("check_id", source),
        "kind": item.get("kind", "hallazgo"),
        "file": item.get("file", "no_detectado"),
        "detail": item.get("detail", ""),
        "evidence": item.get("evidence", ""),
    }


def dedupe_key(item: dict[str, Any]) -> tuple[str, str, str, str]:
    return (
        item.get("check_id", ""),
        item.get("kind", ""),
        item.get("file", ""),
        item.get("detail", ""),
    )


def extract_source_context(root: Path, item: dict[str, Any], radius: int = 6) -> dict[str, Any]:
    file_rel = item.get("file", "")
    path = root / file_rel
    if not path.exists() or not path.is_file():
        return {"matched_line": None, "lines": []}

    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    evidence = (item.get("evidence") or "").strip()
    detail = (item.get("detail") or "").lstrip("- ").strip()
    needles = [value for value in (evidence, detail) if value]

    matched = None
    for needle in needles:
        for index, line in enumerate(lines):
            if needle in line:
                matched = index
                break
        if matched is not None:
            break

    if matched is None:
        return {"matched_line": None, "lines": []}

    start = max(0, matched - radius)
    end = min(len(lines), matched + radius + 1)
    return {
        "matched_line": matched + 1,
        "lines": [
            {"line": line_no + 1, "text": lines[line_no]}
            for line_no in range(start, end)
        ],
    }


def context_text(source_context: dict[str, Any]) -> str:
    return "\n".join(str(line.get("text", "")) for line in source_context.get("lines", [])).lower()


def context_class_for(item: dict[str, Any], source_context: dict[str, Any]) -> str:
    file_rel = item.get("file", "")
    evidence = (item.get("evidence") or "").lower()
    detail = (item.get("detail") or "").lower()
    context = context_text(source_context)

    if file_rel == "CHANGELOG.md":
        return "bitacora_historica"
    if file_rel == "05_Estado_Proyecto/DECISIONES.md":
        return "decision_registrada"
    if item.get("check_id", "").startswith("MED-") and "`med-" in context:
        return "meta_check"
    if "indicar si la intervencion modifica" in evidence or "indicar si la intervencion modifica" in context:
        return "control_auditoria"
    if any(marker in context for marker in GUARDRAIL_MARKERS):
        return "guardrail"
    if any(marker in evidence or marker in detail for marker in GUARDRAIL_MARKERS):
        return "guardrail"
    return "riesgo_real"


def treatment_for(context_class: str, category: str) -> str:
    if category == "deuda_documental":
        return "pendiente_normalizacion_documental"
    if category == "advertencia_heredada":
        return "conservar_deuda_historica"
    if category == "advertencia_controlada":
        return {
            "guardrail": "controlado_por_guardrail",
            "decision_registrada": "controlado_por_decision_registrada",
            "bitacora_historica": "controlado_por_historial",
            "meta_check": "controlado_por_definicion_de_check",
            "control_auditoria": "controlado_por_regla_de_auditoria",
        }.get(context_class, "controlado_provisionalmente")
    if category == "riesgo_activo":
        return "pendiente_revision_operativa"
    return "conservado_sin_tratamiento"


def classify(item: dict[str, Any], root: Path) -> dict[str, Any]:
    file_rel = item.get("file", "")
    kind = item.get("kind", "")
    check_id = item.get("check_id", "")
    evidence = (item.get("evidence") or "").lower()
    detail = (item.get("detail") or "").lower()
    active_file = is_active_file(file_rel)
    inherited_file = is_inherited_file(file_rel)
    source_context = extract_source_context(root, item)
    context_class = context_class_for(item, source_context)
    controlled_context = context_class in CONTROLLED_CONTEXT_CLASSES

    if kind in DOCUMENTARY_KINDS or check_id in {"MED-REFERENCIAS", "MED-ESTATUS", "MED-REPORTES"}:
        category = "deuda_documental"
        operational_severity = "media" if active_file else "baja"
        rationale = "Hallazgo documental o de normalizacion; requiere orden, no transformacion inmediata."
    elif kind in HISTORICAL_KINDS or check_id == "MED-HISTORIAL":
        if controlled_context and not inherited_file:
            category = "advertencia_controlada"
            operational_severity = "media"
            rationale = "Aparece en superficie vigente, pero el contexto la controla como guardrail, historial o definicion interna."
        elif active_file:
            category = "riesgo_activo"
            operational_severity = "media"
            rationale = "Aparece en superficie vigente o tecnica activa; revisar que el historial no opere como autoridad."
        else:
            category = "advertencia_heredada"
            operational_severity = "baja"
            rationale = "Proviene de expediente historico, cerrado o pausado; conservar como deuda heredada."
    elif kind == "expediente_cerrado_afectado" or check_id == "MED-CERRADOS":
        if controlled_context and not inherited_file:
            category = "advertencia_controlada"
            operational_severity = "alta"
            rationale = "La mencion de expediente cerrado aparece como prohibicion, compuerta o control registrado."
        else:
            category = "riesgo_activo" if active_file else "advertencia_heredada"
            operational_severity = "alta" if active_file else "media"
            rationale = "Puede tocar expediente cerrado; requiere permiso explicito antes de cualquier cambio."
    elif kind == "accion_de_nivel_sensible" or check_id == "MED-NIVELES":
        if inherited_file:
            category = "advertencia_heredada"
            operational_severity = "baja"
            rationale = "La accion sensible esta registrada en un expediente cerrado, pausado o historico."
        elif controlled_context:
            category = "advertencia_controlada"
            operational_severity = "alta" if file_rel.startswith(("01_Canon/", "02_Documentos/")) else "media"
            rationale = "La linea toca superficie sensible, pero el contexto la controla como prohibicion, decision registrada o regla de auditoria."
        else:
            category = "riesgo_activo"
            operational_severity = "alta" if file_rel.startswith(("01_Canon/", "02_Documentos/")) else "media"
            rationale = "La linea toca Canon, documento oficial, estado o superficie activa."
    elif "canon" in evidence or "documento oficial" in evidence or "expediente cerrado" in evidence or "canon" in detail:
        if controlled_context and not inherited_file:
            category = "advertencia_controlada"
            operational_severity = "media"
            rationale = "Menciona superficie de autoridad, pero el contexto la trata como control o registro no mutante."
        else:
            category = "riesgo_activo" if active_file else "advertencia_heredada"
            operational_severity = "media"
            rationale = "Menciona superficie de autoridad o cierre; mantener control operativo."
    else:
        category = "observacion"
        operational_severity = "baja"
        rationale = "Hallazgo conservado sin clasificacion de riesgo fuerte."

    enriched = dict(item)
    enriched.update({
        "category": category,
        "category_label": CATEGORY_LABELS[category],
        "operational_severity": operational_severity,
        "active_file": active_file,
        "inherited_file": inherited_file,
        "context_class": context_class,
        "treatment_status": treatment_for(context_class, category),
        "risk_blocks_closure": category == "riesgo_activo",
        "source_context": source_context,
        "rationale": rationale,
    })
    return enriched


def load_findings(root: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    source_reports: dict[str, Any] = {}
    raw: list[dict[str, Any]] = []
    for source, rel_path in REPORT_INPUTS.items():
        path = root / rel_path
        if not path.exists():
            continue
        report = read_json(path)
        source_reports[source] = {
            "path": rel_path,
            "report_id": report.get("report_id"),
            "resultado": report.get("resultado"),
            "findings": len(report.get("findings", [])),
        }
        raw.extend(normalize(source, item) for item in report.get("findings", []))

    seen: set[tuple[str, str, str, str]] = set()
    deduped: list[dict[str, Any]] = []
    for item in raw:
        key = dedupe_key(item)
        if key in seen:
            continue
        seen.add(key)
        deduped.append(item)
    return source_reports, deduped


def result_for(classified: list[dict[str, Any]]) -> tuple[str, str]:
    active_high = [item for item in classified if item["category"] == "riesgo_activo" and item["operational_severity"] == "alta"]
    active_any = [item for item in classified if item["category"] == "riesgo_activo"]
    controlled = [item for item in classified if item["category"] == "advertencia_controlada"]
    if active_high:
        return "riesgo_controlado", "revisar_riesgos_activos_sin_transformar"
    if active_any:
        return "advertencia_clasificada", "priorizar_riesgos_activos"
    if controlled:
        return "advertencia_clasificada", "preparar_cierre_tecnico_provisional"
    if classified:
        return "advertencia_clasificada", "normalizar_deuda_documental"
    return "ok", "aprobar_lectura"


def build_report(root: Path) -> dict[str, Any]:
    source_reports, raw_findings = load_findings(root)
    classified = [classify(item, root) for item in raw_findings]
    by_category = dict(Counter(item["category"] for item in classified))
    by_operational_severity = dict(Counter(item["operational_severity"] for item in classified))
    by_context_class = dict(Counter(item["context_class"] for item in classified))
    by_treatment_status = dict(Counter(item["treatment_status"] for item in classified))
    by_check = dict(Counter(item["check_id"] for item in classified))
    by_file = dict(Counter(item["file"] for item in classified))
    resultado, recomendacion = result_for(classified)
    active_any = [item for item in classified if item["category"] == "riesgo_activo"]
    closure_registered = (root / AUT_CLOSE_DECISION).exists()
    if closure_registered and not active_any and recomendacion in {"preparar_cierre_tecnico_provisional", "normalizar_deuda_documental"}:
        recomendacion = "mantener_cierre_operativo"
    next_actions = [
        "Decidir o mantener cierre de AUT-001 si no quedan riesgos activos reales.",
        "Mantener advertencias heredadas como deuda historica sin transformar.",
        "Mantener advertencias controladas visibles; no borrarlas del reporte.",
        "Normalizar referencias o estatus faltantes solo mediante decision posterior.",
    ]
    if closure_registered and not active_any:
        next_actions[0] = "Mantener cierre operativo de AUT-001 con deuda documental visible."

    return {
        "report_id": "DO-LAB-RISK-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": "AUT-001",
        "algoritmo": "DO-LAB-RISK-001",
        "resultado": resultado,
        "recomendacion": recomendacion,
        "transformacion_permitida": False,
        "source_reports": source_reports,
        "summary": {
            "findings_considered": len(classified),
            "by_category": by_category,
            "by_operational_severity": by_operational_severity,
            "by_context_class": by_context_class,
            "by_treatment_status": by_treatment_status,
            "by_check": by_check,
            "top_files": dict(sorted(by_file.items(), key=lambda item: item[1], reverse=True)[:15]),
            "risk_blocks_closure": any(item.get("risk_blocks_closure") for item in active_any),
        },
        "next_actions": next_actions,
        "findings": classified,
    }


def render_md(report: dict[str, Any]) -> str:
    summary = report["summary"]
    findings = report["findings"]
    lines = [
        "# LAB_RISK_REPORT",
        "",
        f"report_id: {report['report_id']}",
        "expediente: AUT-001",
        "algoritmo: DO-LAB-RISK-001",
        f"resultado: {report['resultado']}",
        f"recomendacion: {report['recomendacion']}",
        "transformacion_permitida: false",
        "",
        "## Resumen por categoria",
        "",
    ]
    for category in ("riesgo_activo", "advertencia_controlada", "deuda_documental", "advertencia_heredada", "observacion"):
        lines.append(f"- {category}: {summary['by_category'].get(category, 0)}")
    lines.extend(["", "## Resumen por severidad", ""])
    for severity in ("alta", "media", "baja"):
        lines.append(f"- {severity}: {summary['by_operational_severity'].get(severity, 0)}")
    lines.extend(["", "## Resumen por contexto", ""])
    for context_class, count in sorted(summary.get("by_context_class", {}).items()):
        lines.append(f"- {context_class}: {count}")
    lines.extend(["", "## Riesgos activos", ""])
    active = [item for item in findings if item["category"] == "riesgo_activo"]
    if not active:
        lines.append("- Sin riesgos activos clasificados.")
    else:
        for item in active[:30]:
            line = f"- [{item['operational_severity']}] {item['check_id']} {item['file']} - {item['kind']}: {item['detail']}"
            line += f" | contexto: {item.get('context_class', 'no_detectado')}"
            if item.get("evidence"):
                line += f" | evidencia: {item['evidence']}"
            lines.append(line)
        remaining = len(active) - 30
        if remaining > 0:
            lines.append(f"- ... {remaining} riesgos activos adicionales en JSON.")
    lines.extend(["", "## Advertencias controladas", ""])
    controlled = [item for item in findings if item["category"] == "advertencia_controlada"]
    if not controlled:
        lines.append("- Sin advertencias controladas.")
    else:
        for item in controlled[:30]:
            line = f"- [{item['operational_severity']}] {item['check_id']} {item['file']} - {item['kind']}: {item['treatment_status']}"
            line += f" | contexto: {item.get('context_class', 'no_detectado')}"
            if item.get("evidence"):
                line += f" | evidencia: {item['evidence']}"
            lines.append(line)
        remaining = len(controlled) - 30
        if remaining > 0:
            lines.append(f"- ... {remaining} advertencias controladas adicionales en JSON.")
    lines.extend(["", "## Deuda documental", ""])
    documental = [item for item in findings if item["category"] == "deuda_documental"]
    if not documental:
        lines.append("- Sin deuda documental clasificada.")
    else:
        for item in documental[:20]:
            lines.append(f"- [{item['operational_severity']}] {item['file']} - {item['kind']}: {item['detail']}")
        remaining = len(documental) - 20
        if remaining > 0:
            lines.append(f"- ... {remaining} deudas documentales adicionales en JSON.")
    lines.extend(["", "## Advertencias heredadas", ""])
    inherited = [item for item in findings if item["category"] == "advertencia_heredada"]
    lines.append(f"- total: {len(inherited)}")
    lines.extend(["", "## Siguientes acciones", ""])
    lines.extend(f"- {item}" for item in report["next_actions"])
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Clasificador no mutante de advertencias y riesgos de AUT-001.")
    parser.add_argument("--format", choices=("json", "md"), default="json")
    parser.add_argument("--output", help="Ruta de salida del reporte.")
    args = parser.parse_args(argv)

    root = Path.cwd()
    report = build_report(root)
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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
