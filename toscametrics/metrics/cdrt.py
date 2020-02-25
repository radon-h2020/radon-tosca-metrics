from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscaparser.tosca_template import ToscaTemplate

class CDRT(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of custom defined relationship types in a given .yaml file"""
    
    def count(self):
        '''Function which counts the number of custom defined relationship types'''
        try: 
            cd_relationship_types = self.getyml.get('relationship_types')
            if cd_relationship_types == None:
                return 0
            return len(cd_relationship_types)

        except AttributeError:
            return 0



# string = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\nrelationship_types:\n\n  tosca.relationships.Root:\n    attributes:\n      tosca_id:\n        type: string\n\n  tosca.relationships.DependsOn:\n    derived_from: tosca.relationships.Root\n    valid_target_types: [ tosca.capabilities.Node ]'
# from io import StringIO

# print(string)
# yml = StringIO(string.expandtabs(2)) 
# metric = CDRT(yml)

# print('CDRT count: ', metric.count())