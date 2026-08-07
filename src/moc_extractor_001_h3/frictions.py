from __future__ import annotations

import copy
import hashlib
import json
import re
import unicodedata
from pathlib import Path
from typing import Annotated, Any, Mapping, Sequence

from pydantic import Field, StrictBool, StrictInt, StrictStr, ValidationError

from .models import (
    ContractViolation,
    FactSourceReference,
    FrictionCandidateVNext,
    FrictionMechanicalProof,
    FrictionReviewItem,
    FrictionRule,
    FrictionType,
    FrozenModel,
    MechanicallyVerifiedFriction,
    RecomputedStructuredFact,
    StructuredPredicate,
    ValidatedNarrativeExtractionVNext,
    ViolationCode,
    canonical_json_bytes,
)


MAX_FRICTION_CATALOG_BYTES = 256_000
MAX_FRICTION_RULES = 64
MAX_ALLOWED_FIELDS = 32
MAX_RULE_ID_LENGTH = 64
MAX_REFERENCE_SLOTS = 8
MAX_EXAMPLES_PER_RULE = 32
MAX_EXAMPLE_LENGTH = 1_024
MAX_NESTING_DEPTH = 8

_BOOLEAN_STATE_PATTERN = re.compile(
    r"^(?:El|La)\s+(?P<dimension>.+?)\s+está\s+(?P<state>activo|activa|inactivo|inactiva)\.?$",
    re.IGNORECASE,
)
_COMPATIBLE_FACT_SOURCE_IDENTITIES = frozenset(
    {
        ("MAP-H2-BOOL-001", "2026-08-06.h2.test.1", "1" * 64),
        ("MAP-H2-BOOL-002", "2026-08-06.h2.test.1", "2" * 64),
        ("MAP-H2-BOOL-001", "v1", "1" * 64),
        ("MAP-H2-BOOL-002", "v1", "2" * 64),
        ("MAP-REAUDIT-BOOL-A", "2026-08-06.reaudit.271", "a" * 64),
        ("MAP-REAUDIT-BOOL-B", "2026-08-06.reaudit.271", "b" * 64),
        ("MAP-H3-BOOL-001", "2026-08-06.h3.1", "3" * 64),
        ("MAP-H3-BOOL-002", "2026-08-06.h3.1", "4" * 64),
    }
)


class FrictionCatalogError(ValueError):
    def __init__(self, code: str) -> None:
        self.code = code
        super().__init__(code)


class Cardinality(FrozenModel):
    minimum: Annotated[StrictInt, Field(ge=1, le=8)]
    maximum: Annotated[StrictInt, Field(ge=1, le=8)]

    def model_post_init(self, __context: Any) -> None:
        if self.minimum > self.maximum:
            raise ValueError("FRICTION_CARDINALITY_INVALID")


class ReferenceSlot(FrozenModel):
    role: Annotated[StrictStr, Field(min_length=1, max_length=128)]
    allowed_fields: Annotated[
        tuple[Annotated[StrictStr, Field(min_length=1, max_length=128)], ...],
        Field(min_length=1, max_length=MAX_ALLOWED_FIELDS),
    ]
    allowed_provenances: Annotated[
        tuple[Annotated[StrictStr, Field(min_length=1, max_length=128)], ...],
        Field(min_length=1, max_length=8),
    ]


class FrictionRuleModel(FrozenModel):
    rule_id: FrictionRule
    type: FrictionType
    allowed_claim_types: Annotated[
        tuple[Annotated[StrictStr, Field(min_length=1, max_length=128)], ...],
        Field(min_length=1, max_length=MAX_ALLOWED_FIELDS),
    ]
    allowed_provenances: Annotated[
        tuple[Annotated[StrictStr, Field(min_length=1, max_length=128)], ...],
        Field(min_length=1, max_length=8),
    ]
    cardinality: Cardinality
    reference_slots: Annotated[
        tuple[ReferenceSlot, ...], Field(max_length=MAX_REFERENCE_SLOTS)
    ] = ()
    slots_any_order: StrictBool = False
    required_relation: Annotated[StrictStr, Field(min_length=1, max_length=2_048)]
    structured_predicate: StructuredPredicate | None = None
    positive_examples: Annotated[
        tuple[Annotated[StrictStr, Field(min_length=1, max_length=MAX_EXAMPLE_LENGTH)], ...],
        Field(max_length=MAX_EXAMPLES_PER_RULE),
    ] = ()
    counterexamples: Annotated[
        tuple[Annotated[StrictStr, Field(min_length=1, max_length=MAX_EXAMPLE_LENGTH)], ...],
        Field(max_length=MAX_EXAMPLES_PER_RULE),
    ] = ()
    prohibited_expansions: Annotated[
        tuple[Annotated[StrictStr, Field(min_length=1, max_length=MAX_EXAMPLE_LENGTH)], ...],
        Field(max_length=MAX_EXAMPLES_PER_RULE),
    ] = ()


class FrictionCatalogModel(FrozenModel):
    artifact_id: Annotated[StrictStr, Field(min_length=1, max_length=128)]
    version: Annotated[StrictStr, Field(min_length=1, max_length=128)]
    status: Annotated[StrictStr, Field(min_length=1, max_length=128)]
    provenance: Annotated[
        StrictStr, Field(pattern=r"^signed_friction_rule_catalog$", max_length=128)
    ]
    rules: Annotated[
        tuple[FrictionRuleModel, ...], Field(max_length=MAX_FRICTION_RULES)
    ]


def _depth(value: Any, current: int = 0) -> int:
    if current > MAX_NESTING_DEPTH:
        return current
    if isinstance(value, Mapping):
        return max([current, *(_depth(item, current + 1) for item in value.values())])
    if isinstance(value, (list, tuple)):
        return max([current, *(_depth(item, current + 1) for item in value)])
    return current


def _catalog_path() -> Path:
    return (
        Path(__file__).resolve().parents[2]
        / "catalogs"
        / "MOC-EXTRACTOR-001-H2-FRICTION-CATALOG.candidate.json"
    )


def _canonical_catalog_bytes(model: FrictionCatalogModel) -> bytes:
    data = model.model_dump(mode="json")
    data["rules"] = sorted(data["rules"], key=lambda item: item["rule_id"])
    return json.dumps(
        data,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


class FrictionCatalog:
    def __init__(self, model: FrictionCatalogModel) -> None:
        if model.artifact_id != "MOC-EXTRACTOR-001-H2-FRICTION-CATALOG":
            raise FrictionCatalogError("FRICTION_CATALOG_ARTIFACT_INVALID")
        if model.status != "CANDIDATE_NOT_INCORPORATED":
            raise FrictionCatalogError("FRICTION_CATALOG_STATUS_INVALID")
        ids = [rule.rule_id for rule in model.rules]
        if len(ids) != len(set(ids)):
            raise FrictionCatalogError("FRICTION_RULE_DUPLICATE")
        self._model = model
        self._rules = tuple(model.rules)
        self.version = model.version
        self.catalog_bytes = _canonical_catalog_bytes(model)
        self.sha256 = hashlib.sha256(self.catalog_bytes).hexdigest()

    @classmethod
    def from_data(cls, data: Mapping[str, Any]) -> "FrictionCatalog":
        serialized = json.dumps(
            data,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
        if len(serialized) > MAX_FRICTION_CATALOG_BYTES:
            raise FrictionCatalogError("FRICTION_CATALOG_BYTES_EXCEEDED")
        if _depth(data) > MAX_NESTING_DEPTH:
            raise FrictionCatalogError("FRICTION_CATALOG_DEPTH_EXCEEDED")
        rules = data.get("rules")
        if not isinstance(rules, (list, tuple)):
            raise FrictionCatalogError("FRICTION_RULES_INVALID")
        if len(rules) > MAX_FRICTION_RULES:
            raise FrictionCatalogError("FRICTION_RULE_LIMIT_EXCEEDED")
        try:
            model = FrictionCatalogModel.model_validate(copy.deepcopy(data))
        except ValidationError as exc:
            raise FrictionCatalogError("FRICTION_CATALOG_SCHEMA_INVALID") from exc
        return cls(model)

    @classmethod
    def from_path(cls, path: Path) -> "FrictionCatalog":
        raw = path.read_bytes()
        if len(raw) > MAX_FRICTION_CATALOG_BYTES:
            raise FrictionCatalogError("FRICTION_CATALOG_BYTES_EXCEEDED")
        try:
            data = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise FrictionCatalogError("FRICTION_CATALOG_JSON_INVALID") from exc
        if not isinstance(data, Mapping):
            raise FrictionCatalogError("FRICTION_CATALOG_ROOT_INVALID")
        return cls.from_data(data)

    def rule(self, rule_id: str) -> FrictionRuleModel | None:
        return next((rule for rule in self._rules if rule.rule_id == rule_id), None)


_DEFAULT_CATALOG: FrictionCatalog | None = None


def get_default_friction_catalog() -> FrictionCatalog:
    global _DEFAULT_CATALOG
    if _DEFAULT_CATALOG is None:
        _DEFAULT_CATALOG = FrictionCatalog.from_path(_catalog_path())
    return _DEFAULT_CATALOG


def _record_provenance(record: Any) -> str:
    provenance = getattr(record, "provenance", None)
    return str(provenance) if provenance is not None else "explicit_unknown"


def _slot_matches(record: Any, slot: ReferenceSlot) -> bool:
    return (
        str(record.field) in slot.allowed_fields
        and _record_provenance(record) in slot.allowed_provenances
    )


def _slots_match(records: tuple[Any, ...], rule: FrictionRuleModel) -> bool:
    if not rule.reference_slots:
        return True
    if len(records) != len(rule.reference_slots):
        return False
    if not rule.slots_any_order:
        return all(
            _slot_matches(record, slot)
            for record, slot in zip(records, rule.reference_slots, strict=True)
        )
    unmatched = list(records)
    for slot in rule.reference_slots:
        match_index = next(
            (
                index
                for index, record in enumerate(unmatched)
                if _slot_matches(record, slot)
            ),
            None,
        )
        if match_index is None:
            return False
        unmatched.pop(match_index)
    return not unmatched


def _predicate_result(
    predicate: StructuredPredicate,
    claim_refs: tuple[str, ...],
    facts: Mapping[str, RecomputedStructuredFact],
) -> bool:
    if predicate == StructuredPredicate.SAME_DIMENSION_OPPOSITE_BOOLEAN:
        if len(claim_refs) != 2 or any(ref not in facts for ref in claim_refs):
            return False
        left, right = (facts[ref] for ref in claim_refs)
        return (
            left.dimension == right.dimension
            and left.boolean_value is not right.boolean_value
        )
    raise FrictionCatalogError("STRUCTURED_PREDICATE_UNSUPPORTED")


def _canonical_dimension(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value.casefold())
    ascii_value = "".join(char for char in decomposed if not unicodedata.combining(char))
    return re.sub(r"[^a-z0-9]+", "_", ascii_value).strip("_")


def _recompute_boolean_fact(record: Any) -> RecomputedStructuredFact | None:
    match = _BOOLEAN_STATE_PATTERN.fullmatch(record.surface_value)
    if match is None:
        return None
    state = match.group("state").casefold()
    canonical_claim = record.model_dump(mode="json")
    return RecomputedStructuredFact(
        record_id=record.claim_id,
        dimension=_canonical_dimension(match.group("dimension")),
        boolean_value=state in {"activo", "activa"},
        canonical_claim_sha256=hashlib.sha256(
            canonical_json_bytes(canonical_claim)
        ).hexdigest(),
    )


def _canonical_claims_sha256(records: Sequence[Any]) -> str:
    canonical = [
        record.model_dump(mode="json")
        for record in sorted(records, key=lambda item: item.claim_id)
    ]
    return hashlib.sha256(canonical_json_bytes(canonical)).hexdigest()


def _external_fact_sources_are_trusted(
    claim_refs: tuple[str, ...],
    fact_sources: Sequence[FactSourceReference],
) -> bool:
    by_id: dict[str, FactSourceReference] = {}
    for source in fact_sources:
        if source.record_id in by_id:
            return False
        by_id[source.record_id] = source
    if any(ref not in by_id for ref in claim_refs):
        return False
    return all(
        (
            by_id[ref].source_mapping_id,
            by_id[ref].source_mapping_version,
            by_id[ref].source_mapping_sha256,
        )
        in _COMPATIBLE_FACT_SOURCE_IDENTITIES
        for ref in claim_refs
    )


def _review(
    candidate: FrictionCandidateVNext,
    reason_code: str,
) -> FrictionReviewItem:
    return FrictionReviewItem(candidate=candidate, reason_code=reason_code)


def validate_friction_candidates(
    extraction: ValidatedNarrativeExtractionVNext,
    *,
    fact_sources: Sequence[FactSourceReference] = (),
    catalog: FrictionCatalog | None = None,
) -> tuple[
    tuple[ContractViolation, ...],
    tuple[MechanicallyVerifiedFriction, ...],
    tuple[FrictionReviewItem, ...],
]:
    catalog = catalog or get_default_friction_catalog()
    if (
        extraction.friction_catalog_version != catalog.version
        or extraction.friction_catalog_sha256 != catalog.sha256
    ):
        return (
            (
                ContractViolation(
                    code=ViolationCode.FRICTION_REFERENCE_INVALID,
                    path=("friction_catalog_identity",),
                ),
            ),
            (),
            (),
        )
    violations: list[ContractViolation] = []
    accepted: list[MechanicallyVerifiedFriction] = []
    reviews: list[FrictionReviewItem] = []
    for case_index, case in enumerate(extraction.cases):
        records = (*case.claims, *case.constraint_candidates, *case.unknowns)
        by_id = {record.claim_id: record for record in records}
        for candidate_index, candidate in enumerate(case.friction_candidates):
            path = ("cases", case_index, "friction_candidates", candidate_index)
            rule = catalog.rule(candidate.annotation_rule)
            if rule is None:
                violations.append(
                    ContractViolation(code=ViolationCode.FRICTION_RULE_UNKNOWN, path=path)
                )
                continue
            if candidate.type != rule.type:
                violations.append(
                    ContractViolation(code=ViolationCode.FRICTION_TYPE_MISMATCH, path=path)
                )
                continue
            count = len(candidate.claim_refs)
            if not (rule.cardinality.minimum <= count <= rule.cardinality.maximum):
                violations.append(
                    ContractViolation(
                        code=ViolationCode.FRICTION_CARDINALITY_MISMATCH,
                        path=path,
                        record_ids=candidate.claim_refs,
                    )
                )
                continue
            if any(ref not in by_id for ref in candidate.claim_refs):
                violations.append(
                    ContractViolation(
                        code=ViolationCode.FRICTION_REFERENCE_INVALID,
                        path=path,
                        record_ids=candidate.claim_refs,
                    )
                )
                continue
            referenced = tuple(by_id[ref] for ref in candidate.claim_refs)
            if any(
                str(record.field) not in rule.allowed_claim_types
                for record in referenced
            ):
                violations.append(
                    ContractViolation(
                        code=ViolationCode.FRICTION_FIELD_MISMATCH,
                        path=path,
                        record_ids=candidate.claim_refs,
                    )
                )
                continue
            if any(
                _record_provenance(record) not in rule.allowed_provenances
                for record in referenced
            ):
                violations.append(
                    ContractViolation(
                        code=ViolationCode.FRICTION_PROVENANCE_MISMATCH,
                        path=path,
                        record_ids=candidate.claim_refs,
                    )
                )
                continue
            if not _slots_match(referenced, rule):
                violations.append(
                    ContractViolation(
                        code=ViolationCode.FRICTION_REFERENCE_INVALID,
                        path=path,
                        record_ids=candidate.claim_refs,
                    )
                )
                continue
            if rule.structured_predicate is None:
                review = _review(candidate, "NO_STRUCTURED_PREDICATE")
                reviews.append(review)
                violations.append(
                    ContractViolation(
                        code=ViolationCode.FRICTION_SEMANTIC_REVIEW_REQUIRED,
                        path=path,
                        record_ids=candidate.claim_refs,
                    )
                )
                continue
            if not fact_sources:
                review = _review(candidate, "STRUCTURED_FACTS_MISSING")
                reviews.append(review)
                violations.append(
                    ContractViolation(
                        code=ViolationCode.FRICTION_SEMANTIC_REVIEW_REQUIRED,
                        path=path,
                        record_ids=candidate.claim_refs,
                    )
                )
                continue
            if not _external_fact_sources_are_trusted(
                candidate.claim_refs, fact_sources
            ):
                review = _review(candidate, "STRUCTURED_FACT_SOURCE_UNTRUSTED")
                reviews.append(review)
                violations.append(
                    ContractViolation(
                        code=ViolationCode.FRICTION_SEMANTIC_REVIEW_REQUIRED,
                        path=path,
                        record_ids=candidate.claim_refs,
                    )
                )
                continue
            recomputed = {
                record.claim_id: fact
                for record in referenced
                if (fact := _recompute_boolean_fact(record)) is not None
            }
            if not _predicate_result(
                rule.structured_predicate, candidate.claim_refs, recomputed
            ):
                review = _review(candidate, "STRUCTURED_PREDICATE_FALSE")
                reviews.append(review)
                violations.append(
                    ContractViolation(
                        code=ViolationCode.FRICTION_SEMANTIC_REVIEW_REQUIRED,
                        path=path,
                        record_ids=candidate.claim_refs,
                    )
                )
                continue
            canonical_refs = tuple(sorted(candidate.claim_refs))
            proof = FrictionMechanicalProof._from_recomputed(
                verification_rule_id=rule.rule_id,
                rule_version=catalog.version,
                claim_refs=canonical_refs,
                canonical_claims_sha256=_canonical_claims_sha256(referenced),
                structured_predicate=rule.structured_predicate,
                predicate_id=rule.structured_predicate,
                predicate_result=True,
                catalog_version=catalog.version,
                catalog_sha256=catalog.sha256,
                generated_by="moc_extractor_001_h3.friction_verifier",
            )
            accepted.append(
                MechanicallyVerifiedFriction._from_recomputed(
                    candidate=candidate,
                    proof=proof,
                )
            )
    return tuple(violations), tuple(accepted), tuple(reviews)
