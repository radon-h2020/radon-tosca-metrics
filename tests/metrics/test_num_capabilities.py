import unittest
from parameterized import parameterized_class
from toscametrics.blueprint.num_capabilities import NumCapabilities

yaml_0 = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\ntopology_template:\n\t\n\tnode_templates:\n\t' \
         '\tmy_web_app_tier_1:\n\t\t\ttype: tosca.nodes.Compute\n\n\t\t\trequirements:\n\t\t\t\t- ' \
         'local_storage:\n\t\t\t\t\t\tnode: my_storage\n\t\t\t\t\t\trelationship: MyAttachesTo\n '

yaml_4 = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\ntopology_template:\n\t\n\tnode_templates:\n\t' \
         '\tmy_web_app_tier_1:\n\t\t\ttype: ' \
         'tosca.nodes.Compute\n\t\t\tcapabilities:\n\t\t\t\thost:\n\t\t\t\t\tproperties:\n\t\t\t\t\t\tdisk_size: 10 ' \
         'GB\n\t\t\t\t\t\tnum_cpus: { get_input: cpus }\n\t\t\t\t\t\tmem_size: 4096 ' \
         'MB\n\t\t\t\tos:\n\t\t\t\t\tproperties:\n\t\t\t\t\t\tarchitecture: x86_64\n\t\t\t\t\t\ttype: ' \
         'Linux\n\t\t\t\t\t\tdistribution: Fedora\n\t\t\t\t\t\tversion: 18.0\n\t\t\trequirements:\n\t\t\t\t- ' \
         'local_storage:\n\t\t\t\t\t\tnode: my_storage\n\t\t\t\t\t\trelationship: ' \
         'MyAttachesTo\n\n\t\tmy_web_app_tier_2:\n\t\t\ttype: ' \
         'tosca.nodes.Compute\n\t\t\tcapabilities:\n\t\t\t\thost:\n\t\t\t\t\tproperties:\n\t\t\t\t\t\tdisk_size: 10 ' \
         'GB\n\t\t\t\t\t\tnum_cpus: { get_input: cpus }\n\t\t\t\t\t\tmem_size: 4096 ' \
         'MB\n\t\t\t\tos:\n\t\t\t\t\tproperties:\n\t\t\t\t\t\tarchitecture: x86_64\n\t\t\t\t\t\ttype: ' \
         'Linux\n\t\t\t\t\t\tdistribution: Fedora\n\t\t\t\t\t\tversion: 18.0 '


@parameterized_class([
    {'yaml': yaml_0, 'expected': 0},
    {'yaml': yaml_4, 'expected': 4},
])
class TestNumCapabilitiesCount(unittest.TestCase):
    def setUp(self):
        self.blueprint = self.yaml.expandtabs(2)

    def test(self):
        self.assertEqual(NumCapabilities(self.blueprint).count(), self.expected)
