import unittest
from parameterized import parameterized_class

from toscametrics.classes.definitions.operation_implementation import OperationImplementationDefinition

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': 'inline string', 'expected': False},
   { 'input': [], 'expected': True},
   { 'input': True, 'expected': True},
   { 'input': 2, 'expected': True},
   { 'input': 2.0, 'expected': True},
   { 'input': {}, 'expected': True}
])
class TestOperationImplementationDefinitionOperationHost(unittest.TestCase):

    def test(self):
        raised = False

        try:
            OperationImplementationDefinition(operationHost=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()