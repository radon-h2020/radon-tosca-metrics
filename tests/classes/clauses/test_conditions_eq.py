import unittest

import toscametrics.classes.clauses.conditions as conditions

class TestConditionClauseEq(unittest.TestCase):

    def testEqual1(self):
        c1 = conditions.ConditionClause(
             pAnd=[{'and_attribute': { 'equal': 'and_value'}}],
             pOr=[{'or_attribute': [{'equal': 'or_value'}]}],
             pNot=[{'not_attribute': [{'equal': 'not_value'}]}],
             pAssert=[{'assert_attribute': [{'equal': 'assert_value'}]}]
        )

        c2 = conditions.ConditionClause(
             pAnd=[{'and_attribute': { 'equal': 'and_value'}}],
             pOr=[{'or_attribute': [{'equal': 'or_value'}]}],
             pNot=[{'not_attribute': [{'equal': 'not_value'}]}],
             pAssert=[{'assert_attribute': [{'equal': 'assert_value'}]}]
        )

        self.assertEqual(c1, c2, 'Test failed because expected equality but actual is \'not equal\'!') 


    def testEqual2(self):
        c1 = conditions.ConditionClause(
             pAnd=conditions.ConditionClause(pNot=[{'protocol': { 'equal': 'http' }}]),
             pOr=conditions.ConditionClause(pNot=[{'protocol': { 'equal': 'http' }}]),
             pNot=[{'not_attribute': [{'equal': 'not_value'}]}],
             pAssert=[{'assert_attribute': [{'equal': 'assert_value'}]}]
        )

        c2 = conditions.ConditionClause(
             pAnd=conditions.ConditionClause(pNot=[{'protocol': { 'equal': 'http' }}]),
             pOr=conditions.ConditionClause(pNot=[{'protocol': { 'equal': 'http' }}]),
             pNot=[{'not_attribute': [{'equal': 'not_value'}]}],
             pAssert=[{'assert_attribute': [{'equal': 'assert_value'}]}]
        )

        self.assertEqual(c1, c2, 'Test failed because expected equality but actual is \'not equal\'!') 
    

    def testNotEqual1(self):
        c1 = conditions.ConditionClause(
             pAnd=[{'and_attribute_1': { 'equal': 'and_value'}}],
             pOr=[{'or_attribute_1': [{'equal': 'or_value'}]}],
             pNot=[{'not_attribute_1': [{'equal': 'not_value'}]}],
             pAssert=[{'assert_attribute_1': [{'equal': 'assert_value'}]}]
        )

        c2 = conditions.ConditionClause(
             pAnd=[{'and_attribute_2': { 'equal': 'and_value'}}],
             pOr=[{'or_attribute_2': [{'equal': 'or_value'}]}],
             pNot=[{'not_attribute_2': [{'equal': 'not_value'}]}],
             pAssert=[{'assert_attribute_2': [{'equal': 'assert_value'}]}]
        )

        self.assertNotEqual(c1, c2, 'Test failed because expected not equal but actual is \'equal\'!') 
    
    def testNotEqual2(self):
        c1 = conditions.ConditionClause(
             pAnd=conditions.ConditionClause(pNot=[{'protocol': { 'equal': 'http' }}]),
             pOr=[{'or_attribute_1': [{'equal': 'or_value'}]}],
             pNot=[{'not_attribute_1': [{'equal': 'not_value'}]}],
             pAssert=[{'assert_attribute_1': [{'equal': 'assert_value'}]}]
        )

        c2 = conditions.ConditionClause(
             pAnd=[{'and_attribute_2': { 'equal': 'and_value'}}],
             pOr=conditions.ConditionClause(pNot=[{'protocol': { 'equal': 'http' }}]),
             pNot=[{'not_attribute_2': [{'equal': 'not_value'}]}],
             pAssert=[{'assert_attribute_2': [{'equal': 'assert_value'}]}]
        )

        self.assertNotEqual(c1, c2, 'Test failed because expected not equal but actual is \'equal\'!') 
    
if __name__ == "__main__":
    unittest.main()