import unittest
from parameterized import parameterized_class

from toscametrics.classes.assignments.capability import CapabilityAssignment
from toscametrics.classes.types.range_type       import RangeType

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': RangeType(1,2), 'expected': False},
   { 'input': 'tosca.nodes.A', 'expected': True},
   { 'input': True, 'expected': True},
   { 'input': 2, 'expected': True},
   { 'input': 2.0, 'expected': True},
   { 'input': {}, 'expected': True},
   { 'input': [], 'expected': True}
])
class TestCapabilityAssignmentOccurrences(unittest.TestCase):

    def test(self):
        raised = False

        try:
            CapabilityAssignment(occurrences=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
        
if __name__ == "__main__":
    unittest.main()