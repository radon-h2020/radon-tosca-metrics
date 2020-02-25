
class ImportDefinition():
    """
    An import definition is used within a TOSCA Service Template to locate and uniquely name another
    TOSCA Service Template file which has type and template definitions to be imported (included) and
    referenced within another Service Template.
    """

    def __init__(self, file, repository=None, namespacePrefix=None, namespaceUri=None):
        self.file = file
        self.repository = repository
        self.namespacePrefix = namespacePrefix
        self.namespaceUri = namespaceUri     # deprecated

    @property
    def file(self):
        return self.__file
    
    @file.setter
    def file(self, value):
        if value is None or not isinstance(value, str):
            raise TypeError('Argument value must be a string') 
        
        self.__file = value

    @property
    def repository(self):
        return self.__repository
    
    @repository.setter
    def repository(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError('Argument value must be a string') 
        
        self.__repository = value

    @property
    def namespacePrefix(self):
        return self.__namespacePrefix
    
    @namespacePrefix.setter
    def namespacePrefix(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError('Argument value must be a string') 
        
        self.__namespacePrefix = value

    @property
    def namespaceUri(self):
        return self.__namespaceUri
    
    @namespaceUri.setter
    def namespaceUri(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError('Argument value must be a string') 
        
        self.__namespaceUri = value

    def __eq__(self, other):
        if isinstance(other, ImportDefinition):
            return (self.__file         == other.file         and 
                    self.__repository   == other.repository   and 
                    self.__namespaceUri == other.namespaceUri and 
                    self.__namespacePrefix == other.namespacePrefix
                   )

        return False

    def __repr__(self):
        return '(file: {}\nrepository: {}\nnnamespace_prefix: {}\nnamespace_uri: {})'.format(self.__file, self.__repository, self.__namespacePrefix, self.__namespaceUri)