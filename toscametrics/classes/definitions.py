import toscametrics.classes.clauses as clauses
import toscametrics.classes.filters as filters
import toscametrics.classes.types   as types

class OperationDefinition():
    """
    An operation definition defines a named function or procedure that can be bound to an operation implementation.

    Grammar
    <operation_name>: <implementation_artifact_name> or
    <operation_name>:
        description: <operation_description>
        implementation: <Operation implementation definition>
        inputs: <property_definitions>
        outputs: <attribute mappings> 
    """

    def __init__(self):
        self.description = ''
        self.implementation = OperationImplementationDefinition()
        self.inputs = {}        # map of ParameterDefinition or property assignments
        self.outputs = {}       # map of AttributeMapping



class NotificationDefinition():
    """
    A notification definition defines a named notification that can be associated with an interface. The
    notification is a way for an external event to be transmitted to the TOSCA orchestrator. Parameter values
    can be sent together with a notification and we can map them to node/relationship attributes imilarly to the
    way operation outputs are mapped to attributes. The artifact that the orchestrator is registering with in
    order to receive the notification is specified using the “implementation” keyname in a similar way to
    operations.
    When the notification is received an event is generated within the orchestrator that can be associated to
    triggers in policies to call other internal operations and workflows. The notification name (the unqualified
    full name) itself identifies the event type that is generated and can be textually used when defining the
    associated triggers.

    Grammar
    <notification_name>:
        description: <notification_description>
        implementation: <notification_implementation_definition>
        outputs: <attribute_mappings>
    """

    def __init__(self):
        self.description = ''
        self.implementation = NotificationImplementationDefinition()
        self.outputs = {}       # map of AttributeMapping
        
class TriggerDefinition():
    """
    A trigger definition defines the event, condition and action that is used to “trigger” a policy it is associated with.

    Grammar <trigger_name>:
              description: <trigger_description>
              event: <event _name>
              schedule: <time_interval_for_trigger>
              target_filter: <event_filter_definition>
              condition: <condition_clause_definition>
              action: 
                - <list_of_activity_definition> 
    or
            <trigger_name>:
              description: <trigger_description>
              event: <event _name>
              schedule: <time_interval_for_trigger>
              target_filter: <event_filter_definition>
              condition:
                constraint: <condition_clause_definition>
                period: <scalar-unit.time> # e.g., 60 sec
                evaluations: <integer> # e.g., 1
                method: <string> # e.g., average
              action:
                - <list_of_activity_definition>
    """

    def __init__(self):
        self.description = ''
        self.event = ''
        self.schedule     = types.TimeInterval()      
        self.targetFilter = filters.EventFilter()   
        self.condition    = ConditionClause()  
        self.action = []  # list of ActivityDefinition

        # Additional keynames dor the extendned condition notation
        self.constraint = ConditionClause()
        self.period = ''    # scalar-unit.time (http://docs.oasis-open.org/tosca/TOSCA-Simple-Profile-YAML/v1.3/TOSCA-Simple-Profile-YAML-v1.3.pdf#page=71&zoom=100,0,74)
        self.evaluations = 0
        self.method = ''


class InterfaceDefinition():
    """
    An interface definition defines a named interface that can be associated with a Node or Relationship Type 

    Grammar <interface_definition_name>:
              type: <interface_type_name>
              inputs: <property_definitions>
              operations: <operation_definitions>
              notifications: <notification definitions>
    """

    def __init__(self):
        self.type = ''
        self.inputs = {}        # map of SchemaDefinition or PropertyAssignment
        self.operations = {}    # map of OperationDefinition
        self.notifications = {} # map of NotificationDefinition


class RequirementDefinition():
    """
    The Requirement definition describes a named requirement (dependencies) of a TOSCA Node Type or
    Node template which needs to be fulfilled by a matching Capability definition declared by another TOSCA
    modelable entity. The requirement definition may itself include the specific name of the fulfilling entity
    (explicitly) or provide an abstract type, along with additional filtering characteristics, that a TOSCA
    orchestrator can use to fulfill the capability at runtime (implicitly).

    Grammar <requirement_definition_name>: <capability_type_name> or
            <requirement_definition_name>:
              capability: <capability_type_name>
              node: <node_type_name>
              relationship: <relationship_type_name>
              occurrences: [ <min_occurrences>, <max_occurrences> ]

            <requirement_definition_name>:
              # Other keynames omitted for brevity
              relationship:
              type: <relationship_type_name>
              interfaces: <interface_definitions>
    """

    def __init__(self):

        self.capability = ''
        self.node = ''
        self.relationship = ''
        self.occurrences = []   # range of integer

        # Additional keynames for multi-line relationship grammar
        self.type       = ''
        self.interfaces = {}    # Map of interface definitions



class PolicyDefinition():
    """
    A policy definition defines a policy that can be associated with a TOSCA topology or top-level entity
    definition (e.g., group definition, node template, etc.). 

    Grammar
    <policy_name>:
      type: <policy_type_name>
      description: <policy_description>
      metadata: <map of string>
      properties: <property_assignments>
      targets: [<list_of_policy_targets>]
      triggers: <trigger_definitions>
    """

    def __init__(self):
        self.type = ''
        self.description = ''
        self.metadata = {}      # map of string
        self.properties = {}    # map of property assignments
        self.targets = []       # list of string
        self.triggers = {}      # map of TriggerDefinition