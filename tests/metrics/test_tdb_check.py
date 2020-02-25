import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.metrics.tdb import TDB


#yaml_tdb_id
yaml_true_1 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ntopology_template:\n  relationship_templates:\n    storage_attachesto_1:\n      type: MyAttachesTo\n      properties:\n        location: /my_data_location\n\n    storage_attachesto_2:\n      type: MyAttachesTo\n      properties:\n        location: /some_other_data_location\n    \n    my_connectsto_relationship:\n      type: tosca.relationships.ConnectsTo\n      interfaces:\n        Configure:\n          inputs:\n            speed: { get_attribute: [ SOURCE, connect_speed ] }  \n\n  relationship_types:\n    MyAttachesTo:\n      derived_from: AttachesTo\n      interfaces:\n        some_interface_name:\n          some_operation:\n            implementation: default_script.sh\n'
yaml_false_1 = 'description:\nname: install\ninitial:\n  steps:\n    node1_initial:\n      node: node1\n      state: initial\n      to:\n        - node1_creating\nexpected:\n  steps:\n    node1_initial:\n      node: node1\n      state: initial'

@parameterized_class([
   { 'yaml': yaml_true_1, 'expected': True},
   { 'yaml': yaml_false_1, 'expected': False}
])

class TestTDBCheck(unittest.TestCase):
    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()
    
    def test(self):
        metric = TDB(self.yaml)
        check = metric.check()
        self.assertEqual(check, self.expected, 'Test failed because expected ' + str(self.expected) + ' and got ' + str(check) +'!') 
    
if __name__ == "__main__":
    unittest.main()

