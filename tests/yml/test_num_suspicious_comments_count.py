import unittest
from parameterized import parameterized_class
from toscametrics.general.num_suspicious_comments import NumSuspiciousComments

yaml_0 = 'topology_template:\n  node_templates:\n    my_server:\n      type: tosca.nodes.Compute\n\t  \n    ' \
           'cluster:\n      type: tosca.nodes.DBMS.Cluster\n      requirements:\n        - host: my_server\n      ' \
           'interfaces:\n        tosca.interfaces.nodes.custom.Backup:\n          operations:\n            backup: ' \
           'backup.sh '
yaml_2 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template for deploying a single server ' \
           'with predefined properties.\n\n#TODO: add extra valid values \ntopology_template:\n  inputs:\n    cpus:\n ' \
           '     type: integer\n      description: Number of CPUs for the server.\n      constraints:\n        - ' \
           'valid_values: [ 1, 2, 4, 8 ]\n\n  node_templates:\n    my_server:\n      type: tosca.nodes.Compute\n      ' \
           'capabilities:\n        # Host container properties\n        host:\n          properties:\n            ' \
           '#TESTME: test the memory size\n            num_cpus: { get_input: cpus }\n            mem_size: 2048  ' \
           'MB\n            disk_size: 10 GB '


@parameterized_class([
   {'yaml': yaml_0, 'expected': 0},
   {'yaml': yaml_2, 'expected': 2}
])
class TestNSCMCount(unittest.TestCase):

    def setUp(self):
        self.yaml = self.yaml.expandtabs(2)

    def test(self):
        self.assertEqual(NumSuspiciousComments(self.yaml).count(), self.expected)
