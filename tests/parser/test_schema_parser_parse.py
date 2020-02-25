import unittest

from toscametrics.classes.clauses.constraints import ConstraintClause
from toscametrics.classes.definitions.schema  import SchemaDefinition
from toscametrics.parser.schema_parser        import SchemaParser

class TestSchemaParserParse(unittest.TestCase):

    def testNone1(self):
        parser = SchemaParser()
        actual = parser.parse([])
        self.assertIsNone(actual, 'Test failed because expected None and got ' + str(actual) +'!') 

    def testNone2(self):
        input = {'node_type': {'type': 'MySQL', 'properties': [{'property_1':{'type': 'string'}}]}}
        parser = SchemaParser()
        actual = parser.parse(input)
        self.assertIsNone(actual, 'Test failed because expected None and got ' + str(actual) +'!') 

    def testValid(self):
        input = {'type': 'A', 'description': 'Description', 'constraints': [{'pattern': "^(http|https|ftp)://.+/.*$"}], 'key_schema':{'type': 'B', 'description': 'Description B', 'constraints': [{'min_length': 0}, {'max_length':5}]}, 'entry_schema':{'type': 'C'}}
        parser = SchemaParser()
        actual = parser.parse(input)
        expected = SchemaDefinition(
            type='A', 
            description='Description',
            constraints=[ConstraintClause(pattern="^(http|https|ftp)://.+/.*$")],
            keySchema=SchemaDefinition(type='B',
                description='Description B',
                constraints=[ConstraintClause(minLength=0, maxLength=5)]
            ),
            entrySchema=SchemaDefinition(type='C')
        )

        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 
    
if __name__ == "__main__":
    unittest.main()