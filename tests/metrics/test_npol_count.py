import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.metrics.npol import NPOL


#yaml_npol_id
yaml_1_1 = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ntopology_template:\n  node_templates:\n    wordpress_server:\n      type: tosca.nodes.WebServer\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n\n  groups:\n    my_co_location_group:\n      type: tosca.groups.Root\n      members: [ wordpress_server, mysql ]\n\t  \n  policies:\n    - my_anti_collocation_policy:\n        type: my.policies.anticolocateion\n        targets: [ my_co_location_group ]'
yaml_1_2 = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ntopology_template:\n  node_templates:\n    server2:\n      type: Compute\n\n    storage:\n      type: ObjectStorage\n      properties:\n        name: My Storage\n\n  groups:\n\n    redundants:\n      type: Redundants\n      properties:\n        priority: 0.8\n      members:\n      # Member node templates must match our definition at the group type\n      # (Can include derived types)\n      - server3\n      - server4\n\n  policies:\n\n    backup:\n      type: ContinuousBackup\n      properties:\n        frequency: .5 d\n      targets:\n      # Target node templates and groups must match our definition at the policy type\n      # (Can include derived types)\n      - storage\n      - server2\n      - redundants'

@parameterized_class([
   { 'yaml': yaml_1_1, 'expected': 1},
   { 'yaml': yaml_1_2, 'expected': 1}
])

class TestNPOLCount(unittest.TestCase):
    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()
    
    def test(self):
        metric = NPOL(self.yaml)
        count = metric.count()
        self.assertEqual(count, self.expected, 'Test failed because expected ' + str(self.expected) + ' and got ' + str(count) +'!') 
    
if __name__ == "__main__":
    unittest.main()

