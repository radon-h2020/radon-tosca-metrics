import unittest
from parameterized import parameterized_class

import toscametrics.classes.clauses.constraints as constraints

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': [1, 2], 'expected': False},
   { 'input': [], 'expected': True},
   { 'input': [1, 2, 3], 'expected': True},
   { 'input': ['item 1', 'item 2'], 'expected': True},
   { 'input': 2, 'expected': True},
   { 'input': 'not a list', 'expected': True}
])
class TestConstraintClauseInRange(unittest.TestCase):

    def test(self):
        raised = False

        try:
            constraints.ConstraintClause(inRange=self.input)
        except Exception:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()