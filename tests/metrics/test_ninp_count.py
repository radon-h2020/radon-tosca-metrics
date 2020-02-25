import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.metrics.ninp import NINP


#yaml_ninp_id
yaml_0_1 = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\ndescription: Template for deploying a single server with MySQL software on top.\n\ntopology_template:\n  node_templates:\n    db_server:\n      type: tosca.nodes.Compute\n\n    mysql:\n      type: tosca.nodes.DBMS.MySQL'
yaml_1_1 = 'tosca_definitions_version: alien_dsl_2_0_0\n\n#\n# Ystia Forge\n# Copyright (C) 2018 Bull S. A. S. - Bull, Rue Jean Jaures, B.P.68, 78340, Les Clayes-sous-Bois, France.\n# Use of this source code is governed by Apache 2 LICENSE that can be found in the LICENSE file.\n#\n\nmetadata:\n  template_name: org.ystia.topologies.flink\n  template_version: 2.2.0-SNAPSHOT\n  template_author: Ystia\n\n\nimports:\n  - tosca-normative-types:1.0.0-ALIEN20\n  - org.ystia.common:2.2.0-SNAPSHOT\n  - org.ystia.consul.pub:2.2.0-SNAPSHOT\n  - org.ystia.flink.pub:2.2.0-SNAPSHOT\n  - org.ystia.java.linux.bash:2.2.0-SNAPSHOT\n  - org.ystia.consul.linux.bash:2.2.0-SNAPSHOT\n  - org.ystia.java.pub:2.2.0-SNAPSHOT\n  - org.ystia.flink.linux.bash:2.2.0-SNAPSHOT\n\ntopology_template:\n  description: A basic topology template with Flink\n\n  inputs:\n    repository:\n      type: string\n      required: false\n      default: "http://archive.apache.org/dist/flink"\n      constraints:\n        - pattern: ^(http|https|ftp)://.+/.*$\n\n  node_templates:\n\n    # Network\n\n    Network:\n      type: tosca.nodes.Network\n      properties:\n        ip_version: 4\n\n    # VM for Flink Job Manager\n\n    Compute_FJM:\n      type: tosca.nodes.Compute\n      requirements:\n        - network:\n            node: Network\n            relationship: tosca.relationships.Network\n    Consul_FJM:\n      type: org.ystia.consul.linux.bash.nodes.Consul\n      requirements:\n        - host:\n            node: Compute_FJM\n    Java_FJM:\n      type: org.ystia.java.linux.bash.nodes.Java\n      requirements:\n        - host:\n            node: Compute_FJM\n    FlinkJobManager:\n      type: org.ystia.flink.linux.bash.nodes.JobManager\n      properties:\n        repository: { get_input: repository }\n      requirements:\n        - host:\n            node: Java_FJM\n        - consul:\n            node: Consul_FJM'
yaml_2_1 = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ndescription: Template for deploying SD-WAN with a variable number of sites.\n\ntopology_template:\n  inputs:\n    numberOfSites:\n      type: integer\n    locations:\n      type: list\n      entry_schema: Location\n\n  node_templates:\n    sdwan:\n      type: VPN\n    site:\n      type: VPNSite\n      occurrences: [1, UNBOUNDED]\n      instance_count: { get_input: numberOfSites }\n      properties:\n        location: { get_input: [ locations, INDEX ] }\n      requirements:\n        - vpn: sdwan\n'
yaml_2_2 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template for deploying a single server with predefined properties.\n\ntopology_template:\n  inputs:\n    cpus:\n      type: integer\n      description: Number of CPUs for the server.\n      constraints:\n        - valid_values: [ 1, 2, 4, 8 ]\n\n  node_templates:\n    my_server:\n      type: tosca.nodes.Compute\n      capabilities:\n        # Host container properties\n        host:\n          properties:\n            # Compute properties\n            num_cpus: { get_input: cpus }\n            mem_size: 2048  MB\n            disk_size: 10 GB\n    \n    wordpress:\n      type: tosca.nodes.WebApplication.WordPress\n      interfaces:\n        Standard:\n          configure:\n            inputs:\n              wp_db_name: { get_property: [ mysql_database, name ] }\n'
yaml_2_3 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ntopology_template:\n  node_templates:\n    my_server:\n      type: tosca.nodes.Compute\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      requirements:\n        - host: my_server\n      interfaces:\n        tosca.interfaces.nodes.custom.Backup:\n          operations:\n            backup:\n              implementation: backup.sh\n              inputs:\n                storage_url: { get_input: storage_url }\n\n  workflows:\n    backup:\n      description: Performs a snapshot of the MySQL data.\n      preconditions:\n        - target: my_server\n          valid_states: [available]\n        - target: mysql\n          valid_states: [started, available]\n          attributes:\n            my_attribute: [ready]\n      inputs:\n        storage_url:\n          type: string\n      steps:\n        my_step:\n          target: mysql\n          activities:\n            - call_operation: tosca.interfaces.nodes.custom.Backup.backup'

@parameterized_class([
   { 'yaml': yaml_0_1, 'expected': 0},
   { 'yaml': yaml_1_1, 'expected': 1},
   { 'yaml': yaml_2_1, 'expected': 2},
   { 'yaml': yaml_2_2, 'expected': 2},
   { 'yaml': yaml_2_3, 'expected': 2}
])

class TestNINPCount(unittest.TestCase):
    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()
    
    def test(self):
        metric = NINP(self.yaml)
        count = metric.count()
        self.assertEqual(count, self.expected, 'Test failed because expected ' + str(self.expected) + ' and got ' + str(count) +'!') 
    
if __name__ == "__main__":
    unittest.main()

