from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscaparser.tosca_template import ToscaTemplate
from toscaparser.topology_template import TopologyTemplate
from toscaparser.substitution_mappings import SubstitutionMappings
from toscametrics.utils import getNodeTypes

class NNT(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of node types defined in a given .yaml file"""

    def count(self):
        try:
            template = ToscaTemplate(yaml_dict_tpl=self.getyml)
            node_temps = template.nodetemplates

            unique_types = set()
            for temp in node_temps:
                nodes = temp.templates
                for value in nodes.values():
                    unique_types.add(value.get('type'))
            return len(unique_types)
        
        except AttributeError:
            return 0


# from io import StringIO

# string = ''

# yml = StringIO(string.expandtabs(2)) 
# metric = NNT(yml)

# print('NNT count: ', metric.count())