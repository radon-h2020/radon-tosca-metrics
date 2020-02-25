import yaml
from io import StringIO
from toscametrics.exceptions import NotBlueprintError, NotStringIOError

class BlueprintMetric():

    def __init__(self, blueprintStream):
        """
        Initialize a new blueprint metric.
        blueprintStream -- a StringIO object representing the blueprint to parse
        """
        if not isinstance(blueprintStream, StringIO):
            raise NotStringIOError

        try:
            self.__yml = yaml.safe_load(blueprintStream.getvalue())
            if self.__yml is None:
                raise NotBlueprintError
            self.__StringIOobject = blueprintStream.getvalue()
        except yaml.YAMLError:
            raise NotBlueprintError

    @property
    def getyml(self):
        return self.__yml

    @property
    def getStringIOobject(self):
        return self.__StringIOobject