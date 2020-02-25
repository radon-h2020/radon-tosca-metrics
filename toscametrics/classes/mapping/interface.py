class InterfaceMapping():
    """
    An interface mapping allows to map a workflow of the topology template to an operation of the node type the service template offers an implementation for.
    """

    def __init__(self, mapping=None, properties=None, attributes=None):
        self.properties = properties    # map of property assignments

    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, value):
        if value is not None:
            if not isinstance(value, dict):
                raise TypeError("Value must be a map of property assignments")
                
        self.__properties = value

    def __eq__(self, other):
        return isinstance(other, InterfaceMapping) and self.properties == other.properties