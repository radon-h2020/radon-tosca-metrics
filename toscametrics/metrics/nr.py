from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscaparser.tosca_template import ToscaTemplate

class NR(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of relationship templates defined in a given .yaml file"""
    
    def count(self):
        try:
            template = ToscaTemplate(yaml_dict_tpl=self.getyml)
            rel_types = template.relationship_templates
            print(rel_types)
            return(len(rel_types))
        except AttributeError:
            return 0        