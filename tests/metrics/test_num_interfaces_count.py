import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.blueprint.num_interfaces import NumInterfaces


yaml_0 = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\ndescription: Template for deploying a single server ' \
         'with MySQL software on top.\n\ntopology_template:\n  inputs:\n    mysql_rootpw:\n      type: string\n\t  \n ' \
         '   mysql_port:\n      type: integer\n\n  node_templates:\n    db_server:\n      type: ' \
         'tosca.nodes.Compute\n\n    mysql:\n      type: tosca.nodes.DBMS.MySQL '
yaml_2 = 'tosca_definitions_version: tosca_simple_yaml_1_3\ntopology_template:\n\n\tnode_templates:\n\t\twordpress:\n' \
         '\t\t\ttype: tosca.nodes.WebApplication.WordPress\n\t\t\tproperties:\n\t\t\t\tadmin_user: { get_input: ' \
         'wp_admin_username }\n\t\t\t\tadmin_password: { get_input: wp_admin_password }\n\t\t\t\tdb_host: { ' \
         'get_attribute: [ db_server, private_address ] ' \
         '}\n\t\t\tinterfaces:\n\t\t\t\tStandard:\n\t\t\t\t\tinputs:\n\t\t\t\t\t\tdb_host: { get_attribute: [ ' \
         'db_server, private_address ] }\n\t\t\t\t\t\tdb_port: { get_property: [ mysql, ' \
         'port ] }\n\n\trelationship_templates:\n\t\twp_db_connection:\n\t\t\ttype: ' \
         'ConnectsTo\n\t\t\tinterfaces:\n\t\t\t\tConfigure:\n\t\t\t\t\tpre_configure_source: ' \
         'scripts/wp_db_configure.sh '


@parameterized_class([
   {'yaml': yaml_0, 'expected': 0},
   {'yaml': yaml_2, 'expected': 2}
])
class TestNumInterfacesCount(unittest.TestCase):
    def setUp(self):
        self.blueprint = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.blueprint.close()
    
    def test(self):
        self.assertEqual(NumInterfaces(self.blueprint).count(), self.expected)
