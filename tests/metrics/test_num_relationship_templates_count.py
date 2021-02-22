import unittest
from parameterized import parameterized_class
from toscametrics.blueprint.num_relationship_templates import NumRelationshipTemplates


yaml_0 = 'tosca_definitions_version: tosca_simple_yaml_1_0'
yaml_2 = 'tosca_definitions_version: tosca_simple_yaml_1_3\ntopology_template:\n\trelationship_templates:\n\t' \
         '\tstorage_attachesto_1:\n\t\t\ttype: MyAttachesTo\n\t\t\tproperties:\n\t\t\t\tlocation: ' \
         '/my_data_location\n\t\tstorage_attachesto_2:\n\t\t\ttype: ' \
         'MyAttachesTo\n\t\t\tproperties:\n\t\t\t\tlocation: ' \
         '/some_other_data_location\n\n\trelationship_types:\n\t\tMyAttachesTo:\n\t\t\tderived_from: ' \
         'AttachesTo\n\t\t\tinterfaces:\n\t\t\t\tsome_interface_name:\n\t\t\t\t\tsome_operation:\n\t\t\t\t\t' \
         '\timplementation: default_script.sh '


@parameterized_class([
   {'yaml': yaml_0, 'expected': 0},
   {'yaml': yaml_2, 'expected': 2}
])
class TestNumRelationshipTemplatesCount(unittest.TestCase):
    def setUp(self):
        self.blueprint = self.yaml.expandtabs(2)

    def test(self):
        self.assertEqual(NumRelationshipTemplates(self.blueprint).count(), self.expected)

