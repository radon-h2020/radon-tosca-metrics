import toscametrics.classes.definitions as definitions

class NodeType(EntityType):
    """
    A Node Type is a reusable entity that defines the type of one or more Node Templates. As such, a Node
    Type defines the structure of observable properties via a Properties Definition, the Requirements and
    Capabilities of the node as well as its supported interfaces.

    Grammar <node_type_name>:
              derived_from: <parent_node_type_name>
              version: <version_number>
              metadata: <map of string>
              description: <node_type_description>
              attributes: <attribute_definitions>
              properties: <property_definitions>
              requirements:
                - <requirement_definitions>
              capabilities: <capability_definitions>
              interfaces: <interface_definitions>
              artifacts: <artifact_definitions>
    """

    def __init__(self):
        self.attributesDefinitions = {}     # map of AttributeDefinition
        self.propertiesDefinitions = {}     # map of SchemaDefinition
        self.requirementsDefinitions = []   # list of RequirementDefinition
        self.capabilityDefinitions = {}     # map of CapabilityDefinition
        self.interfaceDefinitions = {}      # map of InterfaceDefinition
        self.artifcatDefinitions = {}       # map of ArtifactDefinition


class RelationshipType(EntityType):
    """
    A Relationship Type is a reusable entity that defines the type of one or more relationships between Node
    Types or Node Templates. 

    Grammar <relationship_type_name>:
              derived_from: <parent_relationship_type_name>
              version: <version_number>
              metadata: <map of string>
              description: <relationship_description>
              properties: <property_definitions>
              attributes: <attribute_definitions>
              interfaces: <interface_definitions>
              valid_target_types: [ <capability_type_names> ]
    """

    def __init__(self):
        self.attributesDefinitions = {}     # map of AttributeDefinition
        self.propertiesDefinitions = {}     # map of SchemaDefinition
        self.interfaceDefinitions = {}      # map of InterfaceDefinition
        self.validTargetTypes = []          # list of string
  

class InterfaceType(EntityType):
    """
    An Interface Type is a reusable entity that describes a set of operations that can be used to interact with
    or manage a node or relationship in a TOSCA topology. 

    Grammar
    <interface_type_name>:
        derived_from: <parent_interface_type_name>
        version: <version_number>
        metadata: <map of string>
        description: <interface_description>
        inputs: <property_definitions>
        operations: <operation_definitions>
        notifications: <notification definitions>
    """

    def __init__(self):
        self.inputs = {}        # map of definitions.property_definitions
        self.operations = {}    # map of definitions.OperationDefinition
        self.notifications = {} # map of definitions.NotificationDefinition



    
class PolicyType(EntityType):
    """
    A Policy Type defines a type of requirement that affects or governs an application or service’s topology at
    some stage of its lifecycle, but is not explicitly part of the topology itself (i.e., it does not prevent the
    application or service from being deployed or run if it did not exist).

    Grammar <policy_type_name>:
              derived_from: <parent_policy_type_name>
              version: <version_number>
              metadata: <map of string>
              description: <policy_description>
              properties: <property_definitions>
              targets: [ <list_of_valid_target_types> ]
              triggers: <trigger_definitions>
    """

    def __init__(self):
        self.propertiesDefinitions = {}     # map of SchemaDefinition
        self.targets = []                   # list of string
        self.triggers = {}                  # ma of TriggerDefinition
