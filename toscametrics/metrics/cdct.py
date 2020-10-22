from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscaparser.tosca_template import ToscaTemplate

class CDCT(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of custom defined capability types in a given .yaml file"""
    
    def count(self):
        '''Function which counts the number of custom defined capability types''' 
        try:
            cd_capability_types = self.getyml.get('capability_types')
            if not cd_capability_types:
                return 0
            return len(cd_capability_types)

        except AttributeError:
            return 0