import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.metrics.au import AU


#yaml_au_id
yaml_1_0 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\nimports:\n  - paypalpizzastore_nodejs_app.yaml' 
yaml_1_2 = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ndescription: >\n  TOSCA simple profile that just defines a YAML macro for commonly reused Compute\n  properties.\n\ndsl_definitions:\n  my_compute_node_props: &my_compute_node_props\n    disk_size: 10 GB\n    num_cpus: 1\n    mem_size: 2 GB\n\ntopology_template:\n  node_templates:\n    my_server:\n      type: Compute\n      capabilities:\n        host:\n          properties: *my_compute_node_props\n\n    my_database:\n      type: Compute\n      capabilities:\n        host:\n          properties: *my_compute_node_props'

@parameterized_class([
   { 'yaml': yaml_1_0, 'expected': 0},
   { 'yaml': yaml_1_2, 'expected': 2}
])

class TestAUCount(unittest.TestCase):
    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()
    
    def test(self):
        metric = AU(self.yaml)
        count = metric.count()
        self.assertEqual(count, self.expected, 'Test failed because expected ' + str(self.expected) + ' and got ' + str(count) +'!') 
    
if __name__ == "__main__":
    unittest.main()

