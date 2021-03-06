import unittest
from parameterized import parameterized_class

from toscametrics.classes.definitions.capability import CapabilityDefinition
from toscametrics.classes.definitions.attribute   import AttributeDefinition


@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': {},   'expected': False},
   { 'input': {'attribute':AttributeDefinition(type='integer')},   'expected': False},
   { 'input': 'active', 'expected': True},
   { 'input': 2,    'expected': True},
   { 'input': 2.0,  'expected': True},
   { 'input': [],   'expected': True}
])
class TestCapabilityDefinitionAttributes(unittest.TestCase):

    def test(self):
        raised = False

        try:
            CapabilityDefinition(type='Test', attributes=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()