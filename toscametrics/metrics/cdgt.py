from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscaparser.tosca_template import ToscaTemplate

class CDGT(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of custom defined group types in a given .yaml file"""
    
    def count(self):
        '''Function which counts the number of custom defined group types''' 
        try:
            cd_group_types = self.getyml.get('group_types')
            if cd_group_types == None:
                return 0
            return len(cd_group_types)

        except AttributeError:
            return 0