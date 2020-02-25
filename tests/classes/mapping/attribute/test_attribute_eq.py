import unittest

from toscametrics.classes.mapping.attribute import AttributeMapping


class TestAttributeMappingEq(unittest.TestCase):

    def testEqual(self):
        a1 = AttributeMapping(mapping=['path1/path2/file.yaml'])
        a2 = AttributeMapping(mapping=['path1/path2/file.yaml'])
        self.assertEqual(a1, a2, 'Test failed because expected equality but actual is \'not equal\'!') 

    def testNotEqual(self):
        a1 = AttributeMapping(mapping=['path1/path2/file.yaml'])
        a2 = AttributeMapping(mapping=['pathA/pathB/fileAB.yaml'])
        self.assertNotEqual(a1, a2, 'Test failed because expected not equal but actual is \'equal\'!') 
    
if __name__ == "__main__":
    unittest.main()