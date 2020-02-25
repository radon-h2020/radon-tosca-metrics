import unittest
from parameterized import parameterized_class

from toscametrics.classes.definitions.activity.call_operation    import CallOperationActivityDefinition
from toscametrics.classes.definitions.activity.delegate_workflow import DelegateWorkflowActivityDefinition
from toscametrics.classes.definitions.activity.inline_workflow   import InlineWorkflowActivityDefinition
from toscametrics.classes.definitions.activity.set_state         import SetStateActivityDefinition
from toscametrics.classes.definitions.workflow_step              import WorkflowStepDefinition

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': [], 'expected': False},
   { 'input': [CallOperationActivityDefinition(callOperation='activate')], 'expected': False},
   { 'input': [DelegateWorkflowActivityDefinition(delegate='delegate')], 'expected': False},
   { 'input': [InlineWorkflowActivityDefinition(inline='inline')], 'expected': False},
   { 'input': [SetStateActivityDefinition(state='supported')], 'expected': False},
   { 'input': [SetStateActivityDefinition(state='supported'), 2], 'expected': True},
   { 'input': 'This is a target relationship', 'expected': True},
   { 'input': 2, 'expected': True},
   { 'input': 2.0, 'expected': True},
   { 'input': {}, 'expected': True}
])
class TestWorkflowStepDefinitionActivities(unittest.TestCase):

    def test(self):
        raised = False

        try:
            WorkflowStepDefinition(target='test', activities=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()