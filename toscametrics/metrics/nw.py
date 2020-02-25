from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscaparser.tosca_template import ToscaTemplate

class NW(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of imperative workflows defined in a given .yaml file"""
    
    def count(self):
        try:
            template = self.getyml.get('topology_template')
            workflows = template.get('workflows')
            if workflows == None:
                return 0
            return len(workflows)
        except AttributeError:
            return 0

# string = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\ntopology_template:\n  node_templates:\n    my_server:\n      type: tosca.nodes.Compute\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      requirements:\n        - host: my_server\n      interfaces:\n        tosca.interfaces.nodes.custom.Backup:\n          operations:\n            backup: backup.sh\n\n  workflows:\n    backup:\n      description: Performs a snapshot of the MySQL data.\n      steps:\n        my_step:\n          target: mysql\n          activities:\n            - call_operation: tosca.interfaces.nodes.custom.Backup.backup\n    remove:\n      steps:\n        my_step:\n          target: mysql\n          activities:\n            - call_operation: tosca.interfaces.nodes.custom.Remove.remove'
# string = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\nnode_types:\n  tosca.nodes.Root:\n    attributes:\n      tosca_id:\n        type: string\n      tosca_name:\n        type: string\n\npolicy_types:\n  mycompany.mytypes.policies.placement.Container.Linux:\n    description: My companyâ€™s placement policy for linux\n    derived_from: tosca.policies.Root\n'


# from io import StringIO

# print(string)
# yml = StringIO(string.expandtabs(2)) 
# metric = NW(yml)

# print('NW count: ', metric.count())
