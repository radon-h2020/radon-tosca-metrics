import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.metrics.nop import NOP


#yaml_nop_id
yaml_0_1 = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ntopology_template:\n  description: Template of a database including its hosting stack.\n\n  inputs:\n    mq_service_ip:\n      type: string\n      description: IP address of the message queuing server to receive messages from\n    receiver_port:\n      type: string\n      description: Port to be used for receiving messages '
yaml_14_1 = "tosca_definitions_version: tosca_simple_yaml_1_1\n\ninterface_types:\n\n  tosca.interfaces.Root:\n    metadata:\n      normative: 'true'\n      citation: '[TOSCA-Simple-Profile-YAML-v1.1]'\n      citation_location: 5.8.3\n    description: >-\n      This is the default (root) TOSCA Interface Type definition that all other TOSCA Interface\n      Types derive from.\n\n  tosca.interfaces.node.lifecycle.Standard:\n    metadata:\n      normative: 'true'\n      citation: '[TOSCA-Simple-Profile-YAML-v1.1]'\n      citation_location: 5.8.4\n    description: >-\n      This lifecycle interface defines the essential, normative operations that TOSCA nodes may\n      support.\n    derived_from: tosca.interfaces.Root\n    create:\n      description: >-\n        Standard lifecycle create operation.\n    configure:\n      description: >-\n        Standard lifecycle configure operation.\n    start:\n      description: >-\n        Standard lifecycle start operation.\n    stop:\n      description: >-\n        Standard lifecycle stop operation.\n    delete:\n      description: >-\n        Standard lifecycle delete operation.\n\n  tosca.interfaces.relationship.Configure:\n    metadata:\n      normative: 'true'\n      citation: '[TOSCA-Simple-Profile-YAML-v1.1]'\n      citation_location: 5.8.5\n    description: >-\n      The lifecycle interfaces define the essential, normative operations that each TOSCA\n      Relationship Types may support.\n    derived_from: tosca.interfaces.Root\n    pre_configure_source:\n      description: >-\n        Operation to pre-configure the source endpoint.\n    pre_configure_target:\n      description: >-\n        Operation to pre-configure the target endpoint.\n    post_configure_source:\n      description: >-\n        Operation to post-configure the source endpoint.\n    post_configure_target:\n      description: >-\n        Operation to post-configure the target endpoint.\n    add_target:\n      description: >-\n        Operation to notify the source node of a target node being added via a relationship.\n    add_source:\n      description: >-\n        Operation to notify the target node of a source node which is now available via a\n        relationship.\n    target_changed:\n      description: >-\n        Operation to notify source some property or attribute of the target changed\n    remove_target:\n      description: >-\n        Operation to remove a target node.\n    remove_source: # ERRATUM: does not appear in spec, but is mentioned\n      description: >-\n        Operation to remove the source node.\n"
yaml_7_1 = 'tosca_definitions_version: tosca_simple_yaml_1_0_0_wd03\n\nname: apache-lb\ndescription: apacheLB recipe.\n\nimports:\n  - tosca-base-types:1.0\n  - tomcat-types:0.1\n\nnode_types:\n  fastconnect.nodes.apacheLB:\n    derived_from: tosca.nodes.SoftwareComponent\n    description: >\n      This is the definition of the Apache LB Recipe.\n      This is based on Cloudify Apache LB groovy recipe.\n    tags:\n      icon: /images/apache.png\n    properties:\n      version:\n        type: version\n        default: 2\n        constraints:\n          - equal: 2\n    interfaces:\n      Standard:\n        operations:\n          create:\n            implementation_artifact:\n              artifact_type: tosca.artifacts.GroovyScript\n              artifact_ref: "scripts/alien_apacheLB_install.groovy"\n          start:\n            implementation_artifact:\n              artifact_type: tosca.artifacts.GroovyScript\n              artifact_ref: "scripts/apacheLB_start.groovy"\n          stop:\n            implementation_artifact:\n              artifact_type: tosca.artifacts.GroovyScript\n              artifact_ref: "scripts/apacheLB_stop.groovy"\n          delete:\n            implementation_artifact:\n              artifact_type: tosca.artifacts.GroovyScript\n              artifact_ref: "scripts/apacheLB_uninstall.groovy"\n      fastconnect.cloudify.extensions:\n        operations:\n          start_detection:\n            implementation_artifact:\n              artifact_type: tosca.artifacts.GroovyScript\n              artifact_ref: scripts/apacheLB_startDetection.groovy\n      custom:\n        operations:\n          addNode:\n            implementation_artifact:\n              artifact_type: tosca.artifacts.GroovyScript\n              artifact_ref: "scripts/apacheLB_addNode.groovy"\n          removeNode:\n            implementation_artifact:\n              artifact_type: tosca.artifacts.GroovyScript\n              artifact_ref: "scripts/apacheLB_removeNode.groovy"\n    capabilities:\n      httpEndpoint:\n        type: alien4cloud.capabilities.HttpEndpoint\n        lower_bound: 0\n        upper_bound: unbounded\n    artifacts:\n       - scripts: scripts\n         type: fastconnect.artifacts.ResourceDirectory\n'

@parameterized_class([
   { 'yaml': yaml_0_1, 'expected': 0},
   { 'yaml': yaml_14_1, 'expected': 14},
   { 'yaml': yaml_7_1, 'expected': 7}
])

class TestNOPCount(unittest.TestCase):
    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()
    
    def test(self):
        metric = NOP(self.yaml)
        count = metric.count()
        self.assertEqual(count, self.expected, 'Test failed because expected ' + str(self.expected) + ' and got ' + str(count) +'!') 
    
if __name__ == "__main__":
    unittest.main()

