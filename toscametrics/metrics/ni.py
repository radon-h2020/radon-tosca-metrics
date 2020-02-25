from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscaparser.tosca_template import ToscaTemplate

class NI(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of imports defined in a given .yaml file"""
    
    def count(self):
        try:
            template = ToscaTemplate(yaml_dict_tpl=self.getyml)
            imports = template._tpl_imports()
            return len(imports)

        except TypeError:
            return 0
