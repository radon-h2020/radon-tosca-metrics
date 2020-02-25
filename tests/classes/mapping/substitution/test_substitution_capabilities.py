import unittest
from parameterized import parameterized_class

from toscametrics.classes.mapping.capability   import CapabilityMapping
from toscametrics.classes.mapping.substitution import SubstitutionMapping

@parameterized_class([
   { 'input': None,  'expected': False},
   { 'input': {},    'expected': False},
   { 'input': {'capability':CapabilityMapping()},  'expected': False},
   { 'input': {'capability_1':CapabilityMapping(), 'capability_2':1},  'expected': True},
   { 'input': 'path/file.yaml', 'expected': True},
   { 'input': True,  'expected': True},
   { 'input': False, 'expected': True},
   { 'input': 2,     'expected': True},
   { 'input': 2.0,   'expected': True},
   { 'input': [],    'expected': True}
])
class TestSubstitutionMappingCapabilities(unittest.TestCase):

    def test(self):
        raised = False

        try:
            SubstitutionMapping(nodeType='test', capabilities=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()