import unittest
from toscametrics.parser.constraints_parser import ConstraintsParser
from toscametrics.classes.clauses.constraints import ConstraintClause

class TestConstraintsParserParse(unittest.TestCase):

    def testNone1(self):
        parser = ConstraintsParser()
        actual = parser.parse(None)
        self.assertIsNone(actual, 'Test failed because expected None and got ' + str(actual) +'!') 

    def testNone2(self):
        parser = ConstraintsParser()
        actual = parser.parse([])
        self.assertIsNone(actual, 'Test failed because expected None and got ' + str(actual) +'!') 

    def testValid1(self):
        input = [{'length': 6}, {'min_length': 4}, {'max_length': 8},{'in_range': [2, 10]}, {'valid_values': [2, 4, 6, 8, 16, 24, 32]}]
        parser = ConstraintsParser()
        actual = parser.parse(input)
        
        expected = ConstraintClause(length=6,
                                   minLength=4, 
                                   maxLength=8,
                                   inRange=[2, 10],
                                   validValues=[2, 4, 6, 8, 16, 24, 32]
                                   )

        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 
    
    def testValid2(self):
        input = [{'valid_values': [1, 2, 4, 8]}]
        parser = ConstraintsParser()
        actual = parser.parse(input)
        expected = ConstraintClause(validValues=[1, 2, 4, 8])

        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 
    

if __name__ == "__main__":
    unittest.main()