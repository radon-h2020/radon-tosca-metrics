import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.metrics.num_operation_inputs import NumOperationInputs


yaml_0 = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\ndescription: Template for deploying a single server ' \
         'with MySQL software on top.\n\ntopology_template:\n  node_templates:\n    db_server:\n      type: ' \
         'tosca.nodes.Compute\n\n    mysql:\n      type: tosca.nodes.DBMS.MySQL '
yaml_1 = 'topology_template:\n\tnode_templates:\n\t\tmy_server:\n\t\t\ttype: ' \
         'tosca.nodes.Compute\n\t\tmysql:\n\t\t\ttype: tosca.nodes.DBMS.MySQL\n\t\t\trequirements:\n\t\t\t\t- host: ' \
         'my_server\n\t\t\tinterfaces:\n\t\t\t\ttosca.interfaces.nodes.custom.Backup:\n\t\t\t\t\toperations:\n\t\t\t' \
         '\t\t\tbackup:\n\t\t\t\t\t\t\timplementation: backup.sh\n\t\t\t\t\t\t\tinputs:\n\t\t\t\t\t\t\t\tstorage_url: ' \
         '{ get_input: storage_url } '


@parameterized_class([
   {'yaml': yaml_0, 'expected': 0},
   {'yaml': yaml_1, 'expected': 1},
])
class TestNumOperationInputsCount(unittest.TestCase):
    def setUp(self):
        self.blueprint = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.blueprint.close()
    
    def test(self):
        self.assertEqual(NumOperationInputs(self.blueprint).count(), self.expected)
