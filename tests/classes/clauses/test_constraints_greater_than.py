import unittest
from parameterized import parameterized_class

import toscametrics.classes.clauses.constraints as constraints

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': 2, 'expected': False},
   { 'input': 2.0, 'expected': True},
   { 'input': 'not a number', 'expected': True},
   { 'input': [], 'expected': True},
   { 'input': {}, 'expected': True}
])
class TestConstraintClauseLessThan(unittest.TestCase):

    def test(self):
        raised = False

        try:
            constraints.ConstraintClause(lessThan=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()