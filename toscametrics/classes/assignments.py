import toscametrics.classes.filters as filters

"""
Properties assignments

<property_name>: <property_value> | { <property_value_expression> }

Attribute assignments
<attribute_name>: <attribute_value> | { <attribute_value_expression> }
or
<attribute_name>:
 description: <attribute_description>
 value: <attribute_value> | { <attribute_value_expression> }
"""


class RequirementAssignment():
    """
    A Requirement assignment allows template authors to provide either concrete names of TOSCA
    templates or provide abstract selection criteria for providers to use to find matching TOSCA templates
    that are used to fulfill a named requirement’s declared TOSCA Node Type
    
    Grammar <requirement_name>: <node_template_name> or
 
            <requirement_name>:
              node: <node_template_name> | <node_type_name>
              relationship: <relationship_template_name> | <relationship_type_name>
              capability: <capability_symbolic_name> | <capability_type_name>
              node_filter: <node_filter_definition>
              occurrences: [ min_occurrences, max_occurrences ] or
 
            <requirement_name>:
              # Other keynames omitted for brevity
              relationship:
                type: <relationship_template_name> | <relationship_type_name>
                properties: <property_assignments>
                interfaces: <interface_assignments>
    """

    def __init__(self):
        self.capability = ''
        self.node = ''
        self.relationship = ''
        self.nodeFilter = filters.NodeFilter()
        self.occurrences = []   # range of integer

        # Additional relationship keyname
        self.relationshipType = '' 
        self.relationshipProperties = {}    # map of properties assignment
        self.relationshipInterfaces = {}    # map of interface definitions