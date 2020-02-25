import unittest

from toscametrics.classes.clauses.constraints    import ConstraintClause
from toscametrics.classes.definitions.property   import PropertyDefinition
from toscametrics.classes.definitions.schema     import SchemaDefinition

class TestPropertyEq(unittest.TestCase):

    def testEqual(self):
        p1 = PropertyDefinition(
             type='A type',
             description='A description',
             required=True,
             status='supported',
             constraints=[ConstraintClause(equal=1), ConstraintClause(length=10)],
             keySchema = SchemaDefinition(type='B'),
             entrySchema = SchemaDefinition(type='B'),
             externalSchema='external schema',
             metadata={'input':'string', 'key':'string_value'}
        )

        p2 = PropertyDefinition(
             type='A type',
             description='A description',
             status='supported',
             required=True,
             constraints=[ConstraintClause(equal=1), ConstraintClause(length=10)],
             keySchema = SchemaDefinition(type='B'),
             entrySchema = SchemaDefinition(type='B'),
             externalSchema='external schema',
             metadata={'input':'string', 'key':'string_value'}
        )

        self.assertEqual(p1, p2, 'Test failed because expected equality but actual is \'not equal\'!') 


    def testNotEqual(self):
        p1 = PropertyDefinition(
             type='A type',
             description='A description',
             status='unsupported',
             constraints=[ConstraintClause(equal=1), ConstraintClause(length=10)],
             keySchema = SchemaDefinition(type='C'),
             entrySchema = SchemaDefinition(type='C')
        )

        p2 = PropertyDefinition(
             type='B type',
             description='A description',
             required=False,
             constraints=[ConstraintClause(equal=1), ConstraintClause(length=10)],
             keySchema = SchemaDefinition(type='D'),
             entrySchema = SchemaDefinition(type='D')
        )

        self.assertNotEqual(p1, p2, 'Test failed because expected not equal but actual is \'equal\'!') 
    
if __name__ == "__main__":
    unittest.main()