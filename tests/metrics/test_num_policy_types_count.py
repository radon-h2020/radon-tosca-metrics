import unittest
from parameterized import parameterized_class
from toscametrics.blueprint.num_policy_types import NumPolicyTypes


yaml_0 = 'tosca_definitions_version: tosca_simple_yaml_1_0'
yaml_2 = '''
tosca_definitions_version: tosca_simple_yaml_1_0

policy_types:

  tosca.policies.Placement:
    derived_from: tosca.policies.Root
    description: The TOSCA Policy Type definition that is used to govern placement of TOSCA nodes or groups of nodes.

  tosca.policies.Scaling:
    derived_from: tosca.policies.Root
    description: The TOSCA Policy Type definition that is used to govern scaling of TOSCA nodes or groups of nodes.
'''


@parameterized_class([
    {'yaml': yaml_0, 'expected': 0},
    {'yaml': yaml_2, 'expected': 2}
])
class TestNumPolicyTypesCount(unittest.TestCase):
    def setUp(self):
        self.blueprint = self.yaml.expandtabs(2)

    def test(self):
        self.assertEqual(NumPolicyTypes(self.blueprint).count(), self.expected)
