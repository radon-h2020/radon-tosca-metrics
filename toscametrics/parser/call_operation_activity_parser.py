from toscametrics.classes.definitions.activity.call_operation import CallOperationActivityDefinition 

class CallOperationActivityParser():

    def parse(self, d):
        """ 
        Returns a CallOperationActivityDefinition object, if any. None otherwise
        d - a dictionary to parse
        """        
        
        if not isinstance(d, dict):
            return None

        try:
            return CallOperationActivityDefinition(
                callOperation=d.get('call_operation'),
                operation=d.get('operation'),
                inputs=d.get('inputs')
            )

        except TypeError:
            return None