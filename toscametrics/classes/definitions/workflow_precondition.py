from toscametrics.classes.clauses.conditions import ConditionClause

class WorkflowPreconditionDefinition():
    """
    A workflow condition can be used as a filter or precondition to check if a workflow can be processed or
    not based on the state of the instances of a TOSCA topology deployment.
    """

    def __init__(self, target, targetRelationship=None, condition=None):
        self.target = target
        self.targetRelationship = targetRelationship
        self.condition = condition            # list of ConditionClause

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        if value is None or not isinstance(value, str):
            raise TypeError("Argument value must be an instance of string")
            
        self.__target = value

    @property
    def targetRelationship(self):
        return self.__targetRelationship

    @targetRelationship.setter
    def targetRelationship(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Argument value must be an instance of string")
            
        self.__targetRelationship = value
    
    @property
    def condition(self):
        return self.__condition

    @condition.setter
    def condition(self, value):
        if value is not None:
            if not isinstance(value, list):
                raise TypeError("Argument value must be a list")
            
            for item in value:
                if not isinstance(item, ConditionClause):
                    raise TypeError("Argument value must be a list of ConditionClause")

        self.__condition = value

    
    def __eq__(self, other):
        if isinstance(other, WorkflowPreconditionDefinition):
            return (self.target             == other.target             and 
                    self.targetRelationship == other.targetRelationship and 
                    self.condition          == other.condition
                    )

        return False