import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.metrics.na import NA


#yaml_na_id
yaml_0_1 = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\ndescription: Template for deploying a single server with MySQL software on top.\n\ntopology_template:\n  inputs:\n    mysql_rootpw:\n      type: string\n\t  \n    mysql_port:\n      type: integer\n\n  node_templates:\n    db_server:\n      type: tosca.nodes.Compute\n\n    mysql:\n      type: tosca.nodes.DBMS.MySQL'
yaml_1_1 = 'tosca_definitions_version: alien_dsl_2_0_0\n\ntopology_template:\n  node_templates:\n    Logstash:\n      type: org.ystia.logstash.linux.bash.nodes.Logstash\n      properties:\n        repository: { get_input: repository }\n      artifacts:\n        filters_conf:\n          file: config/logstash-apache-generator-filters.conf\n          type: tosca.artifacts.File'
yaml_2_1 = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\ndescription: Template for deploying a single server with MySQL software on top.\n\ntopology_template:\n  inputs:\n    mysql_rootpw:\n      type: string\n      \n    mysql_port:\n      type: integer\n    \n  node_templates:\n    dbServer:\n      type: tosca.nodes.Compute\n      properties:\n        name:\n        description:\n      artifacts:\n        configuration:\n          type: tosca.artifacts.Implementation.Ansible\n          file: implementation/configuration/Ansible/configure.yml\n        template_configuration:\n          type: tosca.artifacts.template.Jinja2\n          file: implementation/configuration/templates/template_configuration.jinja2\n      \n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        root_password: { get_input: my_mysql_rootpw }\n        port: { get_input: my_mysql_port }\n      requirements:\n        - host: db_server\n      interfaces:\n        Standard:\n          configure: scripts/my_own_configure.sh\n        Configure:\n          add_target:\n            inputs:\n              member_ip: { get_attribute: [ TARGET, ip_address ] }\n            implementation: scripts/configure_members.py\n'
yaml_1_2 = "tosca_definitions_version: tosca_simple_yaml_1_2\n\nimports:\n- artifacts.yaml\n- relationships.yaml\n\nnode_types:\n\n  tosca.nodes.nfv.VDU.Compute:\n    derived_from: tosca.nodes.Compute\n    capabilities:\n      virtual_compute:\n        description: >-\n          Describes virtual compute resources capabilities.\n        type: tosca.capabilities.nfv.VirtualCompute\n    artifacts:\n      sw_image:\n        description: >-\n          Describes the software image which is directly loaded on the virtualization container\n          realizing this virtual storage.\n        file: '' # ERRATUM: missing value even though it is required in TOSCA\n        type: tosca.artifacts.nfv.SwImage"

@parameterized_class([
   { 'yaml': yaml_0_1, 'expected': 0},
   { 'yaml': yaml_1_1, 'expected': 1},
   { 'yaml': yaml_2_1, 'expected': 2},
   { 'yaml': yaml_1_2, 'expected': 1}
])

class TestNACount(unittest.TestCase):
    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()
    
    def test(self):
        metric = NA(self.yaml)
        count = metric.count()
        self.assertEqual(count, self.expected, 'Test failed because expected ' + str(self.expected) + ' and got ' + str(count) +'!') 
    
if __name__ == "__main__":
    unittest.main()

