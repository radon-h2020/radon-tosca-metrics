from toscametrics.classes.types.entity import EntityType

class EntityParser():

    def parse(self, d):
        """ 
        Returns a SchemaDefinition object, if any. None otherwise
        d - a dictionary to parse
        """        
        
        if not isinstance(d, dict):
            return None

        try:
            return EntityType(
                derivedFrom=d.get('derived_from'),
                version=d.get('version'),
                metadata=d.get('metadata'),
                description=d.get('description')
            )

        except Exception:
            return None