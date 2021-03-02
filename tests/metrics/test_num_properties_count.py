import unittest
from parameterized import parameterized_class
from toscametrics.blueprint.num_properties import NumProperties


yaml_0 = 'tosca_definitions_version: tosca_simple_yaml_1_0\ntopology_template:\n\tnode_templates:\n\t\tmysql:\n\t\t' \
         '\ttype: tosca.nodes.DBMS.MySQL\n\t\t\tproperties: 1'
yaml_7 = 'tosca_definitions_version: tosca_simple_yaml_1_0\ntopology_template:\n\tnode_templates:\n\t\tmysql:\n\t\t' \
         '\ttype: tosca.nodes.DBMS.MySQL\n\t\t\tproperties:\n\t\t\t\troot_password: { get_input: my_mysql_rootpw ' \
         '}\n\t\t\t\tport: { get_input: my_mysql_port }\n\t\t\trequirements:\n\t\t\t\t- ' \
         'host:\n\t\t\t\t\t\tnode_filter:\n\t\t\t\t\t\t\tcapabilities:\n\t\t\t\t\t\t\t\t- ' \
         'host:\n\t\t\t\t\t\t\t\t\t\tproperties:\n\t\t\t\t\t\t\t\t\t\t\t- num_cpus: { in_range: [ 1, ' \
         '4 ] }\n\t\t\t\t\t\t\t\t\t\t\t- mem_size: { greater_or_equal: 2 GB }\n\t\t\t\t\t\t\t\t- ' \
         'os:\n\t\t\t\t\t\t\t\t\t\tproperties:\n\t\t\t\t\t\t\t\t\t\t\t- architecture: { equal: x86_64 ' \
         '}\n\t\t\t\t\t\t\t\t\t\t\t- type: linux\n\t\t\t\t\t\t\t\t\t\t\t- distribution: ubuntu '


@parameterized_class([
   {'yaml': yaml_0, 'expected': 0},
   {'yaml': yaml_7, 'expected': 7}
])
class TestNumPropertiesCount(unittest.TestCase):
    def setUp(self):
        self.yaml = self.yaml.expandtabs(2)

    def test(self):
        self.assertEqual(NumProperties(self.yaml).count(), self.expected)

