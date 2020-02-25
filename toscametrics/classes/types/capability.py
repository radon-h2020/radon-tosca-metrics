from toscametrics.classes.definitions.attribute import AttributeDefinition
from toscametrics.classes.definitions.property  import PropertyDefinition
from toscametrics.classes.types.entity          import EntityType

class CapabilityType(EntityType):
    """
    The Capability Type is a TOSCA Entity and has the common keynames as TOSCA Entity Schema.
    """  
    def __init__(self, properties=None, attributes=None, validSourceTypes=None):
       super(CapabilityType, self).__init__()
       self.properties = properties # map of property definitions
       self.attributes = attributes # map of attribute definitions (definitions.AttributeDefinition)
       self.validSourceTypes = validSourceTypes # list of strings

    @property
    def properties(self):
        return self.__properties 

    @properties.setter
    def properties(self, value):
        if value is not None:
            if not isinstance(value, dict):
                raise TypeError('Parameter value must be a dictionary')
            
            for k in value.keys():
                if not isinstance(value[k], PropertyDefinition):
                    raise TypeError('Parameter value must be a map of PropertyDefinition')
            
        self.__properties = value

    @property
    def attributes(self):
        return self.__attributes 

    @attributes.setter
    def attributes(self, value):
        if value is not None:
            if not isinstance(value, dict):
                raise TypeError('Parameter value must be a dictionary')
            
            for k in value.keys():
                if not isinstance(value[k], AttributeDefinition):
                    raise TypeError('Parameter value must be a map of AttributeDefinition')
            
        self.__attributes = value


    @property
    def validSourceTypes(self):
        return self.__validSourceTypes 

    @validSourceTypes.setter
    def validSourceTypes(self, value):
        if value is not None:
            if not isinstance(value, list):
                raise TypeError('Parameter value must be a list')
            
            for item in value:
                if not isinstance(item, str):
                    raise TypeError('Parameter value must be a list of strings')
            
        self.__validSourceTypes = value

    def __eq__(self, other):
        return (super(CapabilityType, self).__eq__(other) and 
            self.properties == other.properties and 
            self.attributes == other.attributes and
            self.validSourceTypes == other.validSourceTypes
        )

    def __repr__(self):
        return 'super: {}\nproperties: {}\nattributes: {}\nvalid_source_types: {})'.format(super().__repr__(), self.properties, self.attributes, self.validSourceTypes)
