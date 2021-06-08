from toscametrics.blueprint_metric import BlueprintMetric


class NumImports(BlueprintMetric):
    """ This class counts the blueprint's number of imports"""

    def count(self):

        imports = self.blueprint.get('imports', [])
        if type(imports) == list:
            return len(imports)
        elif type(imports) == dict:
            return 1
