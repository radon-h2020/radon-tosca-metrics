import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.metrics.nnt import NNT


#yaml_nnt_id
yaml_0_1 = 'tosca_definitions_version: tosca_simple_yaml_1_0'
yaml_1_1 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\n \n\ndescription: Template for deploying a single server with predefined properties.\n\n \n\ntopology_template:\n\n  inputs:\n\n    cpus:\n\n      type: integer\n\n      description: Number of CPUs for the server.\n\n      constraints:\n\n        - valid_values: [ 1, 2, 4, 8 ]\n\n \n\n  node_templates:\n\n    my_server:\n\n      type: tosca.nodes.Compute\n\n      capabilities:\n\n        # Host container properties\n\n        host:\n\n          properties:\n\n            # Compute properties\n\n            num_cpus: { get_input: cpus }\n\n            mem_size: 2048  MB\n\n            disk_size: 10 GB'
yaml_2_1 = 'topology_template:\n\n  inputs:\n\n    mysql_rootpw:\n\n      type: string\n\n    mysql_port:\n\n      type: integer\n\n    # rest omitted here for brevity\n\n \n\n  node_templates:\n\n    db_server:\n\n      type: tosca.nodes.Compute\n\n      # rest omitted here for brevity\n\n \n\n    mysql:\n\n      type: tosca.nodes.DBMS.MySQL'

@parameterized_class([
   { 'yaml': yaml_0_1, 'expected': 0},
   { 'yaml': yaml_1_1, 'expected': 1},
   { 'yaml': yaml_2_1, 'expected': 2}
])

class TestNNTCount(unittest.TestCase):
    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()
    
    def test(self):
        metric = NNT(self.yaml)
        count = metric.count()
        self.assertEqual(count, self.expected, 'Test failed because expected ' + str(self.expected) + ' and got ' + str(count) +'!') 
    
if __name__ == "__main__":
    unittest.main()

