import unittest

from toscametrics.classes.definitions.attribute  import AttributeDefinition
from toscametrics.classes.definitions.schema     import SchemaDefinition
from toscametrics.parser.attributes_parser       import AttributesParser

class TestAttributesParserParse(unittest.TestCase):

    def testNone1(self):
        parser = AttributesParser()
        actual = parser.parse([])
        self.assertIsNone(actual, 'Test failed because expected None and got ' + str(actual) +'!') 

    def testNone2(self):
        parser = AttributesParser()
        actual = parser.parse(None)
        self.assertIsNone(actual, 'Test failed because expected None and got ' + str(actual) +'!') 

    def testValid(self):
        input = {'status': 'supported', 'key_schema': {'type': 'A'}, 'description': 'test', 'entry_schema': {'type': 'B'}, 'type': 'integer'}
        parser = AttributesParser()
        actual = parser.parse(input)
        expected = AttributeDefinition(
            type='integer', 
            description='test',
            status='supported',
            keySchema=SchemaDefinition(type='A'),
            entrySchema=SchemaDefinition(type='B')
        )

        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 
    
if __name__ == "__main__":
    unittest.main()