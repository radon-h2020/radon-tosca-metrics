from toscametrics.classes.definitions.activity.set_state import SetStateActivityDefinition 

class SetStateActivityParser():

    def parse(self, d):
        """ 
        Returns a SetStateActivityDefinition object, if any. None otherwise
        d - a dictionary to parse
        """        
        
        if not isinstance(d, dict):
            return None

        try:
            return SetStateActivityDefinition(state=d.get('set_state'))

        except Exception:
            return None