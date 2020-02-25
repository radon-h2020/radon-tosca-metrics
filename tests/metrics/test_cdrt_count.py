import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.metrics.cdrt import CDRT


#yaml_cdrt_id
yaml_0_1 = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\n \n\ndescription: Template for deploying a single server with MySQL software on top.\n\n \n\ntopology_template:\n\n  inputs:\n\n    mysql_rootpw:\n\n      type: string\n\n    mysql_port:\n\n      type: integer\n\n    # rest omitted here for brevity\n\n \n\n  node_templates:\n\n    db_server:\n\n      type: tosca.nodes.Compute\n\n      # rest omitted here for brevity\n\n \n\n    mysql:\n\n      type: tosca.nodes.DBMS.MySQL'
yaml_1_1 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ntopology_template:\n  relationship_templates:\n    storage_attachesto_1:\n      type: MyAttachesTo\n      properties:\n        location: /my_data_location\n\nrelationship_types:\n  MyAttachesTo:\n    derived_from: AttachesTo\n    interfaces:\n      some_interface_name:\n        some_operation:\n          implementation: default_script.sh'
yaml_2_1 = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\nrelationship_types:\n\n  tosca.relationships.Root:\n    attributes:\n      tosca_id:\n        type: string\n\n  tosca.relationships.DependsOn:\n    derived_from: tosca.relationships.Root\n    valid_target_types: [ tosca.capabilities.Node ]'

@parameterized_class([
   { 'yaml': yaml_0_1, 'expected': 0},
   { 'yaml': yaml_1_1, 'expected': 1},
   { 'yaml': yaml_2_1, 'expected': 2}
])

class TestCDRTCount(unittest.TestCase):
    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()
    
    def test(self):
        metric = CDRT(self.yaml)
        count = metric.count()
        self.assertEqual(count, self.expected, 'Test failed because expected ' + str(self.expected) + ' and got ' + str(count) +'!') 
    
if __name__ == "__main__":
    unittest.main()

