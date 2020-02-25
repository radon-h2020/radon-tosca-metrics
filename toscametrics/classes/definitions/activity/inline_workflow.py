from toscametrics.classes.definitions.activity.activity_definition import ActivityDefinition

class InlineWorkflowActivityDefinition(ActivityDefinition):
    """
    Inline another workflow defined in the topology (to allow reusability). The definition includes the
    name of a workflow to be inlined and optional workflow input assignments.
   
    Grammar
    - inline: <inlined_workflow_name> or
    - inline:
        workflow: <inlined_workflow_name>
        inputs: <parameter_assignments>
    """

    def __init__(self, inline, workflow=None, inputs=None):
        self.inline = inline
        self.workflow = workflow
        self.inputs = inputs            # map of parameter assignments

    @property
    def inline(self):
        return self.__inline

    @inline.setter
    def inline(self, value):
        if value is None or not isinstance(value, str):
            raise TypeError("Argument value must be an instance of string")
            
        self.__inline = value

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
        if isinstance(other, InlineWorkflowActivityDefinition):
            return (self.inline   == other.inline and
                    self.workflow == other.workflow and
                    self.inputs   == other.inputs
            )

        return False    

    def __repr__(self):
        return '(inline: {}\nworkflow: {}\ninputs: {})'.format(self.inline, self.workflow, self.inputs)