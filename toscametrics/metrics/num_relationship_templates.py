from toscametrics.blueprint_metric import BlueprintMetric
from toscametrics.utils import key_value_list


class NumRelationshipTemplates(BlueprintMetric):
    """ This class counts the blueprint's number of node templates"""

    def count(self):
        return sum(len(value) for key, value in key_value_list(self.blueprint) if key == 'relationship_templates')
