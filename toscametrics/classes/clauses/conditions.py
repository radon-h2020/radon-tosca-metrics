class ConditionClause():
    """
    A workflow condition clause definition is used to specify a condition that can be used within a workflow precondition or workflow filter.

    Grammar
    and: <list_of_condition_clause_definition>
    or: <list_of_condition_clause_definition>
    not: <list_of_condition_clause_definition>
    (direct assertion definition) <attribute_name>: <list_of_constraint_clauses>

    """
    
    def __init__(self, pAnd=None, pOr=None, pNot=None, pAssert=None):
        self.And = pAnd    # list of ConditionClause
        self.Or  = pOr      # list of ConditionClause
        self.Not = pNot      # list of ConditionClause
        self.Assert = pAssert   # list of AssertionDefinition: <attribute_name>: <list_of_constraint_clauses>

    @property
    def And(self):
        return self.__and
        
    @And.setter
    def And(self, value):
        if value is not None and not isinstance(value, list) and not isinstance(value, ConditionClause):
            raise TypeError("Argument value must be an instance of list")

        self.__and = value

    @property
    def Or(self):
        return self.__or
        
    @Or.setter
    def Or(self, value):
        if value is not None and not isinstance(value, list) and not isinstance(value, ConditionClause):
            raise TypeError("Argument value must be an instance of list")

        self.__or = value

    @property
    def Not(self):
        return self.__not
        
    @Not.setter
    def Not(self, value):
        if value is not None and not isinstance(value, list) and not isinstance(value, ConditionClause):
            raise TypeError("Argument value must be an instance of list")

        self.__not = value

    @property
    def Assert(self):
        return self.__not
        
    @Assert.setter
    def Assert(self, value):
        if value is not None and not isinstance(value, list) and not isinstance(value, ConditionClause):
            raise TypeError("Argument value must be an instance of list")

        self.__assert = value


    def __eq__(self, other):
        if isinstance(other, ConditionClause):
            return (self.And == other.And and 
                    self.Or == other.Or and 
                    self.Not == other.Not and 
                    self.Assert == other.Assert
                   )
                   
        return False

    def __repr__(self):
        return '(and: {}\nor: {}\nnot: {}\nassert: {})\n'.format(self.__and, self.__or, self.__not, self.__assert)