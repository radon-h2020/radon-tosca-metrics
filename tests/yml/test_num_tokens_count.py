import unittest
from parameterized import parameterized_class
from toscametrics.general.num_tokens import NumTokens

yaml_12_1 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template for deploying a single server ' \
            'with predefined properties. '
yaml_30_1 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template for deploying a single server ' \
            'with predefined properties.\n\ntopology_template:\n  inputs:\n    cpus:\n      type: integer\n      ' \
            'description: Number of CPUs for the server.\n      constraints:\n        - valid_values: [ 1, 2, 4, 8 ] '


@parameterized_class([
   {'yaml': yaml_12_1, 'expected': 12},
   {'yaml': yaml_30_1, 'expected': 30}
])
class TestNumTokensCount(unittest.TestCase):

    def setUp(self):
        self.yaml = self.yaml.expandtabs(2)

    def test(self):
        self.assertEqual(NumTokens(self.yaml).count(), self.expected)
