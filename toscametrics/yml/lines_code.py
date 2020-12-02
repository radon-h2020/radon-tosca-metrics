import yaml
from io import StringIO


class LinesCode:
    """ This class counts the blueprint's executable lines of code"""

    def __init__(self, blueprint):
        """
        Initialize a new LinesCode metric.
        :param blueprint: a StringIO object representing a valid TOSCA blueprint
        """
        if not isinstance(blueprint, StringIO):
            raise TypeError("Expected a StringIO object")

        try:
            # Check if is a valid yaml
            self.__blueprint = yaml.safe_load(blueprint.getvalue())
            if self.__blueprint is None:
                raise TypeError("Expected a non-empty blueprint")
            
            self.__blueprint = blueprint.getvalue()

        except yaml.YAMLError:
            raise TypeError("Expected a valid YAML")

    def count(self):
        """
        :return: unsigned int
        """
        loc = 0

        for l in self.__blueprint.splitlines():
            if l.strip() and l.strip() != '---' and l.strip() != '-' and not l.strip().startswith('#'):
                loc = loc + 1
                
        return loc

    @property
    def blueprint(self):
        return self.__blueprint
