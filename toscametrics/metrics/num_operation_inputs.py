from toscametrics.blueprint_metric import BlueprintMetric
from toscametrics.utils import key_value_list


class NumOperationInputs(BlueprintMetric):
    """ This class is responsible counts the blueprint's number of parameters"""

    def count(self):

        params = 0
        for key, value in key_value_list(self.blueprint):

            if key == 'operations':
                for interface, items in value.items():
                    params += len(items.get('inputs', dict()))

        return params
