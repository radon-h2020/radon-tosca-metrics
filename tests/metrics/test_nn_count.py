import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.metrics.nn import NN


#yaml_nn_id
yaml_0_1 = 'tosca_definitions_version: tosca_simple_yaml_1_0'
yaml_1_1 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template for deploying a single server with predefined properties.\n\ntopology_template:\n  inputs:\n    cpus:\n      type: integer\n      description: Number of CPUs for the server.\n      constraints:\n        - valid_values: [ 1, 2, 4, 8 ]\n\n  node_templates:\n    my_server:\n      type: tosca.nodes.Compute\n      capabilities:\n        # Host container properties\n        host:\n          properties:\n            # Compute properties\n            num_cpus: { get_input: cpus }\n            mem_size: 2048  MB\n            disk_size: 10 GB'
yaml_2_1 = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\ndescription: Template for deploying a single server with MySQL software on top.\n\ntopology_template:\n  inputs:\n    mysql_rootpw:\n      type: string\n      \n    mysql_port:\n      type: integer\n    \n  node_templates:\n    db_server:\n      type: tosca.nodes.Compute\n      \n    mysql:\n      type: tosca.nodes.DBMS.MySQL'

@parameterized_class([
   { 'yaml': yaml_0_1, 'expected': 0},
   { 'yaml': yaml_1_1, 'expected': 1},
   { 'yaml': yaml_2_1, 'expected': 2}
])

class TestNNCount(unittest.TestCase):
    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()

    """
    def test(self):
        metric = NN(self.yaml)
        count = metric.count()
        self.assertEqual(count, self.expected, 'Test failed because expected ' + str(self.expected) + ' and got ' + str(count) +'!') 
    """
if __name__ == "__main__":
    unittest.main()

