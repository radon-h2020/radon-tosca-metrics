import unittest
from toscametrics.parser.conditions_parser import ConditionsParser
from toscametrics.classes.clauses.conditions import ConditionClause

class TestConditionsParserParseAll(unittest.TestCase):

    def testEmpty(self):
        input = {'node_types': {'fastconnect.nodes.ConstraintSample': {'properties': {'property_1': {'type': 'string'}}}}}
        parser = ConditionsParser()
        actual = parser.parseAll(input)
        self.assertEqual(actual, [], 'Test failed because expected and empty list and got ' + str(actual) +'!') 

    def testValid(self):
        input = {'node_types': {'fastconnect.nodes.ConstraintSample': {'properties': {'property_1': {'type': 'integer', 'condition': [{'or': [{'not': [{'my_attribute1': [{'equal': 'value1'}]}]}, {'not': [{'my_attribute2': [{'equal': 'value1'}]}]}]}]}, 'property_2': {'type': 'integer', 'condition': [{'or': [{'and': [{'protocol': {'equal': 'http'}}, {'port': {'equal': 80}}]}, {'and': [{'protocol': {'equal': 'https'}}, {'port': {'equal': 431}}]}]}]}}}}}
        parser = ConditionsParser()
        actual = parser.parseAll(input)
        
        clause1 = ConditionClause(
            pOr=[ConditionClause(pNot=[{'my_attribute1': [{'equal': 'value1'}]}]), ConditionClause(pNot=[{'my_attribute2': [{'equal': 'value1'}]}])]
        )

        clause2 = ConditionClause(
            pOr=[ConditionClause(pAnd=[{'protocol': {'equal': 'http'}}, {'port': {'equal': 80}}]), ConditionClause(pAnd=[{'protocol': {'equal': 'https'}}, {'port': {'equal': 431}}])]
        )

        expected = [clause1, clause2]

        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 
    
if __name__ == "__main__":
    unittest.main()