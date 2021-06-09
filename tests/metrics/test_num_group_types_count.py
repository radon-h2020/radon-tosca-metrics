import unittest
from parameterized import parameterized_class
from toscametrics.blueprint.num_group_types import NumGroupTypes


yaml_0 = 'tosca_definitions_version: tosca_simple_yaml_1_0'
yaml_1 = '''tosca_definitions_version: tosca_simple_yaml_1_0
group_types:
  tosca.groups.Root:
    description: The TOSCA Group Type all other TOSCA Group Types derive from
    interfaces:
      tosca.interfaces.node.lifecycle.Standard:
        create:
          description: Standard lifecycle create operation.
        configure:
          description: Standard lifecycle configure operation.
        start:
          description: Standard lifecycle start operation.
        stop:
          description: Standard lifecycle stop operation.
        delete:
          description: Standard lifecycle delete operation.
'''


@parameterized_class([
    {'yaml': yaml_0, 'expected': 0},
    {'yaml': yaml_1, 'expected': 1}
])
class TestNumGroupTypesCount(unittest.TestCase):
    def setUp(self):
        self.blueprint = self.yaml.expandtabs(2)

    def test(self):
        self.assertEqual(NumGroupTypes(self.blueprint).count(), self.expected)
