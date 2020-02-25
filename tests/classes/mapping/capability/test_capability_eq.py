import unittest

from toscametrics.classes.mapping.capability import CapabilityMapping

class TestPropertyMappingEq(unittest.TestCase):

    def testEqual(self):
        c1 = CapabilityMapping(mapping=['templates.node.A', 'capabilities.nodeA'], properties={'p1':'value'}, attributes={'a1':'value'})
        c2 = CapabilityMapping(mapping=['templates.node.A', 'capabilities.nodeA'], properties={'p1':'value'}, attributes={'a1':'value'})
        self.assertEqual(c1, c2, 'Test failed because expected equality but actual is \'not equal\'!') 

    def testNotEqual(self):
        c1 = CapabilityMapping(mapping=['templates.node.A', 'capabilities.nodeA'], properties={'p1':'value'}, attributes={'a1':'value'})
        c2 = CapabilityMapping(mapping=['templates.node.B', 'capabilities.nodeB'], properties={'p2':'value2'}, attributes={'aa':'value2'})
        self.assertNotEqual(c1, c2, 'Test failed because expected not equal but actual is \'equal\'!') 
    
if __name__ == "__main__":
    unittest.main()