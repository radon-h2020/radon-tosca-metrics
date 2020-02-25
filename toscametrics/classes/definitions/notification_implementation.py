from toscametrics.classes.definitions.artifact import ArtifactDefinition

class NotificationImplementationDefinition():
    """
    A notification implementation definition specifies one or more artifacts to be used by the orchestrator to
    subscribe to that particular notification. We use the primary and dependencies keynames as in the
    operation implementation definition. 

    Grammar
    implementation: <primary_artifact_name>
    implementation:
        primary: <primary_artifact_name>
        dependencies:
            - <list_of_dependent_artifact_names>
    """

    def __init__(self, primary=None, dependencies=None):
        self.primary = primary
        self.dependencies = dependencies      # list of ArtifactDefinition

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

    def __eq__(self, other):
        if isinstance(other, NotificationImplementationDefinition):
            return (self.primary == other.primary and self.dependencies  == other.dependencies)

        return False