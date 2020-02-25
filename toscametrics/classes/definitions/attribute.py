from toscametrics.classes.definitions.schema import SchemaDefinition

class AttributeDefinition():
    """
    An attribute definition defines a named, typed value that can be associated with an entity defined in the TOSCA specification.
    Specifically, it is used to expose the “actual state” of some property of a TOSCA entity after it has been deployed and instantiated (as set by the TOSCA 
    orchestrator). 
    Attribute values can be retrieved via the get_attribute function from the instance model and used as values to other entities within TOSCA Service Templates.
    """

    def __init__(self, type, description=None, default=None, status=None, keySchema=None, entrySchema=None):
        self.type        = type
        self.description = description
        self.default     = default          # <Any> An optional key that may provide a value to be used as a default if not provided by another means. 
        self.status      = status
        self.keySchema   = keySchema
        self.entrySchema = entrySchema

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
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Argument value must be an instance of string")
            
        self.__status = value

    @property
    def keySchema(self):
        return self.__keySchema

    @keySchema.setter
    def keySchema(self, value):
        if value is not None and not isinstance(value, SchemaDefinition):
            raise TypeError("Argument value must be an instance of SchemaDefinition")
            
        self.__keySchema = value
  
    @property
    def entrySchema(self):
        return self.__entrySchema

    @entrySchema.setter
    def entrySchema(self, value):
        if value is not None and not isinstance(value, SchemaDefinition):
            raise TypeError("Argument value must be an instance of SchemaDefinition")
            
        self.__entrySchema = value
 
    def __eq__(self, other):
        if isinstance(other, AttributeDefinition):
            return (self.__type         == other.type           and 
                    self.__description  == other.description    and 
                    self.default        == other.default        and 
                    self.__status       == other.status         and 
                    self.__keySchema    == other.keySchema      and
                    self.__entrySchema  == other.entrySchema
                   )

        return False

    def __repr__(self):
        return '(type: {}\ndescription: {}\ndefault: {}\nstatus: {}\nkey_schema: {}\nentry_schema: {})'.format(self.__type, self.__description, self.default, self.__status, self.__keySchema, self.__entrySchema)