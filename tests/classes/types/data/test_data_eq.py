import unittest
from toscametrics.classes.clauses.constraints  import ConstraintClause
from toscametrics.classes.definitions.property import PropertyDefinition
from toscametrics.classes.definitions.schema   import SchemaDefinition
from toscametrics.classes.types.data           import DataType

class TestCapabilityTypeEq(unittest.TestCase):

    def testEqual(self):
        g1 = DataType(
            properties={'p1':PropertyDefinition(type='tosca.properties.A')},
            constraints=[ConstraintClause(equal=5), ConstraintClause(length=1)],
            keySchema=SchemaDefinition(type='key_schema.examples.A'),
            entrySchema=SchemaDefinition(type='entry_schema.examples.A')
        )

        g2 = DataType(
            properties={'p1':PropertyDefinition(type='tosca.properties.A')},
            constraints=[ConstraintClause(equal=5), ConstraintClause(length=1)],
            keySchema=SchemaDefinition(type='key_schema.examples.A'),
            entrySchema=SchemaDefinition(type='entry_schema.examples.A')
        )

        self.assertEqual(g1, g2, 'Test failed because expected equality but actual is \'not equal\'!') 


    def testNotEqual(self):
        g1 = DataType(
            properties={'p1':PropertyDefinition(type='tosca.properties.A')},
            constraints=[ConstraintClause(equal=5), ConstraintClause(length=1)],
            keySchema=SchemaDefinition(type='key_schema.examples.A'),
            entrySchema=SchemaDefinition(type='entry_schema.examples.A')
        )

        g2 = DataType(
            properties={'p1':PropertyDefinition(type='tosca.properties.B')},
            constraints=[ConstraintClause(equal=2), ConstraintClause(length=5)],
            keySchema=SchemaDefinition(type='key_schema.examples.B'),
            entrySchema=SchemaDefinition(type='entry_schema.examples.B')
        )

        self.assertNotEqual(g1, g2, 'Test failed because expected not equal but actual is \'equal\'!') 
    
if __name__ == "__main__":
    unittest.main()