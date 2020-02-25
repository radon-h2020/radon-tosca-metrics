import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.metrics.tob import TOB


#yaml_tob_id
yaml_true_1 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ntopology_template:\n  relationship_templates:\n    storage_attachesto_1:\n      type: MyAttachesTo\n      properties:\n        location: /my_data_location\n\n    storage_attachesto_2:\n      type: MyAttachesTo\n      properties:\n        location: /some_other_data_location\n    \n    my_connectsto_relationship:\n      type: tosca.relationships.ConnectsTo\n      interfaces:\n        Configure:\n          inputs:\n            speed: { get_attribute: [ SOURCE, connect_speed ] }  \n\n  relationship_types:\n    MyAttachesTo:\n      derived_from: AttachesTo\n      interfaces:\n        some_interface_name:\n          some_operation:\n            implementation: default_script.sh\n'
yaml_false_1 = 'description:\nname: install\ninitial:\n  steps:\n    node1_initial:\n      node: node1\n      state: initial\n      to:\n        - node1_creating\nexpected:\n  steps:\n    node1_initial:\n      node: node1\n      state: initial'
yaml_false_2 = 'tosca_definitions_version: alien_dsl_2_0_0\n\nnode_types:\n  org.ystia.ntp.ansible.nodes.NtpServer:\n    derived_from: org.ystia.ntp.pub.nodes.NtpServer\n    interfaces:\n      Standard:\n        create: playbooks/create.yaml\n        configure:\n          inputs:\n            TYPE: "server"\n          implementation: playbooks/configure.yaml\n        start: playbooks/start.yaml\n        stop: playbooks/stop.yaml'

@parameterized_class([
   { 'yaml': yaml_true_1, 'expected': True},
   { 'yaml': yaml_false_1, 'expected': False},
   { 'yaml': yaml_false_2, 'expected': False}
])

class TestTOBCheck(unittest.TestCase):
    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()
    
    def test(self):
        metric = TOB(self.yaml)
        check = metric.check()
        self.assertEqual(check, self.expected, 'Test failed because expected ' + str(self.expected) + ' and got ' + str(check) +'!') 
    
if __name__ == "__main__":
    unittest.main()

