import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.metrics.ninpc import NINPC


#yaml_ninpc_id
yaml_0_1 = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ndescription: Template for deploying SD-WAN with a variable number of sites.\n\ntopology_template:\n  inputs:\n    numberOfSites:\n      type: integer\n    locations:\n      type: list\n      entry_schema: Location'
yaml_1_1 = 'tosca_definitions_version: alien_dsl_2_0_0\n\n#\n# Ystia Forge\n# Copyright (C) 2018 Bull S. A. S. - Bull, Rue Jean Jaures, B.P.68, 78340, Les Clayes-sous-Bois, France.\n# Use of this source code is governed by Apache 2 LICENSE that can be found in the LICENSE file.\n#\n\nmetadata:\n  template_name: org.ystia.topologies.flink\n  template_version: 2.2.0-SNAPSHOT\n  template_author: Ystia\n\n\nimports:\n  - tosca-normative-types:1.0.0-ALIEN20\n  - org.ystia.common:2.2.0-SNAPSHOT\n  - org.ystia.consul.pub:2.2.0-SNAPSHOT\n  - org.ystia.flink.pub:2.2.0-SNAPSHOT\n  - org.ystia.java.linux.bash:2.2.0-SNAPSHOT\n  - org.ystia.consul.linux.bash:2.2.0-SNAPSHOT\n  - org.ystia.java.pub:2.2.0-SNAPSHOT\n  - org.ystia.flink.linux.bash:2.2.0-SNAPSHOT\n\ntopology_template:\n  description: A basic topology template with Flink\n\n  inputs:\n    repository:\n      type: string\n      required: false\n      default: "http://archive.apache.org/dist/flink"\n      constraints:\n        - pattern: ^(http|https|ftp)://.+/.*$\n'
yaml_2_1 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template for deploying a single server with predefined properties.\n\ntopology_template:\n  inputs:\n    cpus:\n      type: integer\n      description: Number of CPUs for the server.\n      constraints:\n        - valid_values: [ 1, 2, 4, 8 ]\n        - less_than: 10'

@parameterized_class([
   { 'yaml': yaml_0_1, 'expected': 0.0},
   { 'yaml': yaml_1_1, 'expected': 1.0},
   { 'yaml': yaml_2_1, 'expected': 2.0}
])

class TestNINPCCount(unittest.TestCase):
    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()
    
    def test(self):
        metric = NINPC(self.yaml)
        count = metric.count()
        self.assertEqual(count, self.expected, 'Test failed because expected ' + str(self.expected) + ' and got ' + str(count) +'!') 
    
if __name__ == "__main__":
    unittest.main()

