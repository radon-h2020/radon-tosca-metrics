from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscametrics.utils import getPolicies
from toscametrics.yml.loc import LOC
from toscametrics.yml.etp import ETP

from io import StringIO

class NPOL(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of policies defined in a given .yaml file"""


    def _get_elements(self):
        '''Function which collects all the policies in the topology template with their attributes in a list'''
        try:
            template = self.getyml     
            policies = getPolicies(template)

            policies_list = []
            for policy in policies:
                if isinstance(policy, list):
                    policies_list.extend(policy)

                elif isinstance(policy, dict):
                    for policy_name, policy_values in policy.items():
                        policies_list.append({policy_name : policy_values})
                else:
                    continue
            return policies_list

        except (KeyError, AttributeError):
            return []    

    def count(self):
        '''Function which counts the number of policies within the whole script'''
        try:
            policies_list = self._get_elements()

            names = []
            for policy in policies_list:
                names.extend(policy.keys())
            unique_names = set(names)

            return len(unique_names)

        except AttributeError:
            return 0   


    def relative(self):
        '''Count relative to the lines of code'''
        try:
            strio = StringIO(self.getStringIOobject)
            return self.count() / LOC(strio).count()

        except (KeyError, AttributeError, ZeroDivisionError):
            return 0


    def entropy(self):
        '''Counts the entropy for the _get_elements blocks'''
        try:
            strio = StringIO(self.getStringIOobject)

            block = {}
            for element in self._get_elements():
                if isinstance(element, dict):
                    block.update(element)
            
            return ETP(strio).count(custom=block)

        except (KeyError, AttributeError, ZeroDivisionError):
            return 0



# string = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ntopology_template:\n  node_templates:\n    server2:\n      type: Compute\n\n    storage:\n      type: ObjectStorage\n      properties:\n        name: My Storage\n\n  groups:\n\n    redundants:\n      type: Redundants\n      properties:\n        priority: 0.8\n      members:\n      # Member node templates must match our definition at the group type\n      # (Can include derived types)\n      - server3\n      - server4\n\n  policies:\n\n    backup:\n      type: ContinuousBackup\n      properties:\n        frequency: .5 d\n      targets:\n      # Target node templates and groups must match our definition at the policy type\n      # (Can include derived types)\n      - storage\n      - server2\n      - redundants'
# #string = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ntopology_template:\n  node_templates:\n    wordpress_server:\n      type: tosca.nodes.WebServer\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n\n  groups:\n    my_co_location_group:\n      type: tosca.groups.Root\n      members: [ wordpress_server, mysql ]\n\t  \n  policies:\n    - my_anti_collocation_policy:\n        type: my.policies.anticolocateion\n        targets: [ my_co_location_group ]'
# print(string)
# from io import StringIO

# yml = StringIO(string.expandtabs(2)) 
# metric = NPOL(yml)

# print(metric._get_elements())
# print('check NPOL: ', metric.count())