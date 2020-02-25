from toscametrics.classes.definitions.artifact import ArtifactDefinition

class OperationImplementationDefinition():
    """
    An operation implementation definition specifies one or more artifacts (e.g. scripts) to be used as the
    implementation for an operation in an interface.

    Grammar
    implementation: <primary_artifact_name> or
    implementation:
        primary: <primary_artifact_name>
        dependencies: 
            - <list_of_dependent_artifact_names>
        operation_host : SELF
        timeout : 60
    """

    def __init__(self, primary=None, dependencies=None, timeout=None, operationHost=None):
        self.primary = primary
        self.dependencies = dependencies      # list of ArtifactDefinition
        self.timeout = timeout
        self.operationHost = operationHost

    @property
    def primary(self):
        return self.__primary
   
    @primary.setter
    def primary(self, value):
        if value is not None and not isinstance(value, ArtifactDefinition):
            raise TypeError('Argument value must be an instance of ArtifactDefinition') 

        self.__primary = value

    @property
    def dependencies(self):
        return self.__dependencies
   
    @dependencies.setter
    def dependencies(self, value):
        if value is not None:
            if not isinstance(value, list):
                raise TypeError('Argument value must be a list') 

            for item in value:
                if not isinstance(item, ArtifactDefinition):
                    raise TypeError('Argument value must be an list of ArtifactDefinition') 

        self.__dependencies = value

    @property
    def operationHost(self):
        return self.__operationHost
   
    @operationHost.setter
    def operationHost(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError('Argument value must be a string') 

        self.__operationHost = value

    @property
    def timeout(self):
        return self.__timeout
   
    @timeout.setter
    def timeout(self, value):
        if value is not None and not isinstance(value, int) or value == True or value == False :
            raise TypeError('Argument value must be an integer') 

        self.__timeout = value

    def __eq__(self, other):
        if isinstance(other, OperationImplementationDefinition):
            return (self.primary       == other.primary       and 
                    self.dependencies  == other.dependencies  and
                    self.operationHost == other.operationHost and
                    self.timeout       == other.timeout)

        return False