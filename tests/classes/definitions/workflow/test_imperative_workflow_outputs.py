import unittest
from parameterized import parameterized_class

from toscametrics.classes.definitions.imperative_workflow import ImperativeWorkflowDefinition
from toscametrics.classes.mapping.attribute               import AttributeMapping

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': {}, 'expected': False},
   { 'input': {'attribute_1':AttributeMapping(mapping=['output'])}, 'expected': False},
   { 'input': 'string', 'expected': True},
   { 'input': 2, 'expected': True},
   { 'input': 2.0, 'expected': True},
   { 'input': [], 'expected': True}
])
class TestImperativeWorkflowDefinitionOutputs(unittest.TestCase):

    def test(self):
        raised = False

        try:
            ImperativeWorkflowDefinition(outputs=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()