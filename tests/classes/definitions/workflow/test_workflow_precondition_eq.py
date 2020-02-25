import unittest

from toscametrics.classes.clauses.conditions                import ConditionClause
from toscametrics.classes.definitions.workflow_precondition import WorkflowPreconditionDefinition

class TestWorkflowPreconditionDefinitionEq(unittest.TestCase):

    def testEqual(self):
        w1 = WorkflowPreconditionDefinition(
            target='templates.nodes.A',
            targetRelationship='relationships.R1',
            condition=[ConditionClause()]
          )

        w2 = WorkflowPreconditionDefinition(
            target='templates.nodes.A',
            targetRelationship='relationships.R1',
            condition=[ConditionClause()]
          )

        self.assertEqual(w1, w2, 'Test failed because expected equality but actual is \'not equal\'!') 

    def testNotEqual1(self):
        w1 = WorkflowPreconditionDefinition(
            target='templates.nodes.A',
            targetRelationship='relationships.R1',
            condition=[ConditionClause()]
          )

        w2 = WorkflowPreconditionDefinition(
            target='templates.nodes.B',
            targetRelationship='relationships.R2'
          )

        self.assertNotEqual(w1, w2, 'Test failed because expected not equal but actual is \'equal\'!') 
    
if __name__ == "__main__":
    unittest.main()