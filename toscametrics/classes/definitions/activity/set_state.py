from toscametrics.classes.definitions.activity.activity_definition import ActivityDefinition

class SetStateActivityDefinition(ActivityDefinition):
    """ Sets the state of a node. """
    #set_state: <new_node_state>
    def __init__(self, state):
        self.state = state

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        if value is None or not isinstance(value, str):
            raise TypeError("Argument value must be an instance of string")
            
        self.__state = value

    def __eq__(self, other):
        if isinstance(other, SetStateActivityDefinition):
            return self.state == other.state

        return False    

