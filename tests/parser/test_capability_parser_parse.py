import unittest

from toscametrics.classes.definitions.capability import CapabilityDefinition
from toscametrics.classes.definitions.property   import PropertyDefinition
from toscametrics.parser.capability_parser       import CapabilityParser

class TestCapabilityParserParse(unittest.TestCase):

    def testEmpty1(self):
        parser = CapabilityParser()
        actual = parser.parse([])
        self.assertIsNone(actual, 'Test failed because expected None and got ' + str(actual) +'!') 

    def testEmpty2(self):
        input = {'node_type': {'type': 'MySQL', 'properties': [{'property_1':{'type': 'string'}}]}}
        parser = CapabilityParser()
        actual = parser.parse(input)
        self.assertIsNone(actual, 'Test failed because expected None and got ' + str(actual) +'!') 
        
    def testValid(self):
        input = {'type': 'mytypes.mycapabilities.MyCapabilityTypeName', 'properties': { 'limit': { 'type': 'integer', 'default': 100 }}}
        parser = CapabilityParser()
        actual = parser.parse(input)
        expected = CapabilityDefinition(
            type='mytypes.mycapabilities.MyCapabilityTypeName',
            properties={'limit':PropertyDefinition(type='integer', default=100)}
        )

        self.assertEqual(actual.properties, expected.properties, 'Test failed because expected ' + str(expected.properties) + ' and got ' + str(actual.properties) +'!') 
        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 
    
if __name__ == "__main__":
    unittest.main()