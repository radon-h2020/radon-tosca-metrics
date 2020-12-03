import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.metrics.num_parameters import NumParameters


#yaml_ninp_id
yaml_0 = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\ndescription: Template for deploying a single server ' \
         'with MySQL software on top.\n\ntopology_template:\n  node_templates:\n    db_server:\n      type: ' \
         'tosca.nodes.Compute\n\n    mysql:\n      type: tosca.nodes.DBMS.MySQL '
yaml_5 = 'tosca_definitions_version: tosca_simple_yaml_1_3\ntopology_template:\n\n\tinputs:\n\t\t# Admin user name ' \
         'and password to use with the WordPress application\n\t\twp_admin_username:\n\t\t\ttype: ' \
         'string\n\t\twp_admin_password:\n\t\t\ttype: string\n\t\tcontext_root:\n\t\t\ttype: ' \
         'string\n\n\tnode_templates:\n\t\twordpress:\n\t\t\ttype: ' \
         'tosca.nodes.WebApplication.WordPress\n\t\t\tproperties:\n\t\t\t\tadmin_user: { get_input: wp_admin_username ' \
         '}\n\t\t\t\tadmin_password: { get_input: wp_admin_password }\n\t\t\t\tdb_host: { get_attribute: [ db_server, ' \
         'private_address ] }\n\t\t\tinterfaces:\n\t\t\t\tStandard:\n\t\t\t\t\tinputs:\n\t\t\t\t\t\tdb_host: { ' \
         'get_attribute: [ db_server, private_address ] }\n\t\t\t\t\t\tdb_port: { get_property: [ mysql, ' \
         'port ] }\n\t\t\t\t\t\tdb_name: { get_property: [ wordpress_db, name ] }\n\t\t\t\t\t\tdb_user: { ' \
         'get_property: [ wordpress_db, user ] }\n\t\t\t\t\t\tdb_password: { get_property: [ wordpress_db, ' \
         'password ] } '


@parameterized_class([
   { 'yaml': yaml_0, 'expected': 0},
   { 'yaml': yaml_5, 'expected': 5},
])
class TestNumParametersCount(unittest.TestCase):
    def setUp(self):
        self.blueprint = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.blueprint.close()
    
    def test(self):
        self.assertEqual(NumParameters(self.blueprint).count(), self.expected)
