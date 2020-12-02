import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.yml.text_entropy import TextEntropy

yaml_535_1 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template for deploying a single server ' \
             'with predefined properties.\n\ntopology_template:\n  inputs:\n    cpus:\n      type: integer\n      ' \
             'description: Number of CPUs for the server.\n      constraints:\n        - valid_values: [ 1, 2, 4, ' \
             '8 ]\n\n  node_templates:\n    my_server:\n      type: tosca.nodes.Compute\n      capabilities:\n        ' \
             '# Host container properties\n        host:\n          properties:\n            # Compute properties\n   ' \
             '         num_cpus: { get_input: cpus }\n            mem_size: 2048  MB\n            disk_size: 10 GB '
yaml_527_1 = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ntopology_template:\n  description: Template of a ' \
             'database including its hosting stack.\n\n  inputs:\n    mq_service_ip:\n      type: string\n      ' \
             'description: IP address of the message queuing server to receive messages from\n    receiver_port:\n    ' \
             '  type: string\n      description: Port to be used for receiving messages \n\n  outputs:\n    ' \
             'receiver_ip:\n      description: private IP address of the message receiver application\n      value: { ' \
             'get_attribute: [ server, private_address ] }\n    receiver_port:\n      description: Port of the ' \
             'message receiver endpoint\n      value: { get_attribute: [ app, app_endpoint, port ] } '

@parameterized_class([
   {'yaml': yaml_535_1, 'expected': 5.35},
   {'yaml': yaml_527_1, 'expected': 5.27}
])
class TestETPCount(unittest.TestCase):

    def setUp(self):
        self.blueprint = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.blueprint.close()

    def test(self):
        self.assertEqual(TextEntropy(self.blueprint).count, self.expected)
