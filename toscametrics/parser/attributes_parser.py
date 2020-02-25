import toscametrics.utils as utils
from toscametrics.classes.definitions.attribute import AttributeDefinition
from toscametrics.parser.schema_parser import SchemaParser

class AttributesParser():

    def parseAll(self, artifact):
        """ 
        Returns a list of AttributesDefinition
        artifact -- a dictionary or a list of dictionary to parse.
        """ 

        if not isinstance(artifact, dict) and not isinstance(artifact, list):
            return []

        attributes = []

        keyValueList = utils.keyValueList(artifact)
        for kv in keyValueList:
            if kv[0] ==  'attributes':
                values = kv[1]

                for d in values:
                    item = values[d]
                    
                    attribute = self.parse(item)
                    if attribute is not None:
                        attributes.append(attribute)

        return attributes


    def parse(self, item):
        """ 
        Returns an AttributesDefinition
        item -- a dictionary to parse.
        """ 

        if not isinstance(item, dict):
            return None

        sp = SchemaParser()

        try:
            return AttributeDefinition(
                type        = item.get('type'),
                description = item.get('description'),
                default     = item.get('default'),
                status      = item.get('status'),
                keySchema   = sp.parse(item.get('key_schema')),
                entrySchema = sp.parse(item.get('entry_schema'))
            )
        except (TypeError, ValueError):
            return None