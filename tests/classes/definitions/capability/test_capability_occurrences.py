import unittest
from parameterized import parameterized_class

from toscametrics.classes.definitions.capability import CapabilityDefinition

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': [1, 2], 'expected': False},
   { 'input': [5, 'UNBOUNDED'], 'expected': False},
   { 'input': [],   'expected': True},
   { 'input': ['first', 'second'], 'expected': True},
   { 'input': 'This is a description', 'expected': True},
   { 'input': True,  'expected': True},
   { 'input': False, 'expected': True},
   { 'input': 2,     'expected': True},
   { 'input': 2.0,   'expected': True},
   { 'input': {},    'expected': True}
])
class TestCapabilityDefinitionOccurrences(unittest.TestCase):

    def test(self):
        raised = False

        try:
            CapabilityDefinition(type='Test', occurrences=self.input)
        except (TypeError, ValueError):
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()