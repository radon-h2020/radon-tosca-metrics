import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.metrics.nout import NOUT


#yaml_nout_id
yaml_0_1 = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ntopology_template:\n  description: Template of a database including its hosting stack.\n\n  inputs:\n    mq_service_ip:\n      type: string\n      description: IP address of the message queuing server to receive messages from\n    receiver_port:\n      type: string\n      description: Port to be used for receiving messages '
yaml_1_1 = '\ntosca_definitions_version: alien_dsl_2_0_0\n\nmetadata:\n  template_name: org.ystia.tests.topologies.nifi\n  template_version: 2.2.0-SNAPSHOT\n  template_author: Ystia\n\nimports:\n  - tosca-normative-types:1.0.0-ALIEN20\n  - org.ystia.common:2.2.0-SNAPSHOT\n  - org.ystia.consul.pub:2.2.0-SNAPSHOT\n  - org.ystia.consul.linux.bash:2.2.0-SNAPSHOT\n  - org.ystia.java.pub:2.2.0-SNAPSHOT\n  - org.ystia.java.linux.bash:2.2.0-SNAPSHOT\n  - org.ystia.nifi.linux.bash:2.2.0-SNAPSHOT\n\ntopology_template:\n  description: A basic topology template with NiFi\n\n  inputs:\n    repository:\n      type: string\n      required: false\n      default: "http://archive.apache.org/dist/nifi/1.1.2"\n      constraints:\n        - pattern: ^(http|https|ftp)://.+/.*$\n\n  node_templates:\n    Network:\n      type: tosca.nodes.Network\n      properties:\n        ip_version: 4\n    Compute:\n      type: tosca.nodes.Compute\n      properties:\n        mem_size: 12GB\n      requirements:\n        - network:\n            node: Network\n            relationship: tosca.relationships.Network\n    Java:\n      type: org.ystia.java.linux.bash.nodes.Java\n      requirements:\n        - host:\n            node: Compute\n    NiFi:\n      type: org.ystia.nifi.linux.bash.nodes.NiFi\n      properties:\n        repository: { get_input: repository }\n      requirements:\n        - host:\n            node: Java\n\n  outputs:\n    nifi_url:\n      description: The URL to access the NiFi GUI\n      value: { get_attribute: [ NiFi, url ] }\n'
yaml_2_1 = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ntopology_template:\n  description: Template of a database including its hosting stack.\n\n  inputs:\n    mq_service_ip:\n      type: string\n      description: IP address of the message queuing server to receive messages from\n    receiver_port:\n      type: string\n      description: Port to be used for receiving messages \n\n  outputs:\n    receiver_ip:\n      description: private IP address of the message receiver application\n      value: { get_attribute: [ server, private_address ] }\n    receiver_port:\n      description: Port of the message receiver endpoint\n      value: { get_attribute: [ app, app_endpoint, port ] }\n'

@parameterized_class([
   { 'yaml': yaml_0_1, 'expected': 0},
   { 'yaml': yaml_1_1, 'expected': 1},
   { 'yaml': yaml_2_1, 'expected': 2}
])

class TestNOUTCount(unittest.TestCase):
    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()
    
    def test(self):
        metric = NOUT(self.yaml)
        count = metric.count()
        self.assertEqual(count, self.expected, 'Test failed because expected ' + str(self.expected) + ' and got ' + str(count) +'!') 
    
if __name__ == "__main__":
    unittest.main()

