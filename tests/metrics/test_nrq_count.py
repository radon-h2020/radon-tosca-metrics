import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.metrics.nrq import NRQ


#yaml_nrq_id
yaml_0_1 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ntopology_template:\n  relationship_types:\n    MyAttachesTo:\n      derived_from: AttachesTo\n      interfaces:\n        some_interface_name:\n          some_operation:\n            implementation: default_script.sh'
yaml_1_1 = 'tosca_definitions_version: alien_dsl_2_0_0\n\ndescription: Cloudera big data distribution for Linux system\n\n\nnode_types:\n  org.ystia.cloudera.linux.bash.nodes.ClouderAgent:\n    derived_from: org.ystia.consul.pub.nodes.ConsulUser\n    requirements:\n      - server_endpoint:\n           capability: org.ystia.cloudera.pub.capabilities.ClouderaServerEndpoint\n           relationship: org.ystia.cloudera.linux.bash.relationships.ClouderaAgentConnectsToClouderaServer\n           occurrences: [1,1]'
yaml_2_1 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ntopology_template:\n  node_templates:\n    my_block_storage:\n      type: BlockStorage\n      properties:\n        size: 10\n\n    my_web_app_tier_1:\n      type: Compute\n      requirements:\n        - local_storage:\n            node: my_block_storage\n            relationship: MyAttachesTo\n              # use default property settings in the Relationship Type definition\n\n    my_web_app_tier_2:\n      type: Compute\n      requirements:\n        - local_stooooorage:\n            node: my_block_storage\n            relationship:\n              type: MyAttachesTo\n              # Override default property setting for just the â€˜locationâ€™ property\n              properties:\n                location: /some_other_data_location '

@parameterized_class([
   { 'yaml': yaml_0_1, 'expected': 0},
   { 'yaml': yaml_1_1, 'expected': 1},
   { 'yaml': yaml_2_1, 'expected': 2}
])

class TestNRQCount(unittest.TestCase):
    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()
    
    def test(self):
        metric = NRQ(self.yaml)
        count = metric.count()
        self.assertEqual(count, self.expected, 'Test failed because expected ' + str(self.expected) + ' and got ' + str(count) +'!') 
    
if __name__ == "__main__":
    unittest.main()

