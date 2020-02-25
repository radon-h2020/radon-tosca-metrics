import unittest

from toscametrics.classes.types.entity  import EntityType
from toscametrics.classes.types.version import VersionType
from toscametrics.parser.entity_parser  import EntityParser

class TestEntityParserParse(unittest.TestCase):

    def testNone1(self):
        parser = EntityParser()
        actual = parser.parse([])
        self.assertIsNone(actual, 'Test failed because expected None and got ' + str(actual) +'!') 

    def testNone2(self):
        input = {'node_type': {'type': 'MySQL', 'properties': [{'property_1':{'type': 'string'}}]}}
        parser = EntityParser()
        actual = parser.parse(input)
        expected = EntityType()

        self.assertEqual(actual, expected) 

    def testValid(self):
        input = {'derived_from':'nodes.parent', 'version':'1.0.0.alpha-1', 'metadata':{'key':'value'}, 'description':'Testing entity parser'}
        parser = EntityParser()
        actual = parser.parse(input)
        expected = EntityType(
            derivedFrom='nodes.parent',
            version='1.0.0.alpha-1',
            metadata={'key':'value'},
            description='Testing entity parser'
        )

        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 
    
if __name__ == "__main__":
    unittest.main()