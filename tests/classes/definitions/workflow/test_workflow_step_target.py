import unittest
from parameterized import parameterized_class

from toscametrics.classes.definitions.workflow_step import WorkflowStepDefinition

@parameterized_class([
   { 'input': 'This is a target', 'expected': False},
   { 'input': None, 'expected': True},
   { 'input': 2, 'expected': True},
   { 'input': 2.0, 'expected': True},
   { 'input': [], 'expected': True},
   { 'input': {}, 'expected': True}
])
class TestWorkflowStepDefinitionDefinitionTarget(unittest.TestCase):

    def test(self):
        raised = False

        try:
            WorkflowStepDefinition(target=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()