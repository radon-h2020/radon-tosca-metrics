import unittest
from toscametrics.classes.definitions.activity.call_operation    import CallOperationActivityDefinition
from toscametrics.classes.definitions.activity.delegate_workflow import DelegateWorkflowActivityDefinition
from toscametrics.classes.definitions.activity.inline_workflow   import InlineWorkflowActivityDefinition
from toscametrics.classes.definitions.activity.set_state         import SetStateActivityDefinition
from toscametrics.parser.activities_parser                       import ActivitiesParser

class TestCallOperationActivityParserParse(unittest.TestCase):

    def testNone1(self):
        parser = ActivitiesParser()
        actual = parser.parse(None)
        self.assertIsNone(actual, 'Test failed because expected None and got ' + str(actual) +'!') 

    def testNone2(self):
        parser = ActivitiesParser()
        actual = parser.parse([])
        self.assertIsNone(actual, 'Test failed because expected None and got ' + str(actual) +'!') 

    def testValidCallOperation(self):
        input = {"call_operation": "Standard.stop", "operation":"Stop", "inputs":{"delay_ms":10000}}
        parser = ActivitiesParser()
        actual = parser.parse(input)
        
        expected = CallOperationActivityDefinition(
            callOperation='Standard.stop',
            operation='Stop',
            inputs={'delay_ms':10000}
        )

        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 
  
    def testValidDelegateWorkflow(self):
        input = {"delegate": "workflows.WelcomeStopping", "workflow":"Stop", "inputs":{"delay_ms":10000}}
        parser = ActivitiesParser()
        actual = parser.parse(input)
        
        expected = DelegateWorkflowActivityDefinition(
            delegate='workflows.WelcomeStopping',
            workflow='Stop',
            inputs={"delay_ms":10000}   
        )

        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 

    def testValidInlineWorkflow(self):
        input = {"inline": "workflows.WelcomeStopping", "workflow":"Stop", "inputs":{"delay_ms":10000}}
        parser = ActivitiesParser()
        actual = parser.parse(input)
        
        expected = InlineWorkflowActivityDefinition(
            inline='workflows.WelcomeStopping',
            workflow='Stop',
            inputs={"delay_ms":10000}   
        )

        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 
          
    
    def testValidSetState(self):
        input = {"set_state": "stopping"}
        parser = ActivitiesParser()
        actual = parser.parse(input)
        
        expected = SetStateActivityDefinition(state='stopping')

        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 


if __name__ == "__main__":
    unittest.main()

