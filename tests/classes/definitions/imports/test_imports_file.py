import unittest
from parameterized import parameterized_class

from toscametrics.classes.definitions.imports import ImportDefinition

@parameterized_class([
   { 'input': 'path/file.yaml', 'expected': False},
   { 'input': None,  'expected': True},
   { 'input': True,  'expected': True},
   { 'input': False, 'expected': True},
   { 'input': 2,     'expected': True},
   { 'input': 2.0,   'expected': True},
   { 'input': [],    'expected': True},
   { 'input': {},    'expected': True}
])
class TestImportDefinitionFile(unittest.TestCase):

    def test(self):
        raised = False

        try:
            ImportDefinition(file=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()