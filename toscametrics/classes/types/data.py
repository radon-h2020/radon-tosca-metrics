from toscametrics.classes.clauses.constraints  import ConstraintClause
from toscametrics.classes.definitions.property import PropertyDefinition
from toscametrics.classes.definitions.schema   import SchemaDefinition
from toscametrics.classes.types.entity         import EntityType

    
class DataType(EntityType):
    """
    A Data Type definition defines the schema for new named datatypes in TOSCA.
    """

    def __init__(self, properties=None, constraints=None, keySchema=None, entrySchema=None):
       super(DataType, self).__init__()
       self.properties = properties     # map of property definitions
       self.constraints = constraints   # list of constraint clauses
       self.keySchema = keySchema     
       self.entrySchema = entrySchema     

    @property
    def properties(self):
        return self.__properties 

    @properties.setter
    def properties(self, value):
        if value is not None:
            if not isinstance(value, dict):
                raise TypeError('Parameter value must be a dictionary')
            
            for k in value.keys():
                if not isinstance(value[k], PropertyDefinition):
                    raise TypeError('Parameter value must be a map of PropertyDefinition')
            
        self.__properties = value

    @property
    def constraints(self):
        return self.__constraints 

    @constraints.setter
    def constraints(self, value):
        if value is not None:
            if not isinstance(value, list):
                raise TypeError('Parameter value must be a list')
            
            for item in value:
                if not isinstance(item, ConstraintClause):
                    raise TypeError('Parameter value must be a list of ConstraintClause')
            
        self.__constraints = value

    @property
    def keySchema(self):
        return self.__keySchema

    @keySchema.setter
    def keySchema(self, value):
        if value is not None and not isinstance(value, SchemaDefinition):
                raise TypeError('Parameter value must be an instance of SchemaDefinition')
            
        self.__keySchema = value

    @property
    def entrySchema(self):
        return self.__entrySchema

    @entrySchema.setter
    def entrySchema(self, value):
        if value is not None and not isinstance(value, SchemaDefinition):
                raise TypeError('Parameter value must be an instance of SchemaDefinition')
            
        self.__entrySchema = value

    def __eq__(self, other):
        return (super(DataType, self).__eq__(other) and 
            self.properties  == other.properties and 
            self.constraints == other.constraints and
            self.keySchema   == other.keySchema and
            self.entrySchema == other.entrySchema
        )

    def __repr__(self):
        return '(super: {}\nproperties: {}\nconstraints: {}\nkey_schema: {}\nentry_schema: {})'.format(super().__repr__(), self.properties, self.constraints, self.keySchema, self.entrySchema)