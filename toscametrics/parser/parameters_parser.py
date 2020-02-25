import toscametrics.utils as utils
from toscametrics.classes.definitions.parameter  import ParameterDefinition
from toscametrics.parser.constraints_parser      import ConstraintsParser
from toscametrics.parser.schema_parser           import SchemaParser

class ParametersParser():

    def parseAll(self, artifact):
        """ 
        Returns a list of ParameterDefinition
        artifact -- a dictionary or a list of dictionary to parse.
        """ 

        if not isinstance(artifact, dict) and not isinstance(artifact, list):
            return []

        parameters = []

        keyValueList = utils.keyValueList(artifact)
        for kv in keyValueList:
            if kv[0] ==  'properties':
                values = kv[1]
                
                for d in values:
                    item = values[d]
                    property = self.parse(item)
                    if property is not None:
                        parameters.append(property)

        return parameters

    def parse(self, item):
        """ 
        Returns a ParameterDefinition
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

            return ParameterDefinition(
                    type=item.get('type'),
                    value=item.get('value'),
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
