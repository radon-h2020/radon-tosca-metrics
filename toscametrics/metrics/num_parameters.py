from toscametrics.blueprint_metric import BlueprintMetric


class NumParameters(BlueprintMetric):
    """ This class is responsible to count the number of parameters in a blueprint's interface"""

    def count(self):
        for key, value in self.blueprint.items():
            if key == 'inputs':
                return len(value)

        return 0
