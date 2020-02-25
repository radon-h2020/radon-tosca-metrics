import unittest
from parameterized import parameterized_class

from toscametrics.classes.definitions.property import PropertyDefinition

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': {}, 'expected': False},
   { 'input': {'input':'string', 'key':'string_value'}, 'expected': False},
   { 'input': {'input': 1}, 'expected': True},
   { 'input': 'This is a type', 'expected': True},
   { 'input': 2, 'expected': True},
   { 'input': 2.0, 'expected': True},
   { 'input': [], 'expected': True},
])
class TestPropertyDefinitionType(unittest.TestCase):

    def test(self):
        raised = False

        try:
            PropertyDefinition(type='Test', metadata=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()