import unittest
from parameterized import parameterized_class

from toscametrics.classes.definitions.workflow_step import WorkflowStepDefinition

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': [], 'expected': False},
   { 'input': ['some on_success'], 'expected': False},
   { 'input': ['some on_success', 1], 'expected': True},
   { 'input': 'This is a target relationship', 'expected': True},
   { 'input': 2, 'expected': True},
   { 'input': 2.0, 'expected': True},
   { 'input': {}, 'expected': True}
])
class TestWorkflowStepDefinitionFilter(unittest.TestCase):

    def test(self):
        raised = False

        try:
            WorkflowStepDefinition(target='test', onSuccess=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()