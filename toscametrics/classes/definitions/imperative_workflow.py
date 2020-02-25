from toscametrics.classes.definitions.operation_implementation import OperationImplementationDefinition
from toscametrics.classes.definitions.property                 import PropertyDefinition
from toscametrics.classes.definitions.workflow_precondition    import WorkflowPreconditionDefinition
from toscametrics.classes.definitions.workflow_step            import WorkflowStepDefinition
from toscametrics.classes.mapping.attribute                    import AttributeMapping


class ImperativeWorkflowDefinition():
    """
    A workflow step allows to define one or multiple sequenced activities in a workflow and how they are
    connected to other steps in the workflow. They are the building blocks of a declarative workflow.
    """

    def __init__(self, 
        description=None, 
        metadata=None, 
        inputs=None, 
        preconditions=None, 
        steps=None, 
        implementation=None, 
        outputs=None
        ):

        self.description = description
        self.metadata = metadata
        self.inputs = inputs
        self.preconditions = preconditions
        self.steps = steps             
        self.implementation = implementation        
        self.outputs = outputs         

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
        if value is not None:
            if not isinstance(value, dict):
                raise TypeError("Argument value must be a dictionary")
            
            for k in value.keys():
                if not isinstance(value[k], str):
                    raise TypeError("Argument value must be a map of strings")

        self.__metadata = value
        
    @property
    def inputs(self):
        return self.__inputs

    @inputs.setter
    def inputs(self, value):
        if value is not None:
            if not isinstance(value, dict):
                raise TypeError("Argument value must be a dictionary")
            
            for k in value.keys():
                if not isinstance(value[k], PropertyDefinition):
                    raise TypeError("Argument value must be a map of PropertyDefinition")

        self.__inputs = value
    
    @property
    def preconditions(self):
        return self.__preconditions

    @preconditions.setter
    def preconditions(self, value):
        if value is not None:
            if not isinstance(value, list):
                raise TypeError("Argument value must be a list")
            
            for item in value:
                if not isinstance(item, WorkflowPreconditionDefinition):
                    raise TypeError("Argument value must be a list of WorkflowPreconditionDefinition")

        self.__preconditions = value

    @property
    def steps(self):
        return self.__steps

    @steps.setter
    def steps(self, value):
        if value is not None:
            if not isinstance(value, dict):
                raise TypeError("Argument value must be a dictionary")
            
            for k in value.keys():
                if not isinstance(value[k], WorkflowStepDefinition):
                    raise TypeError("Argument value must be a map of WorkflowStepDefinition")

        self.__steps = value

    @property
    def implementation(self):
        return self.__implementation

    @implementation.setter
    def implementation(self, value):
        if value is not None and not isinstance(value, OperationImplementationDefinition):
            raise TypeError("Argument value must be an instance of OperationImplementationDefinition")
            
        self.__implementation = value

    @property
    def outputs(self):
        return self.__outputs

    @outputs.setter
    def outputs(self, value):
        if value is not None:
            if not isinstance(value, dict):
                raise TypeError("Argument value must be a dictionary")
            
            for k in value.keys():
                if not isinstance(value[k], AttributeMapping):
                    raise TypeError("Argument value must be a map of AttributeMapping")

        self.__outputs = value


    def __eq__(self, other):
        if isinstance(other, ImperativeWorkflowDefinition):
            return (self.description    == other.description    and 
                    self.metadata       == other.metadata       and 
                    self.inputs         == other.inputs         and 
                    self.preconditions  == other.preconditions  and 
                    self.steps          == other.steps          and 
                    self.implementation == other.implementation and 
                    self.outputs        == other.outputs
            )

        return False