import unittest
from parameterized import parameterized_class

from toscametrics.classes.definitions.property import PropertyDefinition


@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': True, 'expected': False},
   { 'input': False, 'expected': False},
   { 'input': 'This is a description', 'expected': True},
   { 'input': 2,    'expected': True},
   { 'input': 2.0,  'expected': True},
   { 'input': [],   'expected': True},
   { 'input': {},   'expected': True}
])
class TestPropertyDefinitionDescription(unittest.TestCase):

    def test(self):
        raised = False

        try:
            PropertyDefinition(type='Test', required=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()