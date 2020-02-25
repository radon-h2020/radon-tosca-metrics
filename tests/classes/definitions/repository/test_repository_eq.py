import unittest

from toscametrics.classes.definitions.repository import RepositoryDefinition

class TestRepositoryDefinitionEq(unittest.TestCase):

    def testEqual(self):
        r1 = RepositoryDefinition(
             url='https://github.com/my-project/',
             description='My project’s code repository in GitHub'
          )

        r2 = RepositoryDefinition(
            url='https://github.com/my-project/',
            description='My project’s code repository in GitHub'
        )

        self.assertEqual(r1, r2, 'Test failed because expected equality but actual is \'not equal\'!') 

    def testNotEqual1(self):
        r1 = RepositoryDefinition(
             url='https://github.com/my-project/',
             description='My project’s code repository in GitHub'
          )

        r2 = RepositoryDefinition(
            url='https://github.com/my-project_2/',
            description='My project’s code repository in GitHub'
        )

        self.assertNotEqual(r1, r2, 'Test failed because expected not equal but actual is \'equal\'!') 
    
    def testNotEqual2(self):
        r1 = RepositoryDefinition(
             url='https://github.com/my-project/',
             description='My project’s code repository in GitHub'
          )

        r2 = RepositoryDefinition(
            url='https://github.com/my-project/',
            description='My beautiful project’s code repository in GitHub '
        )

        self.assertNotEqual(r1, r2, 'Test failed because expected not equal but actual is \'equal\'!') 
    
if __name__ == "__main__":
    unittest.main()