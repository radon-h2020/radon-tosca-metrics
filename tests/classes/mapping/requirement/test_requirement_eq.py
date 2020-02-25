import unittest

from toscametrics.classes.mapping.requirement import RequirementMapping

class TestRequirementMappingEq(unittest.TestCase):

    def testEqual(self):
        r1 = RequirementMapping(mapping=['templates.node.A', 'capabilities.nodeA'], properties={'p1':'value'}, attributes={'a1':'value'})
        r2 = RequirementMapping(mapping=['templates.node.A', 'capabilities.nodeA'], properties={'p1':'value'}, attributes={'a1':'value'})
        self.assertEqual(r1, r2, 'Test failed because expected equality but actual is \'not equal\'!') 

    def testNotEqual(self):
        r1 = RequirementMapping(mapping=['templates.node.A', 'capabilities.nodeA'], properties={'p1':'value'}, attributes={'a1':'value'})
        r2 = RequirementMapping(mapping=['templates.node.B', 'capabilities.nodeB'], properties={'p2':'value2'}, attributes={'aa':'value2'})
        self.assertNotEqual(r1, r2, 'Test failed because expected not equal but actual is \'equal\'!') 
    
if __name__ == "__main__":
    unittest.main()