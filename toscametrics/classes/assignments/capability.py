from toscametrics.classes.types.range_type import RangeType

class CapabilityAssignment():
    """
    A capability assignment allows node template authors to assign values to properties and attributes for a named capability definition that is part of a Node Template’s type definition.
    """

    def __init__(self, properties=None, attributes=None, occurrences=None):
        self.properties = properties
        self.attributes = attributes 
        self.occurrences = occurrences 

    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, value):
        if value is not None and not isinstance(value, dict):
            raise TypeError('Parameter value must be a dictionary')

        self.__properties = value

    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        if value is not None and not isinstance(value, dict):
            raise TypeError('Parameter value must be a dictionary')

        self.__attributes = value

    @property
    def occurrences(self):
        return self.__occurrences

    @occurrences.setter
    def occurrences(self, value):
        if value is not None and not isinstance(value, RangeType):
            raise TypeError('Parameter value must be an instance of RangeType')

        self.__occurrences = value
   

    def __eq__(self, other):
        return (isinstance(other, CapabilityAssignment) and
                self.properties  == other.properties    and
                self.attributes  == other.attributes    and
                self.occurrences == other.occurrences
        )