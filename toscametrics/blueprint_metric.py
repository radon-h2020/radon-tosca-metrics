import yaml


class BlueprintMetric:

    def __init__(self, blueprint: str):
        """
        Initialize a new blueprint metric.
        :param blueprint: a StringIO object representing the blueprint to parse
        """
        try:
            self.__plain_blueprint = blueprint
            self.__blueprint = yaml.safe_load(blueprint)
            if type(self.__blueprint) == list:
                self.__blueprint = self.__blueprint[0]

            if self.__blueprint is None or len(self.__blueprint) == 0:
                raise TypeError("Expected a non-empty blueprint")

        except yaml.YAMLError:
            raise TypeError("Expected a valid YAML")

    @property
    def blueprint(self):
        return self.__blueprint

    @property
    def plain_blueprint(self):
        return self.__plain_blueprint
