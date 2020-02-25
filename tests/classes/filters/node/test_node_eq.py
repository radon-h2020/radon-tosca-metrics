import unittest

from toscametrics.classes.clauses.constraints import ConstraintClause
from toscametrics.classes.filters.node        import NodeFilter
from toscametrics.classes.filters.property    import PropertyFilter
from toscametrics.classes.types.capability    import CapabilityType

class TestNodeFilterEq(unittest.TestCase):
    pass

    def testEqual(self):
        n1 = NodeFilter(
             properties=[PropertyFilter('property', [ConstraintClause(equal=1)])],
             capabilities=[CapabilityType(validSourceTypes=['source A'])]
        )

        n2 = NodeFilter(
             properties=[PropertyFilter('property', [ConstraintClause(equal=1)])],
             capabilities=[CapabilityType(validSourceTypes=['source A'])]
        )

        self.assertEqual(n1, n2, 'Test failed because expected equality but actual is \'not equal\'!') 


    def testNotEqual(self):
        n1 = NodeFilter(
             properties=[PropertyFilter('property 1', [ConstraintClause(equal=1)])],
             capabilities=[CapabilityType(validSourceTypes=['source A'])]
        )

        n2 = NodeFilter(
             properties=[PropertyFilter('property 2', [ConstraintClause(equal=5)])],
             capabilities=[CapabilityType(validSourceTypes=['source B'])]
        )

        self.assertNotEqual(n1, n2, 'Test failed because expected not equal but actual is \'equal\'!') 

if __name__ == "__main__":
    unittest.main()