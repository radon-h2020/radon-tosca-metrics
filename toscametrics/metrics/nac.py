from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscametrics.utils import keyValueList

class NAC(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of activities in a given .yaml file. They only occur in workflows."""   

    def count(self):
        '''Function which counts the activities within the whole script'''

        try:
            template = self.getyml
            kvlist = keyValueList(template)
            activities = [activity[1] for activity in kvlist if activity[0] == 'activities']
            
            activity_list = []
            for activity in activities:
                if isinstance(activity, list):
                    activity_list.extend(activity)
                else:
                    activity_list.append(activity)

            return len(activity_list)

        except AttributeError:
            return 0


# # string = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ntopology_template:\n\n  inputs:\n    rulesInput:\n      type: list\n      entry_schema: FirewallRules\n      \n  substitution_mappings:\n    node_type: abstract.Firewall\n    substitution_filter:\n      properties:\n        - vendor: { equal: Simple }\n    properties:\n      rules: [ rulesInput ]\n  node_templates:\n    acme:\n      type: SimpleFirewall\n      properties:\n        rules: { get_input: rulesInput }\n'
# string = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ntopology_template:\n  node_templates:\n    my_server:\n      type: tosca.nodes.Compute\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      requirements:\n        - host: my_server\n      interfaces:\n        tosca.interfaces.nodes.custom.Backup:\n          operations:\n            backup: backup.sh\n\n  workflows:\n    backup:\n      description: Performs a snapshot of the MySQL data.\n      preconditions:\n        - target: my_server\n          condition:\n            - assert:\n              - state: [{equal: available}]\n        - target: mysql\n          condition:\n            - assert:\n              - state: [{valid_values: [started, available]}]\n              - my_attribute: [{equal: ready }]\n\n      steps:\n        my_step:\n          target: mysql\n          activities:\n            - call_operation: tosca.interfaces.nodes.custom.Backup.backup\n            - do_something_else: tosca.interfaces.nodes.custom.Backup.else'

# print(string)
# from io import StringIO

# yml = StringIO(string.expandtabs(2)) 
# metric = NAC(yml)

# print('check NAC: ', metric.count())