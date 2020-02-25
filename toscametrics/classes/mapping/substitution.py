from toscametrics.classes.filters.node         import NodeFilter
from toscametrics.classes.mapping.attribute    import AttributeMapping
from toscametrics.classes.mapping.capability   import CapabilityMapping
from toscametrics.classes.mapping.interface    import InterfaceMapping
from toscametrics.classes.mapping.property     import PropertyMapping
from toscametrics.classes.mapping.requirement  import RequirementMapping

class SubstitutionMapping():
    """
    A substitution mapping allows a given topology template to be used as an implementation of abstract
    node templates of a specific node type. This allows the consumption of complex systems using a
    simplified vision.
    """

    def __init__(self, nodeType, substitutionFilter=None, properties=None, attributes=None, capabilities=None, requirements=None, interfaces=None):
        self.nodeType = nodeType     
        self.substitutionFilter = substitutionFilter    # NodeFilter
        self.properties = properties      # map of PropertyMapping
        self.attributes = attributes      # map of AttributeMapping
        self.capabilities = capabilities  # map of CapabilityMapping
        self.requirements = requirements  # map of RequirementMapping
        self.interfaces = interfaces      # map of InterfaceMapping

    @property
    def nodeType(self):
        return self.__nodeType

    @nodeType.setter
    def nodeType(self, value):
        if value is None or not isinstance(value, str):
                raise TypeError("Value must be a string")
                
        self.__nodeType = value

    @property
    def substitutionFilter(self):
        return self.__substitutionFilter

    @substitutionFilter.setter
    def substitutionFilter(self, value):
        if value is not None and not isinstance(value, NodeFilter):
                raise TypeError("Value must be an instance of NodeFilter")
                
        self.__substitutionFilter = value

    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, value):
        if value is not None:
            if not isinstance(value, dict):
                raise TypeError("Value must be a dictionary")

            for k in value.keys():
                if not isinstance(value[k], PropertyMapping):
                    raise TypeError("Value must be a map of PropertyMapping")

        self.__properties = value

    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        if value is not None:
            if not isinstance(value, dict):
                raise TypeError("Value must be a dictionary")

            for k in value.keys():
                if not isinstance(value[k], AttributeMapping):
                    raise TypeError("Value must be a map of AttributeMapping")
                
        self.__attributes = value


    @property
    def capabilities(self):
        return self.__capabilities

    @capabilities.setter
    def capabilities(self, value):
        if value is not None:
            if not isinstance(value, dict):
                raise TypeError("Value must be a dictionary")

            for k in value.keys():
                if not isinstance(value[k], CapabilityMapping):
                    raise TypeError("Value must be a map of CapabilityMapping")
                
        self.__capabilities = value


    @property
    def requirements(self):
        return self.__requirements

    @requirements.setter
    def requirements(self, value):
        if value is not None:
            if not isinstance(value, dict):
                raise TypeError("Value must be a dictionary")

            for k in value.keys():
                if not isinstance(value[k], RequirementMapping):
                    raise TypeError("Value must be a map of RequirementMapping")
                
        self.__requirements = value

    @property
    def interfaces(self):
        return self.__interfaces

    @interfaces.setter
    def interfaces(self, value):
        if value is not None:
            if not isinstance(value, dict):
                raise TypeError("Value must be a dictionary")

            for k in value.keys():
                if not isinstance(value[k], InterfaceMapping):
                    raise TypeError("Value must be a map of InterfaceMapping")
                
        self.__interfaces = value


    def __eq__(self, other):
        return (isinstance(other, SubstitutionMapping)               and 
                self.nodeType           == other.nodeType            and 
                self.substitutionFilter == other.substitutionFilter  and 
                self.properties         == other.properties          and 
                self.attributes         == other.attributes          and 
                self.capabilities       == other.capabilities        and 
                self.requirements       == other.requirements        and 
                self.interfaces         == other.interfaces)