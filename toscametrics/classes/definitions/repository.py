
class RepositoryDefinition():
    """
    A repository definition defines a named external repository which contains deployment and
    implementation artifacts that are referenced within the TOSCA Service Template.
    """

    def __init__(self, url, description=None, credential=None):
        self.url = url
        self.description = description
        self.credential = credential


    @property
    def url(self):
        return self.__url
    
    @url.setter
    def url(self, value):
        if value is None or not isinstance(value, str):
            raise TypeError('Argument value must be a string') 
        
        self.__url = value

    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError('Argument value must be a string') 
        
        self.__description = value

    def __eq__(self, other):
        if isinstance(other, RepositoryDefinition):
            return (self.__url == other.url and 
                    self.__description == other.description
                    )

        return False

    def __repr__(self):
        return '(url: {}\ndescription: {}\ncredential: {})'.format(self.__url, self.__description, self.credential)