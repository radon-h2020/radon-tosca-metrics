import toscametrics.utils as utils
from toscametrics.classes.definitions.property  import PropertyDefinition
from toscametrics.parser.constraints_parser     import ConstraintsParser
from toscametrics.parser.schema_parser          import SchemaParser

class PropertiesParser():

    def parseAll(self, artifact):
        """ 
        Returns a list of PropertyDefinition
        artifact -- a dictionary or a list of dictionary to parse.
        """ 

        if not isinstance(artifact, dict) and not isinstance(artifact, list):
            return []

        properties = []

        keyValueList = utils.keyValueList(artifact)
        for kv in keyValueList:
            if kv[0] ==  'properties':
                values = kv[1]
                
                for d in values:
                    item = values[d]
                    property = self.parse(item)
                    if property is not None:
                        properties.append(property)

        return properties

    def parse(self, item):
        """ 
        Returns a PropertyDefinition
        item -- a dictionary to parse.
        """ 

        if not isinstance(item, dict):
            return None
        
        cp = ConstraintsParser()
        sp = SchemaParser()

        try:
            constraints = cp.parseAll(item)
            if len(constraints) == 0:
                constraints = None

            return PropertyDefinition(
                    type=item.get('type'),
                    description=item.get('description'),
                    required=utils.str2bool(item.get('default')),
                    default=item.get('default'),
                    status=item.get('status'),
                    constraints=constraints,
                    keySchema=sp.parse(item.get('key_schema')),
                    entrySchema=sp.parse(item.get('entry_schema')),
                    externalSchema=item.get('external_schema'),
                    metadata=item.get('metadata')
            )
        except (TypeError, ValueError):
            return None
