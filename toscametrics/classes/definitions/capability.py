from toscametrics.classes.definitions.property  import PropertyDefinition
from toscametrics.classes.definitions.attribute import AttributeDefinition
from toscametrics.classes.types.range_type      import RangeType

class CapabilityDefinition():
    """
    A capability definition defines a named, typed set of data that can be associated with Node Type or Node
    Template to describe a transparent capability or feature of the software component the node describes.
    """

    def __init__(self, type, description=None, properties=None, attributes=None, validSourceTypes=None, occurrences=None):

        self.type = type
        self.description = description
        self.properties = properties            # map of PropertyDefinition
        self.attributes = attributes            # map of AttributeDefinition
        self.validSourceTypes = validSourceTypes  # list of string
        self.occurrences = occurrences          # range of integer

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        if value is None or not isinstance(value, str):
            raise TypeError("Argument value must be an instance of string")
            
        self.__type = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Argument value must be an instance of string")
            
        self.__description = value
  
    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, value):
        if value is not None:
            if not isinstance(value, dict):
                raise TypeError("Argument value must be a dictionary")
            
            for k in value.keys():
                if not isinstance(value[k], PropertyDefinition):
                    raise TypeError("Argument value must be a map of PropertyDefinition")

        self.__properties = value

    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        if value is not None:
            if not isinstance(value, dict):
                raise TypeError("Argument value must be a dictionary")
            
            for k in value.keys():
                if not isinstance(value[k], AttributeDefinition):
                    raise TypeError("Argument value must be a map of AttributeDefinition")

        self.__attributes = value
  
    @property
    def validSourceTypes(self):
        return self.__validSourceTypes

    @validSourceTypes.setter
    def validSourceTypes(self, value):
        if value is not None:
            if not isinstance(value, list):
                raise TypeError("Argument value must be a list")
            
            for item in value:
                if not isinstance(item, str):
                    raise TypeError("Argument value must be a list of string")

        self.__validSourceTypes = value

    @property
    def occurrences(self):
        return self.__occurrences

    @occurrences.setter
    def occurrences(self, value):

        if value is not None:
            if not isinstance(value, list):
                raise TypeError("Argument value must be a list")
            
            if len(value) != 2:
                raise ValueError("Argument value must have length=2")

            self.__occurrences = RangeType(value[0], value[1])
        else:
            self.__occurrences = value    

    def __eq__(self, other):
        if isinstance(other, CapabilityDefinition):
            return (self.__type             == other.type            and 
                    self.__description      == other.description     and 
                    self.__properties       == other.properties      and 
                    self.__attributes       == other.attributes      and 
                    self.__validSourceTypes == other.validSourceTypes and
                    self.__occurrences      == other.occurrences
                   )

        return False

    def __repr__(self):
        return '(type: {}\ndescription: {}\nproperties: {}\nattributes: {}\nvalid_source_types: {}\noccurrences: {})'.format(self.__type, self.__description, self.__properties, self.__attributes, self.__validSourceTypes, self.__occurrences)