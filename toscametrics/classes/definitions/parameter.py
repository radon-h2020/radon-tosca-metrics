from toscametrics.classes.definitions.property import PropertyDefinition

class ParameterDefinition(PropertyDefinition):
    """
    A parameter definition is essentially a TOSCA property definition; however, it also allows a value to be assigned to it (as for a TOSCA property assignment). 
    In addition, in the case of output parameters, it can optionally inherit the data type of the value assigned to it rather than have an explicit data type defined for it
    """
    def __init__(self, type=None, value=None, description=None, required=True, default=None, status='supported', constraints=None, keySchema=None, entrySchema=None, externalSchema=None, metadata=None):
        super(ParameterDefinition, self).__init__('', description, required, default, status, constraints, keySchema, entrySchema, externalSchema, metadata)
        self.type = type
        self.value = value # value = <any>
        
    @property
    def type(self):
        return self.__type
    
    @type.setter
    def type(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError('Argument value must be a string') 
        
        self.__type = value

    def __eq__(self, other):
        return super(ParameterDefinition, self).__eq__(other) and self.value == other.value

    def __repr__(self):
        return '(type: {}\ndescription: {}\nrequired: {}\ndefault: {}\nstatus: {}\nconstraints: {}\nkey_schema: {}\nentry_schema: {}\nexternal_schema: {}\nmetadata: {}\nvalue: {})'.format(self.type, self.description, self.required, self.default, self.status,  self.constraints, self.keySchema, self.entrySchema, self.externalSchema, self.metadata, self.value)