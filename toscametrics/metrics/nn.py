from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscaparser.tosca_template import ToscaTemplate

class NN(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of nodes defined in a given .yaml file"""
    
    #Possible issue here: is it possible nodes are specified without template?
    def count(self):
        try:
            template = ToscaTemplate(yaml_dict_tpl=self.getyml)
            node_temps = template.nodetemplates
            return(len(node_temps))

        except AttributeError:
            return 0        