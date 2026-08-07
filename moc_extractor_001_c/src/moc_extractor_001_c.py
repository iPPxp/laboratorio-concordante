#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


EXPECTED_BANK_SHA256 = "69e655ccf3ca655d415b2868a072086682ad42a97f7e00c141129967faa64d54"
SCHEMA_VERSION = "1.0.0"
EXTRACTOR_ID = "MOC-EXTRACTOR-001-C"

EXPECTED_INVENTORY = {
    "cases": 12,
    "claims": 35,
    "constraint_candidates": 5,
    "unknowns": 4,
    "frictions": 8,
    "ids_total": 44,
    "ids_unique": 44,
    "normative_rules": 21,
}

PRINCIPAL_FIELDS = {
    "accion_candidata",
    "accion_rechazada",
    "accion_reportada",
    "clima_emocional",
    "condicion_futura",
    "estado_factual",
    "estado_temporal",
    "evaluacion_situacional",
    "horizonte_temporal",
    "intencion_declarada",
    "obligacion_declarada",
    "recurso_mencionado",
    "valor_declarado",
}
CONSTRAINT_FIELDS = {
    "restriccion_externa",
    "restriccion_financiera",
    "restriccion_tecnica",
}
FRICTION_TYPES = {"ambiguity", "contradiction", "tension"}
COLLECTION_KEYS = ("claims", "constraint_candidates", "unknowns", "frictions")
BANK_TO_OUTPUT = {
    "expected_claims": "claims",
    "constraint_candidates": "constraint_candidates",
    "expected_unknowns": "unknowns",
    "expected_frictions": "frictions",
}


class ContractError(RuntimeError):
    pass


@dataclass(frozen=True)
class Issue:
    phase: str
    category: str
    case_id: str
    path: str
    message: str
    expected: Any = None
    actual: Any = None


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ContractError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _reject_non_finite(value: str) -> None:
    raise ContractError(f"non-finite JSON number is forbidden: {value}")


def strict_json_loads(raw: str) -> Any:
    if raw.startswith("\ufeff"):
        raise ContractError("UTF-8 BOM is forbidden")
    try:
        return json.loads(
            raw,
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_non_finite,
        )
    except json.JSONDecodeError as exc:
        raise ContractError(
            f"invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc


def strict_json_load(path: Path) -> Any:
    try:
        raw = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise ContractError(f"file is not strict UTF-8: {path}") from exc
    return strict_json_loads(raw)


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def bank_inventory(bank: Mapping[str, Any]) -> dict[str, int]:
    cases = bank.get("dev_cases", [])
    ids: list[str] = []
    for case in cases:
        for key in ("expected_claims", "constraint_candidates", "expected_unknowns"):
            ids.extend(item.get("claim_id", "") for item in case.get(key, []))
    return {
        "cases": len(cases),
        "claims": sum(len(case.get("expected_claims", [])) for case in cases),
        "constraint_candidates": sum(
            len(case.get("constraint_candidates", [])) for case in cases
        ),
        "unknowns": sum(len(case.get("expected_unknowns", [])) for case in cases),
        "frictions": sum(len(case.get("expected_frictions", [])) for case in cases),
        "ids_total": len(ids),
        "ids_unique": len(set(ids)),
        "normative_rules": len(bank.get("normative_catalog", [])),
    }


def _bank_case_prefix(case_id: str) -> str:
    match = re.fullmatch(r"EXP-A-DEV-(\d{3})", case_id)
    if not match:
        raise ContractError(f"invalid bank case_id: {case_id!r}")
    return f"DEV{match.group(1)}"


def _validate_bank_internals(bank: Mapping[str, Any]) -> None:
    if set(bank) != {"metadata", "dev_cases", "normative_catalog"}:
        raise ContractError("bank top-level keys do not match v3.1 contract")
    metadata = bank.get("metadata")
    if not isinstance(metadata, dict) or metadata.get("version") != "3.1":
        raise ContractError("bank metadata.version is not 3.1")
    inventory = bank_inventory(bank)
    if inventory != EXPECTED_INVENTORY:
        raise ContractError(
            f"bank inventory mismatch: expected {EXPECTED_INVENTORY}, got {inventory}"
        )

    rules = bank["normative_catalog"]
    rule_ids = [rule.get("rule_id") for rule in rules]
    if len(rule_ids) != len(set(rule_ids)) or any(not item for item in rule_ids):
        raise ContractError("normative rule IDs are missing or duplicated")
    rule_fields = {rule["rule_id"]: rule.get("output_field") for rule in rules}

    all_case_ids: set[str] = set()
    for case in bank["dev_cases"]:
        case_id = case.get("case_id")
        if not isinstance(case_id, str) or case_id in all_case_ids:
            raise ContractError(f"missing or duplicated case_id: {case_id!r}")
        all_case_ids.add(case_id)
        prefix = _bank_case_prefix(case_id)
        narrative = case.get("raw_narrative")
        if not isinstance(narrative, str):
            raise ContractError(f"{case_id}: raw_narrative must be a string")

        local_ids: set[str] = set()
        for bank_key, marker in (
            ("expected_claims", "C"),
            ("constraint_candidates", "R"),
            ("expected_unknowns", "U"),
        ):
            records = case.get(bank_key)
            if not isinstance(records, list):
                raise ContractError(f"{case_id}: {bank_key} must be an array")
            for index, record in enumerate(records, start=1):
                claim_id = record.get("claim_id")
                expected_id = f"{prefix}-{marker}{index:02d}"
                if claim_id != expected_id or claim_id in local_ids:
                    raise ContractError(
                        f"{case_id}: expected deterministic ID {expected_id}, got {claim_id}"
                    )
                local_ids.add(claim_id)
                span = record.get("evidence_span")
                if not isinstance(span, dict):
                    raise ContractError(f"{case_id}/{claim_id}: missing evidence_span")
                start, end, text = span.get("start"), span.get("end"), span.get("text")
                if (
                    type(start) is not int
                    or type(end) is not int
                    or not 0 <= start < end <= len(narrative)
                    or narrative[start:end] != text
                ):
                    raise ContractError(f"{case_id}/{claim_id}: invalid authoritative span")
                if bank_key != "expected_unknowns":
                    if record.get("surface_value") != text:
                        raise ContractError(
                            f"{case_id}/{claim_id}: surface_value differs from span text"
                        )
                    rule_id = record.get("normalization_rule")
                    if rule_id not in rule_fields or rule_fields[rule_id] != record.get("field"):
                        raise ContractError(
                            f"{case_id}/{claim_id}: invalid normalization rule linkage"
                        )

        for friction in case.get("expected_frictions", []):
            refs = friction.get("claim_refs")
            if not isinstance(refs, list) or len(refs) < 1:
                raise ContractError(f"{case_id}: invalid authoritative friction refs")
            missing = set(refs) - local_ids
            if missing:
                raise ContractError(
                    f"{case_id}: authoritative friction has broken refs {sorted(missing)}"
                )


def load_bank(path: Path, expected_sha256: str = EXPECTED_BANK_SHA256) -> dict[str, Any]:
    if not path.is_file():
        raise ContractError(f"bank not found: {path}")
    actual_sha256 = sha256_file(path)
    if actual_sha256.lower() != expected_sha256.lower():
        raise ContractError(
            f"bank SHA-256 mismatch: expected {expected_sha256}, got {actual_sha256}"
        )
    bank = strict_json_load(path)
    if not isinstance(bank, dict):
        raise ContractError("bank root must be an object")
    _validate_bank_internals(bank)
    return bank


def project_model_input(
    bank: Mapping[str, Any], selected_case_ids: Sequence[str] | None = None
) -> dict[str, Any]:
    selected = set(selected_case_ids) if selected_case_ids else None
    cases = [
        {"case_id": case["case_id"], "raw_narrative": case["raw_narrative"]}
        for case in bank["dev_cases"]
        if selected is None or case["case_id"] in selected
    ]
    if selected is not None and {case["case_id"] for case in cases} != selected:
        missing = sorted(selected - {case["case_id"] for case in cases})
        raise ContractError(f"selected case IDs are absent from bank: {missing}")
    friction_rules: dict[str, set[str]] = {}
    for case in bank["dev_cases"]:
        for friction in case["expected_frictions"]:
            friction_rules.setdefault(friction["annotation_rule"], set()).add(friction["type"])
    return {
        "schema_version": SCHEMA_VERSION,
        "extractor_id": EXTRACTOR_ID,
        "normative_catalog": bank["normative_catalog"],
        "friction_rule_catalog": [
            {"rule_id": rule_id, "allowed_types": sorted(types)}
            for rule_id, types in sorted(friction_rules.items())
        ],
        "cases": cases,
    }


def gold_batch(
    bank: Mapping[str, Any], selected_case_ids: Sequence[str] | None = None
) -> dict[str, Any]:
    selected = set(selected_case_ids) if selected_case_ids else None
    cases = []
    for case in bank["dev_cases"]:
        if selected is not None and case["case_id"] not in selected:
            continue
        cases.append(
            {
                "case_id": case["case_id"],
                "claims": case["expected_claims"],
                "constraint_candidates": case["constraint_candidates"],
                "unknowns": case["expected_unknowns"],
                "frictions": case["expected_frictions"],
            }
        )
    return {
        "schema_version": SCHEMA_VERSION,
        "extractor_id": EXTRACTOR_ID,
        "cases": cases,
    }


def canonicalize_candidate_spans(
    candidate: Any, bank: Mapping[str, Any]
) -> tuple[Any, list[dict[str, Any]]]:
    canonical = copy.deepcopy(candidate)
    notes: list[dict[str, Any]] = []
    if not isinstance(canonical, dict) or not isinstance(canonical.get("cases"), list):
        return canonical, notes
    bank_cases = {case["case_id"]: case for case in bank["dev_cases"]}
    for case_index, case in enumerate(canonical["cases"]):
        if not isinstance(case, dict) or case.get("case_id") not in bank_cases:
            continue
        case_id = case["case_id"]
        narrative = bank_cases[case_id]["raw_narrative"]
        for collection in ("claims", "constraint_candidates", "unknowns"):
            records = case.get(collection)
            if not isinstance(records, list):
                continue
            for record_index, record in enumerate(records):
                if not isinstance(record, dict):
                    continue
                span = record.get("evidence_span")
                if not isinstance(span, dict) or not isinstance(span.get("text"), str):
                    continue
                text = span["text"]
                path = f"$.cases[{case_index}].{collection}[{record_index}].evidence_span"
                start, end = span.get("start"), span.get("end")
                if (
                    type(start) is int
                    and type(end) is int
                    and 0 <= start < end <= len(narrative)
                    and narrative[start:end] == text
                ):
                    continue
                if "surface_value" in record and record.get("surface_value") != text:
                    notes.append(
                        {
                            "case_id": case_id,
                            "path": path,
                            "status": "unresolved",
                            "reason": "surface_value differs from evidence_span.text",
                        }
                    )
                    continue
                occurrences: list[int] = []
                search_from = 0
                while text:
                    found = narrative.find(text, search_from)
                    if found < 0:
                        break
                    occurrences.append(found)
                    search_from = found + 1
                if len(occurrences) != 1:
                    notes.append(
                        {
                            "case_id": case_id,
                            "path": path,
                            "status": "unresolved",
                            "reason": "evidence text must have exactly one narrative occurrence",
                            "occurrences": occurrences,
                        }
                    )
                    continue
                corrected_start = occurrences[0]
                corrected_end = corrected_start + len(text)
                span["start"] = corrected_start
                span["end"] = corrected_end
                notes.append(
                    {
                        "case_id": case_id,
                        "path": path,
                        "status": "canonicalized",
                        "original": {"start": start, "end": end},
                        "canonical": {"start": corrected_start, "end": corrected_end},
                    }
                )
    return canonical, notes


def _add_issue(
    issues: list[Issue],
    phase: str,
    category: str,
    case_id: str,
    path: str,
    message: str,
    expected: Any = None,
    actual: Any = None,
) -> None:
    issues.append(Issue(phase, category, case_id, path, message, expected, actual))


def _exact_keys(
    value: Any,
    allowed: set[str],
    issues: list[Issue],
    case_id: str,
    path: str,
) -> bool:
    if not isinstance(value, dict):
        _add_issue(
            issues,
            "structural",
            "schema_error",
            case_id,
            path,
            "expected JSON object",
            "object",
            type(value).__name__,
        )
        return False
    actual = set(value)
    missing = sorted(allowed - actual)
    extra = sorted(actual - allowed)
    if missing:
        _add_issue(
            issues,
            "structural",
            "schema_error",
            case_id,
            path,
            "missing required keys",
            sorted(allowed),
            sorted(actual),
        )
    if extra:
        _add_issue(
            issues,
            "structural",
            "schema_error",
            case_id,
            path,
            "additional keys are forbidden",
            sorted(allowed),
            sorted(actual),
        )
    return not missing and not extra


def _validate_string(
    value: Any,
    issues: list[Issue],
    case_id: str,
    path: str,
    allowed: set[str] | None = None,
) -> bool:
    if not isinstance(value, str) or not value:
        _add_issue(
            issues,
            "structural",
            "schema_error",
            case_id,
            path,
            "expected non-empty string",
            actual=value,
        )
        return False
    if allowed is not None and value not in allowed:
        _add_issue(
            issues,
            "structural",
            "schema_error",
            case_id,
            path,
            "value is outside the allowed enumeration",
            sorted(allowed),
            value,
        )
        return False
    return True


def _validate_span(
    record: Mapping[str, Any],
    narrative: str,
    issues: list[Issue],
    case_id: str,
    path: str,
    require_surface: bool,
) -> None:
    span = record.get("evidence_span")
    span_path = f"{path}.evidence_span"
    if not _exact_keys(span, {"text", "start", "end"}, issues, case_id, span_path):
        return
    text = span.get("text")
    start = span.get("start")
    end = span.get("end")
    valid_types = _validate_string(text, issues, case_id, f"{span_path}.text")
    if type(start) is not int or type(end) is not int:
        _add_issue(
            issues,
            "structural",
            "invalid_span",
            case_id,
            span_path,
            "span bounds must be integers, not booleans",
            actual={"start": start, "end": end},
        )
        return
    if not 0 <= start < end <= len(narrative):
        _add_issue(
            issues,
            "structural",
            "invalid_span",
            case_id,
            span_path,
            "span is outside narrative bounds or empty",
            f"0 <= start < end <= {len(narrative)}",
            {"start": start, "end": end},
        )
        return
    actual_text = narrative[start:end]
    if valid_types and actual_text != text:
        _add_issue(
            issues,
            "structural",
            "invalid_span",
            case_id,
            span_path,
            "Unicode [start,end) slice does not equal evidence_span.text",
            actual_text,
            text,
        )
    if require_surface and record.get("surface_value") != text:
        _add_issue(
            issues,
            "structural",
            "invalid_span",
            case_id,
            f"{path}.surface_value",
            "surface_value must equal evidence_span.text",
            text,
            record.get("surface_value"),
        )


def _case_prefix(case_id: str) -> str | None:
    match = re.fullmatch(r"EXP-A-DEV-(\d{3})", case_id)
    return f"DEV{match.group(1)}" if match else None


def _walk_json(value: Any, path: str = "$") -> Iterable[tuple[str, str | None, Any]]:
    if isinstance(value, dict):
        for key, item in value.items():
            item_path = f"{path}.{key}"
            yield item_path, key, item
            yield from _walk_json(item, item_path)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            item_path = f"{path}[{index}]"
            yield item_path, None, item
            yield from _walk_json(item, item_path)


def _prohibited_counterexample_tokens(bank: Mapping[str, Any]) -> set[str]:
    tokens: set[str] = set()
    for rule in bank["normative_catalog"]:
        for counterexample in rule.get("counterexamples", []):
            if "->" not in counterexample:
                continue
            right = counterexample.split("->", 1)[1].strip()
            token = re.sub(r"\s*\(PROHIBIDO\)\s*$", "", right)
            if token:
                tokens.add(token)
    return tokens


def validate_structure(
    candidate: Any,
    bank: Mapping[str, Any],
    selected_case_ids: Sequence[str] | None = None,
) -> list[Issue]:
    issues: list[Issue] = []
    if not _exact_keys(
        candidate,
        {"schema_version", "extractor_id", "cases"},
        issues,
        "BATCH",
        "$",
    ):
        if not isinstance(candidate, dict):
            return issues
    if candidate.get("schema_version") != SCHEMA_VERSION:
        _add_issue(
            issues,
            "structural",
            "schema_error",
            "BATCH",
            "$.schema_version",
            "unsupported schema version",
            SCHEMA_VERSION,
            candidate.get("schema_version"),
        )
    if candidate.get("extractor_id") != EXTRACTOR_ID:
        _add_issue(
            issues,
            "structural",
            "schema_error",
            "BATCH",
            "$.extractor_id",
            "unexpected extractor identifier",
            EXTRACTOR_ID,
            candidate.get("extractor_id"),
        )

    bank_cases = {case["case_id"]: case for case in bank["dev_cases"]}
    expected_ids = (
        list(selected_case_ids)
        if selected_case_ids is not None
        else [case["case_id"] for case in bank["dev_cases"]]
    )
    cases = candidate.get("cases")
    if not isinstance(cases, list) or not cases:
        _add_issue(
            issues,
            "structural",
            "schema_error",
            "BATCH",
            "$.cases",
            "cases must be a non-empty array",
            actual=cases,
        )
        return issues

    actual_ids = [case.get("case_id") if isinstance(case, dict) else None for case in cases]
    if actual_ids != expected_ids:
        _add_issue(
            issues,
            "structural",
            "case_set_error",
            "BATCH",
            "$.cases",
            "case IDs and order must exactly match the requested input",
            expected_ids,
            actual_ids,
        )
    if len(actual_ids) != len(set(actual_ids)):
        _add_issue(
            issues,
            "structural",
            "duplicate_id",
            "BATCH",
            "$.cases",
            "case IDs must be unique",
            actual=actual_ids,
        )

    rule_fields = {
        rule["rule_id"]: rule["output_field"] for rule in bank["normative_catalog"]
    }
    friction_rules = {
        friction["annotation_rule"]
        for case in bank["dev_cases"]
        for friction in case["expected_frictions"]
    }
    prohibited_tokens = _prohibited_counterexample_tokens(bank)

    for case_index, case_output in enumerate(cases):
        path = f"$.cases[{case_index}]"
        case_id = (
            case_output.get("case_id", f"CASE-{case_index}")
            if isinstance(case_output, dict)
            else f"CASE-{case_index}"
        )
        if not _exact_keys(
            case_output,
            {"case_id", "claims", "constraint_candidates", "unknowns", "frictions"},
            issues,
            str(case_id),
            path,
        ):
            if not isinstance(case_output, dict):
                continue
        if case_id not in bank_cases:
            _add_issue(
                issues,
                "structural",
                "case_set_error",
                str(case_id),
                f"{path}.case_id",
                "case_id is absent from authoritative bank",
                actual=case_id,
            )
            continue
        prefix = _case_prefix(case_id)
        narrative = bank_cases[case_id]["raw_narrative"]
        local_ids: dict[str, str] = {}

        for collection in COLLECTION_KEYS:
            if not isinstance(case_output.get(collection), list):
                _add_issue(
                    issues,
                    "structural",
                    "schema_error",
                    case_id,
                    f"{path}.{collection}",
                    "collection must be an array",
                    actual=case_output.get(collection),
                )

        collection_specs = (
            (
                "claims",
                "C",
                {"claim_id", "field", "surface_value", "normalized_value", "provenance", "normalization_rule", "evidence_span"},
                PRINCIPAL_FIELDS,
            ),
            (
                "constraint_candidates",
                "R",
                {"claim_id", "field", "surface_value", "normalized_value", "provenance", "normalization_rule", "operational_effect", "requires_verification", "evidence_span"},
                CONSTRAINT_FIELDS,
            ),
            (
                "unknowns",
                "U",
                {"claim_id", "field", "type", "evidence_span"},
                None,
            ),
        )

        for collection, marker, allowed_keys, allowed_fields in collection_specs:
            records = case_output.get(collection)
            if not isinstance(records, list):
                continue
            for index, record in enumerate(records, start=1):
                record_path = f"{path}.{collection}[{index - 1}]"
                if not _exact_keys(record, allowed_keys, issues, case_id, record_path):
                    if not isinstance(record, dict):
                        continue
                claim_id = record.get("claim_id")
                if not _validate_string(claim_id, issues, case_id, f"{record_path}.claim_id"):
                    claim_id = f"INVALID-{index}"
                elif not re.fullmatch(rf"{prefix}-{marker}\d{{2}}", claim_id):
                    _add_issue(
                        issues,
                        "structural",
                        "nondeterministic_id",
                        case_id,
                        f"{record_path}.claim_id",
                        "ID must use the case prefix and collection marker",
                        f"{prefix}-{marker}NN",
                        claim_id,
                    )
                if claim_id in local_ids:
                    _add_issue(
                        issues,
                        "structural",
                        "duplicate_id",
                        case_id,
                        f"{record_path}.claim_id",
                        "claim_id is duplicated within case",
                        actual=claim_id,
                    )
                else:
                    local_ids[claim_id] = record_path

                field = record.get("field")
                _validate_string(
                    field,
                    issues,
                    case_id,
                    f"{record_path}.field",
                    allowed_fields,
                )
                _validate_span(
                    record,
                    narrative,
                    issues,
                    case_id,
                    record_path,
                    require_surface=collection != "unknowns",
                )

                if collection == "unknowns":
                    if record.get("type") != "explicit_unknown":
                        _add_issue(
                            issues,
                            "structural",
                            "schema_error",
                            case_id,
                            f"{record_path}.type",
                            "only explicit_unknown is permitted",
                            "explicit_unknown",
                            record.get("type"),
                        )
                    continue

                _validate_string(
                    record.get("surface_value"),
                    issues,
                    case_id,
                    f"{record_path}.surface_value",
                )
                _validate_string(
                    record.get("normalized_value"),
                    issues,
                    case_id,
                    f"{record_path}.normalized_value",
                )
                rule_id = record.get("normalization_rule")
                if not _validate_string(
                    rule_id, issues, case_id, f"{record_path}.normalization_rule"
                ):
                    rule_id = None
                if rule_id not in rule_fields or rule_fields.get(rule_id) != field:
                    _add_issue(
                        issues,
                        "structural",
                        "rule_resolution_error",
                        case_id,
                        f"{record_path}.normalization_rule",
                        "normalization rule must exist and resolve to record field",
                        field,
                        {"rule": rule_id, "output_field": rule_fields.get(rule_id)},
                    )
                if collection == "claims" and record.get("provenance") != "reported":
                    _add_issue(
                        issues,
                        "structural",
                        "schema_error",
                        case_id,
                        f"{record_path}.provenance",
                        "principal claim provenance must be reported",
                        "reported",
                        record.get("provenance"),
                    )
                if collection == "constraint_candidates":
                    if record.get("provenance") != "reported_constraint":
                        _add_issue(
                            issues,
                            "structural",
                            "schema_error",
                            case_id,
                            f"{record_path}.provenance",
                            "constraint provenance must be reported_constraint",
                            "reported_constraint",
                            record.get("provenance"),
                        )
                    if record.get("operational_effect") != "unknown":
                        _add_issue(
                            issues,
                            "structural",
                            "schema_error",
                            case_id,
                            f"{record_path}.operational_effect",
                            "constraint operational effect must remain unknown",
                            "unknown",
                            record.get("operational_effect"),
                        )
                    if record.get("requires_verification") is not True:
                        _add_issue(
                            issues,
                            "structural",
                            "schema_error",
                            case_id,
                            f"{record_path}.requires_verification",
                            "constraint must require verification",
                            True,
                            record.get("requires_verification"),
                        )

        frictions = case_output.get("frictions")
        if isinstance(frictions, list):
            for index, friction in enumerate(frictions):
                friction_path = f"{path}.frictions[{index}]"
                if not _exact_keys(
                    friction,
                    {"type", "claim_refs", "annotation_rule", "description"},
                    issues,
                    case_id,
                    friction_path,
                ):
                    if not isinstance(friction, dict):
                        continue
                _validate_string(
                    friction.get("type"),
                    issues,
                    case_id,
                    f"{friction_path}.type",
                    FRICTION_TYPES,
                )
                _validate_string(
                    friction.get("description"),
                    issues,
                    case_id,
                    f"{friction_path}.description",
                )
                annotation_rule = friction.get("annotation_rule")
                if not _validate_string(
                    annotation_rule,
                    issues,
                    case_id,
                    f"{friction_path}.annotation_rule",
                ) or annotation_rule not in friction_rules:
                    _add_issue(
                        issues,
                        "structural",
                        "rule_resolution_error",
                        case_id,
                        f"{friction_path}.annotation_rule",
                        "friction rule must exist in the DEV contract",
                        sorted(friction_rules),
                        annotation_rule,
                    )
                refs = friction.get("claim_refs")
                minimum_refs = 1 if friction.get("type") == "ambiguity" else 2
                if not isinstance(refs, list) or len(refs) < minimum_refs or any(
                    not isinstance(ref, str) for ref in refs
                ):
                    _add_issue(
                        issues,
                        "structural",
                        "schema_error",
                        case_id,
                        f"{friction_path}.claim_refs",
                        "claim_refs cardinality does not match friction type",
                        actual=refs,
                    )
                    continue
                if len(refs) != len(set(refs)):
                    _add_issue(
                        issues,
                        "structural",
                        "duplicate_id",
                        case_id,
                        f"{friction_path}.claim_refs",
                        "claim_refs must be unique",
                        actual=refs,
                    )
                missing = sorted(set(refs) - set(local_ids))
                if missing:
                    _add_issue(
                        issues,
                        "structural",
                        "broken_reference",
                        case_id,
                        f"{friction_path}.claim_refs",
                        "friction references unresolved claim IDs",
                        actual=missing,
                    )

        must_not = set(bank_cases[case_id].get("must_not_produce", []))
        for value_path, key, value in _walk_json(case_output, path):
            if key in must_not or (isinstance(value, str) and value in must_not):
                _add_issue(
                    issues,
                    "semantic",
                    "must_not_produce",
                    case_id,
                    value_path,
                    "output contains a token forbidden by the case",
                    sorted(must_not),
                    key if key in must_not else value,
                )
            if isinstance(value, str) and value in prohibited_tokens:
                _add_issue(
                    issues,
                    "semantic",
                    "prohibited_inference",
                    case_id,
                    value_path,
                    "output matches a normative counterexample marked PROHIBIDO",
                    actual=value,
                )

    return issues


def _semantic_anchor(record: Mapping[str, Any]) -> tuple[Any, ...]:
    span = record.get("evidence_span")
    if not isinstance(span, dict):
        span = {}
    return (
        record.get("field"),
        span.get("start"),
        span.get("end"),
        span.get("text"),
    )


def _anchor_map(records: Any) -> dict[tuple[Any, ...], Mapping[str, Any]]:
    if not isinstance(records, list):
        return {}
    return {
        _semantic_anchor(record): record
        for record in records
        if isinstance(record, dict)
    }


def _friction_key(
    record: Mapping[str, Any], id_translation: Mapping[str, str] | None = None
) -> tuple[Any, ...]:
    refs = record.get("claim_refs")
    if isinstance(refs, list):
        translated = [id_translation.get(ref, ref) for ref in refs] if id_translation else refs
        normalized_refs = tuple(sorted(translated))
    else:
        normalized_refs = ()
    return record.get("type"), normalized_refs, record.get("annotation_rule")


def _safe_ratio(numerator: int, denominator: int) -> float | None:
    return round(numerator / denominator, 6) if denominator else None


def compare_semantics(
    candidate: Any,
    bank: Mapping[str, Any],
    selected_case_ids: Sequence[str] | None = None,
) -> tuple[list[Issue], dict[str, Any]]:
    issues: list[Issue] = []
    selected = set(selected_case_ids) if selected_case_ids else None
    candidate_cases = {}
    if isinstance(candidate, dict) and isinstance(candidate.get("cases"), list):
        candidate_cases = {
            case.get("case_id"): case
            for case in candidate["cases"]
            if isinstance(case, dict) and isinstance(case.get("case_id"), str)
        }

    metrics: dict[str, dict[str, int]] = {
        key: {"expected": 0, "predicted": 0, "exact": 0} for key in COLLECTION_KEYS
    }
    case_metrics: dict[str, Any] = {}

    for expected_case in bank["dev_cases"]:
        case_id = expected_case["case_id"]
        if selected is not None and case_id not in selected:
            continue
        candidate_case = candidate_cases.get(case_id, {})
        current = {
            key: {"expected": 0, "predicted": 0, "exact": 0}
            for key in COLLECTION_KEYS
        }
        id_translation: dict[str, str] = {}

        for bank_key, output_key in BANK_TO_OUTPUT.items():
            expected_records = expected_case[bank_key]
            actual_records = candidate_case.get(output_key, [])
            if not isinstance(actual_records, list):
                actual_records = []
            metrics[output_key]["expected"] += len(expected_records)
            metrics[output_key]["predicted"] += len(actual_records)
            current[output_key]["expected"] = len(expected_records)
            current[output_key]["predicted"] = len(actual_records)

            if output_key == "frictions":
                expected_map = {_friction_key(record): record for record in expected_records}
                actual_map = {
                    _friction_key(record, id_translation): record
                    for record in actual_records
                    if isinstance(record, dict)
                }
                for key in sorted(expected_map.keys() - actual_map.keys(), key=str):
                    _add_issue(
                        issues,
                        "semantic",
                        "omission",
                        case_id,
                        f"$.cases[{case_id}].frictions",
                        "expected friction was omitted",
                        expected_map[key],
                    )
                for key in sorted(actual_map.keys() - expected_map.keys(), key=str):
                    _add_issue(
                        issues,
                        "semantic",
                        "spurious_extraction",
                        case_id,
                        f"$.cases[{case_id}].frictions",
                        "unexpected friction was produced",
                        actual=actual_map[key],
                    )
                for key in expected_map.keys() & actual_map.keys():
                    expected_record = expected_map[key]
                    actual_record = actual_map[key]
                    if canonical_json(expected_record) == canonical_json(actual_record):
                        metrics[output_key]["exact"] += 1
                        current[output_key]["exact"] += 1
                    elif expected_record.get("description") != actual_record.get("description"):
                        _add_issue(
                            issues,
                            "semantic",
                            "attribute_mismatch",
                            case_id,
                            f"$.cases[{case_id}].frictions.description",
                            "friction description differs from DEV annotation",
                            expected_record.get("description"),
                            actual_record.get("description"),
                        )
                continue

            expected_map = _anchor_map(expected_records)
            actual_map = _anchor_map(actual_records)
            for anchor in sorted(expected_map.keys() - actual_map.keys(), key=str):
                _add_issue(
                    issues,
                    "semantic",
                    "omission",
                    case_id,
                    f"$.cases[{case_id}].{output_key}",
                    "expected record was omitted",
                    expected_map[anchor],
                )
            for anchor in sorted(actual_map.keys() - expected_map.keys(), key=str):
                _add_issue(
                    issues,
                    "semantic",
                    "spurious_extraction",
                    case_id,
                    f"$.cases[{case_id}].{output_key}",
                    "unexpected record was produced",
                    actual=actual_map[anchor],
                )
            for anchor in sorted(expected_map.keys() & actual_map.keys(), key=str):
                expected_record = expected_map[anchor]
                actual_record = actual_map[anchor]
                candidate_id = actual_record.get("claim_id", "UNKNOWN")
                expected_id = expected_record.get("claim_id")
                if isinstance(candidate_id, str) and isinstance(expected_id, str):
                    id_translation[candidate_id] = expected_id
                expected_without_id = {
                    key: value for key, value in expected_record.items() if key != "claim_id"
                }
                actual_without_id = {
                    key: value for key, value in actual_record.items() if key != "claim_id"
                }
                if canonical_json(expected_without_id) == canonical_json(actual_without_id):
                    metrics[output_key]["exact"] += 1
                    current[output_key]["exact"] += 1
                    continue
                if expected_record.get("normalized_value") != actual_record.get(
                    "normalized_value"
                ):
                    _add_issue(
                        issues,
                        "semantic",
                        "incorrect_normalization",
                        case_id,
                        f"$.cases[{case_id}].{output_key}.{candidate_id}.normalized_value",
                        "normalized_value differs from DEV annotation",
                        expected_record.get("normalized_value"),
                        actual_record.get("normalized_value"),
                    )
                if expected_record.get("evidence_span") != actual_record.get("evidence_span") or (
                    "surface_value" in expected_record
                    and expected_record.get("surface_value") != actual_record.get("surface_value")
                ):
                    _add_issue(
                        issues,
                        "semantic",
                        "evidence_mismatch",
                        case_id,
                        f"$.cases[{case_id}].{output_key}.{candidate_id}.evidence_span",
                        "evidence selection differs from DEV annotation",
                        expected_record.get("evidence_span"),
                        actual_record.get("evidence_span"),
                    )
                ignored = {"claim_id", "normalized_value", "evidence_span", "surface_value"}
                expected_other = {k: v for k, v in expected_record.items() if k not in ignored}
                actual_other = {k: v for k, v in actual_record.items() if k not in ignored}
                if expected_other != actual_other:
                    _add_issue(
                        issues,
                        "semantic",
                        "attribute_mismatch",
                        case_id,
                        f"$.cases[{case_id}].{output_key}.{candidate_id}",
                        "record attributes differ from DEV annotation",
                        expected_other,
                        actual_other,
                    )

        case_metrics[case_id] = current

    enriched_metrics: dict[str, Any] = {}
    for key, counts in metrics.items():
        precision = _safe_ratio(counts["exact"], counts["predicted"])
        recall = _safe_ratio(counts["exact"], counts["expected"])
        f1 = (
            round(2 * precision * recall / (precision + recall), 6)
            if precision is not None and recall is not None and precision + recall
            else None
        )
        enriched_metrics[key] = {
            **counts,
            "precision_exact": precision,
            "recall_exact": recall,
            "f1_exact": f1,
        }

    return issues, {"by_category": enriched_metrics, "by_case": case_metrics}


def build_report(
    candidate: Any,
    bank: Mapping[str, Any],
    bank_path: Path,
    candidate_path: Path,
    selected_case_ids: Sequence[str] | None = None,
) -> dict[str, Any]:
    structural_and_prohibited = validate_structure(candidate, bank, selected_case_ids)
    semantic_issues, metrics = compare_semantics(candidate, bank, selected_case_ids)
    issues = structural_and_prohibited + semantic_issues
    issue_dicts = [asdict(issue) for issue in issues]
    category_counts: dict[str, int] = {}
    case_counts: dict[str, int] = {}
    for issue in issues:
        category_counts[issue.category] = category_counts.get(issue.category, 0) + 1
        case_counts[issue.case_id] = case_counts.get(issue.case_id, 0) + 1

    structural_count = sum(issue.phase == "structural" for issue in issues)
    semantic_count = sum(issue.phase == "semantic" for issue in issues)
    return {
        "report_version": "1.0.0",
        "extractor_id": EXTRACTOR_ID,
        "bank": {
            "path": str(bank_path.resolve()),
            "sha256": sha256_file(bank_path),
            "inventory": bank_inventory(bank),
        },
        "candidate": {
            "path": str(candidate_path.resolve()),
            "sha256": sha256_file(candidate_path),
        },
        "selection": list(selected_case_ids) if selected_case_ids else None,
        "summary": {
            "structural_errors": structural_count,
            "semantic_findings": semantic_count,
            "broken_references": category_counts.get("broken_reference", 0),
            "invalid_spans": category_counts.get("invalid_span", 0),
            "must_not_produce_violations": category_counts.get("must_not_produce", 0),
            "prohibited_inferences": category_counts.get("prohibited_inference", 0),
            "structural_pass": structural_count == 0,
        },
        "taxonomy": {
            "by_category": dict(sorted(category_counts.items())),
            "by_case": dict(sorted(case_counts.items())),
        },
        "metrics": metrics,
        "issues": issue_dicts,
    }


def report_markdown(report: Mapping[str, Any]) -> str:
    summary = report["summary"]
    lines = [
        "# MOC-EXTRACTOR-001-C — Reporte de validación DEV",
        "",
        f"- Banco: `{report['bank']['path']}`",
        f"- SHA-256 banco: `{report['bank']['sha256']}`",
        f"- Candidato: `{report['candidate']['path']}`",
        f"- SHA-256 candidato: `{report['candidate']['sha256']}`",
        f"- Resultado estructural: **{'PASS' if summary['structural_pass'] else 'FAIL'}**",
        f"- Errores estructurales: {summary['structural_errors']}",
        f"- Referencias rotas: {summary['broken_references']}",
        f"- Spans inválidos: {summary['invalid_spans']}",
        f"- Hallazgos semánticos: {summary['semantic_findings']}",
        f"- Violaciones `must_not_produce`: {summary['must_not_produce_violations']}",
        "",
        "## Métricas exactas por categoría",
        "",
        "| Categoría | Esperados | Producidos | Exactos | Precisión | Recall | F1 |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for category, metric in report["metrics"]["by_category"].items():
        def fmt(value: Any) -> str:
            return "n/a" if value is None else str(value)

        lines.append(
            f"| {category} | {metric['expected']} | {metric['predicted']} | "
            f"{metric['exact']} | {fmt(metric['precision_exact'])} | "
            f"{fmt(metric['recall_exact'])} | {fmt(metric['f1_exact'])} |"
        )

    lines.extend(["", "## Taxonomía", ""])
    if report["taxonomy"]["by_category"]:
        for category, count in report["taxonomy"]["by_category"].items():
            lines.append(f"- `{category}`: {count}")
    else:
        lines.append("- Sin hallazgos.")

    lines.extend(["", "## Hallazgos exactos", ""])
    if not report["issues"]:
        lines.append("- Ninguno.")
    else:
        for issue in report["issues"]:
            lines.append(
                f"- [{issue['phase']}/{issue['category']}] "
                f"`{issue['case_id']}` `{issue['path']}` — {issue['message']}"
            )
    lines.extend(
        [
            "",
            "## Límite del dictamen",
            "",
            "Este reporte evalúa el banco DEV visible. No constituye evidencia sobre conjuntos VAL, adversariales ocultos o TEST, y no autoriza uso clínico.",
            "",
        ]
    )
    return "\n".join(lines)


def validate_candidate_file(
    bank_path: Path,
    candidate_path: Path,
    expected_sha256: str = EXPECTED_BANK_SHA256,
    selected_case_ids: Sequence[str] | None = None,
) -> dict[str, Any]:
    bank = load_bank(bank_path, expected_sha256)
    candidate = strict_json_load(candidate_path)
    return build_report(
        candidate,
        bank,
        bank_path,
        candidate_path,
        selected_case_ids,
    )


def _command_inspect_bank(args: argparse.Namespace) -> int:
    bank_path = Path(args.bank)
    bank = load_bank(bank_path, args.expected_sha256)
    result = {
        "path": str(bank_path.resolve()),
        "sha256": sha256_file(bank_path),
        "inventory": bank_inventory(bank),
        "status": "PASS",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def _command_project_input(args: argparse.Namespace) -> int:
    bank = load_bank(Path(args.bank), args.expected_sha256)
    output = project_model_input(bank, args.case_id)
    write_json(Path(args.output), output)
    return 0


def _command_validate(args: argparse.Namespace) -> int:
    report = validate_candidate_file(
        Path(args.bank),
        Path(args.candidate),
        args.expected_sha256,
        args.case_id,
    )
    if args.report_json:
        write_json(Path(args.report_json), report)
    if args.report_md:
        path = Path(args.report_md)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(report_markdown(report), encoding="utf-8", newline="\n")
    print(json.dumps(report["summary"], ensure_ascii=False, indent=2))
    return 0 if report["summary"]["structural_pass"] else 2


def build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="MOC-EXTRACTOR-001-C validator")
    subparsers = parser.add_subparsers(dest="command", required=True)

    inspect_parser = subparsers.add_parser("inspect-bank")
    inspect_parser.add_argument("--bank", required=True)
    inspect_parser.add_argument("--expected-sha256", default=EXPECTED_BANK_SHA256)
    inspect_parser.set_defaults(func=_command_inspect_bank)

    project_parser = subparsers.add_parser("project-input")
    project_parser.add_argument("--bank", required=True)
    project_parser.add_argument("--output", required=True)
    project_parser.add_argument("--expected-sha256", default=EXPECTED_BANK_SHA256)
    project_parser.add_argument("--case-id", action="append")
    project_parser.set_defaults(func=_command_project_input)

    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("--bank", required=True)
    validate_parser.add_argument("--candidate", required=True)
    validate_parser.add_argument("--expected-sha256", default=EXPECTED_BANK_SHA256)
    validate_parser.add_argument("--case-id", action="append")
    validate_parser.add_argument("--report-json")
    validate_parser.add_argument("--report-md")
    validate_parser.set_defaults(func=_command_validate)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_argument_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except ContractError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
