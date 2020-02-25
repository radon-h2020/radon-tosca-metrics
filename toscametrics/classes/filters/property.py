from toscametrics.classes.clauses.constraints import ConstraintClause

class PropertyFilter():
    """
    A property filter definition defines criteria, using constraint clauses, for selection of a TOSCA entity based upon it property values.
    """    
    def __init__(self, name, constraints):
        self.name = name
        self.constraints = constraints # list of clauses.ConstraintClause

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value is None or not isinstance(value, str):
            raise TypeError('Parameter value must be a string')

        self.__name = value

    @property
    def constraints(self):
        return self.__constraints

    @constraints.setter
    def constraints(self, value):
        if value is None or not isinstance(value, list):
            raise TypeError('Parameter value must be a list')
        else:
            for item in value:
                if not isinstance(item, ConstraintClause):
                    raise TypeError('Parameter value must be a list of ConstraintClause')

        self.__constraints= value

    def __eq__(self, other):
        return (isinstance(other, PropertyFilter) and
                self.name == other.name and
                self.constraints ==  other.constraints
        )