from toscametrics.classes.clauses.constraints import ConstraintClause

class SchemaDefinition():
    """
    All entries in a map or list for one property or parameter must be of the same type. 
    Similarly, all keys for map entries for one property or parameter must be of the same type as well. 
    A TOSCA schema definition specifies the type (for simple entries) or schema (for complex entries) for keys and entries in TOSCA set types such as the TOSCA list or map
    """

    def __init__(self, type, description=None, constraints=None, keySchema=None, entrySchema=None):
        self.type = type
        self.description = description
        self.constraints = constraints   # List of constraints clauses (of class clauses.ConstraintClause)
        self.keySchema   = keySchema     # map of SchemaDefinition
        self.entrySchema = entrySchema   # map of SchemaDefinition

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
    def constraints(self):
        return self.__constraints

    @constraints.setter
    def constraints(self, value):
        if value is not None:
            if not isinstance(value, list):
                raise TypeError("Argument value must be an instance of list")
            
            for item in value:
                if not isinstance(item, ConstraintClause):
                    raise TypeError("Argument in list must be instances of ConstraintClause")

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
 
    def __eq__(self, other):
        if isinstance(other, SchemaDefinition):
            return (self.__type        == other.type and 
                    self.__description == other.description and 
                    self.__constraints == other.constraints and 
                    self.__keySchema   == other.keySchema and 
                    self.__entrySchema == other.entrySchema
                   )
                   
        return False

    def __repr__(self):
        return '(type: {}\ndescription: {}\nconstraints: {}\nkey_schema: {}\nentry_schema: {})\n'.format(self.__type, self.__description, self.__constraints, self.__keySchema, self.__entrySchema)