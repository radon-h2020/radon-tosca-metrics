import unittest
from parameterized import parameterized_class

from toscametrics.classes.mapping.capability import CapabilityMapping

@parameterized_class([
   { 'input': None,  'expected': False},
   { 'input': {},    'expected': False},
   { 'input': {'key':'value'},  'expected': False},
   { 'input': 'path/file.yaml', 'expected': True},
   { 'input': True,  'expected': True},
   { 'input': False, 'expected': True},
   { 'input': 2,     'expected': True},
   { 'input': 2.0,   'expected': True},
   { 'input': [],    'expected': True}
])
class TestCapabilityMappingAttributes(unittest.TestCase):

    def test(self):
        raised = False

        try:
            CapabilityMapping(attributes=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()