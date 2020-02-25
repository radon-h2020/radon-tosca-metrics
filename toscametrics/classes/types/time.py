import re

from toscametrics.classes.types.entity import EntityType

YAML_ISO_8601 = r'\d{4}-\d{2}-\d{2}(([Tt]|[\s\t]+)\d{1,2}?:\d{2}:\d{2}(\.[0-9]*)?(([ \t]*)Z|\s*[-+][0-9][0-9]?(:\d{2})?)?)?'

class TimeInterval(EntityType):
    """
    The TimeInterval type is a complex TOSCA data Type used when describing a period of time using the
    YAML ISO 8601 format to declare the start and end times.
    """

    def __init__(self, start, end):
        
        if re.match(YAML_ISO_8601, start) != None and re.match(YAML_ISO_8601, end) != None:
            self.__start = start 
            self.__end   = end 
        else:
            raise TypeError('Parameters start and end must be string and follow the YAML ISO 8601 format to declare the start and end times')


    @property
    def startTime(self): 
        return self.__start

    @property
    def endTime(self): 
        return self.__end

    def __eq__(self, other):
        if isinstance(other, TimeInterval):
            return (self.__start == other.startTime and 
                    self.__end   == other.endTime
                )

        return False
