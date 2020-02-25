import unittest
from parameterized import parameterized_class

from toscametrics.classes.definitions.capability import CapabilityDefinition

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': [],   'expected': False},
   { 'input': ['first', 'second'], 'expected': False},
   { 'input': 'This is a description', 'expected': True},
   { 'input': True,  'expected': True},
   { 'input': False, 'expected': True},
   { 'input': 2,     'expected': True},
   { 'input': 2.0,   'expected': True},
   { 'input': [1, 2], 'expected': True},
   { 'input': {},    'expected': True}
])
class TestCapabilityDefinitionvalidSourceTypess(unittest.TestCase):

    def test(self):
        raised = False

        try:
            CapabilityDefinition(type='Test', validSourceTypes=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()