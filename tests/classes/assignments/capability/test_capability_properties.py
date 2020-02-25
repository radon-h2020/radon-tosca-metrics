import unittest
from parameterized import parameterized_class

from toscametrics.classes.assignments.capability import CapabilityAssignment

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': {}, 'expected': False},
   { 'input': {'p1':'value'}, 'expected': False},
   { 'input': 'tosca.nodes.A', 'expected': True},
   { 'input': True, 'expected': True},
   { 'input': 2, 'expected': True},
   { 'input': 2.0, 'expected': True},
   { 'input': [], 'expected': True}
])
class TestCapabilityAssignmentProperties(unittest.TestCase):

    def test(self):
        raised = False

        try:
            CapabilityAssignment(properties=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
        
if __name__ == "__main__":
    unittest.main()