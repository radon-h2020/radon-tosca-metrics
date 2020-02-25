import unittest

from toscametrics.classes.types.range_type import RangeType

class TestRangeTypeEq(unittest.TestCase):

    def testEqual(self):
        r1 = RangeType(lower=1, upper=2)
        r2 = RangeType(lower=1, upper=2)

        self.assertEqual(r1, r2, 'Test failed because expected equality but actual is \'not equal\'!') 


    def testNotEqual(self):
        r1 = RangeType(lower=1, upper=2)
        r2 = RangeType(lower=1, upper='UNBOUNDED')

        self.assertNotEqual(r1, r2, 'Test failed because expected not equal but actual is \'equal\'!') 
    
if __name__ == "__main__":
    unittest.main()