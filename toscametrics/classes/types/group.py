from toscametrics.classes.definitions.attribute import AttributeDefinition
from toscametrics.classes.definitions.property  import PropertyDefinition
from toscametrics.classes.types.entity          import EntityType

class GroupType(EntityType):
    """
    A Group Type defines logical grouping types for nodes, typically for different management purposes.
    Conceptually, group definitions allow the creation of logical “membership” relationships to nodes in a
    service template that are not a part of the application’s explicit requirement dependencies in the topology
    template (i.e. those required to actually get the application deployed and running). Instead, such logical
    membership allows for the introduction of things such as group management and uniform application of
    policies (i.e., requirements that are also not bound to the application itself) to the group’s members.
    """
    def __init__(self, properties=None, attributes=None, members=None):
       super(GroupType, self).__init__()
       self.properties = properties # map of property definitions
       self.attributes = attributes # map of attribute definitions (definitions.AttributeDefinition)
       self.members = members # list of strings

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
    def members(self):
        return self.__members 

    @members.setter
    def members(self, value):
        if value is not None:
            if not isinstance(value, list):
                raise TypeError('Parameter value must be a list')
            
            for item in value:
                if not isinstance(item, str):
                    raise TypeError('Parameter value must be a list of strings')
            
        self.__members = value

    def __eq__(self, other):
        return (super(GroupType, self).__eq__(other) and 
            self.properties == other.properties and 
            self.attributes == other.attributes and
            self.members    == other.members
        )

    def __repr__(self):
        return 'super: {}\nproperties: {}\nattributes: {}\nmembers: {})'.format(super().__repr__(), self.properties, self.attributes, self.members)