from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscaparser.tosca_template import ToscaTemplate
from toscametrics.utils import getProperties

class NGP(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of properties defined in a given .yaml file"""

    def count(self):
        '''Function which counts the number of properties within the whole script'''
        try:
            template = self.getyml
            properties = getProperties(template)
            count = 0
            for prop in properties:
                count += len(prop[1])
            return count

        except AttributeError:
            return 0



# from io import StringIO

# string = 'tosca_definitions_version: tosca_simple_yaml_1_1\n\nrelationship_types:\n\n  tosca.relationships.Root:\n    interfaces:\n      Configure:\n        type: tosca.interfaces.relationship.Configure\n\n  tosca.relationships.HostedOn:\n    derived_from: tosca.relationships.Root\n    valid_target_types: [ tosca.capabilities.Container ]\n\n  tosca.relationships.ConnectsTo:\n    properties:\n      credential:\n        type: tosca.datatypes.Credential\n        required: false\n\t\t\n  tosca.relationships.AttachesTo:\n    properties:\n      location:\n        type: string\n        constraints:\n          - min_length: 1\n      device:\n        type: string\n        required: false\n    attributes:\n      device:\n        type: string'

# print(string)
# yml = StringIO(string.expandtabs(2)) 
# metric = NGP(yml)

# print('NGP count: ', metric.count())
