import yaml

class Parser():
    
    def __init__(self, plainYaml):
        """
        Initialize a new parser.
        plainYaml -- a plain yaml file
        """
        self.yaml = plainYaml

    @property
    def yaml(self):
        return self.__yaml

    @yaml.setter
    def yaml(self, plain):
        """ Tansform plain yaml text to a yaml dictionary """
        self.__yaml = yaml.safe_load(plain)
        if self.__yaml is None:
            raise yaml.YAMLError