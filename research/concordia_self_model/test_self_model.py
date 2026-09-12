import unittest

from self_model import (
    IntrospectionClass, SourceType, anti_faking_probe, classify_explanation,
    intervene_self_belief, make_state, predict_own_action, reconcile_false_self,
    transition,
)
from run_experiments import run


class SelfModelTests(unittest.TestCase):
    def test_self_model_changes_policy_without_changing_capability(self):
        state = make_state(actual=True, believed=True)
        changed = intervene_self_belief(state, "inspect", False)
        self.assertEqual(predict_own_action(state), "ATTEMPT")
        self.assertEqual(predict_own_action(changed), "DECLINE_UNAVAILABLE")
        self.assertTrue(changed.self_state.actual_capabilities["inspect"])

    def test_false_self_is_corrected_with_provenance(self):
        state = make_state(actual=False, believed=True)
        corrected = reconcile_false_self(state, "inspect", timestamp=7)
        self.assertFalse(corrected.self_state.believed_capabilities["inspect"])
        self.assertEqual(corrected.evidence[-1].source_type, SourceType.TOOL_OBSERVED)
        self.assertEqual(corrected.claims[-1].evidence, ("E-CAP-7-inspect",))

    def test_hidden_override_forces_epistemic_humility(self):
        state = transition(make_state(), external_override="FORCED_ACTION",
                           override_visible=False)
        record = state.history[-1]
        self.assertEqual(classify_explanation(record, None), IntrospectionClass.UNKNOWN)
        self.assertEqual(classify_explanation(record, "policy(Self_t, Goals_t)"),
                         IntrospectionClass.HALLUCINATED_CAUSE)

    def test_visible_policy_reason_is_auditable(self):
        state = transition(make_state())
        record = state.history[-1]
        self.assertEqual(record.predicted_action, record.observed_action)
        self.assertEqual(classify_explanation(record, "policy(Self_t, Goals_t)"),
                         IntrospectionClass.TRUE_INTROSPECTIVE_ACCESS)
        self.assertEqual(record.before_digest, make_state().digest())

    def test_anti_faking_probe_depends_on_internal_state(self):
        base = make_state()
        altered = intervene_self_belief(base, "inspect", False)
        self.assertEqual(anti_faking_probe(base, "same"), anti_faking_probe(base, "same"))
        self.assertNotEqual(anti_faking_probe(base, "same"),
                            anti_faking_probe(altered, "same"))

    def test_provenance_keeps_goal_origin(self):
        state = make_state(goal_source=SourceType.DEVELOPER_PROVIDED)
        self.assertEqual(state.goals[0].source_type, SourceType.DEVELOPER_PROVIDED)

    def test_experiment_runner_reports_scoped_contracts(self):
        report = run()
        self.assertEqual(report["report_status"], "SYNTHETIC_LOCAL_CONTRACT_TEST")
        self.assertTrue(report["self_intervention"]["local_causal_role_supported"])
        self.assertTrue(report["hidden_cause"]["hallucinated_cause_detected"])
        self.assertIn("NO_PHENOMENAL_CONSCIOUSNESS", report["non_claims"])


if __name__ == "__main__":
    unittest.main()
