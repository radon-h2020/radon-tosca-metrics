import unittest

from toscametrics.classes.filters.node         import NodeFilter
from toscametrics.classes.mapping.attribute    import AttributeMapping
from toscametrics.classes.mapping.capability   import CapabilityMapping
from toscametrics.classes.mapping.interface    import InterfaceMapping
from toscametrics.classes.mapping.property     import PropertyMapping
from toscametrics.classes.mapping.requirement  import RequirementMapping
from toscametrics.classes.mapping.substitution import SubstitutionMapping

class TestSubstitutionMappingEq(unittest.TestCase):

    def testEqual(self):
        s1 = SubstitutionMapping(
                nodeType='nodes.types.A',
                substitutionFilter=NodeFilter(),
                properties={'property_1':PropertyMapping()},
                attributes={'attribute_1':AttributeMapping()},
                capabilities={'capability_1':CapabilityMapping()},
                requirements={'requirement_1':RequirementMapping()},
                interfaces={'interface_1':InterfaceMapping()}
            )

        s2 = SubstitutionMapping(
                nodeType='nodes.types.A',
                substitutionFilter=NodeFilter(),
                properties={'property_1':PropertyMapping()},
                attributes={'attribute_1':AttributeMapping()},
                capabilities={'capability_1':CapabilityMapping()},
                requirements={'requirement_1':RequirementMapping()},
                interfaces={'interface_1':InterfaceMapping()}
            )
            
        self.assertEqual(s1, s2, 'Test failed because expected equality but actual is \'not equal\'!') 

    def testNotEqual(self):
        s1 = SubstitutionMapping(
                nodeType='nodes.types.A',
                substitutionFilter=NodeFilter(),
                properties={'property_1':PropertyMapping()},
                attributes={'attribute_1':AttributeMapping()},
                capabilities={'capability_1':CapabilityMapping()},
                requirements={'requirement_1':RequirementMapping()},
                interfaces={'interface_1':InterfaceMapping()}
            )

        s2 = SubstitutionMapping(
                nodeType='nodes.types.B',
                properties={'property_1':PropertyMapping()},
                attributes={'attribute_1':AttributeMapping()},
                capabilities={'capability_2':CapabilityMapping()},
                requirements={'requirement_2':RequirementMapping()},
                interfaces={'interface_2':InterfaceMapping()}
            )

        self.assertNotEqual(s1, s2, 'Test failed because expected not equal but actual is \'equal\'!') 
    
if __name__ == "__main__":
    unittest.main()