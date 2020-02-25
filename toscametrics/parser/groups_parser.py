import toscametrics.utils as utils
from toscametrics.classes.definitions.group import GroupDefinition

class GroupsParser():

    def parseAll(self, artifact):
        """ 
        Returns a list of GroupDefinition
        artifact -- a dictionary or a list of dictionary to parse.
        """ 

        if not isinstance(artifact, dict) and not isinstance(artifact, list):
            return []

        groups = []

        keyValueList = utils.keyValueList(artifact)
        for kv in keyValueList:
            if kv[0] ==  'groups':
                values = kv[1]

                for d in values:
                    item = values[d]
                    
                    group = self.parse(item)
                    if group is not None:
                        groups.append(group)

        return groups


    def parse(self, item):
        """ 
        Returns an GroupDefinition
        item -- a dictionary to parse.
        """ 

        if not isinstance(item, dict):
            return None

        try:
            return GroupDefinition(
                type        = item.get('type'),
                description = item.get('description'),
                metadata    = item.get('metadata'),
                properties  = item.get('properties'),
                members     = item.get('members')
            )
        except (TypeError, ValueError):
            return None