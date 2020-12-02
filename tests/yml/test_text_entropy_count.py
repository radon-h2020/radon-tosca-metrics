import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.yml.text_entropy import TextEntropy

blueprint = 'tosca_definitions_version: tosca_simple_yaml_1_0\ndescription: Template for deploying server\n' \
             'topology_template:\n\tinputs:\n\t\tcpus:\n\t\t\ttype: integer'


@parameterized_class([
   {'yaml': blueprint, 'expected': 3.58},
])
class TestTextEntropyCount(unittest.TestCase):

    def setUp(self):
        self.blueprint = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.blueprint.close()

    def test(self):
        self.assertEqual(TextEntropy(self.blueprint).count(), self.expected)
