from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscametrics.utils import getNodeTemplates
from toscametrics.yml.loc import LOC
from toscametrics.yml.etp import ETP

from io import StringIO

class NN(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of nodes defined in a given .yaml file"""
    
    def _get_elements(self):
        '''Function which collects all the nodes in the node templates with their attributes in a list'''
        try:
            template = self.getyml     
            node_templates = getNodeTemplates(template)

            nodes = []
            for node_template in node_templates:
                if isinstance(node_template, dict):
                    for node_name, node_values in node_template.items():
                        nodes.append({node_name : node_values})
                else:
                    continue
            return nodes

        except (KeyError, AttributeError):
            return []     


    def count(self):
        '''Function which counts the number of unique defined nodes in a node template''' 
        try:
            nodes_list = self._get_elements()

            names = []
            for nodes in nodes_list:
                names.extend(nodes.keys())
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


# from io import StringIO

# path = r'C:\Users\s145559\OneDrive - TU Eindhoven\School\JADS\Jaar 2\Thesis\RADON PROJECT\GIT projects\ANALYSIS\dataminer\tmp\tliron\puccini\Example\artifacts.yaml'
# with open(path, 'r') as file:
#             string = file.read()


# #string = 'tosca_definitions_version: tosca_simple_yaml_1_0\ndescription: Template with requirements against hosting infrastructure.\n\ntopology_template:\n  inputs:\n    # omitted here for brevity\n\n  node_templates:\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        root_password: { get_input: my_mysql_rootpw }\n        port: { get_input: my_mysql_port }\n      requirements:\n        - host:\n            node_filter:\n              capabilities:\n                - host:\n                    properties:\n                      - num_cpus: { in_range: [ 1, 4 ] }\n                      - mem_size: { greater_or_equal: 2 GB }\n                - os:\n                    properties:\n                      - architecture: { equal: x86_64 }\n                      - type: linux\n                      - distribution: ubuntu\n                - backup_os:\n                    properties:\n                      - architecture: { equal: x86_64 }\n                      - type: linux\n                      - distribution: ubuntu\n                      \n    backup_mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        # omitted here for brevity\n      requirements:\n        - host:\n            node_filter:\n              capabilities:\n                - host:\n                    properties:\n                      - num_cpus: { in_range: [ 1, 4 ] }\n                      - mem_size: { greater_or_equal: 2 GB }\n                - os:\n                    properties:\n                      - architecture: { equal: x86_64 }\n                      - type: linux\n                      - distribution: ubuntu'

# string = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template for deploying a single server with predefined properties.\n\ntopology_template:\n  inputs:\n    cpus:\n      type: integer\n      description: Number of CPUs for the server.\n      constraints:\n        - valid_values: [ 1, 2, 4, 8 ]\n\n  node_templates:\n    my_server:\n      type: tosca.nodes.Compute\n      capabilities:\n        # Host container properties\n        host:\n          properties:\n            # Compute properties\n            num_cpus: { get_input: cpus }\n            mem_size: 2048  MB\n            disk_size: 10 GB'
# print(string)
# yml = StringIO(string) 
# metric = NN(yml)

# print('NN count: ', metric.count())