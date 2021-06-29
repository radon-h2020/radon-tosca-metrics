import unittest
from parameterized import parameterized_class
from toscametrics.blueprint.lcot import LCOT


yaml_0 = 'tosca_definitions_version: tosca_simple_yaml_1_0'
yaml_1 = '\tnode_templates:\n\t\tDocker:\n\t\t\ttype: ' \
         '"tosca.nodes.indigo.Container.Runtime.Docker"\n\t\t\tcapabilities:\n\t\t\t\thost:\n\t\t\t\t\tproperties:\n' \
         '\t\t\t\t\t\tpublish_all: false\n\t\t\t\t\t\tpublish_ports:\n\t\t\t\t\t\t- protocol: ' \
         '"tcp"\n\t\t\t\t\t\t\tsource: 5000 \n\t\t\t\t\t\t- protocol: "tcp"\n\t\t\t\t\t\t\tsource: ' \
         '6006\n\t\t\t\t\t\t- protocol: "tcp"\n\t\t\t\t\t\t\tsource: 8888\n\t\t\t\t\t\tmem_size: { get_input: ' \
         'mem_size }\n\t\t\t\t\t\tnum_cpus: { get_input: num_cpus }\n\t\t\t\t\t\tnum_gpus: { get_input: num_gpus ' \
         '}\n\n\t\tDocker2:\n\t\t\ttype: "tosca.nodes.indigo.Container.Runtime.Docker"\n\t\t\tcapabilities:\n\t\t\t' \
         '\thost:\n\t\t\t\t\tproperties:\n\t\t\t\t\t\tmem_size: { get_input: mem_size } '
yaml_2 = 'topology_template:\n\tinputs:\n\n\t\tmem_size:\n\t\t\ttype: string\n\t\t\tdescription: Amount of ' \
         'memory\n\t\t\trequired: no\n\t\t\tdefault: "4096 MB"\n\n\t\tnum_cpus:\n\t\t\ttype: ' \
         'integer\n\t\t\tdescription: Number of required CPUs\n\t\t\trequired: no\n\t\t\tdefault: ' \
         '1\n\n\t\tnum_gpus:\n\t\t\ttype: integer\n\t\t\tdescription: Number of required GPUs\n\t\t\trequired: ' \
         'no\n\t\t\tdefault: 1\n\n\t\tflaat_disable:\n\t\t\ttype: string\n\t\t\tdescription: disable flaat ' \
         'authentication\n\t\t\trequired: no\n\t\t\tdefault: "yes"\n\n\t\trclone_conf:\n\t\t\ttype: ' \
         'string\n\t\t\tdescription: rclone.conf location\n\t\t\trequired: no\n\t\t\tdefault: ' \
         '"/srv/mods/.rclone.conf"\n\n\t\trclone_url:\n\t\t\ttype: string\n\t\t\tdescription: remote storage link to ' \
         'access via webdav\n\t\t\trequired: no\n\t\t\tdefault: ' \
         '"https://nc.deep-hybrid-datacloud.eu/remote.php/webdav/"\n\n\t\trclone_vendor:\n\t\t\ttype: ' \
         'string\n\t\t\tdescription: rclone vendor\n\t\t\trequired: no\n\t\t\tdefault: ' \
         '"nextcloud"\n\t\n\t\trclone_user:\n\t\t\ttype: string\n\t\t\tdescription: rclone user to access remote ' \
         'storage\n\t\t\trequired: no\n\t\t\tdefault: ""\n\n\t\trclone_password:\n\t\t\ttype: ' \
         'string\n\t\t\tdescription: rclone user password\n\t\t\trequired: no\n\t\t\tdefault: ' \
         '""\n\n\t\tjupyter_password:\n\t\t\ttype: string\n\t\t\tdescription: jupyter password\n\t\t\trequired: ' \
         'no\n\t\t\tdefault: ""\n\n\t\tjupyter_config_url:\n\t\t\ttype: string\n\t\t\tdescription: url to download ' \
         'some jupyter config\n\t\t\trequired: no\n\t\t\tdefault: ""\n\n\t\trun_command:\n\t\t\ttype: ' \
         'string\n\t\t\tdescription: default command to run\n\t\t\trequired: yes\n\t\t\tdefault: "deepaas-run ' \
         '--listen-ip=0.0.0.0 --listen-port=$PORT0"\n\n\tnode_templates:\n\t\tDocker:\n\t\t\ttype: ' \
         '"tosca.nodes.indigo.Container.Runtime.Docker"\n\t\t\tcapabilities:\n\t\t\t\thost:\n\t\t\t\t\tproperties:\n' \
         '\t\t\t\t\t\tpublish_all: false\n\t\t\t\t\t\tpublish_ports:\n\t\t\t\t\t\t- protocol: ' \
         '"tcp"\n\t\t\t\t\t\t\tsource: 5000 \n\t\t\t\t\t\t- protocol: "tcp"\n\t\t\t\t\t\t\tsource: ' \
         '6006\n\t\t\t\t\t\t- protocol: "tcp"\n\t\t\t\t\t\t\tsource: 8888\n\t\t\t\t\t\tmem_size: { get_input: ' \
         'mem_size }\n\t\t\t\t\t\tnum_cpus: { get_input: num_cpus }\n\t\t\t\t\t\tnum_gpus: { get_input: num_gpus ' \
         '}\n\t\tmarathon:\n\t\t\ttype: "tosca.nodes.indigo.Container.Application.Docker.Marathon"\n\t\t\tproperties' \
         ':\n\t\t\t\tforce_pull_image: true\n\t\t\t\tcommand: { get_input: run_command ' \
         '}\n\t\t\t\tenvironment_variables:\n\t\t\t\t\tRCLONE_CONFIG: { get_input: rclone_conf ' \
         '}\n\t\t\t\t\tRCLONE_CONFIG_DEEPNC_TYPE: webdav\n\t\t\t\t\tRCLONE_CONFIG_DEEPNC_URL: { get_input: rclone_url ' \
         '}\n\t\t\t\t\tRCLONE_CONFIG_DEEPNC_VENDOR: { get_input: rclone_vendor ' \
         '}\n\t\t\t\t\tRCLONE_CONFIG_DEEPNC_USER: { get_input: rclone_user }\n\t\t\t\t\tRCLONE_CONFIG_DEEPNC_PASS: { ' \
         'get_input: rclone_password }\n\t\t\t\t\tDISABLE_AUTHENTICATION_AND_ASSUME_AUTHENTICATED_USER: {get_input: ' \
         'flaat_disable}\n\t\t\t\t\tjupyterPASSWORD: {get_input: jupyter_password}\n\t\t\t\t\tjupyterCONFIG_URL: {' \
         'get_input: jupyter_config_url}\n '


@parameterized_class([
    {'yaml': yaml_0, 'expected': 0},
    {'yaml': yaml_1, 'expected': 1},
    {'yaml': yaml_2, 'expected': 2}
])
class TestLCOTCount(unittest.TestCase):
    def setUp(self):
        self.blueprint = self.yaml.expandtabs(2)

    def test(self):
        self.assertEqual(LCOT(self.blueprint).count(), self.expected)
