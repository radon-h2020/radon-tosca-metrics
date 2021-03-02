from toscametrics.blueprint_metric import BlueprintMetric
from toscametrics.utils import key_value_list


class NumProperties(BlueprintMetric):
    """ This class is responsible counts the blueprint's number of propertie"""

    def count(self):
        properties = 0
        for key, value in key_value_list(self.blueprint):
            if key == 'properties' and type(value) in (list, dict):
                properties += len(value)

        return properties
