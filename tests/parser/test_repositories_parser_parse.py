import unittest
from toscametrics.classes.definitions.repository import RepositoryDefinition
from toscametrics.parser.repositories_parser     import RepositoriesParser

class TestRepositoriesParserParse(unittest.TestCase):

    def testNone1(self):
        parser = RepositoriesParser()
        actual = parser.parse(None)
        self.assertIsNone(actual, 'Test failed because expected None and got ' + str(actual) +'!') 

    def testNone2(self):
        parser = RepositoriesParser()
        actual = parser.parse([])
        self.assertIsNone(actual, 'Test failed because expected None and got ' + str(actual) +'!') 

    def testValid(self):
        input = {"url": "https://github.com/my-project/", "description":"My project’s code repository in GitHub"}
        parser = RepositoriesParser()
        actual = parser.parse(input)
        
        expected = RepositoryDefinition(
                        url='https://github.com/my-project/',
                        description='My project’s code repository in GitHub'
                    )

        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 
    
if __name__ == "__main__":
    unittest.main()

