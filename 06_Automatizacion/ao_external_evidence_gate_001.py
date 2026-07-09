#!/usr/bin/env python3
"""Compuerta no mutante de evidencia externa AO-EXT-EVID-GATE-001."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ALGORITHM_ID = "AO-EXT-EVID-GATE-001"
EXPEDIENTE = "AO-001"
DEFAULT_CASE_FILE = Path(__file__).resolve().parent / "fixtures" / "ao_external_evidence_gate_001_manifests.json"
VALID_OUTCOMES = {
    "admisible_preliminar",
    "pendiente_fuente_real",
    "rechazada_por_alcance",
    "rechazada_por_autoridad",
    "rechazada_por_dominio",
}
HISTORICAL_AUTHORITIES = {
    "historial",
    "registro_historico",
    "autoridad_historica",
    "referencia_historica",
}


@dataclass(frozen=True)
class ExternalEvidenceManifestResult:
    manifest_id: str
    artifact_type: str
    source_uri: str
    expected: str
    actual: str
    passed: bool
    source_family: str
    real_external_source: bool
    control_manifest: bool
    authority: str
    comparable_unit: bool
    blockers: tuple[str, ...]
    warnings: tuple[str, ...]


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def load_suite(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def evaluate_manifest(manifest: dict[str, Any]) -> ExternalEvidenceManifestResult:
    blockers: list[str] = []
    warnings: list[str] = []
    authority = str(manifest.get("authority", "")).strip()
    artifact_type = str(manifest.get("artifact_type", "")).strip()
    source_family = str(manifest.get("source_family", "")).strip()
    source_uri = str(manifest.get("source_uri", "")).strip()
    comparable_unit = bool(manifest.get("comparable_unit_present"))
    real_external_source = bool(manifest.get("real_external_source"))
    control_manifest = bool(manifest.get("control_manifest"))

    if bool(manifest.get("clinical_domain")):
        blockers.append("dominio_clinico_no_autorizado")
    if bool(manifest.get("regulated_domain")):
        blockers.append("dominio_regulado_no_autorizado")
    if bool(manifest.get("contains_real_persons")):
        blockers.append("personas_reales_no_autorizadas")
    if blockers:
        actual = "rechazada_por_dominio"
    elif authority in HISTORICAL_AUTHORITIES or bool(manifest.get("historical_authority_direct")):
        blockers.append("autoridad_historica_directa")
        actual = "rechazada_por_autoridad"
    elif bool(manifest.get("global_authority_claim")) or bool(manifest.get("canon_claim")) or bool(manifest.get("level_c_claim")):
        blockers.append("autoridad_global_no_autorizada")
        actual = "rechazada_por_autoridad"
    elif bool(manifest.get("report_as_decision")):
        blockers.append("reporte_convertido_en_decision")
        actual = "rechazada_por_autoridad"
    elif bool(manifest.get("source_generated_by_lab_fixture")):
        blockers.append("fuente_generada_por_fixture_laboratorio")
        actual = "rechazada_por_alcance"
    elif not artifact_type:
        blockers.append("tipo_artefacto_ausente")
        actual = "rechazada_por_alcance"
    elif not comparable_unit:
        blockers.append("unidad_comparable_ausente")
        actual = "rechazada_por_alcance"
    elif not bool(manifest.get("witness_present")):
        blockers.append("testigo_ausente")
        actual = "rechazada_por_alcance"
    elif not bool(manifest.get("traceability_present")):
        blockers.append("trazabilidad_ausente")
        actual = "rechazada_por_alcance"
    elif not as_list(manifest.get("restrictions")):
        blockers.append("restricciones_ausentes")
        actual = "rechazada_por_alcance"
    elif not real_external_source or not bool(manifest.get("source_identifiable")):
        blockers.append("fuente_real_pendiente")
        actual = "pendiente_fuente_real"
    else:
        actual = "admisible_preliminar"

    if actual == "admisible_preliminar" and control_manifest:
        warnings.append("admisible_solo_como_control_de_compuerta")
    if actual == "admisible_preliminar" and not str(manifest.get("source_uri", "")).strip():
        warnings.append("fuente_sin_uri_explicito")
    if bool(manifest.get("transformacion_permitida")):
        warnings.append("transformacion_solicitada_ignorada")

    expected = str(manifest.get("expected", "")).strip()
    if actual not in VALID_OUTCOMES:
        actual = "rechazada_por_alcance"

    return ExternalEvidenceManifestResult(
        manifest_id=str(manifest.get("manifest_id", "")),
        artifact_type=artifact_type,
        source_uri=source_uri,
        expected=expected,
        actual=actual,
        passed=actual == expected,
        source_family=source_family,
        real_external_source=real_external_source,
        control_manifest=control_manifest,
        authority=authority,
        comparable_unit=comparable_unit,
        blockers=tuple(sorted(blockers)),
        warnings=tuple(sorted(warnings)),
    )


def summarize(results: list[ExternalEvidenceManifestResult], suite: dict[str, Any]) -> dict[str, Any]:
    failures = [result for result in results if not result.passed]
    by_outcome: dict[str, int] = {}
    for result in results:
        by_outcome[result.actual] = by_outcome.get(result.actual, 0) + 1
    admissible_real = sum(
        1
        for result in results
        if result.actual == "admisible_preliminar" and result.real_external_source and not result.control_manifest
    )
    return {
        "manifests": len(results),
        "passed": len(results) - len(failures),
        "failed": len(failures),
        "findings": len(failures),
        "admissible_preliminary": by_outcome.get("admisible_preliminar", 0),
        "pending_real_source": by_outcome.get("pendiente_fuente_real", 0),
        "rejected_scope": by_outcome.get("rechazada_por_alcance", 0),
        "rejected_authority": by_outcome.get("rechazada_por_autoridad", 0),
        "rejected_domain": by_outcome.get("rechazada_por_dominio", 0),
        "admissible_real_non_control": admissible_real,
        "real_evidence_supplied": bool(suite.get("real_evidence_supplied")),
        "by_outcome": by_outcome,
    }


def external_evidence_ready(summary: dict[str, Any]) -> bool:
    return (
        summary["failed"] == 0
        and summary["real_evidence_supplied"]
        and summary["admissible_real_non_control"] > 0
        and summary["pending_real_source"] == 0
        and summary["rejected_scope"] == 0
        and summary["rejected_authority"] == 0
        and summary["rejected_domain"] == 0
    )


def build_report(root: Path | None = None, case_file: Path | None = None) -> dict[str, Any]:
    del root
    suite_path = case_file or DEFAULT_CASE_FILE
    suite = load_suite(suite_path)
    results = [evaluate_manifest(item) for item in suite.get("manifests", [])]
    summary = summarize(results, suite)
    failures = [result for result in results if not result.passed]
    ready = external_evidence_ready(summary)
    recommendation = "mantener_no_autorizado_preparar_fuente_externa_real"
    if failures:
        recommendation = "revisar_compuerta_evidencia_externa"
    elif ready:
        recommendation = "solicitar_decision_global_posterior"

    return {
        "report_id": "AO-EXT-EVID-GATE-001-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"),
        "expediente": EXPEDIENTE,
        "algoritmo": ALGORITHM_ID,
        "suite_id": suite.get("suite_id", "AO-EXT-EVID-GATE-MANIFESTS-001"),
        "resultado": "ok" if not failures else "bloqueado",
        "recomendacion": recommendation,
        "external_evidence_ready": ready,
        "external_evidence_executed": False,
        "transformacion_permitida": False,
        "global_closure_authorized": False,
        "global_export_authorized": False,
        "global_equivalence_authorized": False,
        "global_confluence_authorized": False,
        "report_layer_promoted": False,
        "r4_gamma_global_export_authorized": False,
        "source_evidence": suite.get("source_evidence", []),
        "scope_guard": {
            "busca_descarga_evidencia": False,
            "ejecuta_evidencia_real": False,
            "usa_personas_reales": False,
            "usa_dominio_clinico": False,
            "usa_dominio_regulado": False,
            "modifica_doc04": False,
            "modifica_canon": False,
            "modifica_nivel_c": False,
            "crea_nivel_c": False,
            "reabre_p_pi_0": False,
            "reabre_p_pi_1": False,
            "promueve_report_layer": False,
            "exporta_r4_gamma": False,
            "autoriza_transformacion": False,
        },
        "summary": summary,
        "manifest_results": [asdict(result) for result in results],
        "findings": [asdict(result) for result in failures],
    }


def render_md(report: dict[str, Any]) -> str:
    lines = [
        "# AO_EXT_EVID_GATE_001_REPORT",
        "",
        f"report_id: {report['report_id']}",
        f"expediente: {EXPEDIENTE}",
        f"algoritmo: {ALGORITHM_ID}",
        f"suite_id: {report['suite_id']}",
        f"resultado: {report['resultado']}",
        f"recomendacion: {report['recomendacion']}",
        f"external_evidence_ready: {str(report['external_evidence_ready']).lower()}",
        "external_evidence_executed: false",
        "transformacion_permitida: false",
        "global_closure_authorized: false",
        "global_export_authorized: false",
        "global_equivalence_authorized: false",
        "global_confluence_authorized: false",
        "report_layer_promoted: false",
        "r4_gamma_global_export_authorized: false",
        "",
        "## Resumen",
        "",
        f"- manifests: {report['summary']['manifests']}",
        f"- passed: {report['summary']['passed']}",
        f"- failed: {report['summary']['failed']}",
        f"- admissible_preliminary: {report['summary']['admissible_preliminary']}",
        f"- pending_real_source: {report['summary']['pending_real_source']}",
        f"- rejected_scope: {report['summary']['rejected_scope']}",
        f"- rejected_authority: {report['summary']['rejected_authority']}",
        f"- rejected_domain: {report['summary']['rejected_domain']}",
        f"- real_evidence_supplied: {str(report['summary']['real_evidence_supplied']).lower()}",
        "",
        "## Manifiestos",
        "",
    ]
    for result in report["manifest_results"]:
        status = "PASS" if result["passed"] else "FAIL"
        lines.append(
            f"- {status} `{result['manifest_id']}` [{result['artifact_type']} / {result['source_family']}]: {result['actual']}"
        )
        if result.get("source_uri"):
            lines.append(f"  - source_uri: {result['source_uri']}")
        if result["blockers"]:
            lines.append(f"  - blockers: {', '.join(result['blockers'])}")
        if result["warnings"]:
            lines.append(f"  - warnings: {', '.join(result['warnings'])}")
    lines.extend(["", "## Guardas", ""])
    for key, value in report["scope_guard"].items():
        lines.append(f"- {key}: {str(value).lower()}")
    lines.extend(["", "## Dictamen", ""])
    if report["findings"]:
        lines.append("- Hay fallos de expectativa; no usar esta compuerta para pre-ejecucion.")
    elif report["external_evidence_ready"]:
        lines.append("- Hay manifiesto externo real admisible de forma preliminar; requiere decision posterior antes de uso global.")
    else:
        lines.append("- Ruta preparada sin ejecucion empirica.")
        lines.append("- La ausencia de evidencia externa real conserva `mantener_no_autorizado`.")
    return "\n".join(lines) + "\n"


def assert_inside(root: Path, path: Path) -> None:
    root_resolved = root.resolve()
    path_resolved = path.resolve()
    if path_resolved != root_resolved and root_resolved not in path_resolved.parents:
        raise SystemExit(f"Ruta fuera del repositorio: {path}")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Compuerta AO de evidencia externa independiente no mutante.")
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
