class ArtifactDefinition():
    """
    An artifact definition defines a named, typed file that can be associated with Node Type or Node
    Template and used by orchestration engine to facilitate deployment and implementation of interface
    operations.

    Grammar <interface_definition_name>:
              type: <interface_type_name>
              inputs: <property_definitions>
              operations: <operation_definitions>
              notifications: <notification definitions>
    """

    def __init__(self, type, file, repository=None, description=None, deployPath=None, artifactVersion=None, checksum=None, checksumAlgorithm=None, properties=None):
        self.type = type
        self.file = file
        self.repository = repository
        self.description = description
        self.deployPath = deployPath
        self.artifactVersion = artifactVersion
        self.checksum = checksum
        self.checksumAlgorithm = checksumAlgorithm
        self.properties = properties   # map of PropertyAssignment
        
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        if value is None or not isinstance(value, str):
            raise TypeError("Argument value must be an instance of string")
            
        self.__type = value 

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, value):
        if value is None or not isinstance(value, str):
            raise TypeError("Argument value must be an instance of string")
            
        self.__file = value

    @property
    def repository(self):
        return self.__repository

    @repository.setter
    def repository(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Argument value must be an instance of string")
            
        self.__repository = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Argument value must be an instance of string")
            
        self.__description = value

    @property
    def deployPath(self):
        return self.__deployPath

    @deployPath.setter
    def deployPath(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Argument value must be an instance of string")
            
        self.__deployPath = value

    @property
    def artifactVersion(self):
        return self.__artifactVersion

    @artifactVersion.setter
    def artifactVersion(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Argument value must be an instance of string")
            
        self.__artifactVersion = value

    @property
    def checksum(self):
        return self.__checksum

    @checksum.setter
    def checksum(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Argument value must be an instance of string")
            
        self.__checksum = value

    @property
    def checksumAlgorithm(self):
        return self.__checksumAlgorithm

    @checksumAlgorithm.setter
    def checksumAlgorithm(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Argument value must be an instance of string")
            
        self.__checksumAlgorithm = value

    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, value):
        if value is not None and not isinstance(value, dict):
            raise TypeError("Argument value must be a map of property assignments")
            
        self.__properties = value

     
    def __eq__(self, other):
        if isinstance(other, ArtifactDefinition):
            return (self.type              == other.type            and 
                    self.file              == other.file            and 
                    self.description       == other.description     and 
                    self.repository        == other.repository      and 
                    self.deployPath        == other.deployPath      and 
                    self.artifactVersion   == other.artifactVersion and 
                    self.checksum          == other.checksum        and 
                    self.checksumAlgorithm == other.checksumAlgorithm and
                    self.properties        == other.properties 
                   )

        return False