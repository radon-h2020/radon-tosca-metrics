import unittest
from parameterized import parameterized_class

from toscametrics.classes.mapping.property import PropertyMapping

@parameterized_class([
   { 'input': None,  'expected': False},
   { 'input': ['output of the topology'], 'expected': False},
   { 'input': ['first output of the topology', 'second output of the topology'], 'expected': True},
   { 'input': [],    'expected': True},
   { 'input': [1], 'expected': True},
   { 'input': 'path/file.yaml', 'expected': True},
   { 'input': True,  'expected': True},
   { 'input': False, 'expected': True},
   { 'input': 2,     'expected': True},
   { 'input': 2.0,   'expected': True},
   { 'input': {},    'expected': True}
])
class TestPropertyMappingMapping(unittest.TestCase):

    def test(self):
        raised = False

        try:
            PropertyMapping(mapping=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()