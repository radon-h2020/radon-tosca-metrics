import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.yml.num_tokens import NumTokens

yaml_12_1 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template for deploying a single server ' \
            'with predefined properties. '
yaml_30_1 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template for deploying a single server ' \
            'with predefined properties.\n\ntopology_template:\n  inputs:\n    cpus:\n      type: integer\n      ' \
            'description: Number of CPUs for the server.\n      constraints:\n        - valid_values: [ 1, 2, 4, 8 ] '


@parameterized_class([
   { 'yaml': yaml_12_1, 'expected': 12},
   { 'yaml': yaml_30_1, 'expected': 30}
])
class TestNumTokensCount(unittest.TestCase):

    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()

    def test(self):
        metric = NumTokens(self.yaml)
        count = metric.count
        self.assertEqual(count, self.expected)
