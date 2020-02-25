import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.metrics.nsh import NSH


#yaml_nsh_id
yaml_1_1 = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ndescription: Template for deploying a single server with MySQL software on top.\n\ntopology_template:\n  node_templates:\n    db_server:\n      type: tosca.nodes.Compute\n\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        root_password: { get_input: mysql_rootpw }\n        port: { get_input: mysql_port }\n      requirements:\n        - host: db_server\n      interfaces:\n        Standard:\n          configure: scripts/my_own_configure.sh'
yaml_2_1 = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ntopology_template:     \n  node_templates: \n    wordpress:\n      type: tosca.nodes.WebApplication.WordPress\n      requirements:\n        - database_endpoint: mysql_database\n      interfaces:\n        Standard:\n          create: wordpress_install.sh\n          configure:\n            implementation: wordpress_configure.sh           \n            inputs:\n              wp_db_port: { get_property: [ SELF, database_endpoint, port ] }'
yaml_4_1 = 'tosca_definitions_version: alien_dsl_2_0_0\n\nnode_types:\n  org.ystia.cloudera.linux.bash.nodes.ClouderaServer:\n    derived_from: org.ystia.consul.pub.nodes.ConsulUser\n    interfaces:\n      Standard:\n        create:\n          inputs:\n            CLOUDERA_MANAGER_REPO: { get_property: [SELF, cloudera_manager_repository] }\n            NTP_SERVER: { get_property: [SELF, ntp_server] }\n          implementation: scripts/clouderamanager_install.sh\n        configure:\n          implementation: scripts/clouderamanager_config.sh\n        start:\n          implementation: scripts/clouderamanager_start.sh\n        stop:\n          implementation: scripts/clouderamanager_stop.sh'

@parameterized_class([
   { 'yaml': yaml_1_1, 'expected': 1},
   { 'yaml': yaml_2_1, 'expected': 2},
   { 'yaml': yaml_4_1, 'expected': 4}
])

class TestNSHCount(unittest.TestCase):
    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()
    
    def test(self):
        metric = NSH(self.yaml)
        count = metric.count()
        self.assertEqual(count, self.expected, 'Test failed because expected ' + str(self.expected) + ' and got ' + str(count) +'!') 
    
if __name__ == "__main__":
    unittest.main()

