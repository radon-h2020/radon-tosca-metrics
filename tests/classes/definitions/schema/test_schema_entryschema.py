import unittest
from parameterized import parameterized_class

from toscametrics.classes.definitions.schema import SchemaDefinition

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': SchemaDefinition(type='A'), 'expected': False},
   { 'input': 'This is a string', 'expected': True},
   { 'input': 2, 'expected': True},
   { 'input': 2.0, 'expected': True},
   { 'input': [], 'expected': True},
   { 'input': {}, 'expected': True}
])
class TestSchemaDefinitionEntrySchema(unittest.TestCase):

    def test(self):
        raised = False

        try:
            SchemaDefinition(type='Test', entrySchema=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()