from toscametrics.classes.definitions.activity.delegate_workflow import DelegateWorkflowActivityDefinition 

class DelegateWorkflowActivityParser():

    def parse(self, d):
        """ 
        Returns a DelegateWorkflowActivityDefinition object, if any. None otherwise
        d - a dictionary to parse
        """        
        
        if not isinstance(d, dict):
            return None

        try:
            return DelegateWorkflowActivityDefinition(
                delegate=d.get('delegate'),
                workflow=d.get('workflow'),
                inputs=d.get('inputs')
            )

        except TypeError:
            return None