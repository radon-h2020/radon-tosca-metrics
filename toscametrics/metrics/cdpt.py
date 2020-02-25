from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscaparser.tosca_template import ToscaTemplate

class CDPT(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of custom defined policy types in a given .yaml file"""
    
    def count(self):
        '''Function which counts the number of custom defined policy types''' 
        try:
            cd_policy_types = self.getyml.get('policy_types')
            if cd_policy_types == None:
                return 0
            return len(cd_policy_types)

        except AttributeError:
            return 0