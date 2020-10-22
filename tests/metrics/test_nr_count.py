import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.metrics.nr import NR


#yaml_nr_id
yaml_0_1 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ntopology_template:\n  relationship_types:\n    MyAttachesTo:\n      derived_from: AttachesTo\n      interfaces:\n        some_interface_name:\n          some_operation:\n            implementation: default_script.sh'
yaml_1_1 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ntopology_template:\n  relationship_templates:\n    storage_attachesto_1:\n      type: MyAttachesTo\n      properties:\n        location: /my_data_location\n\n  relationship_types:\n    MyAttachesTo:\n      derived_from: AttachesTo\n      interfaces:\n        some_interface_name:\n          some_operation:\n            implementation: default_script.sh'
yaml_3_1 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ntopology_template:\n  relationship_templates:\n    storage_attachesto_1:\n      type: MyAttachesTo\n      properties:\n        location: /my_data_location\n\n    storage_attachesto_2:\n      type: MyAttachesTo\n      properties:\n        location: /some_other_data_location\n    \n    my_connectsto_relationship:\n      type: tosca.relationships.ConnectsTo\n      interfaces:\n        Configure:\n          inputs:\n            speed: { get_attribute: [ SOURCE, connect_speed ] }  \n\n  relationship_types:\n    MyAttachesTo:\n      derived_from: AttachesTo\n      interfaces:\n        some_interface_name:\n          some_operation:\n            implementation: default_script.sh\n'

@parameterized_class([
   { 'yaml': yaml_0_1, 'expected': 0},
   { 'yaml': yaml_1_1, 'expected': 1},
   { 'yaml': yaml_3_1, 'expected': 3}
])

class TestNRCount(unittest.TestCase):
    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()
    
    def test(self):
        metric = NR(self.yaml)
        count = metric.count()
        self.assertEqual(count, self.expected, 'Test failed because expected ' + str(self.expected) + ' and got ' + str(count) +'!') 
    
if __name__ == "__main__":
    unittest.main()

