from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscaparser.tosca_template import ToscaTemplate
from toscametrics.utils import keyValueList

class NF(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of node and substitution filters defined in a given .yaml file"""

    def count(self):
        '''Function which counts the number of node and substitution filters within the whole script'''
        try:
            template = self.getyml
            kvlist = keyValueList(template)
            node_filters = [group for group in kvlist if group[0] == 'node_filter']
            sub_filters = [group for group in kvlist if group[0] == 'substitution_filter']
            return len(node_filters) + len(sub_filters)

        except AttributeError:
            return 0


# string = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ntopology_template:\n\n  inputs:\n    rulesInput:\n      type: list\n      entry_schema: FirewallRules\n      \n  substitution_mappings:\n    node_type: abstract.Firewall\n    substitution_filter:\n      properties:\n        - vendor: { equal: Simple }\n    properties:\n      rules: [ rulesInput ]\n  node_templates:\n    acme:\n      type: SimpleFirewall\n      properties:\n        rules: { get_input: rulesInput }\n'
# print(string)
# from io import StringIO

# yml = StringIO(string.expandtabs(2)) 
# metric = NF(yml)

# print('check NF: ', metric.count())