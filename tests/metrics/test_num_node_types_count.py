import unittest
from parameterized import parameterized_class
from toscametrics.blueprint.num_node_types import NumNodeTypes


yaml_0 = 'tosca_definitions_version: tosca_simple_yaml_1_0'
yaml_2 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: >\n\tNode type that has a requirement of a ' \
         'capability with a defined value\n\nnode_types:\n\n\ttosca.nodes.SomeNode:\n\t\tderived_from: ' \
         'tosca.nodes.Root\n\t\tproperties:\n\t\t\tsome_prop:\n\t\t\t\ttype: string\n\t\t\t\trequired: ' \
         'false\n\t\t\t\tdefault: some\n\t\trequirements:\n\t\t\t- some_req:\n\t\t\t\t\tcapability: ' \
         'tosca.capabilities.SomeCap\n\t\t\t\t\tnode: tosca.nodes.NodeWithCap\n\t\t\t\t\trelationship: ' \
         'tosca.relationships.HostedOn\n\n\ttosca.nodes.NodeWithCap:\n\t\tderived_from: ' \
         'tosca.nodes.Root\n\t\tcapabilities:\n\t\t\t\tsome_req:\n\t\t\t\t\ttype: tosca.capabilities.SomeCap '


@parameterized_class([
   {'yaml': yaml_0, 'expected': 0},
   {'yaml': yaml_2, 'expected': 2}
])
class TestNumNodeTypesCount(unittest.TestCase):
    def setUp(self):
        self.blueprint = self.yaml.expandtabs(2)

    def test(self):
        self.assertEqual(NumNodeTypes(self.blueprint).count(), self.expected)

