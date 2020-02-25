import unittest

from toscametrics.classes.definitions.attribute  import AttributeDefinition
from toscametrics.classes.definitions.capability import CapabilityDefinition
from toscametrics.classes.definitions.property   import PropertyDefinition

class TestCapabilityEq(unittest.TestCase):
    def testEqual(self):
        c1 = CapabilityDefinition(
             type='A',
             description='A description',
             properties={'p1':PropertyDefinition(type='Property 1 type'), 'p2':PropertyDefinition(type='Property 2 type')},
             attributes={'a1':AttributeDefinition(type='Attribute 1 type'), 'a2':AttributeDefinition(type='Attribute 2 type')},
             validSourceTypes=['source 1', 'source 2'],
             occurrences=[1, 'UNBOUNDED']
        )

        c2 = CapabilityDefinition(
             type='A',
             description='A description',
             properties={'p1':PropertyDefinition(type='Property 1 type'), 'p2':PropertyDefinition(type='Property 2 type')},
             attributes={'a1':AttributeDefinition(type='Attribute 1 type'), 'a2':AttributeDefinition(type='Attribute 2 type')},
             validSourceTypes=['source 1', 'source 2'],
             occurrences=[1, 'UNBOUNDED']
        )

        self.assertEqual(c1, c2, 'Test failed because expected equality but actual is \'not equal\'!') 


    def testNotEqual(self):
        c1 = CapabilityDefinition(
             type='A',
             description='A description',
             properties={'p1':PropertyDefinition(type='Property 1a type'), 'p2':PropertyDefinition(type='Property 2a type')},
             attributes={'a1':AttributeDefinition(type='Attribute 1a type'), 'a2':AttributeDefinition(type='Attribute 2a type')},
             validSourceTypes=['source 1', 'source 2'],
             occurrences=[1, 'UNBOUNDED']
        )

        c2 = CapabilityDefinition(
             type='B',
             description='A description',
             properties={'p1':PropertyDefinition(type='Property 1b type'), 'p2':PropertyDefinition(type='Property 2b type')},
             attributes={'a1':AttributeDefinition(type='Attribute 1b type'), 'a2':AttributeDefinition(type='Attribute 2b type')},
             occurrences=[1, 'UNBOUNDED']
        )

        self.assertNotEqual(c1, c2, 'Test failed because expected not equal but actual is \'equal\'!') 
    
if __name__ == "__main__":
    unittest.main()