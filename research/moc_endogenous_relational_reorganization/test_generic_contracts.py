import unittest

from generic_controllers import (
    B0Automatic, B1GenericReflection, B2RewardOptimizer,
    B3ConstrainedOptimizer, B4RelationalSelector, B5GenerativeReplanner,
    B6StructureEditor,
)
from state_model import GeneratorSpec, Relation, RelationalState


def state():
    return RelationalState({"a": 2.0, "b": 1.0}, (Relation("a", "b"),),
                           frozenset({"finite"}), GeneratorSpec("g", ("select_node",), 20))


class GenericContractTests(unittest.TestCase):
    def test_b0_b1_b2_do_not_edit_structure(self):
        for controller in (B0Automatic(), B1GenericReflection(), B2RewardOptimizer()):
            result = controller.run(state())
            self.assertFalse(result.structure_changed)
            self.assertEqual(result.delta.expansion, 0)

    def test_b3_filters_without_editing_constraints(self):
        constrained = RelationalState(
            {"a": 2.0, "b": 1.0}, (Relation("a", "b"),),
            frozenset({"deny:select:a"}), GeneratorSpec("g", ("select_node",), 20),
        )
        result = B3ConstrainedOptimizer().run(constrained)
        self.assertFalse(result.structure_changed)
        self.assertEqual(result.action_after, "select:b")
        self.assertEqual(result.delta.contraction, 1)

    def test_b4_selects_without_reorganization(self):
        result = B4RelationalSelector().run(state())
        self.assertFalse(result.structure_changed)
        self.assertEqual(result.delta.expansion, 0)
        self.assertEqual(result.action_after, "select:a")

    def test_b5_expands_generator_with_provenance(self):
        result = B5GenerativeReplanner().run(state(), add_operation="combine_pair",
                                             event_id="E5", timestamp=1,
                                             rationale="generic expansion")
        self.assertTrue(result.structure_changed)
        self.assertGreater(result.delta.expansion, 0)
        self.assertEqual(result.after.provenance[-1].target, "generator")

    def test_b6_reorganizes_without_changing_action(self):
        result = B6StructureEditor().run(state(), target="K", operation="ADD",
                                         payload="audit", event_id="E6", timestamp=1,
                                         rationale="constraint annotation")
        self.assertTrue(result.structure_changed)
        self.assertEqual(result.action_before, result.action_after)
        self.assertEqual(result.delta.transitability, 1.0)

    def test_b6_node_expansion_and_contraction(self):
        editor = B6StructureEditor()
        expanded = editor.run(state(), target="D", operation="UPSERT", payload=("c", 3.0),
                              event_id="E7", timestamp=1, rationale="expand")
        contracted = editor.run(expanded.after, target="D", operation="REMOVE", payload="c",
                                event_id="E8", timestamp=2, rationale="contract")
        self.assertGreater(expanded.delta.expansion, 0)
        self.assertGreater(contracted.delta.contraction, 0)
        self.assertEqual(len(contracted.after.provenance), 2)


if __name__ == "__main__":
    unittest.main()
