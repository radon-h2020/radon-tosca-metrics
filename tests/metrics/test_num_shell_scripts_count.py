import unittest
from parameterized import parameterized_class
from toscametrics.blueprint.num_shell_scripts import NumShellScripts

yaml_1 = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ndescription: Template for deploying a single server ' \
         'with MySQL software on top.\n\ntopology_template:\n\tnode_templates:\n\t\tdb_server:\n\t\t\ttype: ' \
         'tosca.nodes.Compute\n\n\t\tmysql:\n\t\t\ttype: ' \
         'tosca.nodes.DBMS.MySQL\n\t\t\tproperties:\n\t\t\t\troot_password: { get_input: mysql_rootpw ' \
         '}\n\t\t\t\tport: { get_input: mysql_port }\n\t\t\trequirements:\n\t\t\t\t- host: ' \
         'db_server\n\t\t\tinterfaces:\n\t\t\t\tStandard:\n\t\t\t\t\tconfigure: scripts/my_own_configure.sh '


@parameterized_class([
   {'yaml': yaml_1, 'expected': 1},
])
class TestNumShellScriptsCount(unittest.TestCase):
    def setUp(self):
        self.yaml = self.yaml.expandtabs(2)

    def test(self):
        metric = NumShellScripts(self.yaml)
        count = metric.count()
        self.assertEqual(count, self.expected)

