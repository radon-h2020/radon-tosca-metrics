import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.metrics.nac import NAC


#yaml_nac_id
yaml_1_0 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\nimports:\n  - paypalpizzastore_nodejs_app.yaml' 
yaml_1_2 = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ntopology_template:\n  node_templates:\n    my_server:\n      type: tosca.nodes.Compute\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      requirements:\n        - host: my_server\n      interfaces:\n        tosca.interfaces.nodes.custom.Backup:\n          operations:\n            backup: backup.sh\n\n  workflows:\n    backup:\n      description: Performs a snapshot of the MySQL data.\n      preconditions:\n        - target: my_server\n          condition:\n            - assert:\n              - state: [{equal: available}]\n        - target: mysql\n          condition:\n            - assert:\n              - state: [{valid_values: [started, available]}]\n              - my_attribute: [{equal: ready }]\n\n      steps:\n        my_step:\n          target: mysql\n          activities:\n            - call_operation: tosca.interfaces.nodes.custom.Backup.backup\n            - do_something_else: tosca.interfaces.nodes.custom.Backup.else'

@parameterized_class([
   { 'yaml': yaml_1_0, 'expected': 0},
   { 'yaml': yaml_1_2, 'expected': 2}
])

class TestNACCount(unittest.TestCase):
    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()
    
    def test(self):
        metric = NAC(self.yaml)
        count = metric.count()
        self.assertEqual(count, self.expected, 'Test failed because expected ' + str(self.expected) + ' and got ' + str(count) +'!') 
    
if __name__ == "__main__":
    unittest.main()

