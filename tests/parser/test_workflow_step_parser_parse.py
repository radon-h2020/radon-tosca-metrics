import unittest
from toscametrics.classes.definitions.activity.call_operation import CallOperationActivityDefinition
from toscametrics.classes.definitions.workflow_step           import WorkflowStepDefinition
from toscametrics.parser.workflow_steps_parser                import WorkflowStepsParser

class TestWorkflowStepsParserParse(unittest.TestCase):

    def testNone1(self):
        parser = WorkflowStepsParser()
        actual = parser.parse(None)
        self.assertIsNone(actual, 'Test failed because expected None and got ' + str(actual) +'!') 

    def testNone2(self):
        parser = WorkflowStepsParser()
        actual = parser.parse([])
        self.assertIsNone(actual, 'Test failed because expected None and got ' + str(actual) +'!') 

    def testValid(self):
        input={"target": "Welcome", "activities": [{ "call_operation": "Standard.stop" }]}
        parser = WorkflowStepsParser()
        actual = parser.parse(input)
        
        expected = WorkflowStepDefinition(
                        target='Welcome',
                        activities=[CallOperationActivityDefinition(callOperation='Standard.stop')]
                    )

        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 
    
if __name__ == "__main__":
    unittest.main()


