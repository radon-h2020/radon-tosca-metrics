import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.metrics.ttb import TTB


#yaml_ttb_id
yaml_true_1 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ntopology_template:\n  relationship_templates:\n    storage_attachesto_1:\n      type: MyAttachesTo\n      properties:\n        location: /my_data_location\n\n    storage_attachesto_2:\n      type: MyAttachesTo\n      properties:\n        location: /some_other_data_location\n    \n    my_connectsto_relationship:\n      type: tosca.relationships.ConnectsTo\n      interfaces:\n        Configure:\n          inputs:\n            speed: { get_attribute: [ SOURCE, connect_speed ] }  \n\n  relationship_types:\n    MyAttachesTo:\n      derived_from: AttachesTo\n      interfaces:\n        some_interface_name:\n          some_operation:\n            implementation: default_script.sh\n'
yaml_false_1 = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\nartifact_types:\n\n  kubernetes.Spec:\n    description: >-\n      Object specification\n    derived_from: tosca.artifacts.Root\n    file_ext: [ yaml, yml, json ]'
yaml_false_2 = 'tosca_definitions_version: alien_dsl_2_0_0\n\n#\n# Ystia Forge\n# Copyright (C) 2018 Bull S. A. S. - Bull, Rue Jean Jaures, B.P.68, 78340, Les Clayes-sous-Bois, France.\n# Use of this source code is governed by Apache 2 LICENSE that can be found in the LICENSE file.\n#\n\nmetadata:\n  template_name: org.ystia.logstash.pub\n  template_version: 2.2.0-SNAPSHOT\n  template_author: Ystia\n\ndescription: Public interface types for Logstash support.\n\nimports:\n  - tosca-normative-types:1.0.0-ALIEN20\n  - org.ystia.common:2.2.0-SNAPSHOT\n\ncapability_types:\n  org.ystia.logstash.pub.capabilities.LogstashEndpoint:\n    derived_from: tosca.capabilities.Endpoint\n\n  org.ystia.logstash.pub.capabilities.LogstashConnectorHosting:\n    derived_from: tosca.capabilities.Container\n\n  org.ystia.logstash.pub.capabilities.GeonamesEndpoint:\n    derived_from: tosca.capabilities.Endpoint\n'

@parameterized_class([
   { 'yaml': yaml_true_1, 'expected': True},
   { 'yaml': yaml_false_1, 'expected': False},
   { 'yaml': yaml_false_2, 'expected': False}
])

class TestTTBCheck(unittest.TestCase):
    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()
    
    def test(self):
        metric = TTB(self.yaml)
        check = metric.check()
        self.assertEqual(check, self.expected, 'Test failed because expected ' + str(self.expected) + ' and got ' + str(check) +'!') 
    
if __name__ == "__main__":
    unittest.main()

