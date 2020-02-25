import unittest
from toscametrics.classes.types.range_type import RangeType

class TestRangeTypeInit(unittest.TestCase):

    def testTypeError1(self):
        with self.assertRaises(TypeError):
            RangeType(None, None)
    
    def testTypeError2(self):
        with self.assertRaises(TypeError):
            RangeType(None, 1)
    
    def testTypeError3(self):
        with self.assertRaises(TypeError):
            RangeType(1, None)    
    
    def testTypeError4(self):
        with self.assertRaises(TypeError):
            RangeType(1, None)    

    def testTypeError5(self):
        with self.assertRaises(TypeError):
            RangeType(1, 'NOT UNBOUNDED')
            
    def testValueError1(self):
        with self.assertRaises(ValueError):
            RangeType(10, 5)

    def testValid1(self):
        range = RangeType(1, 2)
        self.assertGreaterEqual(range.upperBound, range.lowerBound)
   
    def testValid2(self):
        range = RangeType(1, 1)
        self.assertGreaterEqual(range.upperBound, range.lowerBound)   
    
    def testValid3(self):
        try:
            RangeType(1, 'UNBOUNDED')
        except Exception:
            self.fail("Raised Exception unexpectedly!")

if __name__ == "__main__":
    unittest.main()