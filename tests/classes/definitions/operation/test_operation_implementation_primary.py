import unittest
from parameterized import parameterized_class

from toscametrics.classes.definitions.artifact import ArtifactDefinition
from toscametrics.classes.definitions.operation_implementation import OperationImplementationDefinition

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': ArtifactDefinition(type='types.node.A', file=r"C:\path\file.yaml"), 'expected': False},
   { 'input': 'inline string', 'expected': True},
   { 'input': True, 'expected': True},
   { 'input': 2, 'expected': True},
   { 'input': 2.0, 'expected': True},
   { 'input': [], 'expected': True},
   { 'input': {}, 'expected': True}
])
class OperationImplementationDefinitionPrimary(unittest.TestCase):

    def test(self):
        raised = False

        try:
            OperationImplementationDefinition(primary=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()