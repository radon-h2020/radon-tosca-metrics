import unittest
from parameterized import parameterized_class

from toscametrics.classes.definitions.imports import ImportDefinition

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': 'This is a repository', 'expected': False},
   { 'input': True,  'expected': True},
   { 'input': False, 'expected': True},
   { 'input': 2,     'expected': True},
   { 'input': 2.0,   'expected': True},
   { 'input': [],    'expected': True},
   { 'input': {},    'expected': True}
])
class TestImportDefinitionRepository(unittest.TestCase):

    def test(self):
        raised = False

        try:
            ImportDefinition(file='Test', repository=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()