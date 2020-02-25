from toscametrics.classes.types.range_type import RangeType

class ConstraintClause():
    """
    A constraint clause defines an operation along with one or more compatible values that can be used to
    define a constraint on a property or parameter’s allowed values when it is defined in a TOSCA Service
    Template or one of its entities
    """
    
    def __init__(
        self,
        equal = None,
        greaterThan = None,
        greaterOrEqual = None,
        lessThan = None,
        lessOrEqual = None,
        inRange = None,
        validValues = None,
        length = None,
        minLength = None,
        maxLength = None,
        pattern = None,
        schema = None
        ):
        
        self.equal = equal
        self.greaterThan = greaterThan
        self.greaterOrEqual = greaterOrEqual
        self.lessThan = lessThan
        self.lessOrEqual = lessOrEqual
        self.inRange = inRange
        self.validValues = validValues
        self.length = length
        self.minLength = minLength
        self.maxLength = maxLength
        self.pattern = pattern
        self.schema = schema

    @property
    def equal(self):
        return self.__equal

    @equal.setter
    def equal(self, value):
        if value is not None and not isinstance(value, int):
            raise TypeError("Argument value must be an integer")

        self.__equal = value

    @property
    def greaterThan(self):
        return self.__greaterThan

    @greaterThan.setter
    def greaterThan(self, value):
        if value is not None and  not isinstance(value, int):
            raise TypeError("Argument value must be an integer")

        self.__greaterThan = value

    @property
    def greaterOrEqual(self):
        return self.__greaterOrEqual

    @greaterOrEqual.setter
    def greaterOrEqual(self, value):
        if value is not None and  not isinstance(value, int):
            raise TypeError("Argument value must be an integer")

        self.__greaterOrEqual = value

    @property
    def lessThan(self):
        return self.__lessThan

    @lessThan.setter
    def lessThan(self, value):
        if value is not None and  not isinstance(value, int):
            raise TypeError("Argument value must be an integer")

        self.__lessThan = value

    @property
    def lessOrEqual(self):
        return self.__lessOrEqual

    @lessOrEqual.setter
    def lessOrEqual(self, value):
        if value is not None and  not isinstance(value, int):
            raise TypeError("Argument value must be an integer")

        self.__lessOrEqual = value


    @property
    def inRange(self):
        return self.__inRange

    @inRange.setter
    def inRange(self, value):
        if value is not None:
            if not isinstance(value, list):
                raise TypeError("Argument value must be an instance of list")
            elif len(value) != 2:
                raise ValueError("Argument list must have two items")
            elif not isinstance(value[0], int) or not isinstance(value[1], int):
                raise TypeError("Argument in list vale must be integers")

            self.__inRange = RangeType(value[0], value[1])
        else:
            self.__inRange = value

    @property
    def validValues(self):
        return self.__validValues

    @validValues.setter
    def validValues(self, value):
        if value is not None:
            if not isinstance(value, list):
                raise TypeError("Argument value must be an instance of list")
            else:
                for item in value:
                    if not isinstance(item, int):
                        raise TypeError("Items in value must be integers")
        
        self.__validValues = value


    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if value is not None and  not isinstance(value, int):
            raise TypeError("Argument value must be an integer")

        self.__length = value

    @property
    def minLength(self):
        return self.__minLength

    @minLength.setter
    def minLength(self, value):
        if value is not None and  not isinstance(value, int):
            raise TypeError("Argument value must be an integer")

        self.__minLength = value

    @property
    def maxLength(self):
        return self.__maxLength

    @maxLength.setter
    def maxLength(self, value):
        if value is not None and  not isinstance(value, int):
            raise TypeError("Argument value must be an integer")

        self.__maxLength = value

    @property
    def pattern(self):
        return self.__pattern

    @pattern.setter
    def pattern(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("Argument value must be a string")

        self.__pattern = value

    @property
    def schema(self):
        return self.__schema

    @schema.setter
    def schema(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("Argument value must be a string")

        self.__schema = value

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, ConstraintClause):
            return (self.__equal == other.equal and 
                    self.__greaterThan == other.greaterThan and 
                    self.__greaterOrEqual == other.greaterOrEqual and 
                    self.__lessThan == other.lessThan and 
                    self.__lessOrEqual == other.lessOrEqual and 
                    self.__inRange == other.inRange and  
                    self.__validValues == other.validValues and 
                    self.__length == other.length and 
                    self.__minLength == other.minLength and 
                    self.__maxLength == other.maxLength and  
                    self.__pattern == other.pattern and 
                    self.__schema == other.schema
                   )
                   
        return False

    def __str__(self):
        """Overrides the default implementation"""
        return 'equal: {}\ngreaterThan: {}\ngreaterOrEqual: {}\nlessThen: {}\nlessOrEqual: {}\ninRange: {}\nvalidValues: {}\nlength: {}\nminLength: {}\nmaxLength: {}\npattern: {}\nschema: {}\n' \
            .format(self.__equal, self.__greaterThan, self.__greaterOrEqual, self.__lessThan, self.__lessOrEqual, self.__inRange, self.__validValues, self.__length, self.__minLength, self.__maxLength, self.__pattern, self.__schema)