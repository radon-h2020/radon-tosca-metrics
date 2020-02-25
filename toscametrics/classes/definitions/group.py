
class GroupDefinition():
    """
    A group definition defines a logical grouping of node templates, typically for management purposes, but is
    separate from the application’s topology template.
    """

    def __init__(self, type, description=None, metadata=None, properties=None, members=None):
        self.type = type
        self.description = description
        self.metadata = metadata        # map of string
        self.properties = properties    # map of property assignments
        self.members = members          # list of string

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
    def metadata(self):
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        if value is not None and not isinstance(value, dict):
            raise TypeError("Argument value mulist be a map of strings")
            
        self.__metadata = value

    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, value):
        if value is not None and not isinstance(value, dict):
            raise TypeError("Argument value must be a map of property assignments")
            
        self.__properties = value

    @property
    def members(self):
        return self.__members

    @members.setter
    def members(self, value):
        if value is not None:
            if not isinstance(value, list):
                raise TypeError("Argument value must be a list")
            
            for item in value:
                if not isinstance(item, str):
                    raise ValueError("Argument value must be a list of strings")

        self.__members = value
     
    def __eq__(self, other):
        if isinstance(other, GroupDefinition):
            return (self.type        == other.type        and 
                    self.description == other.description and 
                    self.metadata    == other.metadata    and 
                    self.properties  == other.properties  and
                    self.members     == other.members 
                   )

        return False