from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscaparser.tosca_template import ToscaTemplate

class CDNT(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of custom defined node types in a given .yaml file"""
    
    def count(self):
        '''Function which counts the number of custom defined node types''' 
        try:
            cd_node_types = self.getyml.get('node_types')
            if cd_node_types == None:
                return 0
            return len(cd_node_types)

        except AttributeError:
            return 0



# string = 'tosca_definitions_version: tosca_simple_yaml_1_2\n'
# from io import StringIO

# print(string)
# yml = StringIO(string.expandtabs(2)) 
# metric = CDNT(yml)

# print('CDNT count: ', metric.count())