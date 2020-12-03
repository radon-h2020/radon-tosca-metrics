from toscametrics.blueprint_metric import BlueprintMetric
from toscametrics.utils import key_value_list


class NumInterfaces(BlueprintMetric):
    """ This class counts the blueprint's number of interfaces"""

    def count(self):
        return sum(len(value) for key, value in key_value_list(self.blueprint) if key == 'interfaces')
