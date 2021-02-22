import re

import toscametrics.utils as utils
from toscametrics.blueprint_metric import BlueprintMetric


class NumTokens(BlueprintMetric):
    """ This class counts the blueprint's number of tokens. """
    
    def count(self):
        keys = len(utils.all_keys(self.blueprint))
        values = utils.all_values(self.blueprint)
        return keys + sum(len(re.split(r'\s+', str(value).strip())) for value in values)
