import toscametrics.utils as utils
from toscametrics.blueprint_metric import BlueprintMetric


class NumKeys(BlueprintMetric):
    """ This class counts the blueprint's dictonary keys"""

    def count(self):
        script = self.blueprint
        return len(utils.all_keys(script))
