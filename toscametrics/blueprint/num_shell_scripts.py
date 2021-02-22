from toscametrics.blueprint_metric import BlueprintMetric
from toscametrics.utils import all_values


class NumShellScripts(BlueprintMetric):
    """ This class is responsible to count the number of shell scripts called by a blueprint"""

    def count(self):
        return sum(1 for item in all_values(self.blueprint) if type(item) == str and item.endswith('.sh'))
