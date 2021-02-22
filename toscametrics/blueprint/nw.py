from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscametrics.utils import getWorkflows
from toscametrics.general.loc import LOC
from toscametrics.general.etp import ETP

from io import StringIO

class NW(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of imperative workflows defined in a given .yaml file"""

    def _get_elements(self):
        '''Function which collects all the workflows with their attributes in a list'''
        try:
            template = self.getyml     
            workflows = getWorkflows(template)

            workflow_list = []
            for workflow in workflows:
                if isinstance(workflow, dict):
                    for workflow_name, workflow_values in workflow.items():
                        workflow_list.append({workflow_name : workflow_values})
                else:
                    continue
            return workflow_list

        except (KeyError, AttributeError):
            return []     


    def count(self):
        '''Function which counts the number of unique defined nodes in a node template''' 
        try:
            workflow_list = self._get_elements()

            names = []
            for worflows in workflow_list:
                names.extend(worflows.keys())
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



# string = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\ntopology_template:\n  node_templates:\n    my_server:\n      type: tosca.nodes.Compute\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      requirements:\n        - host: my_server\n      interfaces:\n        tosca.interfaces.nodes.custom.Backup:\n          operations:\n            backup: backup.sh\n\n  workflows:\n    backup:\n      description: Performs a snapshot of the MySQL data.\n      steps:\n        my_step:\n          target: mysql\n          activities:\n            - call_operation: tosca.interfaces.nodes.custom.Backup.backup\n    remove:\n      steps:\n        my_step:\n          target: mysql\n          activities:\n            - call_operation: tosca.interfaces.nodes.custom.Remove.remove'
# #string = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\nnode_types:\n  tosca.nodes.Root:\n    attributes:\n      tosca_id:\n        type: string\n      tosca_name:\n        type: string\n\npolicy_types:\n  mycompany.mytypes.policies.placement.Container.Linux:\n    description: My companyâ€™s placement policy for linux\n    derived_from: tosca.policies.Root\n'


# from io import StringIO

# print(string)
# general = StringIO(string.expandtabs(2))
# metric = NW(general)

# print('NW count: ', metric.entropy())

