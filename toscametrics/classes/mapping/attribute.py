class AttributeMapping():
    """ An attribute mapping allows to map the attribute of a substituted node type an output of the topology template. """

    def __init__(self, mapping=None):
        self.mapping = mapping   # An array with 1 string element that references an output of the topology

    @property
    def mapping(self):
        return self.__mapping

    @mapping.setter
    def mapping(self, value):
        if value is not None:
            if not isinstance(value, list) or len(value) != 1 or not isinstance(value[0], str):
                raise TypeError("Value must be a list containing one string")
                
        self.__mapping = value

    def __eq__(self, other):
        if isinstance(other, AttributeMapping):
            return (self.mapping == other.mapping)
                   
        return False