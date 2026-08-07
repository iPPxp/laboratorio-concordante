from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from pydantic import ValidationError

import moc_extractor_001_h3.migrate as migrate_internal
from moc_extractor_001_h3 import (
    FactSourceReference,
    FrictionCandidateInput,
    FrictionCatalog,
    MigrationError,
    SemanticNormalizer,
    validate_extraction,
)
from moc_extractor_001_h3.migrate import migrate_v1_payload
from moc_extractor_001_h3.models import (
    CONTRACT_VERSION,
    FrictionMechanicalProof,
    FrictionVerificationStatus,
    MechanicallyVerifiedFriction,
    StructuredPredicate,
    ValidatedNarrativeExtractionVNext,
)


ROOT = Path(__file__).resolve().parents[1]
NORMALIZATION_CATALOG = (
    ROOT / "catalogs" / "MOC-EXTRACTOR-001-H2-NORMALIZATION-CATALOG.candidate.json"
)
FRICTION_CATALOG = (
    ROOT / "catalogs" / "MOC-EXTRACTOR-001-H2-FRICTION-CATALOG.candidate.json"
)


def identities() -> dict[str, str]:
    normalizer = SemanticNormalizer.from_path(NORMALIZATION_CATALOG)
    friction = FrictionCatalog.from_path(FRICTION_CATALOG)
    return {
        "normalization_catalog_version": normalizer.catalog_version,
        "normalization_catalog_sha256": normalizer.catalog_sha256,
        "friction_catalog_version": friction.version,
        "friction_catalog_sha256": friction.sha256,
    }


def span(raw: str, text: str) -> dict[str, object]:
    start = raw.index(text)
    return {"text": text, "start": start, "end": start + len(text)}


def claim(raw: str, text: str, claim_id: str) -> dict[str, object]:
    return {
        "claim_id": claim_id,
        "field": "estado_factual",
        "surface_value": text,
        "provenance": "reported",
        "normalization_rule": "NORM-H3-BOOLEAN-STATE",
        "minimal_evidence_span": span(raw, text),
        "maximal_semantic_span": None,
        "llm_proposed_normalized_values": [],
    }


def candidate(refs: list[str] | None = None) -> dict[str, object]:
    return {
        "type": "contradiction",
        "claim_refs": refs or ["DEV901-C01", "DEV901-C02"],
        "annotation_rule": "FRICTION-CONTRA-001",
        "description": "Contradicción candidata para recomputación H3.",
        "verification_status": "FRICTION_CANDIDATE",
    }


def extraction_payload(
    left: str = "El acceso está activo",
    right: str = "El acceso está inactivo",
    refs: list[str] | None = None,
) -> dict[str, object]:
    raw = f"{left}. {right}."
    return {
        "schema_version": CONTRACT_VERSION,
        "extractor_id": "MOC-EXTRACTOR-001-H",
        **identities(),
        "cases": [
            {
                "case_id": "EXP-A-DEV-901",
                "raw_narrative": raw,
                "claims": [
                    claim(raw, left, "DEV901-C01"),
                    claim(raw, right, "DEV901-C02"),
                ],
                "constraint_candidates": [],
                "unknowns": [],
                "friction_candidates": [candidate(refs)],
            }
        ],
    }


def fact_sources() -> list[dict[str, object]]:
    return [
        {
            "record_id": "DEV901-C01",
            "source_mapping_id": "MAP-H3-BOOL-001",
            "source_mapping_version": "2026-08-06.h3.1",
            "source_mapping_sha256": "3" * 64,
            "provenance": "deterministic_mapping",
        },
        {
            "record_id": "DEV901-C02",
            "source_mapping_id": "MAP-H3-BOOL-002",
            "source_mapping_version": "2026-08-06.h3.1",
            "source_mapping_sha256": "4" * 64,
            "provenance": "deterministic_mapping",
        },
    ]


def legacy_facts(*, falsify_values: bool = False) -> list[dict[str, object]]:
    sources = fact_sources()
    values = []
    for index, source in enumerate(sources):
        values.append(
            {
                **source,
                "dimension": "forged_dimension" if falsify_values else "access_enabled",
                "boolean_value": False if falsify_values else index == 0,
            }
        )
    return values


def source_payload(count: int) -> tuple[dict[str, object], dict[str, object]]:
    cases = []
    projected = []
    for index in range(count):
        case_id = f"EXP-A-DEV-{index:03d}"
        cases.append(
            {
                "case_id": case_id,
                "claims": [],
                "constraint_candidates": [],
                "unknowns": [],
                "frictions": [],
            }
        )
        projected.append(
            {"case_id": case_id, "raw_narrative": f"Caso marítimo {index}."}
        )
    return (
        {
            "schema_version": "1.0.0",
            "extractor_id": "MOC-EXTRACTOR-001-C",
            "cases": cases,
        },
        {"cases": projected},
    )


def migrate(source, projected):
    return migrate_v1_payload(source, projected, **identities())


class ExternalFrictionDtoTests(unittest.TestCase):
    def test_candidate_schema_excludes_verified_outputs(self) -> None:
        schema = FrictionCandidateInput.model_json_schema()
        serialized = json.dumps(schema, sort_keys=True)
        for forbidden in ("proof", "predicate_result", "structured_fact", "accepted_frictions"):
            self.assertNotIn(forbidden, serialized)

    def test_llm_verified_boolean_is_rejected(self) -> None:
        value = candidate()
        value["verified"] = True
        with self.assertRaises(ValidationError):
            FrictionCandidateInput.model_validate(value)

    def test_llm_verified_enum_is_rejected(self) -> None:
        value = candidate()
        value["verification_status"] = "FRICTION_MECHANICALLY_VERIFIED"
        with self.assertRaises(ValidationError):
            FrictionCandidateInput.model_validate(value)

    def test_llm_proof_is_rejected(self) -> None:
        value = candidate()
        value["proof"] = {"predicate_result": True}
        with self.assertRaises(ValidationError):
            FrictionCandidateInput.model_validate(value)

    def test_llm_predicate_is_rejected(self) -> None:
        value = candidate()
        value["predicate_result"] = True
        with self.assertRaises(ValidationError):
            FrictionCandidateInput.model_validate(value)

    def test_llm_structured_fact_is_rejected(self) -> None:
        value = candidate()
        value["structured_fact"] = {"boolean_value": True}
        with self.assertRaises(ValidationError):
            FrictionCandidateInput.model_validate(value)

    def test_input_schema_does_not_contain_mechanical_result(self) -> None:
        schema = ValidatedNarrativeExtractionVNext.model_json_schema()
        self.assertNotIn("MechanicallyVerifiedFriction", json.dumps(schema))

    def test_candidate_subclass_cannot_add_fields_to_json(self) -> None:
        class CandidateSubclass(FrictionCandidateInput):
            model_config = {"extra": "forbid", "frozen": True}

        value = candidate()
        value["verified"] = True
        with self.assertRaises(ValidationError):
            CandidateSubclass.model_validate(value)


class MechanicalRecomputationTests(unittest.TestCase):
    def test_valid_sources_generate_internal_proof(self) -> None:
        result = validate_extraction(extraction_payload(), fact_sources=fact_sources())
        self.assertTrue(result.valid)
        proof = result.accepted_frictions[0].proof
        self.assertEqual(proof.verification_rule_id, "FRICTION-CONTRA-001")
        self.assertEqual(proof.rule_version, identities()["friction_catalog_version"])
        self.assertEqual(proof.predicate_id, StructuredPredicate.SAME_DIMENSION_OPPOSITE_BOOLEAN)
        self.assertTrue(proof.predicate_result)
        self.assertEqual(len(proof.canonical_claims_sha256), 64)

    def test_legacy_values_are_ignored_and_recomputed(self) -> None:
        result = validate_extraction(
            extraction_payload(), structured_facts=legacy_facts(falsify_values=True)
        )
        self.assertTrue(result.valid)
        self.assertEqual(len(result.accepted_frictions), 1)

    def test_forged_source_mapping_is_rejected(self) -> None:
        sources = fact_sources()
        sources[0]["source_mapping_id"] = "MAP-H3-FORGED-001"
        result = validate_extraction(extraction_payload(), fact_sources=sources)
        self.assertFalse(result.valid)
        self.assertEqual(result.accepted_frictions, ())

    def test_forged_source_hash_is_rejected(self) -> None:
        sources = fact_sources()
        sources[0]["source_mapping_sha256"] = "f" * 64
        result = validate_extraction(extraction_payload(), fact_sources=sources)
        self.assertFalse(result.valid)

    def test_altered_claims_are_recomputed_not_trusted(self) -> None:
        result = validate_extraction(
            extraction_payload(right="El acceso está activo"),
            fact_sources=fact_sources(),
        )
        self.assertFalse(result.valid)
        self.assertEqual(result.accepted_frictions, ())

    def test_claim_hash_changes_with_claim_content(self) -> None:
        first = validate_extraction(extraction_payload(), fact_sources=fact_sources())
        second = validate_extraction(
            extraction_payload(
                left="La compuerta está activa",
                right="La compuerta está inactiva",
            ),
            fact_sources=fact_sources(),
        )
        self.assertNotEqual(
            first.accepted_frictions[0].proof.canonical_claims_sha256,
            second.accepted_frictions[0].proof.canonical_claims_sha256,
        )

    def test_refs_reordered_are_canonicalized_in_proof(self) -> None:
        result = validate_extraction(
            extraction_payload(refs=["DEV901-C02", "DEV901-C01"]),
            fact_sources=fact_sources(),
        )
        self.assertTrue(result.valid)
        self.assertEqual(
            result.accepted_frictions[0].proof.claim_refs,
            ("DEV901-C01", "DEV901-C02"),
        )

    def test_missing_sources_requires_review(self) -> None:
        result = validate_extraction(extraction_payload())
        self.assertFalse(result.valid)
        self.assertEqual(result.accepted_frictions, ())
        self.assertEqual(
            result.friction_review_required[0].reason_code,
            "STRUCTURED_FACTS_MISSING",
        )

    def test_fact_source_dto_rejects_external_boolean(self) -> None:
        source = fact_sources()[0]
        source["boolean_value"] = True
        with self.assertRaises(ValidationError):
            FactSourceReference.model_validate(source)

    def test_fact_sources_and_legacy_facts_are_ambiguous(self) -> None:
        result = validate_extraction(
            extraction_payload(),
            fact_sources=fact_sources(),
            structured_facts=legacy_facts(),
        )
        self.assertFalse(result.structural_valid)

    def test_direct_proof_constructor_is_rejected(self) -> None:
        with self.assertRaises(TypeError):
            FrictionMechanicalProof(
                verification_rule_id="FRICTION-CONTRA-001",
                rule_version="v1",
                claim_refs=("DEV901-C01", "DEV901-C02"),
                canonical_claims_sha256="0" * 64,
                structured_predicate=StructuredPredicate.SAME_DIMENSION_OPPOSITE_BOOLEAN,
                predicate_id=StructuredPredicate.SAME_DIMENSION_OPPOSITE_BOOLEAN,
                catalog_version="v1",
                catalog_sha256="0" * 64,
            )

    def test_direct_verified_constructor_is_rejected(self) -> None:
        forged_proof = FrictionMechanicalProof.model_construct(
            verification_rule_id="FRICTION-CONTRA-001",
            rule_version="v1",
            claim_refs=("DEV901-C01", "DEV901-C02"),
            canonical_claims_sha256="0" * 64,
            structured_predicate=StructuredPredicate.SAME_DIMENSION_OPPOSITE_BOOLEAN,
            predicate_id=StructuredPredicate.SAME_DIMENSION_OPPOSITE_BOOLEAN,
            predicate_result=True,
            catalog_version="v1",
            catalog_sha256="0" * 64,
            generated_by="moc_extractor_001_h3.friction_verifier",
        )
        with self.assertRaises(TypeError):
            MechanicallyVerifiedFriction(
                candidate=FrictionCandidateInput.model_validate(candidate()),
                proof=forged_proof,
            )

    def test_serialized_internal_result_is_not_rehydrated(self) -> None:
        result = validate_extraction(extraction_payload(), fact_sources=fact_sources())
        serialized = result.accepted_frictions[0].model_dump_json()
        with self.assertRaises(ValidationError):
            MechanicallyVerifiedFriction.model_validate_json(serialized)

    def test_model_construct_does_not_enter_input_payload(self) -> None:
        forged = MechanicallyVerifiedFriction.model_construct(
            candidate=FrictionCandidateInput.model_validate(candidate()),
            verification_status=FrictionVerificationStatus.MECHANICALLY_VERIFIED,
            proof=None,
        )
        value = extraction_payload()
        value["accepted_frictions"] = [forged.model_dump(mode="json")]
        self.assertFalse(validate_extraction(value).structural_valid)

    def test_replayed_proof_does_not_enter_input_payload(self) -> None:
        result = validate_extraction(extraction_payload(), fact_sources=fact_sources())
        value = extraction_payload(
            left="La alarma está activa", right="La alarma está inactiva"
        )
        value["proof"] = result.accepted_frictions[0].proof.model_dump(mode="json")
        self.assertFalse(validate_extraction(value, fact_sources=fact_sources()).structural_valid)

    def test_candidate_cannot_enter_accepted_collection(self) -> None:
        value = extraction_payload()
        value["accepted_frictions"] = [candidate()]
        self.assertFalse(validate_extraction(value).structural_valid)


class StrictMigrationBoundaryTests(unittest.TestCase):
    def test_zero_cases_rejected(self) -> None:
        source, projected = source_payload(0)
        with self.assertRaises(MigrationError):
            migrate(source, projected)

    def test_one_case_valid(self) -> None:
        source, projected = source_payload(1)
        self.assertTrue(migrate(source, projected).validation.valid)

    def test_twelve_cases_valid_without_truncation(self) -> None:
        source, projected = source_payload(12)
        result = migrate(source, projected)
        migrated = json.loads(result.migrated_payload_canonical_json)
        self.assertEqual(len(migrated["cases"]), 12)

    def test_thirteen_cases_rejected(self) -> None:
        source, projected = source_payload(13)
        with self.assertRaises(MigrationError):
            migrate(source, projected)

    def test_tuple_cases_rejected(self) -> None:
        source, projected = source_payload(1)
        source["cases"] = tuple(source["cases"])
        with self.assertRaises(MigrationError):
            migrate(source, projected)

    def test_generator_cases_rejected_with_typed_error(self) -> None:
        source, projected = source_payload(1)
        source["cases"] = (item for item in source["cases"])
        with self.assertRaises(MigrationError):
            migrate(source, projected)

    def test_object_cases_rejected(self) -> None:
        source, projected = source_payload(1)
        source["cases"] = {"case_id": "EXP-A-DEV-000"}
        with self.assertRaises(MigrationError):
            migrate(source, projected)

    def test_custom_iterable_cases_rejected(self) -> None:
        class CustomIterable:
            def __iter__(self):
                return iter(())

        source, projected = source_payload(1)
        source["cases"] = CustomIterable()
        with self.assertRaises(MigrationError):
            migrate(source, projected)

    def test_nested_cases_rejected(self) -> None:
        source, projected = source_payload(1)
        source["cases"] = [source["cases"]]
        with self.assertRaises(MigrationError):
            migrate(source, projected)

    def test_boolean_cases_rejected(self) -> None:
        source, projected = source_payload(1)
        source["cases"] = True
        with self.assertRaises(MigrationError):
            migrate(source, projected)

    def test_lying_list_subclass_rejected(self) -> None:
        class LyingList(list):
            def __len__(self):
                return 1

        source, projected = source_payload(13)
        source["cases"] = LyingList(source["cases"])
        with self.assertRaises(MigrationError):
            migrate(source, projected)

    def test_honest_list_subclass_rejected(self) -> None:
        class HonestList(list):
            pass

        source, projected = source_payload(1)
        source["cases"] = HonestList(source["cases"])
        with self.assertRaises(MigrationError):
            migrate(source, projected)

    def test_projected_tuple_rejected(self) -> None:
        source, projected = source_payload(1)
        projected["cases"] = tuple(projected["cases"])
        with self.assertRaises(MigrationError):
            migrate(source, projected)

    def test_direct_helper_rejects_subclass(self) -> None:
        class HonestList(list):
            pass

        source, _ = source_payload(1)
        source["cases"] = HonestList(source["cases"])
        with self.assertRaises(MigrationError):
            migrate_internal._validate_v1_payload(source)

    def test_invalid_input_is_rejected_before_deepcopy(self) -> None:
        class DeepcopyTrap:
            def __deepcopy__(self, memo):
                raise AssertionError("DEEPCOPY_REACHED")

        source, projected = source_payload(1)
        source["cases"] = DeepcopyTrap()
        with self.assertRaises(MigrationError):
            migrate(source, projected)

    def test_error_is_redacted(self) -> None:
        marker = "CASOS-PRIVADOS-H3"
        source, projected = source_payload(1)
        source["cases"] = marker
        with self.assertRaises(MigrationError) as raised:
            migrate(source, projected)
        self.assertNotIn(marker, str(raised.exception))

    def test_rejected_source_remains_unmodified(self) -> None:
        source, projected = source_payload(13)
        before = copy.deepcopy(source)
        with self.assertRaises(MigrationError):
            migrate(source, projected)
        self.assertEqual(source, before)


if __name__ == "__main__":
    unittest.main()
