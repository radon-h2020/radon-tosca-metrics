import unittest

from toscametrics.classes.definitions.artifact                 import ArtifactDefinition
from toscametrics.classes.definitions.operation_implementation import OperationImplementationDefinition

class TestOperationImplementationDefinitionEq(unittest.TestCase):

    def testEqual(self):
        o1 = OperationImplementationDefinition(
            primary=ArtifactDefinition(type='types.node.A', file=r"C:\path\file.yaml"),
            dependencies=[ArtifactDefinition(type='types.node.A', file=r"C:\path\file.yaml")],
            operationHost='nodes.host1',
            timeout=100
          )

        o2 = OperationImplementationDefinition(
            primary=ArtifactDefinition(type='types.node.A', file=r"C:\path\file.yaml"),
            dependencies=[ArtifactDefinition(type='types.node.A', file=r"C:\path\file.yaml")],
            operationHost='nodes.host1',
            timeout=100
          )

        self.assertEqual(o1, o2, 'Test failed because expected equality but actual is \'not equal\'!') 

    def testNotEqual1(self):
        o1 = OperationImplementationDefinition(
            primary=ArtifactDefinition(type='types.node.A', file=r"C:\path\file.yaml"),
            dependencies=[ArtifactDefinition(type='types.node.A', file=r"C:\path\file.yaml")],
            operationHost='nodes.host1',
            timeout=100
          )

        o2 = OperationImplementationDefinition(
            primary=ArtifactDefinition(type='types.node.B', file=r"C:\path\fileB.yaml"),
            dependencies=[ArtifactDefinition(type='types.node.B', file=r"C:\path\file2.yaml")]
          )

        self.assertNotEqual(o1, o2, 'Test failed because expected not equal but actual is \'equal\'!') 
    
if __name__ == "__main__":
    unittest.main()