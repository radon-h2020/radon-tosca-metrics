from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscametrics.utils import getRequirements
from toscametrics.metrics.nn import NN
from toscametrics.metrics.cdnt import CDNT
from statistics import mean
from statistics import median
from io import StringIO


class NRQ(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of requirements defined in a given .yaml file"""


    def _get_elements(self):
        '''Function which collects all the requirements in the node templates and node types with their attributes in a list'''
        
        try:
            strio = StringIO(self.getStringIOobject)
            nodes = NN(strio)._get_elements()
            custom_nodes = CDNT(strio)._get_elements()

            node_reqs = []
            for node in nodes:
                reqs_lists = getRequirements(node)

                if len(reqs_lists) == 0:
                    node_reqs.append({list(node.keys())[0] : 0})
                    continue

                if isinstance(reqs_lists[0], list):
                    reqs_lists = [item for sublist in reqs_lists for item in sublist]
                
                reqs_dict = {}
                for req in reqs_lists:
                    if not isinstance(req, dict):
                        reqs_dict.update({req : None})
                        continue

                    reqs_dict.update(req)
                
                node_reqs.append({list(node.keys())[0] : reqs_dict})

            for node in custom_nodes:
                reqs_lists = getRequirements(node)

                if len(reqs_lists) == 0:
                    node_reqs.append({list(node.keys())[0] : 0})
                    continue

                if isinstance(reqs_lists[0], list):
                    reqs_lists = [item for sublist in reqs_lists for item in sublist]
                
                reqs_dict = {}
                for req in reqs_lists:
                    if not isinstance(req, dict):
                        reqs_dict.update({req : None})
                        continue

                    reqs_dict.update(req)
                
                node_reqs.append({list(node.keys())[0] : reqs_dict})

            return node_reqs

        except (KeyError, AttributeError):
            return []  


    def count(self):
        try:
            node_reqs = self._get_elements()

            names = []
            for node in node_reqs:
                for _, reqs in node.items():
                    if isinstance(reqs, dict):
                        names.extend(reqs.keys())
            unique_names = set(names)

            return len(unique_names)

        except (ValueError, AttributeError):
            return 0 


    def min(self):   
        try:
            node_reqs = self._get_elements()
            
            names = []
            for node in node_reqs:
                for _, reqs in node.items():
                    if isinstance(reqs, dict):
                        names.append(len(reqs.keys()))
                    else:
                        names.append(0)

            return min(names)

        except (ValueError, AttributeError):
            return 0

    def max(self):   
        try:
            node_reqs = self._get_elements()
            
            names = []
            for node in node_reqs:
                for _, reqs in node.items():
                    if isinstance(reqs, dict):
                        names.append(len(reqs.keys()))
                    else:
                        names.append(0)

            return max(names)

        except (ValueError, AttributeError):
            return 0 

    def mean(self):   
        try:
            node_reqs = self._get_elements()
            
            names = []
            for node in node_reqs:
                for _, reqs in node.items():
                    if isinstance(reqs, dict):
                        names.append(len(reqs.keys()))
                    else:
                        names.append(0)

            return mean(names)

        except (ValueError, AttributeError):
            return 0 


    def median(self):   
        try:
            node_reqs = self._get_elements()
            
            names = []
            for node in node_reqs:
                for _, reqs in node.items():
                    if isinstance(reqs, dict):
                        names.append(len(reqs.keys()))
                    else:
                        names.append(0)

            return median(names)

        except (ValueError, AttributeError):
            return 0  




# string = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ntopology_template:\n  node_templates:\n    my_block_storage:\n      type: BlockStorage\n      properties:\n        size: 10\n\n    my_web_app_tier_1:\n      type: Compute\n      requirements:\n        - local_stoooorage:\n            node: my_block_storage\n            relationship: MyAttachesTo\n              # use default property settings in the Relationship Type definition\n\n    my_web_app_tier_2:\n      type: Compute\n      requirements:\n        - local_storage:\n            node: my_block_storage\n            relationship:\n              type: MyAttachesTo\n              # Override default property setting for just the â€˜locationâ€™ property\n              properties:\n                location: /some_other_data_location '

# from io import StringIO

# print(string)

# yml = StringIO(string.expandtabs(2)) 
# metric = NRQ(yml)

# print('count: ', metric.count())
# print('min: ', metric.min())
# print('max: ', metric.max())
# print('mean: ', metric.mean())
# print('median: ', metric.median())

# print(metric._get_elements())
