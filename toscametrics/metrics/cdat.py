from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscaparser.tosca_template import ToscaTemplate

class CDAT(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of custom defined artifact types in a given .yaml file"""
    
    def count(self):
        '''Function which counts the number of custom defined artifact types''' 
        try:
            cd_artifact_types = self.getyml.get('artifact_types')
            if cd_artifact_types == None:
                return 0
            return len(cd_artifact_types)
        
        except AttributeError:
            return 0