from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscaparser.tosca_template import ToscaTemplate

class CDIT(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of custom defined interface types in a given .yaml file"""
    
    def count(self):
        '''Function which counts the number of custom defined interface types''' 
        try:
            cd_interface_types = self.getyml.get('interface_types')
            if cd_interface_types == None:
                return 0
            return len(cd_interface_types)

        except AttributeError:
            return 0