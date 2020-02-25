import unittest
from parameterized import parameterized_class

import toscametrics.classes.clauses.constraints as constraints

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': 'a pattern', 'expected': False},
   { 'input': 2, 'expected': True},
   { 'input': 2.0, 'expected': True},
   { 'input': [], 'expected': True},
   { 'input': {}, 'expected': True}
])
class TestConstraintClauseSchema(unittest.TestCase):

    def test(self):
        raised = False

        try:
            constraints.ConstraintClause(schema=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()