import unittest
from parameterized import parameterized_class

import toscametrics.classes.clauses.constraints as constraints

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': [], 'expected': False},
   { 'input': [1, 4, 3], 'expected': False},
   { 'input': ['item 1'], 'expected': True},
   { 'input': 2, 'expected': True},
   { 'input': 'not a list', 'expected': True}
])
class TestConstraintClauseValidValues(unittest.TestCase):

    def test(self):
        raised = False

        try:
            constraints.ConstraintClause(validValues=self.input)
        except Exception:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()