from toscametrics.classes.types.version import VersionType

class EntityType():
    """
    An Entity Type is the common, base, polymorphic schema type which is extended by TOSCA base entity
    type schemas (e.g., Node Type, Relationship Type, Artifact Type, etc.) and serves to define once all the
    commonly shared keynames and their types. This is a “meta” type which is abstract and not directly
    instantiatable.
    """

    def __init__(self, derivedFrom=None, version=None, metadata=None, description=None):
        self.derivedFrom = derivedFrom
        self.version = version
        self.metadata = metadata
        self.description = description

    @property
    def derivedFrom(self):
        return self.__derivedFrom  # parent node type name
    
    @derivedFrom.setter
    def derivedFrom(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError('Parameter value must be instance of string')
        self.__derivedFrom = value

    @property
    def version(self):
        return self.__version     #version number
    
    @version.setter
    def version(self, value):
        self.__version = None
        
        if value is not None:
            if not isinstance(value, str):
                raise TypeError('Parameter value must be instance of string')
            
            self.__version = VersionType(value)
        
    @property
    def metadata(self):
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        if value is not None:
            if not isinstance(value, dict):
                raise TypeError('Parameter value must be instance of dict')

            for k in value.keys():
                if not isinstance(value[k], str):
                    raise TypeError('Parameter value must be a map of string')

        self.__metadata = value 

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError('Parameter value must be instance of string')
        
        self.__description = value

    def __eq__(self, other):
        if isinstance(other, EntityType):
            return (self.derivedFrom == other.derivedFrom and 
                    self.version     == other.version and
                    self.metadata    == other.metadata and
                    self.description == other.description
                )

        return False

    def __repr__(self):
        return '(derived_from: {}\nversion: {}\nmetadata: {}\ndescription: {})'.format(self.derivedFrom, self.version, self.metadata, self.description)