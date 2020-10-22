import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.metrics.nif import NIF


#yaml_nif_id
yaml_0_1 = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\ndescription: Template for deploying a single server with MySQL software on top.\n\ntopology_template:\n  inputs:\n    mysql_rootpw:\n      type: string\n\t  \n    mysql_port:\n      type: integer\n\n  node_templates:\n    db_server:\n      type: tosca.nodes.Compute\n\n    mysql:\n      type: tosca.nodes.DBMS.MySQL'
yaml_1_1 = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\ndescription: Template for deploying a single server with MySQL software on top.\n\ntopology_template:\n  inputs:\n    mysql_rootpw:\n      type: string\n      \n    mysql_port:\n      type: integer\n    \n  node_templates:\n    db_server:\n      type: tosca.nodes.Compute\n      \n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        root_password: { get_input: my_mysql_rootpw }\n        port: { get_input: my_mysql_port }\n      requirements:\n        - host: db_server\n      interfaces:\n        Standard:\n          configure: scripts/my_own_configure.sh'
yaml_1_2 = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ndescription: Template for deploying a two-tier application on two servers.\n\ntopology_template:\n\n  node_templates:\n    wordpress:\n      type: tosca.nodes.WebApplication.WordPress\n      requirements:\n        - host: apache\n        - database_endpoint:\n            node: wordpress_db\n            relationship: wp_db_connection  \n  \n  relationship_templates:\n    wp_db_connection:\n      type: ConnectsTo\n      interfaces:\n        Configure:\n          pre_configure_source: scripts/wp_db_configure.sh\n'
#yaml_1_3 = 'tosca_definitions_version: alien_dsl_2_0_0\n\ndescription: Anaconda-Python for linux system\n\nnode_types:\n  org.ystia.python.linux.bash.nodes.Python:\n    derived_from: org.ystia.nodes.SoftwareComponent\n    description: Python Anaconda component for linux\n    tags:\n      icon: /images/python-logo.png\n    properties:\n      component_version:\n        type: version\n        description: The installed Anaconda Python version\n        default: 2.7.15\n        constraints:\n          - valid_values: [2.7.15]\n    capabilities:\n      python_host:\n        type: org.ystia.python.pub.capabilities.PythonHosting\n        occurrences: [0,unbounded]\n    interfaces:\n      Standard:\n        create:\n          inputs:\n            REPOSITORY: { get_property: [SELF, repository] }\n            NLP_TWITTER: { get_property: [SELF, nlp_twitter] }\n            DATAVIZ: { get_property: [SELF, dataviz] }\n            DATAFORMAT: { get_property: [SELF, dataformat] }\n            PYBRAIN: { get_property: [SELF, pybrain] }\n            ML: { get_property: [SELF, ml] }\n          implementation: scripts/anaconda_install.sh\n'
yaml_2_1 = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\ndescription: Template for deploying a single server with MySQL software on top.\n\ntopology_template:\n  inputs:\n    mysql_rootpw:\n      type: string\n      \n    mysql_port:\n      type: integer\n    \n  node_templates:\n    db_server:\n      type: tosca.nodes.Compute\n      \n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        root_password: { get_input: my_mysql_rootpw }\n        port: { get_input: my_mysql_port }\n      requirements:\n        - host: db_server\n      interfaces:\n        Standard:\n          configure: scripts/my_own_configure.sh\n        Configure:\n          add_target:\n            inputs:\n              member_ip: { get_attribute: [ TARGET, ip_address ] }\n            implementation: scripts/configure_members.py\n'
yaml_2_2 = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ndescription: Template for deploying a two-tier application on two servers.\n\ntopology_template:\n\n  node_templates:\n    wordpress:\n      type: tosca.nodes.WebApplication.WordPress\n      requirements:\n        - host: apache\n        - database_endpoint:\n            node: wordpress_db\n            relationship: wp_db_connection  \n  \n  relationship_templates:\n    wp_db_connection:\n      type: ConnectsTo\n      interfaces:\n        Configure:\n          pre_configure_source: scripts/wp_db_configure.sh\n    another_wp_db_connection:\n      type: ConnectsTo\n      interfaces:\n        Configure:\n          pre_configure_source: scripts/wp_db_configure.sh\n'

@parameterized_class([
   { 'yaml': yaml_0_1, 'expected': 0},
   { 'yaml': yaml_1_1, 'expected': 1},
   { 'yaml': yaml_1_2, 'expected': 1},
   #{ 'yaml': yaml_1_3, 'expected': 1},
   { 'yaml': yaml_2_1, 'expected': 2},
   { 'yaml': yaml_2_2, 'expected': 2}
])

class TestNIFCount(unittest.TestCase):
    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()

    """
    def test(self):
        metric = NIF(self.yaml)
        count = metric.count()
        self.assertEqual(count, self.expected, 'Test failed because expected ' + str(self.expected) + ' and got ' + str(count) +'!') 
    """
if __name__ == "__main__":
    unittest.main()

