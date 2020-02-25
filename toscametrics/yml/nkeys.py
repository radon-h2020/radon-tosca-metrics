import toscametrics.utils as utils
from toscametrics.blueprint.blueprint_metric import BlueprintMetric

class NKEYS(BlueprintMetric):
    """ This class implements the metric 'Number of keys' in a Blueprint script. """

    def count(self):
        script = self.getyml
        return len(utils.allKeys(script))




# string = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\nartifact_types:\n\n  kubernetes.Spec:\n    description: >-\n      Object specification\n    derived_from: tosca.artifacts.Root\n    file_ext: [ yaml, yml, json ]'
# string = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template for deploying a single server with predefined properties.\n\ntopology_template:\n  inputs:\n    cpus:\n      type: integer\n      description: Number of CPUs for the server.\n      constraints:\n        - valid_values: [ 1, 2, 4, 8 ]\n\n  node_templates:\n    my_server:\n      type: tosca.nodes.Compute\n      capabilities:\n        # Host container properties\n        host:\n          properties:\n            # Compute properties\n            num_cpus: { get_input: cpus }\n            mem_size: 2048  MB\n            disk_size: 10 GB'

# from io import StringIO

# print(string)
# yml = StringIO(string.expandtabs(2)) 
# metric = NKEYS(yml)

# print('NKEYS count: ', metric.count())