import re
import yaml

from toscametrics.blueprint_metric import BlueprintMetric
from toscametrics.utils import key_value_list

get_input_re = r'\s*get_input:\s*(\w+)'
get_param_re = r'\s*get_parameter:\s*(\w+)'


class LCOT(BlueprintMetric):
    """ This class measure the Lack of Cohesion of Types/Templates"""

    def count(self):

        node_templates_and_types = {}

        for key, value in key_value_list(self.blueprint):
            if key in ('node_templates', 'node_types'):
                node_templates_and_types.update(value)

        nodes_map = {}

        for node_name, node_body in node_templates_and_types.items():
            plain_node = yaml.dump(node_body)
            variables = re.findall(get_input_re, plain_node)
            variables.extend(re.findall(get_param_re, plain_node))
            nodes_map[node_name] = variables

        for node_1, props_1 in list(nodes_map.items()):
            for node_2, props_2 in list(nodes_map.items()):
                if node_1 == node_2:
                    continue

                if not set(props_1).isdisjoint(props_2):
                    nodes_map[node_1] = set(props_1).union(props_2)
                    del nodes_map[node_2]

        return len(nodes_map)
