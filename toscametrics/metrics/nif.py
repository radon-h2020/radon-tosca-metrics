from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscaparser.tosca_template import ToscaTemplate
from toscametrics.utils import getNodeTypes
from toscametrics.utils import getRelationshipTypes
from toscametrics.utils import getInterfaces

class NIF(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of interfaces defined in a given .yaml file"""
    

    def _for_node_templates(self):
        '''Checks for the number of interfaces within node templates'''
        template = ToscaTemplate(yaml_dict_tpl=self.getyml)
        node_temps = template.nodetemplates
        interfs = []
        for temp in node_temps:
            for interface in temp.interfaces:
                interfs.append(interface.name)
        return len(interfs)

    def _for_relationship_templates(self):
        '''Checks for the number of interfaces within relationship templates'''
        template = ToscaTemplate(yaml_dict_tpl=self.getyml)
        rel_temps = template.relationship_templates
        interfs = []
        for temp in rel_temps:
            for interface in temp.interfaces:
                interfs.append(interface.name)
        return len(interfs)

    def _for_relationshiptype_definitions(self):
        '''Checks for the number of interfaces within relationship definition'''
        interfs = []
        reltypes = getRelationshipTypes(self.getyml)[0][1]
        for reltype in reltypes:
            rel_dict = reltypes[reltype]
            inter = getInterfaces(rel_dict)
            interfs.append(len(inter[0][1]))
        return sum(interfs)
    
    def _for_nodetype_definitions(self):
        '''Checks for the number of interfaces within nodetype definition'''
        interfs = []
        nodetypes = getNodeTypes(self.getyml)[0][1]
        for nodetype in nodetypes:
            node_dict = nodetypes[nodetype]
            inter = getInterfaces(node_dict)
            interfs.append(len(inter[0][1]))
        return sum(interfs)


    def count(self):
        '''Function which counts the number of interfaces in a given yaml file'''
        interfs = []
        try:
            interfs.append(self._for_node_templates())
        except (AttributeError, IndexError):
            interfs.append(0)
        
        try:
            interfs.append(self._for_relationship_templates())
        except (AttributeError, IndexError):
            interfs.append(0)
        
        try:
            interfs.append(self._for_relationshiptype_definitions())
        except (AttributeError, IndexError):
            interfs.append(0)

        try:
            interfs.append(self._for_nodetype_definitions())
        except (AttributeError, IndexError):
            interfs.append(0)

        return sum(interfs)


# from io import StringIO

# string = "# Modified from a file that was distributed with this NOTICE:\n#\n#   Apache AriaTosca\n#   Copyright 2016-2017 The Apache Software Foundation\n#\n#   This product includes software developed at\n#   The Apache Software Foundation (http://www.apache.org/).\n\ntosca_definitions_version: tosca_simple_yaml_1_2\n\ninterface_types:\n\n  tosca.interfaces.Root:\n    metadata:\n      normative: 'true'\n      citation: '[TOSCA-Simple-Profile-YAML-v1.2]'\n      citation_location: 5.8.3\n    description: >-\n      This is the default (root) TOSCA Interface Type definition that all other TOSCA Interface\n      Types derive from.\n\n  tosca.interfaces.node.lifecycle.Standard:\n    metadata:\n      normative: 'true'\n      citation: '[TOSCA-Simple-Profile-YAML-v1.2]'\n      citation_location: 5.8.4\n    description: >-\n      This lifecycle interface defines the essential, normative operations that TOSCA nodes may\n      support.\n    derived_from: tosca.interfaces.Root\n    create:\n      description: >-\n        Standard lifecycle create operation.\n    configure:\n      description: >-\n        Standard lifecycle configure operation.\n    start:\n      description: >-\n        Standard lifecycle start operation.\n    stop:\n      description: >-\n        Standard lifecycle stop operation.\n    delete:\n      description: >-\n        Standard lifecycle delete operation.\n\n  tosca.interfaces.relationship.Configure:\n    metadata:\n      normative: 'true'\n      citation: '[TOSCA-Simple-Profile-YAML-v1.2]'\n      citation_location: 5.8.5\n    description: >-\n      The lifecycle interfaces define the essential, normative operations that each TOSCA\n      Relationship Types may support.\n    derived_from: tosca.interfaces.Root\n    pre_configure_source:\n      description: >-\n        Operation to pre-configure the source endpoint.\n    pre_configure_target:\n      description: >-\n        Operation to pre-configure the target endpoint.\n    post_configure_source:\n      description: >-\n        Operation to post-configure the source endpoint.\n    post_configure_target:\n      description: >-\n        Operation to post-configure the target endpoint.\n    add_target:\n      description: >-\n        Operation to notify the source node of a target node being added via a relationship.\n    add_source:\n      description: >-\n        Operation to notify the target node of a source node which is now available via a\n        relationship.\n    target_changed:\n      description: >-\n        Operation to notify source some property or attribute of the target changed\n    remove_target:\n      description: >-\n        Operation to remove a target node.\n    remove_source: # ERRATUM: does not appear in spec, but is mentioned\n      description: >-\n        Operation to remove the source node.\n"
# string = 'tosca_definitions_version: tosca_simple_yaml_1_0_0_wd03\n\nname: apache-lb\ndescription: apacheLB recipe.\n\nimports:\n  - tosca-base-types:1.0\n  - tomcat-types:0.1\n\nnode_types:\n  fastconnect.nodes.apacheLB:\n    derived_from: tosca.nodes.SoftwareComponent\n    description: >\n      This is the definition of the Apache LB Recipe.\n      This is based on Cloudify Apache LB groovy recipe.\n    tags:\n      icon: /images/apache.png\n    properties:\n      version:\n        type: version\n        default: 2\n        constraints:\n          - equal: 2\n    interfaces:\n      Standard:\n        operations:\n          create:\n            implementation_artifact:\n              artifact_type: tosca.artifacts.GroovyScript\n              artifact_ref: "scripts/alien_apacheLB_install.groovy"\n          start:\n            implementation_artifact:\n              artifact_type: tosca.artifacts.GroovyScript\n              artifact_ref: "scripts/apacheLB_start.groovy"\n          stop:\n            implementation_artifact:\n              artifact_type: tosca.artifacts.GroovyScript\n              artifact_ref: "scripts/apacheLB_stop.groovy"\n          delete:\n            implementation_artifact:\n              artifact_type: tosca.artifacts.GroovyScript\n              artifact_ref: "scripts/apacheLB_uninstall.groovy"\n      fastconnect.cloudify.extensions:\n        operations:\n          start_detection:\n            implementation_artifact:\n              artifact_type: tosca.artifacts.GroovyScript\n              artifact_ref: scripts/apacheLB_startDetection.groovy\n      custom:\n        operations:\n          addNode:\n            implementation_artifact:\n              artifact_type: tosca.artifacts.GroovyScript\n              artifact_ref: "scripts/apacheLB_addNode.groovy"\n          removeNode:\n            implementation_artifact:\n              artifact_type: tosca.artifacts.GroovyScript\n              artifact_ref: "scripts/apacheLB_removeNode.groovy"\n    capabilities:\n      httpEndpoint:\n        type: alien4cloud.capabilities.HttpEndpoint\n        lower_bound: 0\n        upper_bound: unbounded\n    artifacts:\n       - scripts: scripts\n         type: fastconnect.artifacts.ResourceDirectory\n'

# print(string)
# yml = StringIO(string.expandtabs(2)) 
# metric = NIF(yml)

# print('NIF count: ', metric.count())




