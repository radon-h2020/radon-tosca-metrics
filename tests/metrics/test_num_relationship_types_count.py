import unittest
from parameterized import parameterized_class
from toscametrics.blueprint.num_relationship_types import NumRelationshipTypes


yaml_0 = 'tosca_definitions_version: tosca_simple_yaml_1_0'
yaml_2 = 'tosca_definitions_version: tosca_simple_yaml_1_0\ntopology_template:\n\trelationship_types:\n\t' \
         '\tMyAttachesTo:\n\t\t\tderived_from: AttachesTo\n\t\tCustomHostedOn:\n\t\t\tderived_from: ' \
         'tosca.relationships.DependsOn\n\t\t\tvalid_target_types: [tosca.capabilities.Container] '


@parameterized_class([
   {'yaml': yaml_0, 'expected': 0},
   {'yaml': yaml_2, 'expected': 2}
])
class TestNumRelationshipTypesCount(unittest.TestCase):
    def setUp(self):
        self.blueprint = self.yaml.expandtabs(2)

    def test(self):
        self.assertEqual(NumRelationshipTypes(self.blueprint).count(), self.expected)


