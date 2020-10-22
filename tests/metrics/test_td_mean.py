import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.metrics.td import TD


#yaml_td_id
yaml_0_1 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\nimports:\n  - paypalpizzastore_nodejs_app.yaml'
yaml_2_1 = 'tosca_definitions_version: tosca_simple_yaml_1_3\ncapability_types:\n  radon.capabilities.kafka.KafkaHosting:\n    derived_from: tosca.capabilities.Container\n'
yaml_53_1 = "tosca_definitions_version: tosca_simple_yaml_1_0_0\n\ndescription: >\n  TOSCA simple profile with 1 network and 1 attached server\n\ntopology_template:\n  inputs:\n    network_name:\n      type: string\n      description: Network name\n\n  node_templates:\n    my_server:\n      type: tosca.nodes.Compute\n      capabilities:\n        host:\n          properties:\n            disk_size: 10\n            num_cpus: 1\n            mem_size: 512\n        os:\n          properties:\n            architecture: x86_64\n            type: Linux\n            distribution: CirrOS\n            version: 0.3.2\n    my_network:\n      type: tosca.nodes.network.Network\n      properties:\n        ip_version: 4\n        cidr: '192.168.0.0/24'\n        network_name: { get_input: network_name }\n        start_ip: '192.168.0.50'\n        end_ip: '192.168.0.200'\n        gateway_ip: '192.168.0.1'\n    my_port:\n      type: tosca.nodes.network.Port\n      requirements:\n        - binding:\n            node: my_server\n        - link:\n            node: my_network\n\n"

@parameterized_class([
   { 'yaml': yaml_0_1, 'expected': 0},
   { 'yaml': yaml_2_1, 'expected': 2},
   { 'yaml': yaml_53_1, 'expected': 5/3}
])

class TestTDMean(unittest.TestCase):
    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()
    
    def test(self):
        metric = TD(self.yaml)
        mean = metric.mean()
        self.assertEqual(mean, self.expected, 'Test failed because expected ' + str(self.expected) + ' and got ' + str(mean) +'!') 
    
if __name__ == "__main__":
    unittest.main()

