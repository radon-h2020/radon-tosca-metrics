import unittest
from toscametrics.classes.definitions.imports import ImportDefinition
from toscametrics.parser.imports_parser       import ImportsParser

class TestImportsParserParse(unittest.TestCase):

    def testEmpty1(self):
        parser = ImportsParser()
        actual = parser.parseAll(None)
        self.assertEqual(actual, [], 'Test failed because expected empty list and got ' + str(actual) +'!') 

    def testEmpty2(self):
        parser = ImportsParser()
        actual = parser.parseAll([])
        self.assertEqual(actual, [], 'Test failed because expected empty list and got ' + str(actual) +'!') 

    def testValid(self):
        input = { "imports": [{ "file": "path1/path2/file1.yaml" },{ "file": "path1/path2/file2.yaml", "repository": "my_service_catalog", "namespace_uri": "http://mycompany.com/tosca/1.0/platform", "namespace_prefix": "mycompany" }]}
        parser = ImportsParser()
        actual = parser.parseAll(input)
        
        i1 = ImportDefinition(
                file='path1/path2/file1.yaml'
            )
        i2 = ImportDefinition(
                file='path1/path2/file2.yaml',
                repository='my_service_catalog',
                namespaceUri='http://mycompany.com/tosca/1.0/platform',
                namespacePrefix='mycompany'
            )
        
        expected = [i1, i2]

        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 
    
if __name__ == "__main__":
    unittest.main()

