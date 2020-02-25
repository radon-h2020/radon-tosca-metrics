import unittest

from toscametrics.classes.mapping.interface import InterfaceMapping

class TestInterfaceMappingEq(unittest.TestCase):

    def testEqual(self):
        i1 = InterfaceMapping(properties={'p1':'value'})
        i2 = InterfaceMapping(properties={'p1':'value'})
        self.assertEqual(i1, i2, 'Test failed because expected equality but actual is \'not equal\'!') 

    def testNotEqual(self):
        i1 = InterfaceMapping(properties={'p1':'value'})
        i2 = InterfaceMapping(properties={'p2':'value2'})
        self.assertNotEqual(i1, i2, 'Test failed because expected not equal but actual is \'equal\'!') 
    
if __name__ == "__main__":
    unittest.main()