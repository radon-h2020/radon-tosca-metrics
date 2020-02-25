import unittest
from parameterized import parameterized_class

from toscametrics.classes.clauses.constraints import ConstraintClause
from toscametrics.classes.definitions.schema import SchemaDefinition

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': [], 'expected': False},
   { 'input': [ConstraintClause(equal=2), ConstraintClause(minLength=0, maxLength=5)], 'expected': False},
   { 'input': 2, 'expected': True},
   { 'input': 2.0, 'expected': True},
   { 'input': [1, 2], 'expected': True},
   { 'input': {}, 'expected': True}
])
class TestSchemaDefinitionConstraints(unittest.TestCase):

    def test(self):
        raised = False

        try:
            SchemaDefinition(type='Test', constraints=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()