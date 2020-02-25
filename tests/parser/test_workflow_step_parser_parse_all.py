import unittest

from toscametrics.classes.definitions.activity.call_operation import CallOperationActivityDefinition
from toscametrics.classes.definitions.activity.set_state      import SetStateActivityDefinition
from toscametrics.classes.definitions.workflow_step           import WorkflowStepDefinition
from toscametrics.parser.workflow_steps_parser                import WorkflowStepsParser

class TestWorkflowStepsParserParseAll(unittest.TestCase):

    def testEmpty1(self):
        parser = WorkflowStepsParser()
        actual = parser.parseAll(None)
        self.assertEqual(actual, [], 'Test failed because expected empty list and got ' + str(actual) +'!') 

    def testEmpty2(self):
        parser = WorkflowStepsParser()
        actual = parser.parseAll([])
        self.assertEqual(actual, [], 'Test failed because expected empty list and got ' + str(actual) +'!') 

    def testValid(self):
        input={"workflows": {"killWebServer": {"steps": {"Welcome_stop": {"target": "Welcome","activities": [{"call_operation": "Standard.stop"}]},"Welcome_stopping": {"target": "Welcome","activities": [{"set_state": "stopping"}],"on_success": ["Welcome_stop"]}}}}}
        parser = WorkflowStepsParser()
        actual = parser.parseAll(input)
        
        w1 = WorkflowStepDefinition(
                        target='Welcome',
                        activities=[CallOperationActivityDefinition(callOperation='Standard.stop')]
            )
        w2 = WorkflowStepDefinition(
                        target='Welcome',
                        activities=[SetStateActivityDefinition(state='stopping')],
                        onSuccess=["Welcome_stop"]
            )
        
        expected = [w1, w2]

        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 
    
if __name__ == "__main__":
    unittest.main()


