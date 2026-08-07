from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from types import MappingProxyType
from typing import Annotated, Any, Mapping, Sequence

from pydantic import Field, StrictBool, StrictStr, ValidationError, field_validator

from .models import (
    ContextFact,
    DeterministicallyNormalizedExtraction,
    FrozenModel,
    MAX_NORMALIZATION_CANDIDATES,
    MappingId,
    NormalizationRequest,
    NormalizationResult,
    NormalizationStatus,
    NormRule,
    ValidatedNarrativeExtractionVNext,
    canonical_json_bytes,
    canonical_sha256,
)


MAX_CATALOG_BYTES = 1_000_000
MAX_CATALOG_MAPPINGS = 1_000
MAX_CATALOG_RULES = 256
MAX_CATALOG_DEPTH = 8
MAX_MAPPING_ID_LENGTH = 64
MAX_ALLOWED_FIELDS = 32


class CatalogError(ValueError):
    def __init__(self, code: str) -> None:
        self.code = code
        super().__init__(code)


ShortString = Annotated[StrictStr, Field(min_length=1, max_length=512)]


class SemanticEffects(FrozenModel):
    adds_causality: StrictBool
    adds_intensity: StrictBool
    adds_certainty: StrictBool
    adds_temporality: StrictBool
    adds_operational_effect: StrictBool


class InputMatch(FrozenModel):
    surface_value: Annotated[StrictStr, Field(min_length=1, max_length=4_096)]
    required_context: tuple[ContextFact, ...] = ()

    @field_validator("required_context", mode="before")
    @classmethod
    def convert_context(cls, value: Any) -> Any:
        if isinstance(value, Mapping):
            return tuple(
                {"key": str(key), "value": item} for key, item in value.items()
            )
        return value

    @field_validator("required_context")
    @classmethod
    def unique_context_keys(
        cls, value: tuple[ContextFact, ...]
    ) -> tuple[ContextFact, ...]:
        keys = [item.key for item in value]
        if len(keys) != len(set(keys)):
            raise ValueError("DUPLICATE_MAPPING_CONTEXT_KEY")
        return value


class ClosedMapping(FrozenModel):
    mapping_id: MappingId
    normalization_rule: NormRule
    input_field: Annotated[StrictStr, Field(min_length=1, max_length=128)]
    input_match: InputMatch
    output_value: ShortString
    transformation_class: Annotated[
        StrictStr, Field(pattern=r"^exact_closed_mapping$", max_length=64)
    ]
    semantic_effects: SemanticEffects
    version: Annotated[StrictStr, Field(min_length=1, max_length=128)]
    provenance: Annotated[
        StrictStr, Field(pattern=r"^signed_mapping_contract$", max_length=128)
    ]
    normalization_family: ShortString | None = None
    normalization_subtype: ShortString | None = None


class NormalizationCatalog(FrozenModel):
    artifact_id: Annotated[StrictStr, Field(min_length=1, max_length=128)]
    version: Annotated[StrictStr, Field(min_length=1, max_length=128)]
    status: Annotated[StrictStr, Field(min_length=1, max_length=128)]
    provenance: Annotated[
        StrictStr, Field(pattern=r"^signed_mapping_catalog$", max_length=128)
    ]
    mappings: Annotated[
        tuple[ClosedMapping, ...], Field(max_length=MAX_CATALOG_MAPPINGS)
    ]


def deep_freeze(value: Any) -> Any:
    if isinstance(value, Mapping):
        return MappingProxyType(
            {str(key): deep_freeze(item) for key, item in copy.deepcopy(value).items()}
        )
    if isinstance(value, list):
        return tuple(deep_freeze(item) for item in copy.deepcopy(value))
    if isinstance(value, tuple):
        return tuple(deep_freeze(item) for item in copy.deepcopy(value))
    if isinstance(value, (set, frozenset)):
        return frozenset(deep_freeze(item) for item in copy.deepcopy(value))
    return copy.deepcopy(value)


def _depth(value: Any, current: int = 0) -> int:
    if current > MAX_CATALOG_DEPTH:
        return current
    if isinstance(value, Mapping):
        return max([current, *(_depth(item, current + 1) for item in value.values())])
    if isinstance(value, (list, tuple, set, frozenset)):
        return max([current, *(_depth(item, current + 1) for item in value)])
    return current


def _mapping_key(mapping: Mapping[str, Any]) -> tuple[str, str, str, str, str]:
    context = json.dumps(
        mapping["input_match"].get("required_context", []),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    return (
        str(mapping["normalization_rule"]),
        str(mapping["input_field"]),
        str(mapping["input_match"]["surface_value"]),
        context,
        str(mapping["mapping_id"]),
    )


def _canonical_mapping_data(mapping: ClosedMapping) -> dict[str, Any]:
    data = mapping.model_dump(mode="json")
    data["input_match"]["required_context"] = sorted(
        data["input_match"]["required_context"],
        key=lambda item: (item["key"], item["value"]),
    )
    return data


def _canonical_catalog_data(model: NormalizationCatalog) -> dict[str, Any]:
    data = model.model_dump(mode="json")
    for mapping in data["mappings"]:
        mapping["input_match"]["required_context"] = sorted(
            mapping["input_match"]["required_context"],
            key=lambda item: (item["key"], item["value"]),
        )
    data["mappings"] = sorted(data["mappings"], key=_mapping_key)
    return data


def _canonical_catalog_bytes(model: NormalizationCatalog) -> bytes:
    return json.dumps(
        _canonical_catalog_data(model),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def _preflight(data: Mapping[str, Any]) -> None:
    mappings = data.get("mappings")
    if not isinstance(mappings, (list, tuple)):
        raise CatalogError("CATALOG_MAPPINGS_INVALID")
    if len(mappings) > MAX_CATALOG_MAPPINGS:
        raise CatalogError("CATALOG_MAPPING_LIMIT_EXCEEDED")
    if _depth(data) > MAX_CATALOG_DEPTH:
        raise CatalogError("CATALOG_DEPTH_EXCEEDED")
    mapping_ids: set[str] = set()
    rules: set[str] = set()
    fields: set[str] = set()
    for mapping in mappings:
        if not isinstance(mapping, Mapping):
            raise CatalogError("CATALOG_MAPPING_INVALID")
        mapping_id = mapping.get("mapping_id")
        if not isinstance(mapping_id, str) or len(mapping_id) > MAX_MAPPING_ID_LENGTH:
            raise CatalogError("CATALOG_MAPPING_ID_INVALID")
        if mapping_id in mapping_ids:
            raise CatalogError("CATALOG_MAPPING_ID_DUPLICATE")
        mapping_ids.add(mapping_id)
        rule = mapping.get("normalization_rule")
        if isinstance(rule, str):
            rules.add(rule)
        field = mapping.get("input_field")
        if isinstance(field, str):
            fields.add(field)
    if len(rules) > MAX_CATALOG_RULES:
        raise CatalogError("CATALOG_RULE_LIMIT_EXCEEDED")
    if len(fields) > MAX_ALLOWED_FIELDS:
        raise CatalogError("CATALOG_FIELD_LIMIT_EXCEEDED")


class SemanticNormalizer:
    def __init__(self, model: NormalizationCatalog) -> None:
        if model.artifact_id != "MOC-EXTRACTOR-001-H2-NORMALIZATION-CATALOG":
            raise CatalogError("CATALOG_ARTIFACT_ID_INVALID")
        if model.status != "CANDIDATE_NOT_INCORPORATED":
            raise CatalogError("CATALOG_STATUS_INVALID")
        for mapping in model.mappings:
            if any(mapping.semantic_effects.model_dump().values()):
                raise CatalogError("MAPPING_FORBIDDEN_SEMANTIC_EFFECT")
        self._model = model
        self._mappings = tuple(model.mappings)
        self._frozen_catalog = deep_freeze(_canonical_catalog_data(model))
        self.catalog_bytes = _canonical_catalog_bytes(model)
        self.catalog_sha256 = hashlib.sha256(self.catalog_bytes).hexdigest()
        self.catalog_version = model.version
        grouped: dict[tuple[str, str, str, str], int] = {}
        for mapping in self._mappings:
            context = json.dumps(
                sorted(
                    (
                        {"key": item.key, "value": item.value}
                        for item in mapping.input_match.required_context
                    ),
                    key=lambda item: (item["key"], item["value"]),
                ),
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            )
            key = (
                mapping.normalization_rule,
                mapping.input_field,
                mapping.input_match.surface_value,
                context,
            )
            grouped[key] = grouped.get(key, 0) + 1
        if any(count > MAX_NORMALIZATION_CANDIDATES for count in grouped.values()):
            raise CatalogError("CATALOG_CANDIDATE_LIMIT_EXCEEDED")

    @classmethod
    def from_path(cls, path: Path) -> "SemanticNormalizer":
        raw = path.read_bytes()
        if len(raw) > MAX_CATALOG_BYTES:
            raise CatalogError("CATALOG_BYTES_EXCEEDED")
        try:
            data = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise CatalogError("CATALOG_JSON_INVALID") from exc
        if not isinstance(data, Mapping):
            raise CatalogError("CATALOG_ROOT_INVALID")
        return cls.from_data(data)

    @classmethod
    def from_data(cls, data: Mapping[str, Any]) -> "SemanticNormalizer":
        if not isinstance(data, Mapping):
            raise CatalogError("CATALOG_ROOT_INVALID")
        serialized = json.dumps(
            data,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
        if len(serialized) > MAX_CATALOG_BYTES:
            raise CatalogError("CATALOG_BYTES_EXCEEDED")
        _preflight(data)
        try:
            model = NormalizationCatalog.model_validate(copy.deepcopy(data))
        except ValidationError as exc:
            raise CatalogError("CATALOG_SCHEMA_INVALID") from exc
        return cls(model)

    @staticmethod
    def mapping_sha256(mapping: ClosedMapping) -> str:
        return hashlib.sha256(canonical_json_bytes(_canonical_mapping_data(mapping))).hexdigest()

    def normalize(self, request: NormalizationRequest) -> NormalizationResult:
        common = {
            "record_id": request.record_id,
            "llm_proposed_normalized_values": request.llm_proposed_normalized_values,
            "rule": request.normalization_rule,
            "catalog_version": self.catalog_version,
            "catalog_sha256": self.catalog_sha256,
        }
        if request.catalog_version != self.catalog_version:
            return NormalizationResult(
                **common,
                status=NormalizationStatus.REJECTED_MAPPING,
                diagnostic_code="CATALOG_VERSION_MISMATCH",
            )
        if request.catalog_sha256 != self.catalog_sha256:
            return NormalizationResult(
                **common,
                status=NormalizationStatus.REJECTED_MAPPING,
                diagnostic_code="CATALOG_HASH_MISMATCH",
            )
        rule_mappings = tuple(
            mapping
            for mapping in self._mappings
            if mapping.normalization_rule == request.normalization_rule
        )
        if not rule_mappings:
            return NormalizationResult(
                **common,
                status=NormalizationStatus.REJECTED_MAPPING,
                diagnostic_code="RULE_NOT_FOUND",
            )
        if all(mapping.input_field != request.field for mapping in rule_mappings):
            return NormalizationResult(
                **common,
                status=NormalizationStatus.REJECTED_MAPPING,
                diagnostic_code="RULE_FIELD_MISMATCH",
            )
        context = {item.key: item.value for item in request.allowed_context}
        matches = tuple(
            mapping
            for mapping in rule_mappings
            if mapping.input_field == request.field
            and mapping.input_match.surface_value == request.surface_value
            and all(
                context.get(item.key) == item.value
                for item in mapping.input_match.required_context
            )
        )
        if not matches:
            return NormalizationResult(
                **common,
                status=NormalizationStatus.UNRESOLVED,
                diagnostic_code="NO_EXACT_MAPPING",
            )
        if len(matches) > 1:
            return NormalizationResult(
                **common,
                status=NormalizationStatus.AMBIGUOUS,
                candidates=tuple(sorted(mapping.output_value for mapping in matches)),
                diagnostic_code="MULTIPLE_EXACT_MAPPINGS",
            )
        selected = matches[0]
        return NormalizationResult(
            **common,
            status=NormalizationStatus.NORMALIZED,
            normalized_value=selected.output_value,
            normalization_family=selected.normalization_family,
            normalization_subtype=selected.normalization_subtype,
            mapping_id=selected.mapping_id,
            mapping_version=selected.version,
            mapping_sha256=self.mapping_sha256(selected),
            diagnostic_code="EXACT_MAPPING_SELECTED",
        )

    def normalize_extraction(
        self,
        extraction: ValidatedNarrativeExtractionVNext,
        *,
        allowed_context: Sequence[ContextFact] = (),
    ) -> DeterministicallyNormalizedExtraction:
        results: list[NormalizationResult] = []
        for case in extraction.cases:
            for record in (*case.claims, *case.constraint_candidates):
                results.append(
                    self.normalize(
                        NormalizationRequest(
                            record_id=record.claim_id,
                            field=str(record.field),
                            surface_value=record.surface_value,
                            normalization_rule=record.normalization_rule,
                            allowed_context=tuple(allowed_context),
                            catalog_version=extraction.normalization_catalog_version,
                            catalog_sha256=extraction.normalization_catalog_sha256,
                            llm_proposed_normalized_values=record.llm_proposed_normalized_values,
                        )
                    )
                )
        return DeterministicallyNormalizedExtraction(
            source_extraction_sha256=canonical_sha256(extraction),
            catalog_version=self.catalog_version,
            catalog_sha256=self.catalog_sha256,
            results=tuple(results),
        )
