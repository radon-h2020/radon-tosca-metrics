import unittest
from parameterized import parameterized_class

from toscametrics.classes.definitions.parameter import ParameterDefinition

@parameterized_class([
   { 'input': 'This is a type', 'expected': False},
   { 'input': None, 'expected': False},
   { 'input': 2, 'expected': True},
   { 'input': 2.0, 'expected': True},
   { 'input': [], 'expected': True},
   { 'input': {}, 'expected': True}
])
class TestParameterDefinitionType(unittest.TestCase):

    def test(self):
        raised = False

        try:
            ParameterDefinition(type=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()