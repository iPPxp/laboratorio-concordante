from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from typing import Any, Literal, Mapping

from pydantic import StrictBool, StrictStr

from .models import (
    CONTRACT_VERSION,
    EXTRACTOR_ID,
    ContractValidationResult,
    FrozenModel,
    NormalizationResult,
    Sha256,
    canonical_json_bytes,
    validate_extraction,
)
from .normalizer import SemanticNormalizer


MIGRATION_CONTRACT_VERSION = "MOC-EXTRACTOR-001-H3-MIGRATION-1.0.0"
MIN_SOURCE_CASES = 1
MAX_SOURCE_CASES = 12
_MIGRATION_CONTRACT = {
    "source_schema_version": "1.0.0",
    "source_extractor_id": "MOC-EXTRACTOR-001-C",
    "target_schema_version": CONTRACT_VERSION,
    "target_extractor_id": EXTRACTOR_ID,
    "normalization_performed": False,
    "legacy_normalized_values_status": "llm_proposed",
    "source_case_count": {"minimum": MIN_SOURCE_CASES, "maximum": MAX_SOURCE_CASES},
    "source_payload_serialization": "RFC8259 JSON; UTF-8; keys sorted; separators comma/colon; ensure_ascii=false",
}
MIGRATION_CONTRACT_SHA256 = hashlib.sha256(
    canonical_json_bytes(_MIGRATION_CONTRACT)
).hexdigest()


class MigrationError(ValueError):
    def __init__(self, code: str) -> None:
        self.code = code
        super().__init__(code)


class MigrationResult(FrozenModel):
    source_schema_version: Literal["1.0.0"]
    target_schema_version: Literal[CONTRACT_VERSION]
    source_bytes_sha256: Sha256
    source_payload_sha256: Sha256
    source_bytes_kind: StrictStr
    migration_contract_version: Literal[MIGRATION_CONTRACT_VERSION]
    migration_contract_sha256: Sha256
    normalization_performed: Literal[False] = False
    legacy_normalized_values_status: Literal["llm_proposed"] = "llm_proposed"
    source_payload_unmodified: Literal[True] = True
    maximal_spans_fabricated: Literal[False] = False
    legacy_normalizations_authoritative: Literal[False] = False
    renormalization_requested: StrictBool = False
    migrated_payload_canonical_json: StrictStr
    validation: ContractValidationResult
    normalization_results: tuple[NormalizationResult, ...] = ()


def _sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise MigrationError("MIGRATION_SOURCE_DUPLICATE_KEY")
        result[key] = value
    return result


def _parse_source_bytes(raw: bytes) -> Mapping[str, Any]:
    try:
        parsed = json.loads(raw.decode("utf-8"), object_pairs_hook=_reject_duplicate_keys)
    except MigrationError:
        raise
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise MigrationError("MIGRATION_SOURCE_BYTES_INVALID") from exc
    if not isinstance(parsed, Mapping):
        raise MigrationError("MIGRATION_SOURCE_ROOT_INVALID")
    return parsed


def _require_mapping(value: Any, code: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise MigrationError(code)
    return value


def _require_sequence(value: Any, code: str) -> list[Any] | tuple[Any, ...]:
    if not isinstance(value, (list, tuple)):
        raise MigrationError(code)
    return value


def _require_exact_json_array(value: Any, code: str) -> list[Any]:
    if type(value) is not list:
        raise MigrationError(code)
    return value


def _validate_v1_payload(payload: Mapping[str, Any]) -> None:
    cases = _require_exact_json_array(payload.get("cases"), "MIGRATION_CASES_INVALID")
    allowed_top = {"schema_version", "extractor_id", "cases"}
    if set(payload) - allowed_top:
        raise MigrationError("MIGRATION_SOURCE_EXTRA_FIELD")
    if payload.get("schema_version") != "1.0.0":
        raise MigrationError("SOURCE_SCHEMA_NOT_1_0_0")
    if payload.get("extractor_id") != "MOC-EXTRACTOR-001-C":
        raise MigrationError("SOURCE_EXTRACTOR_NOT_001_C")
    if not (MIN_SOURCE_CASES <= len(cases) <= MAX_SOURCE_CASES):
        raise MigrationError("MIGRATION_SOURCE_CASE_COUNT_INVALID")
    for case in cases:
        case_map = _require_mapping(case, "MIGRATION_CASE_INVALID")
        allowed_case = {
            "case_id",
            "claims",
            "constraint_candidates",
            "unknowns",
            "frictions",
        }
        if set(case_map) - allowed_case:
            raise MigrationError("MIGRATION_CASE_EXTRA_FIELD")
        if not isinstance(case_map.get("case_id"), str):
            raise MigrationError("MIGRATION_CASE_ID_INVALID")
        for collection_name in ("claims", "constraint_candidates", "unknowns"):
            records = _require_sequence(
                case_map.get(collection_name, []),
                "MIGRATION_RECORD_COLLECTION_INVALID",
            )
            for record in records:
                record_map = _require_mapping(record, "MIGRATION_RECORD_INVALID")
                if "evidence_span" not in record_map:
                    raise MigrationError("MIGRATION_EVIDENCE_SPAN_MISSING")
                span = _require_mapping(
                    record_map["evidence_span"],
                    "MIGRATION_EVIDENCE_SPAN_INVALID",
                )
                if not all(key in span for key in ("text", "start", "end")):
                    raise MigrationError("MIGRATION_EVIDENCE_SPAN_INCOMPLETE")
                if not isinstance(record_map.get("claim_id"), str):
                    raise MigrationError("MIGRATION_RECORD_ID_INVALID")
                if collection_name != "unknowns":
                    required = {
                        "field",
                        "surface_value",
                        "provenance",
                        "normalization_rule",
                    }
                    if not required.issubset(record_map):
                        raise MigrationError("MIGRATION_RECORD_REQUIRED_FIELD_MISSING")
        _require_sequence(case_map.get("frictions", []), "MIGRATION_FRICTIONS_INVALID")


def _narratives_from_projected_input(projected: Mapping[str, Any]) -> dict[str, str]:
    cases = _require_exact_json_array(
        projected.get("cases"), "MIGRATION_PROJECTED_CASES_INVALID"
    )
    narratives: dict[str, str] = {}
    for case in cases:
        case_map = _require_mapping(case, "MIGRATION_PROJECTED_CASE_INVALID")
        case_id = case_map.get("case_id")
        raw_narrative = case_map.get("raw_narrative")
        if not isinstance(case_id, str) or not isinstance(raw_narrative, str):
            raise MigrationError("MIGRATION_PROJECTED_CASE_FIELD_INVALID")
        if case_id in narratives:
            raise MigrationError("MIGRATION_PROJECTED_CASE_DUPLICATE")
        narratives[case_id] = raw_narrative
    return narratives


def _migrate_record(record: Mapping[str, Any], *, unknown: bool = False) -> dict[str, Any]:
    migrated = {
        key: copy.deepcopy(value)
        for key, value in record.items()
        if key != "normalized_value"
    }
    try:
        span = migrated.pop("evidence_span")
    except KeyError as exc:
        raise MigrationError("MIGRATION_EVIDENCE_SPAN_MISSING") from exc
    migrated["minimal_evidence_span"] = span
    migrated["maximal_semantic_span"] = None
    if unknown:
        migrated["surface_value"] = span["text"]
    elif "normalized_value" in record:
        migrated["llm_proposed_normalized_values"] = [record["normalized_value"]]
    return migrated


def _migrate_friction(friction: Any) -> dict[str, Any]:
    friction_map = _require_mapping(friction, "MIGRATION_FRICTION_INVALID")
    migrated = copy.deepcopy(dict(friction_map))
    migrated["verification_status"] = "FRICTION_CANDIDATE"
    return migrated


def migrate_v1_payload(
    payload: Mapping[str, Any],
    projected_input: Mapping[str, Any],
    *,
    normalization_catalog_version: str,
    normalization_catalog_sha256: str,
    friction_catalog_version: str,
    friction_catalog_sha256: str,
    source_bytes: bytes | None = None,
    declared_source_payload_sha256: str | None = None,
    renormalize: bool = False,
    normalizer: SemanticNormalizer | None = None,
) -> MigrationResult:
    del normalizer
    if not isinstance(payload, Mapping):
        raise MigrationError("MIGRATION_SOURCE_ROOT_INVALID")
    if not isinstance(projected_input, Mapping):
        raise MigrationError("MIGRATION_PROJECTED_ROOT_INVALID")
    if renormalize:
        raise MigrationError("MIGRATION_RENORMALIZATION_FORBIDDEN_H2")
    _validate_v1_payload(payload)
    narratives = _narratives_from_projected_input(projected_input)
    original = copy.deepcopy(payload)

    source_payload_bytes = canonical_json_bytes(payload)
    source_payload_sha256 = _sha256(source_payload_bytes)
    if (
        declared_source_payload_sha256 is not None
        and declared_source_payload_sha256 != source_payload_sha256
    ):
        raise MigrationError("MIGRATION_DECLARED_PROVENANCE_MISMATCH")
    if source_bytes is not None:
        parsed_source = _parse_source_bytes(source_bytes)
        if canonical_json_bytes(parsed_source) != source_payload_bytes:
            raise MigrationError("MIGRATION_SOURCE_BYTES_PAYLOAD_MISMATCH")
        effective_source_bytes = bytes(source_bytes)
        source_bytes_kind = "supplied_json_canonically_equivalent"
    else:
        effective_source_bytes = source_payload_bytes
        source_bytes_kind = "canonical_payload_bytes"

    migrated_cases: list[dict[str, Any]] = []
    for case_value in payload["cases"]:
        case = _require_mapping(case_value, "MIGRATION_CASE_INVALID")
        case_id = str(case["case_id"])
        if case_id not in narratives:
            raise MigrationError("MIGRATION_NARRATIVE_MISSING")
        claims = [_migrate_record(record) for record in case.get("claims", [])]
        constraints = [
            _migrate_record(record)
            for record in case.get("constraint_candidates", [])
        ]
        unknowns = [
            _migrate_record(record, unknown=True)
            for record in case.get("unknowns", [])
        ]
        migrated_cases.append(
            {
                "case_id": case_id,
                "raw_narrative": narratives[case_id],
                "claims": claims,
                "constraint_candidates": constraints,
                "unknowns": unknowns,
                "friction_candidates": [
                    _migrate_friction(friction)
                    for friction in case.get("frictions", [])
                ],
            }
        )

    migrated_payload = {
        "schema_version": CONTRACT_VERSION,
        "extractor_id": EXTRACTOR_ID,
        "normalization_catalog_version": normalization_catalog_version,
        "normalization_catalog_sha256": normalization_catalog_sha256,
        "friction_catalog_version": friction_catalog_version,
        "friction_catalog_sha256": friction_catalog_sha256,
        "cases": migrated_cases,
    }
    validation = validate_extraction(migrated_payload)
    if payload != original:
        raise RuntimeError("SOURCE_PAYLOAD_MUTATED")
    return MigrationResult(
        source_schema_version="1.0.0",
        target_schema_version=CONTRACT_VERSION,
        source_bytes_sha256=_sha256(effective_source_bytes),
        source_payload_sha256=source_payload_sha256,
        source_bytes_kind=source_bytes_kind,
        migration_contract_version=MIGRATION_CONTRACT_VERSION,
        migration_contract_sha256=MIGRATION_CONTRACT_SHA256,
        normalization_performed=False,
        legacy_normalized_values_status="llm_proposed",
        renormalization_requested=False,
        migrated_payload_canonical_json=canonical_json_bytes(migrated_payload).decode(
            "utf-8"
        ),
        validation=validation,
        normalization_results=(),
    )


def migrate_v1_file(
    output_path: Path,
    projected_input_path: Path,
    **kwargs: Any,
) -> MigrationResult:
    before = output_path.read_bytes()
    projected_before = projected_input_path.read_bytes()
    payload = _parse_source_bytes(before)
    projected = _parse_source_bytes(projected_before)
    result = migrate_v1_payload(payload, projected, source_bytes=before, **kwargs)
    if output_path.read_bytes() != before or projected_input_path.read_bytes() != projected_before:
        raise RuntimeError("FROZEN_SOURCE_CHANGED_DURING_MIGRATION")
    return result
