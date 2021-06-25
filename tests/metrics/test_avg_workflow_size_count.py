import unittest
from parameterized import parameterized_class
from toscametrics.blueprint.avg_workflow_size import AvgWorkflowSize


yaml_0 = 'tosca_definitions_version: tosca_simple_yaml_1_0\ntopology_template:\n\trelationship_types:\n\t' \
         '\tMyAttachesTo:\n\t\t\tderived_from: AttachesTo\n\t\tCustomHostedOn:\n\t\t\tderived_from: ' \
         'tosca.relationships.DependsOn\n\t\t\tvalid_target_types: [tosca.capabilities.Container] '

yaml_1_5 = 'tosca_definitions_version: alien_dsl_1_4_0\n\ntopology_template:\n\n\tworkflows:\n\t\tinstall:\n\t\t\tsteps' \
         ':\n\t\t\t\tCentosMedium_install:\n\t\t\t\t\tnode: ' \
         'MonitoredCentosMedium\n\t\t\t\t\tactivity:\n\t\t\t\t\t\tdelegate: ' \
         'install\n\t\t\t\t\ton-success:\n\t\t\t\t\t\t- ' \
         'DiamondLinuxAgent_initial\n\t\t\t\tDiamondLinuxAgent_initial:\n\t\t\t\t\tnode: ' \
         'DiamondLinuxAgent\n\t\t\t\t\tactivity:\n\t\t\t\t\t\tset_state: ' \
         'initial\n\t\t\t\t\ton-success:\n\t\t\t\t\t\t- ' \
         'DiamondLinuxAgent_creating\n\t\tuninstall:\n\t\t\tsteps:\n\t\t\t\tCentosMedium_uninstall:\n\t\t\t\t\tnode: ' \
         'MonitoredCentosMedium\n\t\t\t\t\tactivity:\n\t\t\t\t\t\tdelegate: CentosMedium_uninstall\n '


@parameterized_class([
    {'yaml': yaml_0, 'expected': 0},
    {'yaml': yaml_1_5, 'expected': 1.5}
])
class TestAvgWorkflowSizeCount(unittest.TestCase):

    def test(self):
        self.assertEqual(AvgWorkflowSize(self.yaml.expandtabs(2)).count(), self.expected)
