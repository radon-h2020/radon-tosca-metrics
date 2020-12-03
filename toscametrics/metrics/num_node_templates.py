from toscametrics.blueprint_metric import BlueprintMetric
from toscametrics.utils import key_value_list


class NumNodeTemplates(BlueprintMetric):
    """ This class counts the blueprint's number of node templates"""

    def count(self):
        types = 0
        for key, value in key_value_list(self.blueprint):
            if key == 'node_templates':
                types += len(value)

        return types
