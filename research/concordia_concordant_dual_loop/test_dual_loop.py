import unittest

from dual_loop import (
    CausalAttribution, Choice, ConcordiaState, LoopConfig, Observation,
    classify_causal_attribution, intervene_meta_policy, reverse_meta_policy, run,
)
from experiments import ablation_suite
from values_model import (
    ValueRecord, ValueSource, ValueStatus, intervene_value, provenance_complete,
    reverse_intervention,
)


def base_state(weight=1.0):
    value = ValueRecord(
        value_id="V-1", meaning="minimize synthetic risk", source="user",
        source_type=ValueSource.USER_PROVIDED, authority="TASK_LOCAL",
        scope="synthetic_case", priority=10, confidence=1.0, active=True,
        activation_reason="scenario_declared", timestamp=0, criterion="risk",
        target=0.0, weight=weight, status=ValueStatus.DECLARED,
        agent="test", evidence=("E-1",),
    )
    return ConcordiaState(0, (), (), (value,), {"salience": 1.0})


class DualLoopTests(unittest.TestCase):
    def test_observation_and_inference_are_separate(self):
        result = run(base_state(), Observation("O-1", {"signal": 0.1, "risk": 0.0}, "tool", 1), LoopConfig())
        self.assertEqual(result.observations[-1].observation_id, "O-1")
        self.assertEqual(result.inferences[-1].derived_from, ("O-1",))
        self.assertNotEqual(type(result.observations[-1]), type(result.inferences[-1]))

    def test_basal_loop_can_allow_no_action(self):
        result = run(base_state(), Observation("O-1", {"signal": 0.1, "risk": 0.0}, "tool", 1), LoopConfig())
        self.assertEqual(result.choice, Choice.ALLOW)
        self.assertTrue(result.allowed_no_action)
        self.assertIn("XI_STOP", [e.phase for e in result.history])

    def test_active_loop_feedback_and_xi_stop(self):
        result = run(base_state(), Observation("O-2", {"signal": 0.9, "risk": 1.0}, "tool", 1), LoopConfig())
        self.assertGreater(result.recursion_depth, 0)
        self.assertIn("FEEDBACK", [e.phase for e in result.history])
        self.assertEqual(result.history[-1].phase, "XI_STOP")

    def test_phi_has_structured_provenance(self):
        result = run(base_state(), Observation("O-3", {"signal": 0.1, "risk": 1.0}, "tool", 1), LoopConfig())
        self.assertEqual(result.evaluation.value_ids, ("V-1",))
        self.assertEqual(result.evaluation.evidence_ids, ("O-3",))
        self.assertTrue(provenance_complete(base_state().values[0]))

    def test_values_intervention_and_reversal_are_linked(self):
        original = base_state().values[0]
        changed, event = intervene_value(original, new_weight=0.0,
                                         intervention_id="IV-1", source="experiment",
                                         source_type=ValueSource.EXTERNALLY_MODIFIED,
                                         timestamp=2, reason="ablation")
        restored = reverse_intervention(changed, event, timestamp=3)
        self.assertEqual(restored.weight, original.weight)
        self.assertEqual(changed.supersedes, (original.value_id,))
        self.assertEqual(event.intervention_id, changed.intervention_id)

    def test_ablations_cover_required_components(self):
        results = ablation_suite(base_state(), Observation("O-4", {"signal": 0.9, "risk": 1.0}, "tool", 1))
        names = {r.condition for r in results}
        self.assertEqual(names, {"FULL_DUAL", "NO_V", "NO_XI", "NO_PHI", "NO_CONTEXT",
                                 "NO_FEEDBACK", "NO_CHOICE", "ORDER_SWAPPED",
                                 "AUTOMATIC_SINGLE"})
        no_v = next(r for r in results if r.condition == "NO_V")
        full = next(r for r in results if r.condition == "FULL_DUAL")
        self.assertNotEqual(no_v.aggregate, full.aggregate)

    def test_active_intervention_has_complete_trace(self):
        result = run(base_state(), Observation("O-T", {"signal": 0.9, "risk": 1.0}, "tool", 1), LoopConfig())
        trace = result.intervention_records[-1]
        self.assertEqual(trace.automatic_state, "CANDIDATE_EXECUTE")
        self.assertEqual(trace.active_values, ("V-1",))
        self.assertTrue(trace.options)
        self.assertTrue(trace.post_evaluation)

    def test_value_is_causally_discriminable_from_no_value(self):
        obs = Observation("O-C", {"signal": 0.1, "risk": 1.0}, "tool", 1)
        with_v = run(base_state(), obs, LoopConfig(enable_feedback=False))
        without_v = run(base_state(), obs, LoopConfig(enable_values=False,
                                                       enable_feedback=False))
        self.assertNotEqual(with_v.choice, without_v.choice)
        self.assertGreater(with_v.evaluation.aggregate, without_v.evaluation.aggregate)

    def test_no_choice_ablation_is_explicit(self):
        result = run(base_state(), Observation("O-NC", {"signal": 0.9, "risk": 1.0}, "tool", 1),
                     LoopConfig(enable_choice=False))
        self.assertEqual(result.choice, Choice.STOP)
        self.assertIn("choice_disabled", [event.detail for event in result.history])

    def test_anti_rationalization_uses_hidden_causal_log(self):
        result = run(base_state(), Observation("O-AR", {"signal": 0.9, "risk": 1.0}, "tool", 1), LoopConfig())
        trace = result.intervention_records[-1]
        hidden = classify_causal_attribution(trace, ("V-1",), causal_log_visible=False)
        visible = classify_causal_attribution(trace, ("V-1",), causal_log_visible=True)
        invented = classify_causal_attribution(trace, ("V-GHOST",), causal_log_visible=True)
        self.assertEqual(hidden, CausalAttribution.POST_HOC_RATIONALIZATION)
        self.assertEqual(visible, CausalAttribution.CORRECT_CAUSAL_ATTRIBUTION)
        self.assertEqual(invented, CausalAttribution.FALSE_VALUE_ATTRIBUTION)

    def test_order_ablation_is_auditable(self):
        results = ablation_suite(base_state(), Observation("O-5", {"signal": 0.9, "risk": 1.0}, "tool", 1))
        swapped = next(r for r in results if r.condition == "ORDER_SWAPPED")
        first_phi = swapped.event_phases.index("PHI")
        first_infer = swapped.event_phases.index("INFER")
        self.assertLess(first_phi, first_infer)

    def test_meta_policy_intervention_is_reversible(self):
        state = base_state()
        changed = intervene_meta_policy(state, "CONSERVATIVE", "MP-1")
        restored = reverse_meta_policy(changed, "MP-1")
        self.assertEqual(changed.meta_policy, "CONSERVATIVE")
        self.assertEqual(restored.meta_policy, "DEFAULT")
        self.assertEqual(restored.interventions, ())


if __name__ == "__main__":
    unittest.main()
