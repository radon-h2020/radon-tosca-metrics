import unittest

from toscametrics.classes.clauses.constraints    import ConstraintClause
from toscametrics.classes.definitions.parameter  import ParameterDefinition
from toscametrics.classes.definitions.schema     import SchemaDefinition
from toscametrics.parser.parameters_parser       import ParametersParser

class TestPropertyParserParseAll(unittest.TestCase):

    def testEmpty1(self):
        parser = ParametersParser()
        actual = parser.parseAll([])
        self.assertEqual(actual, [], 'Test failed because expected empty list and got ' + str(actual) +'!') 

    def testEmpty2(self):
        input = {'node_type': {'type': 'MySQL', 'attributes': [{'attribute_1':{'type': 'string'}}]}}
        parser = ParametersParser()
        actual = parser.parseAll(input)
        self.assertEqual(actual, [], 'Test failed because expected empty list and got ' + str(actual) +'!') 

    def testValid(self):
        input = {"properties": {"num_cpus": {"description": "Number of CPUs requested for a software node instance.", "value": { "get_attribute": [ "my_server", "private_address" ] }, "default": 1,"required": True,"constraints": [{"valid_values": [1,2,4,8]}]}}}
        parser = ParametersParser()
        actual = parser.parseAll(input)
        expected = []
        expected.append(ParameterDefinition(
                            description='Number of CPUs requested for a software node instance.',
                            value={ "get_attribute": [ "my_server", "private_address" ]},
                            required=True,
                            default=1,
                            constraints=[ConstraintClause(validValues=[1, 2, 4, 8])]
                        )
        )
        
        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 

if __name__ == "__main__":
    unittest.main()