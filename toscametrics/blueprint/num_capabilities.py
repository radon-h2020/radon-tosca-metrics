from toscametrics.blueprint_metric import BlueprintMetric
from toscametrics.utils import key_value_list


class NumCapabilities(BlueprintMetric):
    """
    This class is responsible counts the blueprint's number of capabilities
    """

    def count(self):

        capabilities = 0
        for key, value in key_value_list(self.blueprint):

            if key == 'capabilities':
                capabilities += len(value)

        return capabilities
