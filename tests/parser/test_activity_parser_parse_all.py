import unittest

from toscametrics.classes.definitions.activity.call_operation    import CallOperationActivityDefinition
from toscametrics.classes.definitions.activity.delegate_workflow import DelegateWorkflowActivityDefinition
from toscametrics.classes.definitions.activity.inline_workflow   import InlineWorkflowActivityDefinition
from toscametrics.classes.definitions.activity.set_state         import SetStateActivityDefinition
from toscametrics.parser.activities_parser                       import ActivitiesParser

class TestActivitiesParserParseAll(unittest.TestCase):

    def testEmpty1(self):
        parser = ActivitiesParser()
        actual = parser.parseAll([])
        self.assertEqual(actual, [], 'Test failed because expected empty list and got ' + str(actual) +'!') 

    def testEmpty2(self):
        input = {'node_type': {'type': 'MySQL', 'properties': [{'property_1':{'type': 'string'}}]}}
        parser = ActivitiesParser()
        actual = parser.parseAll(input)
        self.assertEqual(actual, [], 'Test failed because expected empty list and got ' + str(actual) +'!') 

    def testValid(self):
        input = {"activities": [{"call_operation": "Standard.stop"},{"delegate": "workflows.WelcomeStopping"},{"inline": "workflows.InlineStopping"},{"set_state": "stopping"}]}
        
        parser = ActivitiesParser()
        actual = parser.parseAll(input)

        e1 = CallOperationActivityDefinition(callOperation='Standard.stop')
        e2 = DelegateWorkflowActivityDefinition(delegate='workflows.WelcomeStopping')
        e3 = InlineWorkflowActivityDefinition(inline='workflows.InlineStopping')
        e4 = SetStateActivityDefinition(state='stopping')

        self.assertIn(e1, actual, 'Test failed because expected ' + str(e1) + ' in ' + str(actual) +' but not in!') 
        self.assertIn(e2, actual, 'Test failed because expected ' + str(e2) + ' in ' + str(actual) +' but not in!') 
        self.assertIn(e3, actual, 'Test failed because expected ' + str(e3) + ' in ' + str(actual) +' but not in!') 
        self.assertIn(e4, actual, 'Test failed because expected ' + str(e4) + ' in ' + str(actual) +' but not in!') 

if __name__ == "__main__":
    unittest.main()