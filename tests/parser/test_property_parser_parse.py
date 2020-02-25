import unittest

from toscametrics.classes.clauses.constraints   import ConstraintClause
from toscametrics.classes.definitions.property  import PropertyDefinition
from toscametrics.classes.definitions.schema    import SchemaDefinition
from toscametrics.parser.properties_parser      import PropertiesParser

class TestPropertyParserParse(unittest.TestCase):

    def testNone1(self):
        parser = PropertiesParser()
        actual = parser.parse([])
        self.assertIsNone(actual, 'Test failed because expected None list and got ' + str(actual) +'!') 

    def testNone2(self):
        parser = PropertiesParser()
        actual = parser.parse(None)
        self.assertIsNone(actual, 'Test failed because expected None list and got ' + str(actual) +'!') 

    def testValid(self):
        input = {"type": "integer","description": "Number of CPUs requested for a software node instance.","default": 1,"required": True,"constraints": [{"valid_values": [1,2,4,8]}]}
        parser = PropertiesParser()
        actual = parser.parse(input)
        expected = PropertyDefinition(
            type='integer',
            description='Number of CPUs requested for a software node instance.',
            required=True,
            default=1,
            constraints=[ConstraintClause(validValues=[1, 2, 4, 8])]
        )
        
        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 

if __name__ == "__main__":
    unittest.main()