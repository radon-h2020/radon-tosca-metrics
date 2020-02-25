import unittest
from toscametrics.parser.conditions_parser import ConditionsParser
from toscametrics.classes.clauses.conditions import ConditionClause

class TestConditionsParserParse(unittest.TestCase):

    def testNone1(self):
        parser = ConditionsParser()
        actual = parser.parse(None)
        self.assertIsNone(actual, 'Test failed because expected None and got ' + str(actual) +'!') 

    def testNone2(self):
        parser = ConditionsParser()
        actual = parser.parse([])
        self.assertIsNone(actual, 'Test failed because expected None and got ' + str(actual) +'!') 

    def testValid(self):
        input = [{'or': [{'not': [{'my_attribute1': [{'equal': 'value1'}]}]}, {'not': [{'my_attribute2': [{'equal': 'value1'}]}]}]}]
        parser = ConditionsParser()
        actual = parser.parse(input)
        
        expected = ConditionClause(
            pOr=[ConditionClause(pNot=[{'my_attribute1': [{'equal': 'value1'}]}]), ConditionClause(pNot=[{'my_attribute2': [{'equal': 'value1'}]}])]
        )

        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 
    
if __name__ == "__main__":
    unittest.main()