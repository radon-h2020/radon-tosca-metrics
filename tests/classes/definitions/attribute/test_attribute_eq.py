import unittest

from toscametrics.classes.clauses.constraints    import ConstraintClause
from toscametrics.classes.definitions.attribute  import AttributeDefinition
from toscametrics.classes.definitions.schema     import SchemaDefinition

class TestAttributeEq(unittest.TestCase):

    def testEqual(self):
        a1 = AttributeDefinition(
             type='A type',
             description='A description',
             status='active',
             keySchema = SchemaDefinition(type='B'),
             entrySchema = SchemaDefinition(type='B')
        )

        a2 = AttributeDefinition(
             type='A type',
             description='A description',
             status='active',
             keySchema = SchemaDefinition(type='B'),
             entrySchema = SchemaDefinition(type='B')
        )

        self.assertEqual(a1, a2, 'Test failed because expected equality but actual is \'not equal\'!') 


    def testNotEqual(self):
        a1 = AttributeDefinition(
             type='A type',
             description='A description',
             status='active',
             keySchema = SchemaDefinition(type='C'),
             entrySchema = SchemaDefinition(type='C')
        )

        a2 = AttributeDefinition(
             type='B type',
             description='A description',
             status='inactive',
             keySchema = SchemaDefinition(type='D'),
             entrySchema = SchemaDefinition(type='D')
        )

        self.assertNotEqual(a1, a2, 'Test failed because expected not equal but actual is \'equal\'!') 
    
if __name__ == "__main__":
    unittest.main()