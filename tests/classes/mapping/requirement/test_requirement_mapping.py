import unittest
from parameterized import parameterized_class

from toscametrics.classes.mapping.requirement import RequirementMapping

@parameterized_class([
   { 'input': None,  'expected': False},
   { 'input': ['node', 'capability'], 'expected': False},
   { 'input': [],    'expected': True},
   { 'input': ['output of the topology'], 'expected': True},
   { 'input': [1], 'expected': True},
   { 'input': ['node', 2], 'expected': True},
   { 'input': 'path/file.yaml', 'expected': True},
   { 'input': True,  'expected': True},
   { 'input': False, 'expected': True},
   { 'input': 2,     'expected': True},
   { 'input': 2.0,   'expected': True},
   { 'input': {},    'expected': True}
])
class TestRequirementMappingMapping(unittest.TestCase):

    def test(self):
        raised = False

        try:
            RequirementMapping(mapping=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()