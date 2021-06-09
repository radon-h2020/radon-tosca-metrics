from toscametrics.blueprint_metric import BlueprintMetric
from toscametrics.utils import key_value_list


class NumCapabilityTypes(BlueprintMetric):
    """ This class counts the blueprint's number of artifacts types"""

    def count(self):
        types = 0
        for key, value in key_value_list(self.blueprint):
            if key == 'capability_types':
                types += len(value)

        return types
