import unittest
from parameterized import parameterized_class

from toscametrics.classes.filters.node         import NodeFilter
from toscametrics.classes.mapping.substitution import SubstitutionMapping

@parameterized_class([
   { 'input': None,  'expected': False},
   { 'input': NodeFilter(),  'expected': False},
   { 'input': 'string', 'expected': True},
   { 'input': True,  'expected': True},
   { 'input': 2,     'expected': True},
   { 'input': 2.0,   'expected': True},
   { 'input': [],    'expected': True},
   { 'input': {},    'expected': True}
])
class TestSubstitutionMappingSubstitutionFilter(unittest.TestCase):

    def test(self):
        raised = False

        try:
            SubstitutionMapping(nodeType='test', substitutionFilter=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()