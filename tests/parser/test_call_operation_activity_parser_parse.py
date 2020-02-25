import unittest
from toscametrics.classes.definitions.activity.call_operation import CallOperationActivityDefinition
from toscametrics.parser.call_operation_activity_parser       import CallOperationActivityParser

class TestCallOperationActivityParserParse(unittest.TestCase):

    def testNone1(self):
        parser = CallOperationActivityParser()
        actual = parser.parse(None)
        self.assertIsNone(actual, 'Test failed because expected None and got ' + str(actual) +'!') 

    def testNone2(self):
        parser = CallOperationActivityParser()
        actual = parser.parse([])
        self.assertIsNone(actual, 'Test failed because expected None and got ' + str(actual) +'!') 

    def testValid(self):
        input = {"call_operation": "Standard.stop", "operation":"Stop", "inputs":{"delay_ms":10000}}
        parser = CallOperationActivityParser()
        actual = parser.parse(input)
        
        expected = CallOperationActivityDefinition(
            callOperation='Standard.stop',
            operation='Stop',
            inputs={'delay_ms':10000}
        )

        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 
    
if __name__ == "__main__":
    unittest.main()

