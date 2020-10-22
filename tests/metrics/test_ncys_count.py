import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.metrics.ncys import NCYS


#yaml_ncys_id
yaml_1_1 = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ntopology_template:\n  node_templates:\n    my_virtual_machine:\n      type: SoftwareComponent\n      artifacts:\n        my_vm_image:\n          file: images/fedora-18-x86_64.qcow2\n          type: tosca.artifacts.Deployment.Image.VM.QCOW2\n          topology: my_VMs_topology.yaml\n      requirements:\n        - host: my_server\n      interfaces:\n        Standard:\n          create: my_vm_image'
yaml_4_1 = 'tosca_definitions_version: alien_dsl_2_0_0\n\nnode_types:\n  org.ystia.ntp.ansible.nodes.NtpServer:\n    derived_from: org.ystia.ntp.pub.nodes.NtpServer\n    interfaces:\n      Standard:\n        create: playbooks/create.yaml\n        configure:\n          inputs:\n            TYPE: "server"\n          implementation: playbooks/configure.yaml\n        start: playbooks/start.yaml\n        stop: playbooks/stop.yaml'

@parameterized_class([
   { 'yaml': yaml_1_1, 'expected': 1},
   { 'yaml': yaml_4_1, 'expected': 4}
])

class TestNCYSCount(unittest.TestCase):
    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()

    """
    def test(self):
        metric = NCYS(self.yaml)
        count = metric.count()
        self.assertEqual(count, self.expected, 'Test failed because expected ' + str(self.expected) + ' and got ' + str(count) +'!') 
    """
if __name__ == "__main__":
    unittest.main()

