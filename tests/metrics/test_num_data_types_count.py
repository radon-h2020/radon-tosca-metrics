import unittest
from parameterized import parameterized_class
from toscametrics.blueprint.num_data_types import NumDataTypes


yaml_0 = 'tosca_definitions_version: tosca_simple_yaml_1_0'
yaml_2 = '''
tosca_definitions_version: yorc_tosca_simple_yaml_1_0

metadata:
  template_name: tosca-normative-types
  template_author: TOSCA TC
  template_version: 1.2.0

description: >
  Contains the normative types definition as currently supported in yorc.

data_types:
  tosca.datatypes.Credential:
    derived_from: tosca.datatypes.Root
    description: >
      The Credential type is a complex TOSCA data Type used when describing authorization credentials used to access network accessible resources.
    properties:
      protocol:
        type: string
        description: The optional protocol name.
        required: false
      token_type:
        type: string
        description: The required token type.
        default: password
      token:
        type: string
        description: The required token used as a credential for authorization or access to a networked resource.
      keys:
        type: map
        description: The optional list of protocol-specific keys or assertions.
        required: false
        entry_schema:
          type: string
      user:
        type: string
        description: The optional user (name or ID) used for non-token based credentials.
        required: false

  tosca.datatypes.TimeInterval:
    derived_from: tosca.datatypes.Root
    properties:
      start_time:
        type: timestamp
        required: true
      end_time:
        type: timestamp
        required: true
'''


@parameterized_class([
    {'yaml': yaml_0, 'expected': 0},
    {'yaml': yaml_2, 'expected': 2}
])
class TestNumDataTypesCount(unittest.TestCase):
    def setUp(self):
        self.blueprint = self.yaml.expandtabs(2)

    def test(self):
        self.assertEqual(NumDataTypes(self.blueprint).count(), self.expected)
