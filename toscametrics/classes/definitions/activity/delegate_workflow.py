from toscametrics.classes.definitions.activity.activity_definition import ActivityDefinition

class DelegateWorkflowActivityDefinition(ActivityDefinition):
    """
    Defines the name of the delegate workflow and optional input assignments. This activity
    requires the target to be provided by the orchestrator (no-op node or relationship).

    Grammar
    - delegate: <delegate_workflow_name> or
    - delegate:
        workflow: <delegate_workflow_name>
        inputs: <parameter_assignments>

    """
    def __init__(self, delegate, workflow=None, inputs=None):
        self.delegate = delegate
        self.workflow = workflow
        self.inputs = inputs            # map of parameter assignments


    @property
    def delegate(self):
        return self.__delegate

    @delegate.setter
    def delegate(self, value):
        if value is None or not isinstance(value, str):
            raise TypeError("Argument value must be an instance of string")
            
        self.__delegate = value

    @property
    def workflow(self):
        return self.__workflow

    @workflow.setter
    def workflow(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Argument value must be an instance of string")
            
        self.__workflow = value

    @property
    def inputs(self):
        return self.__inputs

    @inputs.setter
    def inputs(self, value):
        if value is not None and not isinstance(value, dict):
            raise TypeError("Argument value must be an instance of string")
            
        self.__inputs = value

    def __eq__(self, other):
        if isinstance(other, DelegateWorkflowActivityDefinition):
            return (self.delegate == other.delegate and
                    self.workflow == other.workflow and
                    self.inputs   == other.inputs
            )

        return False    
