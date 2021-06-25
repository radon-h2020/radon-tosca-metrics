from toscametrics.blueprint_metric import BlueprintMetric
from toscametrics.utils import key_value_list


class NumWorkflows(BlueprintMetric):
    """ This class counts the number of blueprint's workflows.
        Note, this might be applicable to alien4cloud only
    """

    def count(self):
        types = 0
        for key, value in key_value_list(self.blueprint):
            if key == 'workflows':
                types += len(value)

        return types
