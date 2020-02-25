import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.metrics.nf import NF


#yaml_nf_id
yaml_1_1 = 'tosca_definitions_version: tosca_simple_yaml_1_3\n             \ndescription: Template with requirements against hosting infrastructure.\n\ntopology_template:\n  node_templates:\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      requirements:\n        - host: mysql_compute\n\n    mysql_compute:\n      type: Compute\n      directives: [ select ]\n      node_filter:\n        capabilities:\n          - host:\n              properties:\n                num_cpus: { equal: 2 }\n                mem_size: { greater_or_equal: 2 GB }\n          - os:\n              properties:\n                architecture: { equal: x86_64 }\n                type: linux\n                distribution: ubuntu'
yaml_1_2 = 'tosca_definitions_version: tosca_simple_yaml_1_3                \n\ndescription: Template with requirements against hosting infrastructure.\n\ntopology_template:\n  node_templates:\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      requirements:\n        - host:\n            node_filter:\n              capabilities:\n                - host:\n                    properties:\n                      - num_cpus: { in_range: [ 1, 4 ] }\n                      - mem_size: { greater_or_equal: 2 GB }\n                - os:\n                    properties:\n                      - architecture: { equal: x86_64 }\n                      - type: linux\n                      - distribution: ubuntu'
yaml_1_3 = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ntopology_template:\n\n  inputs:\n    rulesInput:\n      type: list\n      entry_schema: FirewallRules\n      \n  substitution_mappings:\n    node_type: abstract.Firewall\n    substitution_filter:\n      properties:\n        - vendor: { equal: Simple }\n    properties:\n      rules: [ rulesInput ]\n  node_templates:\n    acme:\n      type: SimpleFirewall\n      properties:\n        rules: { get_input: rulesInput }\n'


@parameterized_class([
   { 'yaml': yaml_1_1, 'expected': 1},
   { 'yaml': yaml_1_2, 'expected': 1},
   { 'yaml': yaml_1_3, 'expected': 1}
])

class TestNFCount(unittest.TestCase):
    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()
    
    def test(self):
        metric = NF(self.yaml)
        count = metric.count()
        self.assertEqual(count, self.expected, 'Test failed because expected ' + str(self.expected) + ' and got ' + str(count) +'!') 
    
if __name__ == "__main__":
    unittest.main()

