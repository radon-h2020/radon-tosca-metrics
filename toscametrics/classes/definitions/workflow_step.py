from toscametrics.classes.clauses.constraints import ConstraintClause
from toscametrics.classes.definitions.activity.activity_definition import ActivityDefinition


class WorkflowStepDefinition():
    """
    A workflow step allows to define one or multiple sequenced activities in a workflow and how they are
    connected to other steps in the workflow. They are the building blocks of a declarative workflow.
    """

    def __init__(self, 
        target, 
        targetRelationship=None, 
        operationHost=None, 
        filter=None, 
        activities=None, 
        onSuccess=None, 
        onFailure=None):

        self.target = target
        self.targetRelationship = targetRelationship
        self.operationHost = operationHost
        self.filter = filter             # list of ConstraintClause
        self.activities = activities         # list of ActivityDefinition
        self.onSuccess = onSuccess          # list of String
        self.onFailure = onFailure          # list of String

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
    def operationHost(self):
        return self.__operationHost

    @operationHost.setter
    def operationHost(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError("Argument value must be an instance of string")
            
        self.__operationHost = value
    
    @property
    def filter(self):
        return self.__filter

    @filter.setter
    def filter(self, value):
        if value is not None:
            if not isinstance(value, list):
                raise TypeError("Argument value must be a list")
            
            for item in value:
                if not isinstance(item, ConstraintClause):
                    raise TypeError("Argument value must be a list of ConstraintClause")

        self.__filter = value
            
    @property
    def activities(self):
        return self.__activities

    @activities.setter
    def activities(self, value):
        if value is not None:
            if not isinstance(value, list):
                raise TypeError("Argument value must be a list")
            
            for item in value:
                if not isinstance(item, ActivityDefinition):
                    raise TypeError("Argument value must be a list of ActivityDefinition")

        self.__activities = value

    @property
    def onSuccess(self):
        return self.__onSuccess

    @onSuccess.setter
    def onSuccess(self, value):
        if value is not None:
            if not isinstance(value, list):
                raise TypeError("Argument value must be a list")
            
            for item in value:
                if not isinstance(item, str):
                    raise TypeError("Argument value must be a list of string")

        self.__onSuccess = value

    @property
    def onFailure(self):
        return self.__onFailure

    @onFailure.setter
    def onFailure(self, value):
        if value is not None:
            if not isinstance(value, list):
                raise TypeError("Argument value must be a list")
            
            for item in value:
                if not isinstance(item, str):
                    raise TypeError("Argument value must be a list of string")

        self.__onFailure = value


    def __eq__(self, other):
        if isinstance(other, WorkflowStepDefinition):
            return (self.target             == other.target             and 
                    self.targetRelationship == other.targetRelationship and 
                    self.operationHost      == other.operationHost      and 
                    self.filter             == other.filter             and 
                    self.activities         == other.activities         and 
                    self.onSuccess          == other.onSuccess          and 
                    self.onFailure          == other.onFailure
            )

        return False