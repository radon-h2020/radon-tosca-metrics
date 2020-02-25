import unittest

from toscametrics.classes.definitions.imports import ImportDefinition

class TestImportDefinitionEq(unittest.TestCase):

    def testEqual(self):
        i1 = ImportDefinition(
             file='path1/path2/file.yaml',
             repository='my_service_catalog',
             namespaceUri='http://mycompany.com/tosca/1.0/platform',
             namespacePrefix='mycompany'
          )

        i2 = ImportDefinition(
             file='path1/path2/file.yaml',
             repository='my_service_catalog',
             namespaceUri='http://mycompany.com/tosca/1.0/platform',
             namespacePrefix='mycompany'
          )

        self.assertEqual(i1, i2, 'Test failed because expected equality but actual is \'not equal\'!') 

    def testNotEqual(self):
        i1 = ImportDefinition(
             file='path1/path2/file1.yaml',
             repository='my_service_catalog A',
             namespaceUri='http://mycompany.com/tosca/1.0/platform',
             namespacePrefix='mycompany'
          )

        i2 = ImportDefinition(
             file='path1/path2/file2.yaml',
             repository='my_service_catalog B',
             namespaceUri='http://mycompany.com/tosca/1.0/platform',
             namespacePrefix='mycompany'
          )

        self.assertNotEqual(i1, i2, 'Test failed because expected not equal but actual is \'equal\'!') 
    
if __name__ == "__main__":
    unittest.main()