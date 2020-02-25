import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.metrics.cddt import CDDT


#yaml_cddt_id
yaml_0_1 = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\n \n\ndescription: Template for deploying a single server with MySQL software on top.\n\n \n\ntopology_template:\n\n  inputs:\n\n    mysql_rootpw:\n\n      type: string\n\n    mysql_port:\n\n      type: integer\n\n    # rest omitted here for brevity\n\n \n\n  node_templates:\n\n    db_server:\n\n      type: tosca.nodes.Compute\n\n      # rest omitted here for brevity\n\n \n\n    mysql:\n\n      type: tosca.nodes.DBMS.MySQL'
yaml_2_1 = 'tosca_definitions_version: tosca_simple_yaml_1_1\n\ndata_types:\n  NetworkInfo:\n    derived_from: tosca.Data.Root\n    properties:\n      name:\n        type: string\n      gateway:\n        type: string      \n\n  RouterInfo:\n    derived_from: tosca.Data.Root\n    properties:\n      ip:\n        type: string\n      external:\n        type: string\n\ntopology_template:\n  inputs:\n    management_network:\n      type: NetworkInfo\n    router:\n      type: RouterInfo'

@parameterized_class([
   { 'yaml': yaml_0_1, 'expected': 0},
   { 'yaml': yaml_2_1, 'expected': 2}
])

class TestCDDTCount(unittest.TestCase):
    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()
    
    def test(self):
        metric = CDDT(self.yaml)
        count = metric.count()
        self.assertEqual(count, self.expected, 'Test failed because expected ' + str(self.expected) + ' and got ' + str(count) +'!') 
    
if __name__ == "__main__":
    unittest.main()

