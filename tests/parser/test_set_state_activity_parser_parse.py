import unittest
from toscametrics.classes.definitions.activity.set_state import SetStateActivityDefinition
from toscametrics.parser.set_state_activity_parser      import SetStateActivityParser

class TestSetStateActivityParserParserParse(unittest.TestCase):

    def testNone1(self):
        parser = SetStateActivityParser()
        actual = parser.parse(None)
        self.assertIsNone(actual, 'Test failed because expected None and got ' + str(actual) +'!') 

    def testNone2(self):
        parser = SetStateActivityParser()
        actual = parser.parse([])
        self.assertIsNone(actual, 'Test failed because expected None and got ' + str(actual) +'!') 

    def testValid(self):
        input = {"set_state": "stopping"}
        parser = SetStateActivityParser()
        actual = parser.parse(input)
        
        expected = SetStateActivityDefinition(state='stopping')

        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 
    
if __name__ == "__main__":
    unittest.main()

