from toscametrics.classes.definitions.activity.activity_definition import ActivityDefinition

class CallOperationActivityDefinition(ActivityDefinition):
    """
    Calls an operation defined on a TOSCA interface of a node, relationship or group. The
    operation name uses the <interface_name>.<operation_name> notation. Optionally,
    assignments for the operation inputs can also be provided. If provided, they will override
    for this operation call the operation inputs assignment in the node template.

    Grammar
    - call_operation: <operation_name> or
    - call_operation:
        operation: <operation_name>
        inputs: <parameter_assignments>
    """

    def __init__(self, callOperation, operation=None, inputs=None):
        self.callOperation = callOperation
        self.operation = operation
        self.inputs = inputs            # map of parameter assignments

    @property
    def callOperation(self):
        return self.__callOperation

    @callOperation.setter
    def callOperation(self, value):
        if value is None or not isinstance(value, str):
            raise TypeError("Argument value must be an instance of string")
            
        self.__callOperation = value

    @property
    def operation(self):
        return self.__operation

    @operation.setter
    def operation(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Argument value must be an instance of string")
            
        self.__operation = value

    @property
    def inputs(self):
        return self.__inputs

    @inputs.setter
    def inputs(self, value):
        if value is not None and not isinstance(value, dict):
            raise TypeError("Argument value must be an instance of string")
            
        self.__inputs = value

    def __eq__(self, other):
        if isinstance(other, CallOperationActivityDefinition):
            return (self.callOperation == other.callOperation and
                    self.operation     == other.operation     and
                    self.inputs        == other.inputs
            )

        return False    

    def __repr__(self):
        return '(call_operation: {}\noperation: {}\ninputs: {})'.format(self.callOperation, self.operation, self.inputs)