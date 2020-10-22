from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscametrics.yml.loc import LOC
from toscametrics.yml.etp import ETP

from io import StringIO

class CDNT(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of custom defined node types in a given .yaml file"""


    def _get_elements(self):
        '''Function which collects all the custom node type definitions in the service template with their attributes in a list'''
        try:
            cd_node_types = self.getyml.get('node_types')

            node_defs = []
            for node_name, node_values in cd_node_types.items():
                node_defs.append({node_name : node_values})
            return node_defs

        except (KeyError, AttributeError):
            return []  



    def count(self):
        '''Function which counts the number of custom defined node types''' 
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


# string = 'tosca_definitions_version: tosca_simple_yaml_1_2\n'

# path = r'C:\Users\s145559\OneDrive - TU Eindhoven\School\JADS\Jaar 2\Thesis\RADON PROJECT\GIT projects\ANALYSIS\dataminer\tmp\openstack\tosca-parser\Example\node_with_cap.yaml'
# from io import StringIO

# with open(path, 'r') as file:
#     string = file.read()

# print(string)
# yml = StringIO(string.expandtabs(2)) 
# metric = CDNT(yml)

# print('CDNT count: ', metric.count())
# x = metric._get_elements()