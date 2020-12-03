from toscametrics.blueprint_metric import BlueprintMetric
from toscametrics.utils import key_value_list


class NumRelationshipTypes(BlueprintMetric):
    """ This class counts the number of relationship types defined in the blueprint"""

    def count(self):
        types = 0
        for key, value in key_value_list(self.blueprint):
            if key == 'relationship_types':
                types += len(value)

        return types
