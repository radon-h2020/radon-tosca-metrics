import unittest

from toscametrics.classes.assignments.capability import CapabilityAssignment
from toscametrics.classes.types.range_type       import RangeType

class TestCapabilityAssignmentEq(unittest.TestCase):
    pass

    def testEqual(self):
        c1 = CapabilityAssignment({'p1':'value'}, {'a1':'value'}, RangeType(1,2))
        c2 = CapabilityAssignment({'p1':'value'}, {'a1':'value'}, RangeType(1,2))
        self.assertEqual(c1, c2, 'Test failed because expected equality but actual is \'not equal\'!') 


    def testNotEqual(self):
        c1 = CapabilityAssignment({'p1':'value'}, {'a1':'value'}, RangeType(1,2))
        c2 = CapabilityAssignment({'p2':'value2'}, {'a2':'value2'}, RangeType(2,4))
        self.assertNotEqual(c1, c2, 'Test failed because expected not equal but actual is \'equal\'!') 

if __name__ == "__main__":
    unittest.main()