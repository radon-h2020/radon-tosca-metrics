import unittest
from parameterized import parameterized_class

from toscametrics.classes.types.capability import CapabilityType
from toscametrics.classes.filters.node     import NodeFilter

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': [], 'expected': False},
   { 'input': [CapabilityType()], 'expected': False},
   { 'input': [CapabilityType(), 1], 'expected': True},
   { 'input': 'tosca.nodes.A', 'expected': True},
   { 'input': True, 'expected': True},
   { 'input': 2, 'expected': True},
   { 'input': 2.0, 'expected': True},
   { 'input': {}, 'expected': True}
])
class TestNodeFilterCapabilities(unittest.TestCase):

    def test(self):
        raised = False

        try:
            NodeFilter(capabilities=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
        
if __name__ == "__main__":
    unittest.main()