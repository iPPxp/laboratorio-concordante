#!/usr/bin/env python3
"""Serializacion local no mutante de REPORT_LAYER para AO-REPORT-SERIAL-001.

Valida un sobre comun para reportes de varios frentes sin promover
REPORT_LAYER a Nivel C, sin exportarlo como autoridad global y sin autorizar
transformaciones materiales.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ALGORITHM_ID = "AO-REPORT-SERIAL-001"
EXPEDIENTE = "AO-001"
DEFAULT_CASE_FILE = Path(__file__).resolve().parent / "fixtures" / "report_layer_serialization_cases.json"

SCHEMA_ID = "REPORT-LAYER-SERIAL-v0"
ACCEPTED_SCHEMA_VERSIONS = {"0.1-local"}

SERIAL_REQUIRED_FIELDS = {
    "serial_id",
    "schema_id",
    "schema_version",
    "origin_front",
    "source_artifact",
    "source_family",
    "projection_target",
    "witness",
    "authority_claim",
    "export_scope",
    "field_map",
    "roundtrip_loss",
    "global_authority_claim",
    "report_layer",
}

C002_REQUIRED_FIELDS = {
    "report_id",
    "artefacto_revisado",
    "operador_fase",
    "resultado",
    "tipo_hallazgo",
    "ubicacion",
    "evidencia",
    "estatus_afirmacion",
    "decisiones_permitidas",
    "decision_emitida",
    "transformacion_permitida",
    "dependencias",
    "deudas_generadas",
    "recomendacion",
}

FIELD_MAP_REQUIRED = {
    "serial_id",
    "origin_front",
    "source_artifact",
    "source_family",
    "projection_target",
    "witness",
    "evidence",
    "assertion_status",
    "allowed_decisions",
    "emitted_decision",
    "transformation_allowed",
    "debts",
    "recommendation",
    "authority_claim",
    "dependencies",
}

PROTECTED_FIELDS = {
    "report_id",
    "artefacto_revisado",
    "resultado",
    "evidencia",
    "estatus_afirmacion",
    "decision_emitida",
    "transformacion_permitida",
    "deudas_generadas",
    "witness",
    "source_family",
    "projection_target",
    "authority_claim",
}

SAFE_OUTCOMES = {
    "serializable_interfrente_no_mutante",
    "serializable_con_divergencia_clasificada",
    "bloqueo_serializacion_minima",
    "bloqueo_version",
    "bloqueo_testigo",
    "bloqueo_mapa_campos",
    "bloqueo_perdida_campo_protegido",
    "bloqueo_autoridad",
    "bloqueo_recomendacion_como_decision",
    "bloqueo_modo_mutante",
}


@dataclass(frozen=True)
class SerializationResult:
    case_id: str
    expected: str
    actual: str
    passed: bool
    detail: str
    origin_front: str
    source_family: str
    blockers: tuple[str, ...]
    warnings: tuple[str, ...]


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def is_empty(value: Any) -> bool:
    return value is None or value == "" or value == [] or value == {}


def load_suite(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def missing_fields(item: dict[str, Any], fields: set[str], allow_empty: set[str] | None = None) -> list[str]:
    allowed = allow_empty or set()
    return sorted(field for field in fields if field not in item or (field not in allowed and is_empty(item[field])))


def evaluate_case(case: dict[str, Any]) -> SerializationResult:
    envelope = dict(case.get("serial_envelope", {}))
    report_item = dict(envelope.get("report_layer", {}))
    blockers: list[str] = []
    warnings: list[str] = []

    missing_serial = missing_fields(envelope, SERIAL_REQUIRED_FIELDS - {"witness"}, allow_empty={"roundtrip_loss"})
    if not str(envelope.get("witness", "")).strip():
        blockers.append("witness:ausente")
        actual = "bloqueo_testigo"
    elif missing_serial:
        blockers.extend(f"missing_serial:{field}" for field in missing_serial)
        actual = "bloqueo_serializacion_minima"
    elif envelope.get("schema_id") != SCHEMA_ID or envelope.get("schema_version") not in ACCEPTED_SCHEMA_VERSIONS:
        blockers.append(f"version_no_aceptada:{envelope.get('schema_id')}:{envelope.get('schema_version')}")
        actual = "bloqueo_version"
    else:
        field_map = dict(envelope.get("field_map", {}))
        missing_map = missing_fields(field_map, FIELD_MAP_REQUIRED)
        missing_report = missing_fields(report_item, C002_REQUIRED_FIELDS)
        if missing_map:
            blockers.extend(f"missing_map:{field}" for field in missing_map)
            actual = "bloqueo_mapa_campos"
        elif missing_report:
            blockers.extend(f"missing_report:{field}" for field in missing_report)
            actual = "bloqueo_serializacion_minima"
        elif bool(envelope.get("global_authority_claim")) or str(envelope.get("authority_claim")) in {"nivel_c", "canon", "autoridad_global"} or bool(report_item.get("promueve_report_layer")):
            blockers.append(f"autoridad_no_autorizada:{envelope.get('authority_claim')}")
            actual = "bloqueo_autoridad"
        elif bool(report_item.get("recomendacion_convertida_en_decision")):
            blockers.append("recomendacion_convertida_en_decision")
            actual = "bloqueo_recomendacion_como_decision"
        elif bool(report_item.get("transformacion_permitida")) or str(report_item.get("decision_emitida")) == "continuar_con_cambio_acotado":
            blockers.append("modo_mutante_no_autorizado")
            actual = "bloqueo_modo_mutante"
        else:
            lost_fields = set(str(field) for field in as_list(envelope.get("roundtrip_loss")))
            protected_loss = sorted(lost_fields & PROTECTED_FIELDS)
            if protected_loss:
                blockers.extend(f"lost:{field}" for field in protected_loss)
                actual = "bloqueo_perdida_campo_protegido"
            elif envelope.get("expected_projection_family") and envelope.get("expected_projection_family") != envelope.get("projection_family"):
                warnings.append("projection_family:diverge")
                actual = "serializable_con_divergencia_clasificada"
            else:
                actual = "serializable_interfrente_no_mutante"

    if actual not in SAFE_OUTCOMES:
        actual = "bloqueo_serializacion_minima"

    expected = str(case.get("expected"))
    return SerializationResult(
        case_id=str(case.get("case_id", "")),
        expected=expected,
        actual=actual,
        passed=actual == expected,
        detail=str(case.get("description", "")),
        origin_front=str(envelope.get("origin_front", "")),
        source_family=str(envelope.get("source_family", "")),
        blockers=tuple(sorted(blockers)),
        warnings=tuple(sorted(warnings)),
    )


def summarize(results: list[SerializationResult]) -> dict[str, Any]:
    by_outcome: dict[str, int] = {}
    by_front: dict[str, int] = {}
    for result in results:
        by_outcome[result.actual] = by_outcome.get(result.actual, 0) + 1
        by_front[result.origin_front] = by_front.get(result.origin_front, 0) + 1
    failures = [result for result in results if not result.passed]
    return {
        "cases": len(results),
        "passed": len(results) - len(failures),
        "failed": len(failures),
        "findings": len(failures),
        "serializable_cases": sum(1 for result in results if result.actual.startswith("serializable")),
        "blocked_cases": sum(1 for result in results if result.actual.startswith("bloqueo")),
        "by_outcome": by_outcome,
        "by_front": by_front,
    }


def build_report(root: Path | None = None, case_file: Path | None = None) -> dict[str, Any]:
    del root
    suite_path = case_file or DEFAULT_CASE_FILE
    suite = load_suite(suite_path)
    results = [evaluate_case(case) for case in suite.get("cases", [])]
    failures = [result for result in results if not result.passed]
    resultado = "ok" if not failures else "bloqueado"
    return {
        "report_id": "AO-REPORT-SERIAL-001-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": EXPEDIENTE,
        "algoritmo": ALGORITHM_ID,
        "suite_id": suite.get("suite_id", "REPORT-LAYER-SERIAL-CASES-001"),
        "resultado": resultado,
        "recomendacion": "mantener_serializacion_local_pre_c" if not failures else "revisar_serializacion_report_layer",
        "transformacion_permitida": False,
        "serializacion_interfrente_local": not failures,
        "global_export_authorized": False,
        "source_evidence": suite.get("source_evidence", []),
        "contract": {
            "schema_id": SCHEMA_ID,
            "accepted_schema_versions": sorted(ACCEPTED_SCHEMA_VERSIONS),
            "required_envelope_fields": sorted(SERIAL_REQUIRED_FIELDS),
            "required_report_fields": sorted(C002_REQUIRED_FIELDS),
            "required_field_map": sorted(FIELD_MAP_REQUIRED),
            "protected_fields": sorted(PROTECTED_FIELDS),
        },
        "condition_effect": {
            "ao_ppi_gc_004": "atendida_localmente_no_global",
            "global_closure_authorized": False,
            "report_layer_promoted": False,
            "nivel_c_created": False,
        },
        "scope_guard": {
            "modifica_doc04": False,
            "modifica_canon": False,
            "crea_nivel_c": False,
            "promueve_report_layer": False,
            "exporta_report_layer_global": False,
            "autoriza_transformacion": False,
            "cierra_confluencia_global": False,
            "cierra_equivalencia_global": False,
        },
        "summary": summarize(results),
        "results": [asdict(result) for result in results],
        "findings": [asdict(result) for result in failures],
    }


def render_md(report: dict[str, Any]) -> str:
    lines = [
        "# AO_REPORT_SERIAL_001_REPORT",
        "",
        f"report_id: {report['report_id']}",
        f"expediente: {EXPEDIENTE}",
        f"algoritmo: {ALGORITHM_ID}",
        f"suite_id: {report['suite_id']}",
        f"resultado: {report['resultado']}",
        f"recomendacion: {report['recomendacion']}",
        "transformacion_permitida: false",
        f"serializacion_interfrente_local: {str(report['serializacion_interfrente_local']).lower()}",
        "global_export_authorized: false",
        "",
        "## Evidencia fuente",
        "",
    ]
    for item in report["source_evidence"]:
        lines.append(f"- {item}")
    lines.extend([
        "",
        "## Contrato",
        "",
        f"- schema_id: {report['contract']['schema_id']}",
        f"- accepted_schema_versions: {', '.join(report['contract']['accepted_schema_versions'])}",
        f"- protected_fields: {', '.join(report['contract']['protected_fields'])}",
        "",
        "## Resumen",
        "",
        f"- cases: {report['summary']['cases']}",
        f"- passed: {report['summary']['passed']}",
        f"- failed: {report['summary']['failed']}",
        f"- serializable_cases: {report['summary']['serializable_cases']}",
        f"- blocked_cases: {report['summary']['blocked_cases']}",
        "",
        "## Guardas",
        "",
    ])
    for key, value in report["scope_guard"].items():
        lines.append(f"- {key}: {str(value).lower()}")
    lines.extend(["", "## Casos", ""])
    for result in report["results"]:
        status = "PASS" if result["passed"] else "FAIL"
        lines.append(f"- {status} `{result['case_id']}` [{result['origin_front']} / {result['source_family']}]: {result['actual']} (esperado: {result['expected']})")
        if result["blockers"]:
            lines.append(f"  - blockers: {', '.join(result['blockers'])}")
        if result["warnings"]:
            lines.append(f"  - warnings: {', '.join(result['warnings'])}")
    lines.extend(["", "## Efecto sobre AO-PPI-GC-004", ""])
    lines.append(f"- ao_ppi_gc_004: {report['condition_effect']['ao_ppi_gc_004']}")
    lines.append("- global_closure_authorized: false")
    lines.append("- report_layer_promoted: false")
    lines.extend(["", "## Dictamen", ""])
    if report["findings"]:
        lines.append("- Hay fallos de expectativa; no usar el contrato de serializacion.")
    else:
        lines.append("- Sin hallazgos bloqueantes.")
        lines.append("- REPORT_LAYER queda serializable localmente entre frentes internos, con versionado y mapa de campos.")
        lines.append("- El resultado no autoriza cierre global, promocion a Nivel C ni transformaciones materiales.")
    return "\n".join(lines) + "\n"


def assert_inside(root: Path, path: Path) -> None:
    root_resolved = root.resolve()
    path_resolved = path.resolve()
    if path_resolved != root_resolved and root_resolved not in path_resolved.parents:
        raise SystemExit(f"Ruta fuera del repositorio: {path}")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Serializacion local no mutante de REPORT_LAYER.")
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
