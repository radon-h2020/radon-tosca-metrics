import unittest
from toscametrics.classes.definitions.activity.inline_workflow import InlineWorkflowActivityDefinition
from toscametrics.parser.inline_workflow_activity_parser       import InlineWorkflowActivityParser

class TestInlineWorkflowActivityParserParserParse(unittest.TestCase):

    def testNone1(self):
        parser = InlineWorkflowActivityParser()
        actual = parser.parse(None)
        self.assertIsNone(actual, 'Test failed because expected None and got ' + str(actual) +'!') 

    def testNone2(self):
        parser = InlineWorkflowActivityParser()
        actual = parser.parse([])
        self.assertIsNone(actual, 'Test failed because expected None and got ' + str(actual) +'!') 

    def testValid(self):
        input = {"inline": "workflows.WelcomeStopping", "workflow":"Stop", "inputs":{"delay_ms":10000}}
        parser = InlineWorkflowActivityParser()
        actual = parser.parse(input)
        
        expected = InlineWorkflowActivityDefinition(
            inline='workflows.WelcomeStopping',
            workflow='Stop',
            inputs={"delay_ms":10000}   
        )

        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 
    
if __name__ == "__main__":
    unittest.main()

