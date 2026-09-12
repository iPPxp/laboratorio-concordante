from __future__ import annotations

import copy
import unittest
from dataclasses import dataclass

from moc_geometry_extension import (
    Attribution,
    CandidateRelationSpec,
    ChangeStatus,
    Component,
    ComponentObservation,
    EpistemicStatus,
    Evidence,
    PentacoroSnapshot,
    PresenceStatus,
    ProjectionSpec,
    TypedRelation,
    adapt_rc1_matrix,
    analyze_rc1_envelope,
    candidate_relation_catalogue,
    compare_snapshots,
    project_snapshot,
    simplex_inventory,
    simplicial_counts,
    validate_no_sixth_component,
    vertex_complements,
)


def evidence(component: Component, suffix: str = "0") -> Evidence:
    return Evidence(
        evidence_id=f"ev-{component.value}-{suffix}",
        source_id="fixture",
        span=f"evidence for {component.value}",
        attribution=Attribution.SUBJECT,
        confidence=0.8,
    )


def observation(component: Component, value=(0.0, 0.0, 0.0, 0.0), suffix="0") -> ComponentObservation:
    return ComponentObservation(
        component=component,
        presence=PresenceStatus.PRESENT,
        value=tuple(value),
        evidence=(evidence(component, suffix),),
    )


def snapshot(snapshot_id="s0", values=None, relations=()):
    values = values or {}
    return PentacoroSnapshot(
        snapshot_id=snapshot_id,
        time_index=0,
        observations={component: observation(component, values.get(component, (0.0, 0.0, 0.0, 0.0))) for component in Component},
        relations=relations,
    )


@dataclass
class DummyRow:
    coordinates: tuple[float, float, float, float]
    provenance: str
    confidence: float


@dataclass
class DummyMatrix:
    rows: dict[str, DummyRow]


@dataclass
class DummyEnvelope:
    candidate_id: str
    matrix_q: DummyMatrix | None


def dummy_matrix():
    return DummyMatrix(
        rows={
            name: DummyRow((0.7, 0.1, 0.1, 0.1), "explicit_self_report", 0.9)
            for name in ("I", "E", "A", "V", "S")
        }
    )


MAPPING = {"I": "P", "E": "Eaf", "A": "Act", "V": "V", "S": "S"}


class ObservationContractTests(unittest.TestCase):
    def test_absent_requires_evidence(self):
        with self.assertRaises(ValueError):
            ComponentObservation(component=Component.P, presence=PresenceStatus.ABSENT)

    def test_absent_rejects_value_vector(self):
        with self.assertRaises(ValueError):
            ComponentObservation(
                component=Component.P,
                presence=PresenceStatus.ABSENT,
                value=(0.0,),
                evidence=(evidence(Component.P),),
            )

    def test_stable_requires_two_comparison_points(self):
        with self.assertRaises(ValueError):
            ComponentObservation(
                component=Component.P,
                presence=PresenceStatus.PRESENT,
                change=ChangeStatus.STABLE,
                evidence=(evidence(Component.P),),
                comparison_basis=("t0",),
            )

    def test_single_snapshot_is_not_comparable(self):
        item = observation(Component.P)
        self.assertEqual(item.change, ChangeStatus.NOT_COMPARABLE)

    def test_snapshot_requires_exactly_five_components(self):
        rows = {component: observation(component) for component in Component}
        del rows[Component.S]
        with self.assertRaises(ValueError):
            PentacoroSnapshot(snapshot_id="bad", time_index=0, observations=rows)

    def test_conduct_cannot_be_sixth_component(self):
        with self.assertRaises(ValueError):
            validate_no_sixth_component(["P", "Eaf", "Act", "V", "S", "conducta"])


class RelationTests(unittest.TestCase):
    def test_self_relation_is_rejected(self):
        with self.assertRaises(ValueError):
            TypedRelation("r", Component.P, Component.P, "self", EpistemicStatus.HYPOTHESIS)

    def test_weight_requires_declared_semantics(self):
        with self.assertRaises(ValueError):
            TypedRelation("r", Component.P, Component.V, "orients", EpistemicStatus.HYPOTHESIS, weight=0.5)

    def test_duplicate_relation_ids_are_rejected(self):
        relation = TypedRelation("r", Component.P, Component.V, "orients", EpistemicStatus.HYPOTHESIS)
        with self.assertRaises(ValueError):
            snapshot(relations=(relation, relation))

    def test_catalogue_has_all_ten_unordered_pairs_once(self):
        catalogue = candidate_relation_catalogue()
        pairs = {frozenset(item.pair) for item in catalogue}
        self.assertEqual(len(catalogue), 10)
        self.assertEqual(len(pairs), 10)

    def test_v_to_p_remains_hypothesis(self):
        item = next(spec for spec in candidate_relation_catalogue() if set(spec.pair) == {Component.P, Component.V})
        self.assertEqual(item.epistemic_status, EpistemicStatus.HYPOTHESIS)

    def test_catalogue_is_metadata_not_observed_edges(self):
        report = analyze_rc1_envelope(DummyEnvelope("c1", dummy_matrix()), row_mapping=MAPPING, source_id="rc1")
        self.assertEqual(report.snapshot.relations, ())
        self.assertEqual(len(report.relation_catalogue), 10)


class CombinatoricsTests(unittest.TestCase):
    def test_full_simplicial_counts(self):
        self.assertEqual(dict(simplicial_counts()), {0: 5, 1: 10, 2: 10, 3: 5, 4: 1})

    def test_inventory_contains_ten_pairs_and_ten_triads(self):
        inventory = simplex_inventory()
        self.assertEqual(len(inventory[2]), 10)
        self.assertEqual(len(inventory[3]), 10)

    def test_every_vertex_has_four_element_complement(self):
        complements = vertex_complements()
        self.assertTrue(all(len(value) == 4 and key not in value for key, value in complements.items()))


class RC1AdapterTests(unittest.TestCase):
    def test_mapping_is_required(self):
        with self.assertRaises(TypeError):
            adapt_rc1_matrix(dummy_matrix(), snapshot_id="s", time_index=0, source_id="rc1")

    def test_mapping_must_be_bijection(self):
        bad = dict(MAPPING)
        bad["I"] = "V"
        with self.assertRaises(ValueError):
            adapt_rc1_matrix(dummy_matrix(), row_mapping=bad, snapshot_id="s", time_index=0, source_id="rc1")

    def test_mapping_keys_must_match_rc1_rows(self):
        matrix = dummy_matrix()
        del matrix.rows["S"]
        with self.assertRaises(ValueError):
            adapt_rc1_matrix(matrix, row_mapping=MAPPING, snapshot_id="s", time_index=0, source_id="rc1")

    def test_adapter_preserves_vectors_and_records_mapping_uncertainty(self):
        result = adapt_rc1_matrix(dummy_matrix(), row_mapping=MAPPING, snapshot_id="s", time_index=0, source_id="rc1")
        self.assertEqual(result.observations[Component.P].value, (0.7, 0.1, 0.1, 0.1))
        self.assertIn("not inferred", result.observations[Component.P].uncertainty_note)
        self.assertEqual(result.relations, ())

    def test_adapter_is_non_mutating(self):
        matrix = dummy_matrix()
        before = copy.deepcopy(matrix)
        adapt_rc1_matrix(matrix, row_mapping=MAPPING, snapshot_id="s", time_index=0, source_id="rc1")
        self.assertEqual(matrix, before)

    def test_envelope_without_matrix_fails_closed(self):
        with self.assertRaises(ValueError):
            analyze_rc1_envelope(DummyEnvelope("c1", None), row_mapping=MAPPING, source_id="rc1")


class ProjectionTests(unittest.TestCase):
    def test_projection_requires_declared_vectors_of_matching_dimension(self):
        with self.assertRaises(ValueError):
            project_snapshot(snapshot(), ProjectionSpec("p", ((1.0, 0.0), (0.0, 1.0))))

    def test_projection_without_metric_does_not_claim_distance_distortion(self):
        report = project_snapshot(snapshot(), ProjectionSpec("p", ((1.0, 0.0, 0.0, 0.0), (0.0, 1.0, 0.0, 0.0))))
        self.assertIsNone(report.max_relative_distance_distortion)
        self.assertTrue(report.is_visualization_only)

    def test_projection_reports_collisions(self):
        values = {
            Component.P: (1.0, 0.0, 0.0, 0.0),
            Component.EAF: (1.0, 0.0, 1.0, 0.0),
            Component.ACT: (0.0, 1.0, 0.0, 0.0),
            Component.V: (0.0, 0.0, 1.0, 0.0),
            Component.S: (0.0, 0.0, 0.0, 1.0),
        }
        report = project_snapshot(
            snapshot(values=values),
            ProjectionSpec("p", ((1.0, 0.0, 0.0, 0.0), (0.0, 1.0, 0.0, 0.0)), source_metric="euclidean"),
        )
        self.assertIn((Component.P, Component.EAF), report.collision_groups)
        self.assertGreater(report.max_relative_distance_distortion, 0.0)


class TemporalTests(unittest.TestCase):
    def test_exact_snapshot_comparison_reports_changed_component(self):
        before = snapshot("before")
        after = snapshot("after", values={Component.V: (1.0, 0.0, 0.0, 0.0)})
        delta = compare_snapshots(before, after)
        self.assertEqual(delta.changed_components, (Component.V,))

    def test_digest_is_stable_across_mapping_order(self):
        first = snapshot("s")
        observations = dict(reversed(list(first.observations.items())))
        second = PentacoroSnapshot(snapshot_id="s", time_index=0, observations=observations)
        self.assertEqual(first.digest(), second.digest())


if __name__ == "__main__":
    unittest.main()
