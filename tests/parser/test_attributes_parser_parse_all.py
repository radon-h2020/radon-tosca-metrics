import unittest

from toscametrics.classes.definitions.attribute  import AttributeDefinition
from toscametrics.classes.definitions.schema     import SchemaDefinition
from toscametrics.parser.attributes_parser       import AttributesParser

class TestAttributesParserParseAll(unittest.TestCase):

    def testEmpty1(self):
        parser = AttributesParser()
        actual = parser.parseAll([])
        self.assertEqual(actual, [], 'Test failed because expected empty list and got ' + str(actual) +'!') 

    def testEmpty2(self):
        input = {'node_type': {'type': 'MySQL', 'properties': [{'property_1':{'type': 'string'}}]}}
        parser = AttributesParser()
        actual = parser.parseAll(input)
        self.assertEqual(actual, [], 'Test failed because expected empty list and got ' + str(actual) +'!') 

    def testValid(self):
        input = {'node_types': {'io.test.nodes.Welcome': {'attributes': {'actual_cpus': {'status': 'supported', 'key_schema': {'type': 'A'}, 'description': 'test', 'entry_schema': {'type': 'B'}, 'type': 'integer'}}}}}
        parser = AttributesParser()
        actual = parser.parseAll(input)
        expected = []
        expected.append(
            AttributeDefinition(
                type='integer', 
                description='test',
                status='supported',
                keySchema=SchemaDefinition(type='A'),
                entrySchema=SchemaDefinition(type='B')
            )
        )

        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 

if __name__ == "__main__":
    unittest.main()