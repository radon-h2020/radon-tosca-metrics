class RangeType():

    def __init__(self, lower, upper):
        
        if not isinstance(lower, int):
            raise TypeError('The lowerbound must be integer')
        
        self.__lower = lower

        if not isinstance(upper, int):
            if str(upper) == 'UNBOUNDED':
                self.__upper = upper
            else:
                raise TypeError('The upperbound must be integer or UNBOUNDED')
        elif upper < lower:
            raise ValueError('The upper_bound must be greater than or equal to lower_bound')
        else:
            self.__upper = upper

    @property
    def lowerBound(self): 
        return self.__lower

    @property
    def upperBound(self): 
        return self.__upper

    def __eq__(self, other):
        if isinstance(other, RangeType):
            return (self.__lower == other.lowerBound and 
                    self.__upper == other.upperBound
                )

        return False
