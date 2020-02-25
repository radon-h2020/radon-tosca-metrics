import unittest
from parameterized import parameterized_class

from toscametrics.classes.definitions.activity.delegate_workflow import DelegateWorkflowActivityDefinition

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': {}, 'expected': False},
   { 'input': {'property':'some value'}, 'expected': False},
   { 'input': 'inline', 'expected': True},
   { 'input': True, 'expected': True},
   { 'input': 2, 'expected': True},
   { 'input': 2.0, 'expected': True},
   { 'input': [], 'expected': True},
])
class DelegateWorkflowActivityDefinitionInputs(unittest.TestCase):

    def test(self):
        raised = False

        try:
            DelegateWorkflowActivityDefinition(delegate='test', inputs=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()