import unittest
from toscametrics.classes.definitions.repository import RepositoryDefinition
from toscametrics.parser.repositories_parser     import RepositoriesParser

class TestRepositoriesParserParseAll(unittest.TestCase):

    def testEmpty1(self):
        parser = RepositoriesParser()
        actual = parser.parseAll(None)
        self.assertEqual(actual, [], 'Test failed because expected empty list and got ' + str(actual) +'!') 

    def testEmpty2(self):
        parser = RepositoriesParser()
        actual = parser.parseAll([])
        self.assertEqual(actual, [], 'Test failed because expected empty list and got ' + str(actual) +'!') 

    def testValid(self):
        input = {"repositories": {"my_code_repo_1": {"url": "https://github.com/my-project-1/"},"my_code_repo_2": {"description": "My project’s code repository in GitHub","url": "https://github.com/my-project-2/"}}}
        parser = RepositoriesParser()
        actual = parser.parseAll(input)
        
        r1 = RepositoryDefinition(
                url='https://github.com/my-project-1/',
            )
        r2 = RepositoryDefinition(
                url='https://github.com/my-project-2/',
                description='My project’s code repository in GitHub'
            )
        
        expected = [r1, r2]

        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 
    
if __name__ == "__main__":
    unittest.main()


