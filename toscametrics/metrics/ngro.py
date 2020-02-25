from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscaparser.tosca_template import ToscaTemplate
from toscametrics.utils import getGroups

class NGRO(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of groups defined in a given .yaml file"""

    def count(self):
        '''Function which counts the number of groups within the whole script'''
        try:
            template = self.getyml
            groups = getGroups(template)
            count = 0
            for gro in groups:
                count += len(gro[1])
            return count

        except AttributeError:
            return 0


# string = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ntopology_template:\n  node_templates:\n    server2:\n      type: Compute\n\n    storage:\n      type: ObjectStorage\n      properties:\n        name: My Storage\n\n  groups:\n\n    redundants:\n      type: Redundants\n      properties:\n        priority: 0.8\n      members:\n      # Member node templates must match our definition at the group type\n      # (Can include derived types)\n      - server3\n      - server4\n\n  policies:\n\n    backup:\n      type: ContinuousBackup\n      properties:\n        frequency: .5 d\n      targets:\n      # Target node templates and groups must match our definition at the policy type\n      # (Can include derived types)\n      - storage\n      - server2\n      - redundants'
# print(string)
# from io import StringIO

# yml = StringIO(string.expandtabs(2)) 
# metric = NGRO(yml)

# print('check NGRO: ', metric.count())