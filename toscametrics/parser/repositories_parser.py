import toscametrics.utils as utils
from toscametrics.classes.definitions.repository import RepositoryDefinition 

class RepositoriesParser():

    def parseAll(self, artifact):
        """ 
        Returns a list of RepositoryDefinition 
        artifact -- a dictionary or a list of dictionary to parse.
        """ 

        if not isinstance(artifact, dict) and not isinstance(artifact, list):
            return []
       
        repositories = []
        
        keyValueList = utils.keyValueList(artifact)
        for kv in keyValueList:
            if kv[0] ==  'repositories':
                values = kv[1]

                for k in values.keys():
                    item = values[k]
                    repo = self.parse(item)
                    if repo is not None:
                        repositories.append(repo)

        return repositories
    
    def parse(self, item):
        """ 
        Returns an RepositoryDefinition 
        item -- a dictionary to parse.
        """ 
        
        if not isinstance(item, dict):
            return None
        
        try:
            return RepositoryDefinition(
                url=item.get('url'),
                description=item.get('description'),
                credential=item.get('credential')
            )
        except TypeError:
            return None

        return None