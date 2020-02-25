import unittest
from parameterized import parameterized_class

from toscametrics.classes.definitions.capability import CapabilityDefinition
from toscametrics.classes.definitions.property   import PropertyDefinition


@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': {},   'expected': False},
   { 'input': {'limit':PropertyDefinition(type='integer', default=100)},   'expected': False},
   { 'input': 'active', 'expected': True},
   { 'input': 2,    'expected': True},
   { 'input': 2.0,  'expected': True},
   { 'input': [],   'expected': True}
])
class TestCapabilityDefinitionProperties(unittest.TestCase):

    def test(self):
        raised = False

        try:
            CapabilityDefinition(type='Test', properties=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()