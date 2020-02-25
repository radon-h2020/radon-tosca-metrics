from toscametrics.classes.clauses.constraints import ConstraintClause
from toscametrics.classes.definitions.schema  import SchemaDefinition

class PropertyDefinition():
    """
    A property definition defines a named, typed value and related data that can be associated with an entity
    defined in this specification (e.g., Node Types, Relationship Types, Capability Types, etc.). Properties
    are used by template authors to provide input values to TOSCA entities which indicate their “desired
    state” when they are instantiated.
    """

    def __init__(self, type, description=None, required=True, default=None, status='supported', constraints=None, keySchema=None, entrySchema=None, externalSchema=None, metadata=None):
        self.type        = type
        self.description = description
        self.required    = required
        self.default     = default          # <Any> An optional key that may provide a value to be used as a default if not provided by another means. 
        self.status      = status
        self.constraints = constraints
        self.keySchema   = keySchema
        self.entrySchema = entrySchema
        self.externalSchema = externalSchema
        self.entrySchema = entrySchema
        self.metadata    = metadata

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
    def required(self):
        return self.__required

    @required.setter
    def required(self, value):
        if value is None:
            self.__required = True
        elif not isinstance(value, bool):
            raise TypeError("Argument value must be a boolean")
        else:
            self.__required = value
  
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        if value is None:
            self.__status = 'supported'
        elif not isinstance(value, str):
            raise TypeError("Argument value must be an instance of string")
        else:
            self.__status = value
  
    @property
    def constraints(self):
        return self.__constraints

    @constraints.setter
    def constraints(self, value):
        if value is not None:
            if not isinstance(value, list):
                raise TypeError("Argument value must be an instance of string")
            
            for item in value:
                if not isinstance(item, ConstraintClause):
                    raise TypeError("Items in list 'value' must be instances of ConstraintClause")
            
        self.__constraints = value

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
          
    @property
    def externalSchema(self):
        return self.__externalSchema

    @externalSchema.setter
    def externalSchema(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Argument value must be an instance of string")
            
        self.__externalSchema = value
          
    @property
    def metadata(self):
        return self.__metadata

    @metadata.setter
    def metadata(self, value):
        if value is not None:
            if not isinstance(value, dict):
                raise TypeError("Argument value must be a dictionary")
            
            for k in value.keys():
                if not isinstance(value[k], str):
                    raise TypeError("Argument value must be a map of string")
            
        self.__metadata = value
 
    def __eq__(self, other):
        if isinstance(other, PropertyDefinition):
            return (self.type         == other.type           and 
                    self.description  == other.description    and 
                    self.required     == other.required       and 
                    self.default        == other.default        and 
                    self.status       == other.status         and 
                    self.constraints  == other.constraints    and 
                    self.keySchema    == other.keySchema      and
                    self.entrySchema  == other.entrySchema    and
                    self.externalSchema  == other.externalSchema    and
                    self.metadata     == other.metadata
                   )

        return False

    def __repr__(self):
        return '(type: {}\ndescription: {}\nrequired: {}\ndefault: {}\nstatus: {}\nconstraints: {}\nkey_schema: {}\nentry_schema: {}\nexternal_schema: {}\nmetadata: {})'.format(self.__type, self.__description, self.__required, self.default, self.__status,  self.__constraints, self.__keySchema, self.__entrySchema, self.__externalSchema, self.__metadata)