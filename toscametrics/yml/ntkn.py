import re

import toscametrics.utils as utils
from toscametrics.blueprint.blueprint_metric import BlueprintMetric

class NTKN(BlueprintMetric):
    """ This class implements the metric 'Number of Tokens' in a blueprint script. """
    
    def count(self):
        """ Counts the number of tokens in a blueprint script """
        keys = len(utils.allKeys(self.getyml))
        values = utils.allValues(self.getyml)
        return keys + sum(len(re.split(r'\s+', str(value).strip())) for value in values)



# string = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template for deploying a single server with predefined properties.\n\ntopology_template:\n  inputs:\n    cpus:\n      type: integer\n      description: Number of CPUs for the server.\n      constraints:\n        - valid_values: [ 1, 2, 4, 8 ]'

# from io import StringIO

# print(string)
# yml = StringIO(string.expandtabs(2)) 
# metric = NTKN(yml)

# print('NTKN count: ', metric.count())