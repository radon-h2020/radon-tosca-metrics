import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.metrics.noam import NOAM


#yaml_noam_id
yaml_1_0 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\nimports:\n  - paypalpizzastore_nodejs_app.yaml' 
yaml_1_5 = 'node_templates:\n\n  juniper_impl:\n    type: juniper_node_config\n    properties:\n      netconf_auth:\n        user: { get_input: netconf_user }\n        password: { get_input: netconf_password }\n        ip: { get_input: netconf_ip }\n        key_content: { get_input: netconf_key_content }\n        port: { get_input: netconf_port }'
yaml_1_6 = 'tosca_definitions_version: cloudify_dsl_1_3\n\nimports:\n  - http://www.getcloudify.org/spec/cloudify/3.4/types.yaml\n  - https://raw.githubusercontent.com/cloudify-cosmo/cloudify-netconf-plugin/master/plugin.yaml\n\ninputs:\n\n  netconf_ip:\n    type: string\n    description: >\n       netconf server ip\n    default: 127.0.0.1\n\n  netconf_user:\n    type: string\n    description: >\n       netconf server user\n    default: netconf\n  netconf_password:\n    type: string\n    description: >\n       netconf server user password\n    default: netconf\n\n  netconf_key_content:\n    type: string\n    description: >\n       netconf server user rsa key content, can be used instead password\n    default: ""\n\nnode_types:\n\n  vyatta_node_config:\n    derived_from: cloudify.netconf.nodes.xml_rpc\n    properties:\n      metadata:\n        default:\n          capabilities:\n            - urn:ietf:params:netconf:base:1.0\n            - urn:ietf:params:netconf:capability:writeable-running:1.0\n            - urn:ietf:params:netconf:capability:rollback-on-error:1.0\n            - urn:ietf:params:netconf:capability:startup:1.0\n            - urn:ietf:params:netconf:capability:url:1.0\n          xmlns:\n            vyatta-if-v1: urn:vyatta.com:mgmt:vyatta-interfaces:1\n            vyatta-interfaces-dataplane-v1: urn:vyatta.com:mgmt:vyatta-interfaces-dataplane:1\n            vyatta-interfaces-loopback-v1: urn:vyatta.com:mgmt:vyatta-interfaces-loopback:1\n            vyatta-protocols-static-v1: urn:vyatta.com:mgmt:vyatta-protocols-static:1\n            vyatta-protocols-v1: urn:vyatta.com:mgmt:vyatta-protocols:1\n            vyatta-service-https-v1: urn:vyatta.com:mgmt:vyatta-service-https:1\n            vyatta-service-nat-v1: urn:vyatta.com:mgmt:vyatta-service-nat:1\n            vyatta-service-netconf-v1: urn:vyatta.com:mgmt:vyatta-service-netconf:1\n            vyatta-service-ssh-v1: urn:vyatta.com:mgmt:vyatta-service-ssh:1\n            vyatta-services-v1: urn:vyatta.com:mgmt:vyatta-services:1\n            vyatta-system-acm-configd-v1: urn:vyatta.com:mgmt:vyatta-system-acm-configd:1\n            vyatta-system-acm-opd-v1: urn:vyatta.com:mgmt:vyatta-system-acm-opd:1\n            vyatta-system-acm-v1: urn:vyatta.com:mgmt:vyatta-system-acm:1\n            vyatta-system-login-v1: urn:vyatta.com:mgmt:vyatta-system-login:1\n            vyatta-system-mgmt-v1: urn:vyatta.com:mgmt:vyatta-system-mgmt:1\n            vyatta-system-misc-v1: urn:vyatta.com:mgmt:vyatta-system-misc:1\n            vyatta-system-network-v1: urn:vyatta.com:mgmt:vyatta-system-network:1\n            vyatta-system-package-v1: urn:vyatta.com:mgmt:vyatta-system-package:1\n            vyatta-system-syslog-v1: urn:vyatta.com:mgmt:vyatta-system-syslog:1\n            vyatta-system-v1: urn:vyatta.com:mgmt:vyatta-system:1\n\nnode_templates:\n\n  vyatta_impl:\n    type: vyatta_node_config\n    interfaces:\n      cloudify.interfaces.lifecycle:\n        create:\n          inputs:\n            netconf_auth:\n              user: { get_input: netconf_user }\n              password: { get_input: netconf_password }\n              ip: { get_input: netconf_ip }\n              key_content: { get_input: netconf_key_content }\n            calls:\n              # get full config\n              - action: rfc6020@get-config\n                payload:\n                  rfc6020@source:\n                    rfc6020@running: {}\n                save_to: origin_interfaces\n\noutputs:\n  config:\n    description: Full config\n    value:\n        data: { get_attribute: [ vyatta_impl, origin_interfaces ] }\n        ns: { get_attribute: [ vyatta_impl, origin_interfaces_ns ] }\n\n'

@parameterized_class([
   { 'yaml': yaml_1_0, 'expected': 0},
   { 'yaml': yaml_1_5, 'expected': 5},
   { 'yaml': yaml_1_6, 'expected': 6}
])

class TestNOAMCount(unittest.TestCase):
    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()
    
    def test(self):
        metric = NOAM(self.yaml)
        count = metric.count()
        self.assertEqual(count, self.expected, 'Test failed because expected ' + str(self.expected) + ' and got ' + str(count) +'!') 
    
if __name__ == "__main__":
    unittest.main()

