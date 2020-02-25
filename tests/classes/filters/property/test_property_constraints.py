import unittest
from parameterized import parameterized_class

from toscametrics.classes.clauses.constraints import ConstraintClause
from toscametrics.classes.filters.property    import PropertyFilter

@parameterized_class([
   { 'input': [], 'expected': False},
   { 'input': [ConstraintClause(equal=5)], 'expected': False},
   { 'input': [ConstraintClause(equal=5), 'string'], 'expected': True},
   { 'input': None, 'expected': True},
   { 'input': 'name', 'expected': True},
   { 'input': True, 'expected': True},
   { 'input': 2, 'expected': True},
   { 'input': 2.0, 'expected': True},
   { 'input': {}, 'expected': True}
])
class TestPropertyFilterConstraints(unittest.TestCase):

    def test(self):
        raised = False

        try:
            PropertyFilter(name='test', constraints=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()