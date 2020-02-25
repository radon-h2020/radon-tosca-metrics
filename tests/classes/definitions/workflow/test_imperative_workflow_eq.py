import unittest

from toscametrics.classes.definitions.imperative_workflow import ImperativeWorkflowDefinition
from toscametrics.classes.definitions.operation_implementation              import OperationImplementationDefinition
from toscametrics.classes.definitions.property              import PropertyDefinition
from toscametrics.classes.definitions.workflow_precondition              import WorkflowPreconditionDefinition
from toscametrics.classes.definitions.workflow_step              import WorkflowStepDefinition
from toscametrics.classes.mapping.attribute              import AttributeMapping

class TestImperativeWorkflowDefinitionEq(unittest.TestCase):

    def testEqual(self):
        w1 = ImperativeWorkflowDefinition(
              description='a description',
              metadata={'key':'value'},
              inputs={'property_1':PropertyDefinition(type='property type')},
              preconditions=[WorkflowPreconditionDefinition(target='Workflow.Target')],
              steps={'step_1':WorkflowStepDefinition(target='Workflow.A')},
              implementation=OperationImplementationDefinition(),
              outputs={'attribute_1':AttributeMapping()},
          )

        w2 = ImperativeWorkflowDefinition(
              description='a description',
              metadata={'key':'value'},
              inputs={'property_1':PropertyDefinition(type='property type')},
              preconditions=[WorkflowPreconditionDefinition(target='Workflow.Target')],
              steps={'step_1':WorkflowStepDefinition(target='Workflow.A')},
              implementation=OperationImplementationDefinition(),
              outputs={'attribute_1':AttributeMapping()},
          )

        self.assertEqual(w1, w2, 'Test failed because expected equality but actual is \'not equal\'!') 

    def testNotEqual1(self):
        w1 = ImperativeWorkflowDefinition(
              description='a description',
              metadata={'key':'value'},
              inputs={'property_1':PropertyDefinition(type='property type')},
              preconditions=[WorkflowPreconditionDefinition(target='Workflow.Target')],
              steps={'step_1':WorkflowStepDefinition(target='Workflow.A')},
              implementation=OperationImplementationDefinition(),
              outputs={'attribute_1':AttributeMapping()},
          )

        w2 = ImperativeWorkflowDefinition(
              description='a longer description',
              metadata={'keyA':'valueA'},
              inputs={'property_2':PropertyDefinition(type='property type 2')},
              steps={'step_1':WorkflowStepDefinition(target='Workflow.A2')}
          )

        self.assertNotEqual(w1, w2, 'Test failed because expected not equal but actual is \'equal\'!') 
    
if __name__ == "__main__":
    unittest.main()