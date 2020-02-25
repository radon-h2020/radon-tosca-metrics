import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.metrics.ngp import NGP


#yaml_ngp_id
yaml_0_1 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\nimports:\n  - paypalpizzastore_nodejs_app.yaml'
yaml_3_1 = 'tosca_definitions_version: tosca_simple_yaml_1_1\n\nrelationship_types:\n\n  tosca.relationships.Root:\n    interfaces:\n      Configure:\n        type: tosca.interfaces.relationship.Configure\n\n  tosca.relationships.HostedOn:\n    derived_from: tosca.relationships.Root\n    valid_target_types: [ tosca.capabilities.Container ]\n\n  tosca.relationships.ConnectsTo:\n    properties:\n      credential:\n        type: tosca.datatypes.Credential\n        required: false\n\t\t\n  tosca.relationships.AttachesTo:\n    properties:\n      location:\n        type: string\n        constraints:\n          - min_length: 1\n      device:\n        type: string\n        required: false\n    attributes:\n      device:\n        type: string'
yaml_4_1 = 'tosca_definitions_version: alien_dsl_2_0_0\n\nnode_types:\n  org.ystia.ssl.ansible.certificates.nodes.SSLCertificateGenerator:\n    derived_from: tosca.nodes.SoftwareComponent\n    properties:\n      common_name:\n        type: string\n        description: Certificate common name\n      key_path:\n        type: string\n        description: Path of a directory where private keys should be stored.\n      certificate_path:\n        type: string\n        description: Path of a directory where certificates should be stored.\n      linux_owner:\n        type: string'

@parameterized_class([
   { 'yaml': yaml_0_1, 'expected': 0},
   { 'yaml': yaml_3_1, 'expected': 3},
   { 'yaml': yaml_4_1, 'expected': 4}
])

class TestNGPCount(unittest.TestCase):
    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()
    
    def test(self):
        metric = NGP(self.yaml)
        count = metric.count()
        self.assertEqual(count, self.expected, 'Test failed because expected ' + str(self.expected) + ' and got ' + str(count) +'!') 
    
if __name__ == "__main__":
    unittest.main()

