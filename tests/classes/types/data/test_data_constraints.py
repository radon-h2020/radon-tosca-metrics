import unittest
from parameterized import parameterized_class

from toscametrics.classes.clauses.constraints import ConstraintClause
from toscametrics.classes.types.group import GroupType
from toscametrics.classes.types.data import DataType

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': [], 'expected': False},
   { 'input': [ConstraintClause(equal=5), ConstraintClause(length=10)], 'expected': False},
   { 'input': [ConstraintClause(equal=5), 'string 1', 1], 'expected': True},
   { 'input': True, 'expected': True},
   { 'input': 2, 'expected': True},
   { 'input': 2.0, 'expected': True},
   { 'input': {}, 'expected': True}
])
class TestDataTypeConstraints(unittest.TestCase):

    def test(self):
        raised = False

        try:
            DataType(constraints=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()