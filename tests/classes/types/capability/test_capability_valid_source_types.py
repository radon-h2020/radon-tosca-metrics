import unittest
from parameterized import parameterized_class

from toscametrics.classes.types.capability import CapabilityType

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': [], 'expected': False},
   { 'input': ['string 1', 'string 2'], 'expected': False},
   { 'input': ['string 1', 1], 'expected': True},
   { 'input': True, 'expected': True},
   { 'input': 2, 'expected': True},
   { 'input': 2.0, 'expected': True},
   { 'input': {}, 'expected': True}
])
class TestCapabilityTypeValidSourceTypes(unittest.TestCase):

    def test(self):
        raised = False

        try:
            CapabilityType(validSourceTypes=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()