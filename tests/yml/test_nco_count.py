import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.yml.nco import NCO

#yaml_nco_id
yaml_0_1 = 'topology_template:\n  node_templates:\n    my_server:\n      type: tosca.nodes.Compute\n\t  \n    cluster:\n      type: tosca.nodes.DBMS.Cluster\n      requirements:\n        - host: my_server\n      interfaces:\n        tosca.interfaces.nodes.custom.Backup:\n          operations:\n            backup: backup.sh'
yaml_3_1 = 'topology_template:\n  node_templates:\n    my_server:\n      type: tosca.nodes.Compute\n\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      requirements:\n        - host: my_server\n      interfaces:\n        tosca.interfaces.nodes.custom.Backup:\n          operations:\n            backup: backup.sh\n\n  workflows:\n    start_mysql:\n      steps:\n        start_mysql:\n          target: mysql\n          activities :\n            - set_state: starting\n            - call_operation: tosca.interfaces.node.lifecycle.Standard.start\n            - set_state: started\n\n    stop_mysql:\n      steps:\n        stop_mysql:\n          target: mysql\n          activities:\n            - set_state: stopping\n            - call_operation: tosca.interfaces.node.lifecycle.Standard.stop\n            - set_state: stopped\n\n    backup:\n      description: Performs a snapshot of the MySQL data.\n      preconditions:\n        - target: my_server\n          condition:\n            - assert:\n              - state: [{equal: available}]\n        - target: mysql\n          condition:\n            - assert:\n              - state: [{valid_values: [started, available]}]\n              - my_attribute: [{equal: ready }]\n      steps:\n        backup_step:\n          activities:\n            - inline: stop\n            - call_operation: tosca.interfaces.nodes.custom.Backup.backup\n            - inline: start\n\n    restart:\n      steps:\n        backup_step:\n          activities:\n            - inline: stop\n            - inline: start    '
yaml_5_1 = 'topology_template:\n  node_templates:\n    my_server:\n      type: tosca.nodes.Compute\n\t  \n    cluster:\n      type: tosca.nodes.DBMS.Cluster\n      requirements:\n        - host: my_server\n      interfaces:\n        tosca.interfaces.nodes.custom.Backup:\n          operations:\n            backup: backup.sh\n\t\t\t\n  workflows:\n    backup:\n      description: Performs a snapshot of the MySQL data.\n      preconditions:\n        - target: my_server\n          condition:\n            - assert:\n              - state: [{equal: available}]\n        - target: mysql\n          condition:\n            - assert:\n              - state: [{valid_values: [started, available]}]\n              - my_attribute: [{equal: ready }]\n      steps:\n        backup_step:\n          target: cluster\n          filter: # filter is a list of clauses. Matching between clauses is and.\n            - or: # only one of sub-clauses must be true.\n              - assert:\n                - foo: [{equals: true}]\n              - assert:\n                - bar: [{greater_than: 2}, {less_than: 20}]\n          activities:\n            - call_operation: tosca.interfaces.nodes.custom.Backup.backup'

@parameterized_class([
   { 'yaml': yaml_0_1, 'expected': 0},
   { 'yaml': yaml_3_1, 'expected': 3},
   { 'yaml': yaml_5_1, 'expected': 5}
])
class TestNCOCount(unittest.TestCase):

    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()

    def test(self):
        metric = NCO(self.yaml)
        count = metric.count()
        self.assertEqual(count, self.expected, 'Test failed because expected ' + str(self.expected) + ' and got ' + str(count) +'!') 
    
if __name__ == "__main__":
    unittest.main()