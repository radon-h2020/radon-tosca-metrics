import unittest
from parameterized import parameterized_class

from toscametrics.classes.definitions.property            import PropertyDefinition
from toscametrics.classes.definitions.imperative_workflow import ImperativeWorkflowDefinition

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': {}, 'expected': False},
   { 'input': {'property_1': PropertyDefinition(type='nodes.template.A')}, 'expected': False},
   { 'input': {'key':'value'}, 'expected': True},
   { 'input': 'string', 'expected': True},
   { 'input': 2, 'expected': True},
   { 'input': 2.0, 'expected': True},
   { 'input': [], 'expected': True}
])
class TestImperativeWorkflowDefinitionInputs(unittest.TestCase):

    def test(self):
        raised = False

        try:
            ImperativeWorkflowDefinition(inputs=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()