import unittest
from toscametrics.classes.definitions.attribute import AttributeDefinition
from toscametrics.classes.definitions.property  import PropertyDefinition
from toscametrics.classes.types.capability      import CapabilityType

class TestCapabilityTypeEq(unittest.TestCase):

    def testEqual(self):
        c1 = CapabilityType(
            properties={'p1':PropertyDefinition(type='tosca.properties.A')},
            attributes={'a1':AttributeDefinition(type='tosca.attributes.A')},
            validSourceTypes=['string 1', 'string 2']
        )

        c2 = CapabilityType(
            properties={'p1':PropertyDefinition(type='tosca.properties.A')},
            attributes={'a1':AttributeDefinition(type='tosca.attributes.A')},
            validSourceTypes=['string 1', 'string 2']
        )

        self.assertEqual(c1, c2, 'Test failed because expected equality but actual is \'not equal\'!') 


    def testNotEqual(self):
        c1 = CapabilityType(
            properties={'p1':PropertyDefinition(type='tosca.properties.A')},
            attributes={'a1':AttributeDefinition(type='tosca.attributes.A')},
            validSourceTypes=['string 1', 'string 2']
        )

        c2 = CapabilityType(
            properties={'p1':PropertyDefinition(type='tosca.properties.B')},
            attributes={'a1':AttributeDefinition(type='tosca.attributes.B')},
            validSourceTypes=['string 3', 'string 4']
        )

        self.assertNotEqual(c1, c2, 'Test failed because expected not equal but actual is \'equal\'!') 
    
if __name__ == "__main__":
    unittest.main()