import unittest

from toscametrics.classes.clauses.constraints import ConstraintClause
from toscametrics.classes.definitions.schema  import SchemaDefinition

class TestSchemaDefinitionEq(unittest.TestCase):

    def testEqual(self):
        s1 = SchemaDefinition(
             type='A type',
             description='A description',
             constraints=[ConstraintClause(equal=2)],
             keySchema = SchemaDefinition(type='B'),
             entrySchema = SchemaDefinition(type='B')
        )

        s2 = SchemaDefinition(
             type='A type',
             description='A description',
             constraints=[ConstraintClause(equal=2)],
             keySchema = SchemaDefinition(type='B'),
             entrySchema = SchemaDefinition(type='B')
        )

        self.assertEqual(s1, s2, 'Test failed because expected equality but actual is \'not equal\'!') 


    def testNotEqual(self):
        s1 = SchemaDefinition(
             type='A type',
             description='A description',
             constraints=[ConstraintClause(equal=2)],
             keySchema = SchemaDefinition(type='C'),
             entrySchema = SchemaDefinition(type='C')
        )

        s2 = SchemaDefinition(
             type='B type',
             description='A description',
             constraints=[ConstraintClause(equal=2)],
             keySchema = SchemaDefinition(type='D'),
             entrySchema = SchemaDefinition(type='D')
        )

        self.assertNotEqual(s1, s2, 'Test failed because expected not equal but actual is \'equal\'!') 
    
if __name__ == "__main__":
    unittest.main()