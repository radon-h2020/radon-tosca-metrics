import unittest
from parameterized import parameterized_class
from toscametrics.general.num_keys import NumKeys

yaml_2_1 = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\ndescription: Template for deploying a single server ' \
           'with MySQL software on top. '
yaml_19_1 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template for deploying a single server ' \
            'with predefined properties.\n\ntopology_template:\n  inputs:\n    cpus:\n      type: integer\n      ' \
            'description: Number of CPUs for the server.\n      constraints:\n        - valid_values: [ 1, 2, 4, ' \
            '8 ]\n\n  node_templates:\n    my_server:\n      type: tosca.nodes.Compute\n      capabilities:\n        ' \
            '# Host container properties\n        host:\n          properties:\n            # Compute properties\n    ' \
            '        num_cpus: { get_input: cpus }\n            mem_size: 2048  MB\n            disk_size: 10 GB '


@parameterized_class([
   { 'yaml': yaml_2_1, 'expected': 2},
   { 'yaml': yaml_19_1, 'expected': 19}
])
class TestNKEYSCount(unittest.TestCase):

    def setUp(self):
        self.yaml = self.yaml.expandtabs(2)

    def test(self):
        self.assertEqual(NumKeys(self.yaml).count(), self.expected)