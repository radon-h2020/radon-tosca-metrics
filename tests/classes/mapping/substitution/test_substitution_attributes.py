import unittest
from parameterized import parameterized_class

from toscametrics.classes.mapping.attribute    import AttributeMapping
from toscametrics.classes.mapping.substitution import SubstitutionMapping

@parameterized_class([
   { 'input': None,  'expected': False},
   { 'input': {},    'expected': False},
   { 'input': {'key':AttributeMapping()},  'expected': False},
   { 'input': {'key':'value'},  'expected': True},
   { 'input': 'path/file.yaml', 'expected': True},
   { 'input': True,  'expected': True},
   { 'input': False, 'expected': True},
   { 'input': 2,     'expected': True},
   { 'input': 2.0,   'expected': True},
   { 'input': [],    'expected': True}
])
class TestSubstitutionMappingAttributes(unittest.TestCase):

    def test(self):
        raised = False

        try:
            SubstitutionMapping(nodeType='test', attributes=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()