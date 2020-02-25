import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.metrics.ngc import NGC


#yaml_ngc_id
yaml_1_1 = 'tosca_definitions_version: alien_dsl_2_0_0\n\nnode_types:\n  org.ystia.mysql.linux.bash.nodes.MySQLServer:\n    derived_from: org.ystia.nodes.DBMS\n    description: MySQL Server component for linux\n    capabilities:\n      host:\n        type: org.ystia.mysql.pub.capabilities.Container.MySQLServer'
yaml_1_2 = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ntopology_template:\n  node_templates:\n    log_ip:\n      type: tosca.nodes.samples.LogIp\n      requirements:\n        - host:\n            node: compute\n            capability: tosca.capabilities.Container\n            relationship: tosca.relationships.HostedOn'
yaml_5_1 = 'tosca_definitions_version: tosca_simple_yaml_1_0\ndescription: Template with requirements against hosting infrastructure.\n\ntopology_template:\n  inputs:\n    # omitted here for brevity\n\n  node_templates:\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        # omitted here for brevity\n      requirements:\n        - host:\n            node_filter:\n              capabilities:\n                - host:\n                    properties:\n                      - num_cpus: { in_range: [ 1, 4 ] }\n                      - mem_size: { greater_or_equal: 2 GB }\n                - os:\n                    properties:\n                      - architecture: { equal: x86_64 }\n                      - type: linux\n                      - distribution: ubuntu\n                - backup_os:\n                    properties:\n                      - architecture: { equal: x86_64 }\n                      - type: linux\n                      - distribution: ubuntu\n                      \n    backup_mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        # omitted here for brevity\n      requirements:\n        - host:\n            node_filter:\n              capabilities:\n                - host:\n                    properties:\n                      - num_cpus: { in_range: [ 1, 4 ] }\n                      - mem_size: { greater_or_equal: 2 GB }\n                - os:\n                    properties:\n                      - architecture: { equal: x86_64 }\n                      - type: linux\n                      - distribution: ubuntu'

@parameterized_class([
   { 'yaml': yaml_1_1, 'expected': 1},
   { 'yaml': yaml_1_2, 'expected': 1},
   { 'yaml': yaml_5_1, 'expected': 5}
])

class TestNGCCount(unittest.TestCase):
    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()
    
    def test(self):
        metric = NGC(self.yaml)
        count = metric.count()
        self.assertEqual(count, self.expected, 'Test failed because expected ' + str(self.expected) + ' and got ' + str(count) +'!') 
    
if __name__ == "__main__":
    unittest.main()

