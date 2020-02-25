import unittest

from toscametrics.classes.clauses.constraints    import ConstraintClause
from toscametrics.classes.definitions.parameter  import ParameterDefinition
from toscametrics.classes.definitions.schema     import SchemaDefinition
from toscametrics.parser.parameters_parser       import ParametersParser

class TestPropertyParserParse(unittest.TestCase):

    def testNone1(self):
        parser = ParametersParser()
        actual = parser.parse([])
        self.assertIsNone(actual, 'Test failed because expected None list and got ' + str(actual) +'!') 

    def testNone2(self):
        parser = ParametersParser()
        actual = parser.parse(None)
        self.assertIsNone(actual, 'Test failed because expected None list and got ' + str(actual) +'!') 

    def testValid(self):
        input = {"description": "Number of CPUs requested for a software node instance.", "value": { "get_attribute": [ "my_server", "private_address" ] }, "default": 1,"required": True,"constraints": [{"valid_values": [1,2,4,8]}]}
        parser = ParametersParser()
        actual = parser.parse(input)
        expected = ParameterDefinition(
            description='Number of CPUs requested for a software node instance.',
            value={ "get_attribute": [ "my_server", "private_address" ]},
            required=True,
            default=1,
            constraints=[ConstraintClause(validValues=[1, 2, 4, 8])]
        )
        
        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 

if __name__ == "__main__":
    unittest.main()