from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscametrics.utils import keyValueList

class NFUNC(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of functions in a given .yaml file"""   

    def count(self):
        '''Function which counts the functions within the whole script'''

        function_keywords = [
            'concat',
            'join',
            'token',
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
# string = 'node_templates:\n\n  juniper_impl:\n    type: juniper_node_config\n    properties:\n      netconf_auth:\n        user: { get_input: netconf_user }\n        password: { get_input: netconf_password }\n        ip: { get_input: netconf_ip }\n        key_content: { get_input: netconf_key_content }\n        port: { get_input: netconf_port }'

# print(string)
# from io import StringIO

# yml = StringIO(string.expandtabs(2)) 
# metric = NFUNC(yml)

# print('check NFUNC: ', metric.count())