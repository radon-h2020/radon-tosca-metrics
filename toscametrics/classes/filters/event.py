class EventFilter():
    """
    An event filter definition defines criteria for selection of an attribute, for the purpose of monitoring it, within
    a TOSCA entity, or one its capabilities.

    Grammar 
    node: <node_type_name> | <node_template_name>
    requirement: <requirement_name>
    capability: <capability_name>
    """
  
    def __init__(self, node, requirement=None, capability=None):
        self.node   = node
        self.requirement = requirement
        self.capability = capability

    @property
    def node(self):
        return self.__node

    @node.setter
    def node(self, value):
        if value is None or not isinstance(value, str):
            raise TypeError('Parameter value must be a string')

        self.__node = value

    @property
    def requirement(self):
        return self.__requirement

    @requirement.setter
    def requirement(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError('Parameter value must be a string')

        self.__requirement = value

    @property
    def capability(self):
        return self.__capability

    @capability.setter
    def capability(self, value):
        if value is not None and not isinstance(value, str):
            raise TypeError('Parameter value must be a string')

        self.__capability = value

    def __eq__(self, other):
        return (isinstance(other, EventFilter)        and
                self.node        == other.node        and
                self.requirement == other.requirement and
                self.capability  == other.capability
        )