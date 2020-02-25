import toscametrics.utils as utils
from toscametrics.classes.definitions.workflow_step import WorkflowStepDefinition 
from toscametrics.parser.activities_parser          import ActivitiesParser 

class WorkflowStepsParser():

    def parseAll(self, artifact):
        """ 
        Returns a list of WorkflowStepDefinition 
        artifact -- a dictionary or a list of dictionary to parse.
        """ 

        if not isinstance(artifact, dict) and not isinstance(artifact, list):
            return []
       
        steps = []
        
        keyValueList1 = utils.keyValueList(artifact)
        for kv in keyValueList1:
            if kv[0] == 'steps':
                values = kv[1]

                for k in values.keys():
                    item = values[k]

                    step = self.parse(item)
                    if step is not None:
                        steps.append(step)

        return steps
    
    def parse(self, item):
        """ 
        Returns an WorkflowStepDefinition 
        item -- a dictionary to parse.
        """ 
        
        if not isinstance(item, dict):
            return None
        
        ap = ActivitiesParser()
        activities = ap.parseAll(item)
        if len(activities) == 0:
            activities = None

        try:
            return WorkflowStepDefinition(
                target=item.get('target'), 
                targetRelationship=item.get('target_relationship'), 
                operationHost=item.get('operation_host'), 
                filter=item.get('filter'), 
                activities=activities,
                onSuccess=item.get('on_success'), 
                onFailure=item.get('on_failure')
            )
        except TypeError:
            return None

        return None