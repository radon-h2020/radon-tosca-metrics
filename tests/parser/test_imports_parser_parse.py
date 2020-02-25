import unittest
from toscametrics.classes.definitions.imports import ImportDefinition
from toscametrics.parser.imports_parser       import ImportsParser

class TestImportsParserParse(unittest.TestCase):

    def testNone1(self):
        parser = ImportsParser()
        actual = parser.parse(None)
        self.assertIsNone(actual, 'Test failed because expected None and got ' + str(actual) +'!') 

    def testNone2(self):
        parser = ImportsParser()
        actual = parser.parse([])
        self.assertIsNone(actual, 'Test failed because expected None and got ' + str(actual) +'!') 

    def testValid(self):
        input = {"file": "path1/path2/file.yaml", "repository": "my_service_catalog", "namespace_uri": "http://mycompany.com/tosca/1.0/platform", "namespace_prefix": "mycompany"}
        parser = ImportsParser()
        actual = parser.parse(input)
        
        expected = ImportDefinition(
                    file='path1/path2/file.yaml',
                    repository='my_service_catalog',
                    namespaceUri='http://mycompany.com/tosca/1.0/platform',
                    namespacePrefix='mycompany'
                )

        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 
    
if __name__ == "__main__":
    unittest.main()

