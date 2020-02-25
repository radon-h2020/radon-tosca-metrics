import unittest
from toscametrics.parser.constraints_parser import ConstraintsParser
from toscametrics.classes.clauses.constraints import ConstraintClause

class TestConstraintsParserParseAll(unittest.TestCase):

    def testEmpty1(self):
        input = {'node_types': {'fastconnect.nodes.ConstraintSample': {'properties': {'property_1': {'type': 'string'}}}}}
        parser = ConstraintsParser()
        actual = parser.parseAll(input)
        self.assertEqual(actual, [], 'Test failed because expected and empty list and got ' + str(actual) +'!') 

    def testEmpty2(self):
        input = {'constraints': None}
        parser = ConstraintsParser()
        actual = parser.parseAll(input)
        self.assertEqual(actual, [], 'Test failed because expected and empty list and got ' + str(actual) +'!') 


    def testValid(self):
        input = {'node_types': {'fastconnect.nodes.ConstraintSample': {'properties': {'property_1': {'type': 'string', 'constraints': [{'length': 6}]}, 'property_2': {'type': 'string', 'constraints': [{'min_length': 4}, {'max_length': 8}]}, 'property_3': {'type': 'integer', 'constraints': [{'in_range': [2, 10]}]}, 'property_4': {'type': 'integer', 'constraints': [{'valid_values': [2, 4, 6, 8, 16, 24, 32]}]}}}}}
        parser = ConstraintsParser()
        actual = parser.parseAll(input)
        
        clause1 = ConstraintClause(length=6)
        clause2 = ConstraintClause(minLength=4, maxLength=8)
        clause3 = ConstraintClause(inRange=[2, 10])
        clause4 = ConstraintClause(validValues=[2, 4, 6, 8, 16, 24, 32])

        expected = [clause1, clause2, clause3, clause4]

        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 
    
if __name__ == "__main__":
    unittest.main()