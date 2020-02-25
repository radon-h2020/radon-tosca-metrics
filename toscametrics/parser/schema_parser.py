from toscametrics.classes.definitions.schema import SchemaDefinition 
from toscametrics.parser.constraints_parser import ConstraintsParser 

class SchemaParser():

    def parse(self, d):
        """ 
        Returns a SchemaDefinition object, if any. None otherwise
        d - a dictionary to parse
        """        
        
        if not isinstance(d, dict):
            return None

        try:
            cp = ConstraintsParser()
            constraints = cp.parseAll({'constraints':d.get('constraints')})
            if len(constraints) == 0:
                constraints = None

            return SchemaDefinition(
                type=d.get('type'),
                description=d.get('description'),
                constraints=constraints,
                keySchema=self.parse(d.get('key_schema')),
                entrySchema=self.parse(d.get('entry_schema'))
            )

        except Exception:
            return None