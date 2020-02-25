from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscaparser.tosca_template import ToscaTemplate

class NRT(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of relationship types defined in a given .yaml file"""

    def count(self):
        try:
            template = ToscaTemplate(yaml_dict_tpl=self.getyml)
            rel_temps = template.relationship_templates

            unique_types = set()
            for temp in rel_temps:
                unique_types.add(temp.type)
            return len(unique_types)
        
        except AttributeError:
            return 0