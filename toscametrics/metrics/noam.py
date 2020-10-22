from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscametrics.utils import keyValueList

class NOAM(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of accessor methods/functions in a given .yaml file"""   

    def count(self):
        '''Function which counts the accessor methods/functions within the whole script'''

        function_keywords = [
            'get_input',
            'get_property',
            'get_attribute',
            'get_operation_output',
            'get_nodes_of_type',
            'get_artifact'
        ]

        try:
            template = self.getyml
            kvlist = keyValueList(template)
            funcs = [func for func in kvlist if func[0] in function_keywords]
            return len(funcs)

        except AttributeError:
            return 0


# # string = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ntopology_template:\n\n  inputs:\n    rulesInput:\n      type: list\n      entry_schema: FirewallRules\n      \n  substitution_mappings:\n    node_type: abstract.Firewall\n    substitution_filter:\n      properties:\n        - vendor: { equal: Simple }\n    properties:\n      rules: [ rulesInput ]\n  node_templates:\n    acme:\n      type: SimpleFirewall\n      properties:\n        rules: { get_input: rulesInput }\n'
# string = 'tosca_definitions_version: cloudify_dsl_1_3\n\nimports:\n  - http://www.getcloudify.org/spec/cloudify/3.4/types.yaml\n  - https://raw.githubusercontent.com/cloudify-cosmo/cloudify-netconf-plugin/master/plugin.yaml\n\ninputs:\n\n  netconf_ip:\n    type: string\n    description: >\n       netconf server ip\n    default: 127.0.0.1\n\n  netconf_user:\n    type: string\n    description: >\n       netconf server user\n    default: netconf\n  netconf_password:\n    type: string\n    description: >\n       netconf server user password\n    default: netconf\n\n  netconf_key_content:\n    type: string\n    description: >\n       netconf server user rsa key content, can be used instead password\n    default: ""\n\nnode_types:\n\n  vyatta_node_config:\n    derived_from: cloudify.netconf.nodes.xml_rpc\n    properties:\n      metadata:\n        default:\n          capabilities:\n            - urn:ietf:params:netconf:base:1.0\n            - urn:ietf:params:netconf:capability:writeable-running:1.0\n            - urn:ietf:params:netconf:capability:rollback-on-error:1.0\n            - urn:ietf:params:netconf:capability:startup:1.0\n            - urn:ietf:params:netconf:capability:url:1.0\n          xmlns:\n            vyatta-if-v1: urn:vyatta.com:mgmt:vyatta-interfaces:1\n            vyatta-interfaces-dataplane-v1: urn:vyatta.com:mgmt:vyatta-interfaces-dataplane:1\n            vyatta-interfaces-loopback-v1: urn:vyatta.com:mgmt:vyatta-interfaces-loopback:1\n            vyatta-protocols-static-v1: urn:vyatta.com:mgmt:vyatta-protocols-static:1\n            vyatta-protocols-v1: urn:vyatta.com:mgmt:vyatta-protocols:1\n            vyatta-service-https-v1: urn:vyatta.com:mgmt:vyatta-service-https:1\n            vyatta-service-nat-v1: urn:vyatta.com:mgmt:vyatta-service-nat:1\n            vyatta-service-netconf-v1: urn:vyatta.com:mgmt:vyatta-service-netconf:1\n            vyatta-service-ssh-v1: urn:vyatta.com:mgmt:vyatta-service-ssh:1\n            vyatta-services-v1: urn:vyatta.com:mgmt:vyatta-services:1\n            vyatta-system-acm-configd-v1: urn:vyatta.com:mgmt:vyatta-system-acm-configd:1\n            vyatta-system-acm-opd-v1: urn:vyatta.com:mgmt:vyatta-system-acm-opd:1\n            vyatta-system-acm-v1: urn:vyatta.com:mgmt:vyatta-system-acm:1\n            vyatta-system-login-v1: urn:vyatta.com:mgmt:vyatta-system-login:1\n            vyatta-system-mgmt-v1: urn:vyatta.com:mgmt:vyatta-system-mgmt:1\n            vyatta-system-misc-v1: urn:vyatta.com:mgmt:vyatta-system-misc:1\n            vyatta-system-network-v1: urn:vyatta.com:mgmt:vyatta-system-network:1\n            vyatta-system-package-v1: urn:vyatta.com:mgmt:vyatta-system-package:1\n            vyatta-system-syslog-v1: urn:vyatta.com:mgmt:vyatta-system-syslog:1\n            vyatta-system-v1: urn:vyatta.com:mgmt:vyatta-system:1\n\nnode_templates:\n\n  vyatta_impl:\n    type: vyatta_node_config\n    interfaces:\n      cloudify.interfaces.lifecycle:\n        create:\n          inputs:\n            netconf_auth:\n              user: { get_input: netconf_user }\n              password: { get_input: netconf_password }\n              ip: { get_input: netconf_ip }\n              key_content: { get_input: netconf_key_content }\n            calls:\n              # get full config\n              - action: rfc6020@get-config\n                payload:\n                  rfc6020@source:\n                    rfc6020@running: {}\n                save_to: origin_interfaces\n\noutputs:\n  config:\n    description: Full config\n    value:\n        data: { get_attribute: [ vyatta_impl, origin_interfaces ] }\n        ns: { get_attribute: [ vyatta_impl, origin_interfaces_ns ] }\n\n'

# print(string)
# from io import StringIO

# yml = StringIO(string.expandtabs(2)) 
# metric = NOAM(yml)

# print('check NOAM: ', metric.count())