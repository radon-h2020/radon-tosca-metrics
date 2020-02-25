import toscametrics.classes.filters as filters

class NodeTemplate():
    """
    A Node Template specifies the occurrence of a manageable software component as part of an
    application’s topology model which is defined in a TOSCA Service Template. A Node template is an
    instance of a specified Node Type and can provide customized properties, constraints or operations
    which override the defaults provided by its Node Type and its implementations.
    
    Grammar
    <node_template_name>:
      type: <node_type_name>
      description: <node_template_description>
      directives: [<directives>]
      metadata: <map of string>
      properties: <property_assignments>
      attributes: <attribute_assignments>
      requirements:
        - <requirement_assignments>
      capabilities: <capability_assignments>
      interfaces: <interface_definitions>
      artifacts: <artifact_definitions>
      node_filter: <node_filter_definition>
      copy: <source_node_template_name>
    """
    def __init__(self):
        self.type = ''
        self.description = ''
        self.metadata = {}          # map of string
        self.directives = []        # list of string
        self.properties = {}        # map of property assignments
        self.attributes = {}        # map of attribute assignments
        self.requirements = []      # list of RequirementAssignment
        self.capabilities = {}      # map of CapabilityAssignment
        self.interfaces = {}        # map of InterfaceDefinition
        self.artifacts = {}         # map of ArtifactDefinition
        self.nodeFilter = filters.NodeFilter()
        self.copy = ''


class RelationshipTemplate():
    """
    A Relationship Template specifies the occurrence of a manageable relationship between node templates
    as part of an application’s topology model that is defined in a TOSCA Service Template. A Relationship
    template is an instance of a specified Relationship Type and can provide customized properties,
    constraints or operations which override the defaults provided by its Relationship Type and its
    implementations.
    
    Grammar
    <relationship_template_name>:
      type: <relationship_type_name>
      description: <relationship_type_description>
      metadata:  <map of string>
      properties: <property_assignments>
      attributes: <attribute_assignments>
      interfaces: <interface_definitions>
      copy: <source_relationship_template_name>
    """
    def __init__(self):
        self.type = ''
        self.description = ''
        self.metadata = {}          # map of string
        self.properties = {}        # map of property assignments
        self.attributes = {}        # map of attribute assignments
        self.interfaces = {}        # map of InterfaceDefinition
        self.copy = ''


class TopologyTemplate():
    """
    The main ingredients of the topology template are node templates representing components of the application and relationship templates
    representing links between the components. These elements are defined in the nested node_templates
    section and the nested relationship_templates sections, respectively. Furthermore, a topology
    template allows for defining input parameters, output parameters as well as grouping of node templates.
    
    Grammar
    topology_template:
        description: <template_description>
        inputs: <input_parameters>
        outputs: <output_parameters>
        node_templates: <node_templates>
        relationship_templates: <relationship_templates>
        groups: <group_definitions>
        policies:
            - <policy_definition_list>
        workflows: <workflows>
        # Optional declaration that exports the Topology Template
        # as an implementation of a Node Type.
        substitution_mappings: <substitution_mappings>
    """
    def __init__(self):
        self.description = ''
        self.inputs = {}                    # map of definitions.ParameterDefinition
        self.nodeTemplates = {}             # map of NodeTemplate 
        self.relationshipTemplates = {}     # map of RelationshipTemplate 
        self.groups = {}                    # map of definitions.GroupDefinition
        self.policies = []                  # list of definitions.PolicyDefinition
        self.outputs = {}                   # map of definitions.ParameterDefinition
        self.substitutionMappings = mappings.SubstitutionMapping()
        self.workflows = {}                 # map of ImperativeWorkflowDefinitions

class ServiceTemplate():
    """
    A TOSCA Service Template (YAML) document contains element definitions of building blocks for cloud
    application, or complete models of cloud applications. This section describes the top-level structural
    elements (TOSCA keynames) along with their grammars, which are allowed to appear in a TOSCA
    Service Template document.
    
    Grammar
    tosca_definitions_version: <value> # Required
    namespace: <URI>                   # Optional

    # Optional metadata keyname: value pairs
    metadata:
        template_name: <value> # Optional, name of this service
    template
        template_author: <value> # Optional, author of this service
    template
        template_version: <value> # Optional, version of this service
    template
    # More optional entries of domain or profile specific metadata keynames
    # Optional description of the definitions inside the file.
    description: <template_type_description>
    dsl_definitions:
        # map of YAML alias anchors (or macros)
    repositories:
        # map of external repository definitions which host TOSCA artifacts
    imports:
        # ordered list of import definitions
    artifact_types:
        # map of artifact type definitions
    data_types:
        # map of datatype definitions
    capability_types:
        # map of capability type definitions
    interface_types
        # map of interface type definitions
    relationship_types:
        # map of relationship type definitions
    node_types:
        # map of node type definitions
    group_types:
        # map of group type definitions
    policy_types:
        # map of policy type definitions
    topology_template:
        # topology template definition of the cloud application or service
    """

    def __init__(self):
        self.toscaDefinitionsVersion = ''
        self.namespace = ''
        self.description = ''
        self.metadata = {}                  # map of string
        self.repositories = {}              # map of definitions.RepositoryDefinition
        self.imports = {}                   # map of definitions.ImportDefinition
        self.artifactTypes = {}             # map of types.ArtifactType 
        self.dataTypes = {}                 # map of types.DataType 
        self.capabilityTypes = {}           # map of types.CapabilityType 
        self.interfaceTypes = {}            # map of types.InterfaceType 
        self.relationshipTypes = {}         # map of types.RelationshipType 
        self.nodeTypes = {}                 # map of types.NodeType 
        self.groupTypes = {}                # map of types.GroupType
        self.policyTypes = {}               # map of types.PolicyType
        self.topologyTemplate = TopologyTemplate()

class ServiceTemplateMetadata():
    def __init__(self):
        self.templateName = ''
        self.templateAuthor = ''
        self.templateVersion = ''