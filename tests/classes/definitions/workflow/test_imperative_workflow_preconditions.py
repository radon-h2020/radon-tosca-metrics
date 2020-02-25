import unittest
from parameterized import parameterized_class

from toscametrics.classes.definitions.workflow_precondition import WorkflowPreconditionDefinition
from toscametrics.classes.definitions.imperative_workflow   import ImperativeWorkflowDefinition

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': [], 'expected': False},
   { 'input': [WorkflowPreconditionDefinition(target='Welcome.Stop')], 'expected': False},
   { 'input': [1, 2], 'expected': True},
   { 'input': 'string', 'expected': True},
   { 'input': 2, 'expected': True},
   { 'input': 2.0, 'expected': True},
   { 'input': {}, 'expected': True}
])
class TestImperativeWorkflowDefinitionPreconditions(unittest.TestCase):

    def test(self):
        raised = False

        try:
            ImperativeWorkflowDefinition(preconditions=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()