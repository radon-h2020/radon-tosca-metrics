import unittest
from toscametrics.classes.definitions.activity.delegate_workflow import DelegateWorkflowActivityDefinition
from toscametrics.parser.delegate_workflow_activity_parser       import DelegateWorkflowActivityParser

class TestDelegateWorkflowActivityParserParse(unittest.TestCase):

    def testNone1(self):
        parser = DelegateWorkflowActivityParser()
        actual = parser.parse(None)
        self.assertIsNone(actual, 'Test failed because expected None and got ' + str(actual) +'!') 

    def testNone2(self):
        parser = DelegateWorkflowActivityParser()
        actual = parser.parse([])
        self.assertIsNone(actual, 'Test failed because expected None and got ' + str(actual) +'!') 

    def testValid(self):
        input = {"delegate": "workflows.WelcomeStopping", "workflow":"Stop", "inputs":{"delay_ms":10000}}
        parser = DelegateWorkflowActivityParser()
        actual = parser.parse(input)
        
        expected = DelegateWorkflowActivityDefinition(
            delegate='workflows.WelcomeStopping',
            workflow='Stop',
            inputs={"delay_ms":10000}   
        )

        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 
    
if __name__ == "__main__":
    unittest.main()

