from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscaparser.tosca_template import ToscaTemplate

class CDDT(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of custom defined data types in a given .yaml file"""
    
    def count(self):
        '''Function which counts the number of custom defined data types'''
        try: 
            cd_data_types = self.getyml.get('data_types')
            if cd_data_types == None:
                return 0
            return len(cd_data_types)

        except AttributeError:
            return 0