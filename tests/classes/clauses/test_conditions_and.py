import unittest
from parameterized import parameterized_class

import toscametrics.classes.clauses.conditions as conditions

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': [],   'expected': False},
   { 'input': [{'protocol': { 'equal': 'http' }}], 'expected': False},
   { 'input': conditions.ConditionClause(pOr=[{'protocol': { 'equal': 'http' }}]), 'expected': False},
   { 'input': 2,  'expected': True},
   { 'input': 2.0,  'expected': True},
   { 'input': 'not a list', 'expected': True},
   { 'input': {},   'expected': True}
])
class TestConditionClauseAnd(unittest.TestCase):

    def test(self):
        raised = False

        try:
            conditions.ConditionClause(pAnd=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()