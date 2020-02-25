import unittest
from io import StringIO
from toscametrics.yml.dpt import DPT

#Blueprints 
yaml_1_1 = "tosca_definitions_version: cloudify_dsl_1_0\n\nimports:\n    - http://s3.amazonaws.com/vcloud-score/types.yaml\n    - https://raw.githubusercontent.com/cloudify-cosmo/tosca-vcloud-plugin/1.2.1m3/plugin.yaml\n    - http://s3.amazonaws.com/vcloud-score/cloudify-fabric-plugin/1.2.1/plugin.yaml\n    - types/agentless.yaml\n\n\n\ninputs:\n    vcloud_url:\n        type: string\n        default: 'https://vca.vmware.com'\n        description: >\n            Vcloud url\n            en nog iets\n#Hier nog even verder groeienn"
yaml_8_1 = '---\n- hosts: localhost\n\n\ttasks:\n\t- name: task 1    # This is the first task\n\t\tinclude_vars:\n\t\t\tfile: username_info.yml\n\n# This is the second task\n\t- name: task 2\n\t\tinclude_vars:\n\t\t\tfile: username_info.yml'

class TestDPTCount(unittest.TestCase):

    def setUp(self):
        self.yaml = StringIO(yaml_8_1.expandtabs(2))

    def tearDown(self):
        self.yaml.close()

    def test(self):
        metric = DPT(self.yaml)
        count = metric.count()
        self.assertEqual(count, 3)

if __name__ == "__main__":
    unittest.main()
    

