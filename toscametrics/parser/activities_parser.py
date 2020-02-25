import toscametrics.utils as utils

from toscametrics.classes.definitions.activity.call_operation    import CallOperationActivityDefinition
from toscametrics.classes.definitions.activity.delegate_workflow import DelegateWorkflowActivityDefinition
from toscametrics.classes.definitions.activity.inline_workflow   import InlineWorkflowActivityDefinition
from toscametrics.classes.definitions.activity.set_state         import SetStateActivityDefinition

class ActivitiesParser():

    def parseAll(self, artifact):
        """ 
        Returns a list of ActivityDefinition
        artifact -- a dictionary or a list of dictionary to parse.
        """ 
        if not isinstance(artifact, dict) and not isinstance(artifact, list):
            return []

        activities = []

        keyValueList = utils.keyValueList(artifact)
        for kv in keyValueList:
            if kv[0] == 'activities':
                values = kv[1]
                
                for d in values:
                    activity = self.parse(d)
                    if activity is not None:
                        activities.append(activity)

        return activities

    def parse(self, d):
        """ 
        Returns a InlineWorkflowActivityParser object, if any. None otherwise
        d - a dictionary to parse
        """        
        
        if not isinstance(d, dict):
            return None

        if 'call_operation' in d.keys():
            return self.callOperation(d)
        elif 'delegate' in d.keys():
            return self.delegateWorkflow(d)
        elif 'inline' in d.keys():
            return self.inlineWorkflow(d)
        elif 'set_state' in d.keys():
            return self.state(d)
        
        return None
    
    def callOperation(self, d):
        try:
            return CallOperationActivityDefinition(
                callOperation=d.get('call_operation'),
                operation=d.get('operation'),
                inputs=d.get('inputs')
            )
        except TypeError:
            return None
    
    def delegateWorkflow(self, d):
        try:
            return DelegateWorkflowActivityDefinition(
                delegate=d.get('delegate'),
                workflow=d.get('workflow'),
                inputs=d.get('inputs')
            )
        except TypeError:
            return None

    def inlineWorkflow(self, d):
        try:
            return InlineWorkflowActivityDefinition(
                    inline=d.get('inline'),
                    workflow=d.get('workflow'),
                    inputs=d.get('inputs')
            )
        except TypeError:
            return None
    
    def state(self, d):
        try:
            return SetStateActivityDefinition(state=d.get('set_state'))
        except TypeError:
            return None

    
    