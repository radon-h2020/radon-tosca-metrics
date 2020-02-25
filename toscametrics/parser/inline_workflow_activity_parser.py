from toscametrics.classes.definitions.activity.inline_workflow import InlineWorkflowActivityDefinition 

class InlineWorkflowActivityParser():

    def parse(self, d):
        """ 
        Returns a InlineWorkflowActivityParser object, if any. None otherwise
        d - a dictionary to parse
        """        
        
        if not isinstance(d, dict):
            return None

        try:
            return InlineWorkflowActivityDefinition(
                inline=d.get('inline'),
                workflow=d.get('workflow'),
                inputs=d.get('inputs')
            )

        except TypeError:
            return None