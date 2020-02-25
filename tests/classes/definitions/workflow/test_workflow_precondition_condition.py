import unittest
from parameterized import parameterized_class

from toscametrics.classes.clauses.conditions import ConditionClause
from toscametrics.classes.definitions.workflow_precondition import WorkflowPreconditionDefinition

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': [], 'expected': False},
   { 'input': [ConditionClause()], 'expected': False},
   { 'input': [ConditionClause(), 2], 'expected': True},
   { 'input': 'This is a string', 'expected': True},
   { 'input': 2, 'expected': True},
   { 'input': 2.0, 'expected': True},
   { 'input': {}, 'expected': True}
])
class TestWorkflowPreconditionDefinitionCondition(unittest.TestCase):

    def test(self):
        raised = False
        try:
            WorkflowPreconditionDefinition(target='test', condition=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()