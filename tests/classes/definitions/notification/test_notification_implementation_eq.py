import unittest

from toscametrics.classes.definitions.artifact                    import ArtifactDefinition
from toscametrics.classes.definitions.notification_implementation import NotificationImplementationDefinition

class TestNotificationImplementationDefinitionEq(unittest.TestCase):

    def testEqual(self):
        n1 = NotificationImplementationDefinition(
            primary=ArtifactDefinition(type='types.node.A', file=r"C:\path\file.yaml"),
            dependencies=[ArtifactDefinition(type='types.node.B', file=r"C:\path\fileB.yaml")]
          )

        n2 = NotificationImplementationDefinition(
            primary=ArtifactDefinition(type='types.node.A', file=r"C:\path\file.yaml"),
            dependencies=[ArtifactDefinition(type='types.node.B', file=r"C:\path\fileB.yaml")]
          )

        self.assertEqual(n1, n2, 'Test failed because expected equality but actual is \'not equal\'!') 

    def testNotEqual1(self):
        n1 = NotificationImplementationDefinition(
            primary=ArtifactDefinition(type='types.node.A', file=r"C:\path\file.yaml"),
            dependencies=[ArtifactDefinition(type='types.node.A', file=r"C:\path\file.yaml")]
          )

        n2 = NotificationImplementationDefinition(
            primary=ArtifactDefinition(type='types.node.B', file=r"C:\path\fileB.yaml"),
            dependencies=[ArtifactDefinition(type='types.node.B', file=r"C:\path\file2.yaml")]
          )

        self.assertNotEqual(n1, n2, 'Test failed because expected not equal but actual is \'equal\'!') 
    
if __name__ == "__main__":
    unittest.main()