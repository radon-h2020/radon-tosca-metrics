import unittest

from toscametrics.classes.clauses.constraints import ConstraintClause
from toscametrics.classes.filters.property    import PropertyFilter

class TestPropertyFilterEq(unittest.TestCase):
    pass

    def testEqual(self):
        p1 = PropertyFilter('property_1', [ConstraintClause(equal=1)])
        p2 = PropertyFilter('property_1', [ConstraintClause(equal=1)])

        self.assertEqual(p1, p2, 'Test failed because expected equality but actual is \'not equal\'!') 


    def testNotEqual(self):
        p1 = PropertyFilter('property_1', [ConstraintClause(equal=1)])
        p2 = PropertyFilter('property_2', [ConstraintClause(equal=2)])
        self.assertNotEqual(p1, p2, 'Test failed because expected not equal but actual is \'equal\'!') 

if __name__ == "__main__":
    unittest.main()