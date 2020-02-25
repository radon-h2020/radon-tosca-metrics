class CapabilityMapping():
    """
    A capability mapping allows to map the capability of one of the node of the topology template to the capability of the node type the service template offers an implementation for.
    """

    def __init__(self, mapping=None, properties=None, attributes=None):
        self.mapping = mapping          # list of 2 strings
        self.properties = properties    # map of property assignments
        self.attributes = attributes    # map of attributes assignments

    @property
    def mapping(self):
        return self.__mapping

    @mapping.setter
    def mapping(self, value):
        if value is not None:
            if not isinstance(value, list) or len(value) != 2 or not isinstance(value[0], str) or not isinstance(value[1], str):
                raise TypeError("Value must be a list containing two strings")
                
        self.__mapping = value

    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, value):
        if value is not None:
            if not isinstance(value, dict):
                raise TypeError("Value must be a map of property assignments")
                
        self.__properties = value

    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        if value is not None:
            if not isinstance(value, dict):
                raise TypeError("Value must be a map of attributes assignments")
                
        self.__attributes = value

    def __eq__(self, other):
        return (isinstance(other, CapabilityMapping) and 
                self.mapping    == other.mapping     and 
                self.properties == other.properties  and 
                self.attributes == other.attributes)