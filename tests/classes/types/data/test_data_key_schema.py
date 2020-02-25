import unittest
from parameterized import parameterized_class

from toscametrics.classes.definitions.schema import SchemaDefinition
from toscametrics.classes.types.data         import DataType

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': SchemaDefinition(type='schema.examples.A'), 'expected': False},
   { 'input': True, 'expected': True},
   { 'input': 2, 'expected': True},
   { 'input': 2.0, 'expected': True},
   { 'input': {}, 'expected': True},
   { 'input': [], 'expected': True}
])
class TestDataTypeProperties(unittest.TestCase):

    def test(self):
        raised = False

        try:
            DataType(keySchema=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()