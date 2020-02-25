import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.metrics.cdnt import CDNT


#yaml_cdnt_id
yaml_0_1 = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\n \n\ndescription: Template for deploying a single server with MySQL software on top.\n\n \n\ntopology_template:\n\n  inputs:\n\n    mysql_rootpw:\n\n      type: string\n\n    mysql_port:\n\n      type: integer\n\n    # rest omitted here for brevity\n\n \n\n  node_templates:\n\n    db_server:\n\n      type: tosca.nodes.Compute\n\n      # rest omitted here for brevity\n\n \n\n    mysql:\n\n      type: tosca.nodes.DBMS.MySQL'
yaml_3_1 = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\nnode_types:\n\n  tosca.nodes.Root:\n    attributes:\n      tosca_id:\n        type: string\n      tosca_name:\n        type: string\n\n  tosca.nodes.Abstract.Compute:\n    derived_from: tosca.nodes.Root\n    capabilities:\n      host:\n        type: tosca.capabilities.Compute\n\n  tosca.nodes.Compute:\n    attributes:\n      private_address:\n        type: string\n      public_address:\n        type: string\n'

@parameterized_class([
   { 'yaml': yaml_0_1, 'expected': 0},
   { 'yaml': yaml_3_1, 'expected': 3}
])

class TestCDNTCount(unittest.TestCase):
    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()
    
    def test(self):
        metric = CDNT(self.yaml)
        count = metric.count()
        self.assertEqual(count, self.expected, 'Test failed because expected ' + str(self.expected) + ' and got ' + str(count) +'!') 
    
if __name__ == "__main__":
    unittest.main()

