import toscametrics.utils as utils
from toscametrics.classes.definitions.imports import ImportDefinition 

class ImportsParser():

    def parseAll(self, artifact):
        """ 
        Returns a list of ImportDefinition 
        artifact -- a dictionary or a list of dictionary to parse.
        """ 

        if not isinstance(artifact, dict) and not isinstance(artifact, list):
            return []
       
        imports = []
        
        keyValueList = utils.keyValueList(artifact)
        for kv in keyValueList:
            if kv[0] ==  'imports':
                values = kv[1]

                for item in values:
                    id = self.parse(item)
                    if id is not None:
                        imports.append(id)

        return imports
    
    def parse(self, item):
        """ 
        Returns an ImportDefinition 
        item -- a dictionary to parse.
        """ 
        
        if not isinstance(item, dict):
            return None
        
        try:
            return ImportDefinition(
                file=item.get('file'),
                repository=item.get('repository'),
                namespacePrefix=item.get('namespace_prefix'),
                namespaceUri=item.get('namespace_uri')
            )
        except TypeError:
            return None

        return None