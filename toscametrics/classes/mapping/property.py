class PropertyMapping():
    """
    A property mapping allows to map the property of a substituted node type an input of the topology template.
    """

    def __init__(self, mapping=None, value=None):
        self.mapping = mapping   # list of 1 string
        self.value = value       # deprecated

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
        return (isinstance(other, PropertyMapping) and self.mapping == other.mapping and self.value == other.value)