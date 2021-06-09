import unittest
from parameterized import parameterized_class
from toscametrics.blueprint.num_capability_types import NumCapabilityTypes


yaml_0 = 'tosca_definitions_version: tosca_simple_yaml_1_0'
yaml_2 = '''
tosca_definitions_version: yorc_tosca_simple_yaml_1_0

capability_types:
  tosca.capabilities.Root:
    description: The TOSCA root Capability Type all other TOSCA base Capability Types derive from

  tosca.capabilities.Node:
    derived_from: tosca.capabilities.Root
    description: The Node capability indicates the base capabilities of a TOSCA Node Type.
'''


@parameterized_class([
    {'yaml': yaml_0, 'expected': 0},
    {'yaml': yaml_2, 'expected': 2}
])
class TestNumCapabilityTypesCount(unittest.TestCase):
    def setUp(self):
        self.blueprint = self.yaml.expandtabs(2)

    def test(self):
        self.assertEqual(NumCapabilityTypes(self.blueprint).count(), self.expected)
