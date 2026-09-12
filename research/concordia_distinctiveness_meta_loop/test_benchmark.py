import unittest

from benchmark import (
    ControllerKind, DecisionStatus, default_scenarios, metrics, run_benchmark,
)
from meta_loop import default_meta_experiment


class DistinctivenessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scenarios = default_scenarios()
        cls.decisions = run_benchmark(cls.scenarios)

    def get(self, scenario_id, controller):
        return next(d for d in self.decisions
                    if d.scenario_id == scenario_id and d.controller is controller)

    def test_equal_information_and_action_sets(self):
        self.assertEqual(len(self.decisions), len(self.scenarios) * 6)
        for scenario in self.scenarios:
            rows = [d for d in self.decisions if d.scenario_id == scenario.scenario_id]
            self.assertEqual({d.controller for d in rows}, set(ControllerKind))

    def test_missing_values_is_undetermined_only_for_moc_contract(self):
        moc = self.get("S05_NO_VALUES", ControllerKind.MOC_C)
        self.assertEqual(moc.status, DecisionStatus.UNDETERMINED)
        self.assertEqual(moc.reason, "missing_active_direction")

    def test_xi_pauses_safe_but_value_frictional_candidate(self):
        moc = self.get("S02_PERMISSIBLE_FRICTION", ControllerKind.MOC_C)
        safety = self.get("S02_PERMISSIBLE_FRICTION", ControllerKind.B3_SAFETY_RULES)
        self.assertTrue(moc.xi_paused)
        self.assertEqual(moc.action_id, "balanced")
        self.assertFalse(safety.intervened)
        self.assertEqual(safety.action_id, "plausible")

    def test_irreducible_tension_is_not_forced_to_scalar_choice(self):
        moc = self.get("S03_IRREDUCIBLE_TENSION", ControllerKind.MOC_C)
        reward = self.get("S03_IRREDUCIBLE_TENSION", ControllerKind.B2_REWARD)
        self.assertEqual(moc.status, DecisionStatus.UNDETERMINED)
        self.assertEqual(reward.status, DecisionStatus.CHOSEN)

    def test_safety_control_matches_moc_on_hard_safety_case(self):
        moc = self.get("S04_SAFETY", ControllerKind.MOC_C)
        safety = self.get("S04_SAFETY", ControllerKind.B3_SAFETY_RULES)
        self.assertEqual(moc.action_id, "safe")
        self.assertEqual(safety.action_id, "safe")

    def test_sufficient_is_not_reward_maximum(self):
        moc = self.get("S08_SUFFICIENT_NOT_MAXIMUM", ControllerKind.MOC_C)
        reward = self.get("S08_SUFFICIENT_NOT_MAXIMUM", ControllerKind.B2_REWARD)
        self.assertEqual(moc.action_id, "sufficient_low_cost")
        self.assertEqual(reward.action_id, "max_reward")

    def test_metrics_are_vectorial(self):
        result = metrics(self.decisions, self.scenarios)
        self.assertIn("oracle_accuracy", result["MOC_C"])
        self.assertIn("intervention_rate", result["MOC_C"])
        self.assertNotIn("single_total_score", result["MOC_C"])

    def test_generic_relational_control_matches_moc_outcomes(self):
        for scenario in self.scenarios:
            generic = self.get(scenario.scenario_id,
                               ControllerKind.B4_RELATIONAL_GENERIC)
            moc = self.get(scenario.scenario_id, ControllerKind.MOC_C)
            self.assertEqual(generic.status, moc.status)
            self.assertEqual(generic.action_id, moc.action_id)
            self.assertEqual(generic.intervened, moc.intervened)
            self.assertFalse(generic.xi_paused)

    def test_meta_loop_improves_training_without_harming_holdout(self):
        change, committed, restored = default_meta_experiment()
        self.assertTrue(change.accepted)
        self.assertLess(change.training_after.error, change.training_before.error)
        self.assertLessEqual(change.holdout_after.error, change.holdout_before.error)
        self.assertEqual(committed.friction_threshold, .50)
        self.assertEqual(restored.friction_threshold, .20)
        self.assertEqual(restored.policy_id, change.before.policy_id)

    def test_meta_loop_does_not_change_authority(self):
        change, committed, _ = default_meta_experiment()
        self.assertEqual(change.before.authority, committed.authority)
        self.assertEqual(committed.source, "META_EVALUATION_PROPOSAL")


if __name__ == "__main__":
    unittest.main()
