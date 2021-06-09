import unittest
from parameterized import parameterized_class
from toscametrics.blueprint.num_artifact_types import NumArtifactTypes


yaml_0 = 'tosca_definitions_version: tosca_simple_yaml_1_0'
yaml_2 = '''
tosca_definitions_version: yorc_tosca_simple_yaml_1_0

artifact_types:
  tosca.artifacts.Root:
    description: The TOSCA Artifact Type all other TOSCA Artifact Types derive from

  tosca.artifacts.File:
    derived_from: tosca.artifacts.Root
    description: >
      This artifact type is used when an artifact definition needs to have its associated file simply treated as a file and no special handling/handlers are invoked.
'''


@parameterized_class([
    {'yaml': yaml_0, 'expected': 0},
    {'yaml': yaml_2, 'expected': 2}
])
class TestNumArtifactTypesCount(unittest.TestCase):
    def setUp(self):
        self.blueprint = self.yaml.expandtabs(2)

    def test(self):
        self.assertEqual(NumArtifactTypes(self.blueprint).count(), self.expected)
