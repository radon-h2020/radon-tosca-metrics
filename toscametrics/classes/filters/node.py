from toscametrics.classes.filters.property import PropertyFilter
from toscametrics.classes.types.capability import CapabilityType

class NodeFilter():
    """
    A node filter definition defines criteria for selection of a TOSCA Node Template based upon the
    template’s property values, capabilities and capability properties.
    """
    
    def __init__(self, properties=None, capabilities=None):
        self.properties   = properties   # list of property filters
        self.capabilities = capabilities # list of capabilities names or capability type names

    @property
    def properties(self):
        return self.__properties
    
    @properties.setter
    def properties(self, value):
        if value is not None:
            if not isinstance(value, list):
                raise TypeError("Argument value must be an instance of list")
            
            for item in value:
                if not isinstance(item, PropertyFilter):
                    raise TypeError("Argument value must be a list of PropertyFilter")

        self.__properties = value

    @property
    def capabilities(self):
        return self.__capabilities
    
    @capabilities.setter
    def capabilities(self, value):
        if value is not None:
            if not isinstance(value, list):
                raise TypeError("Argument value must be an instance of list")
            
            for item in value:
                if not isinstance(item, CapabilityType):
                    raise TypeError("Argument value must be a list of CapabilityType")
            
        self.__capabilities = value

    def __eq__(self, other):
        if isinstance(other, NodeFilter):
            return self.__properties == other.properties and self.__capabilities == other.capabilities

        return False

    def __repr__(self):
        return '(properties: {}\ncapabilities: {}\n'.format(self.__properties, self.__capabilities)