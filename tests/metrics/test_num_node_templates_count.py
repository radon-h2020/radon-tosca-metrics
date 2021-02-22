import unittest
from parameterized import parameterized_class
from toscametrics.blueprint.num_node_templates import NumNodeTemplates


yaml_0 = 'tosca_definitions_version: tosca_simple_yaml_1_0'
yaml_1 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template for deploying a single server ' \
           'with predefined properties.\n\ntopology_template:\n  inputs:\n    cpus:\n      type: integer\n      ' \
           'description: Number of CPUs for the server.\n      constraints:\n        - valid_values: [ 1, 2, 4, ' \
           '8 ]\n\n  node_templates:\n    my_server:\n      type: tosca.nodes.Compute\n      capabilities:\n        # ' \
           'Host container properties\n        host:\n          properties:\n            # Compute properties\n       ' \
           '     num_cpus: { get_input: cpus }\n            mem_size: 2048  MB\n            disk_size: 10 GB '
yaml_2 = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\ndescription: Template for deploying a single server ' \
           'with MySQL software on top.\n\ntopology_template:\n  inputs:\n    mysql_rootpw:\n      type: string\n     ' \
           ' \n    mysql_port:\n      type: integer\n    \n  node_templates:\n    db_server:\n      type: ' \
           'tosca.nodes.Compute\n      \n    mysql:\n      type: tosca.nodes.DBMS.MySQL '


@parameterized_class([
   {'yaml': yaml_0, 'expected': 0},
   {'yaml': yaml_1, 'expected': 1},
   {'yaml': yaml_2, 'expected': 2}
])
class TestNumNodeTemplatesCount(unittest.TestCase):
    def setUp(self):
        self.blueprint = self.yaml.expandtabs(2)

    def test(self):
        self.assertEqual(NumNodeTemplates(self.blueprint).count(), self.expected)

