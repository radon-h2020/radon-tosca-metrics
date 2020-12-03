from toscametrics.blueprint_metric import BlueprintMetric


class NumImports(BlueprintMetric):
    """ This class counts the blueprint's number of imports"""

    def count(self):
        return len(self.blueprint.get('imports', []))
