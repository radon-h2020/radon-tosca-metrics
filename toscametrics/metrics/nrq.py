from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscaparser.tosca_template import ToscaTemplate
from toscametrics.utils import getRequirements

class NRQ(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of requirements defined in a given .yaml file"""

    def count(self):
        '''Function which counts the number of requirements within the whole script'''
        try:
            template = self.getyml
            reqs = getRequirements(template)
            
            count = 0
            for req in reqs:
                count += len(req[0])
            return count

        except AttributeError:
            return 0


# string = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ntopology_template:\n  node_templates:\n    my_block_storage:\n      type: BlockStorage\n      properties:\n        size: 10\n\n    my_web_app_tier_1:\n      type: Compute\n      requirements:\n        - local_storage:\n            node: my_block_storage\n            relationship: MyAttachesTo\n              # use default property settings in the Relationship Type definition\n\n    my_web_app_tier_2:\n      type: Compute\n      requirements:\n        - local_storage:\n            node: my_block_storage\n            relationship:\n              type: MyAttachesTo\n              # Override default property setting for just the â€˜locationâ€™ property\n              properties:\n                location: /some_other_data_location '

# from io import StringIO

# print(string)

# yml = StringIO(string.expandtabs(2)) 
# metric = NRQ(yml)

# print('NRQ count: ', metric.count())
