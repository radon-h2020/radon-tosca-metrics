import unittest
from toscametrics.classes.definitions.attribute import AttributeDefinition
from toscametrics.classes.definitions.property  import PropertyDefinition
from toscametrics.classes.types.group           import GroupType

class TestCapabilityTypeEq(unittest.TestCase):

    def testEqual(self):
        g1 = GroupType(
            properties={'p1':PropertyDefinition(type='tosca.properties.A')},
            attributes={'a1':AttributeDefinition(type='tosca.attributes.A')},
            members=['string 1', 'string 2']
        )

        g2 = GroupType(
            properties={'p1':PropertyDefinition(type='tosca.properties.A')},
            attributes={'a1':AttributeDefinition(type='tosca.attributes.A')},
            members=['string 1', 'string 2']
        )

        self.assertEqual(g1, g2, 'Test failed because expected equality but actual is \'not equal\'!') 


    def testNotEqual(self):
        g1 = GroupType(
            properties={'p1':PropertyDefinition(type='tosca.properties.A')},
            attributes={'a1':AttributeDefinition(type='tosca.attributes.A')},
            members=['string 1', 'string 2']
        )

        g2 = GroupType(
            properties={'p1':PropertyDefinition(type='tosca.properties.B')},
            attributes={'a1':AttributeDefinition(type='tosca.attributes.B')},
            members=['string 3', 'string 4']
        )

        self.assertNotEqual(g1, g2, 'Test failed because expected not equal but actual is \'equal\'!') 
    
if __name__ == "__main__":
    unittest.main()