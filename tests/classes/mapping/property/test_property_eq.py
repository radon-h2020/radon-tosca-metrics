import unittest

from toscametrics.classes.mapping.property import PropertyMapping

class TestPropertyMappingEq(unittest.TestCase):

    def testEqual(self):
        p1 = PropertyMapping(mapping=['path1/path2/file.yaml'], value=1)
        p2 = PropertyMapping(mapping=['path1/path2/file.yaml'], value=1)
        self.assertEqual(p1, p2, 'Test failed because expected equality but actual is \'not equal\'!') 

    def testNotEqual(self):
        p1 = PropertyMapping(mapping=['path1/path2/file1.yaml'], value=1)
        p2 = PropertyMapping(mapping=['path1/path2/file2.yaml'], value=2)
        self.assertNotEqual(p1, p2, 'Test failed because expected not equal but actual is \'equal\'!') 
    
if __name__ == "__main__":
    unittest.main()