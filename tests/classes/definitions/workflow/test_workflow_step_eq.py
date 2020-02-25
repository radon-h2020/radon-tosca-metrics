import unittest

from toscametrics.classes.clauses.constraints                    import ConstraintClause
from toscametrics.classes.definitions.activity.call_operation    import CallOperationActivityDefinition
from toscametrics.classes.definitions.activity.delegate_workflow import DelegateWorkflowActivityDefinition
from toscametrics.classes.definitions.activity.inline_workflow   import InlineWorkflowActivityDefinition
from toscametrics.classes.definitions.activity.set_state         import SetStateActivityDefinition
from toscametrics.classes.definitions.workflow_step              import WorkflowStepDefinition

class TestWorkflowPreconditionDefinitionEq(unittest.TestCase):

    def testEqual(self):
        w1 = WorkflowStepDefinition(
            target='templates.nodes.A',
            targetRelationship='relationships.R1',
            operationHost='nodes.hosts.A',
            filter=[ConstraintClause(equal=1), ConstraintClause(length=5)],
            activities=[CallOperationActivityDefinition(callOperation='activate'),
                        DelegateWorkflowActivityDefinition(delegate='delegate'),
                        InlineWorkflowActivityDefinition(inline='inline'),
                        SetStateActivityDefinition(state='supported')
            ],
            onSuccess=['s1','s2'],
            onFailure=['s3','s4']
          )

        w2 = WorkflowStepDefinition(
            target='templates.nodes.A',
            targetRelationship='relationships.R1',
            operationHost='nodes.hosts.A',
            filter=[ConstraintClause(equal=1), ConstraintClause(length=5)],
            activities=[CallOperationActivityDefinition(callOperation='activate'),
                        DelegateWorkflowActivityDefinition(delegate='delegate'),
                        InlineWorkflowActivityDefinition(inline='inline'),
                        SetStateActivityDefinition(state='supported')
            ],
            onSuccess=['s1','s2'],
            onFailure=['s3','s4']
          )

        self.assertEqual(w1, w2, 'Test failed because expected equality but actual is \'not equal\'!') 

    def testNotEqual1(self):
        w1 = WorkflowStepDefinition(
            target='templates.nodes.A',
            targetRelationship='relationships.R1',
            operationHost='nodes.hosts.A',
            filter=[ConstraintClause(equal=1), ConstraintClause(length=5)],
            activities=[CallOperationActivityDefinition(callOperation='none')],
            onSuccess=['s1','s2'],
            onFailure=['s3','s4']
          )

        w2 = WorkflowStepDefinition(
            target='templates.nodes.B',
            targetRelationship='relationships.R2',
            operationHost='nodes.hosts.B',
            filter=[ConstraintClause(equal=5), ConstraintClause(length=10)],
            onSuccess=['s1','s5']
          )

        self.assertNotEqual(w1, w2, 'Test failed because expected not equal but actual is \'equal\'!') 
    
if __name__ == "__main__":
    unittest.main()