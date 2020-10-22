from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscametrics.utils import keyValueList
from toscametrics.metrics.ninp import NINP
from io import StringIO

class NINPC(BlueprintMetric):
    """ This class is responsible for providing the methods to count the relative number of input constraints per input defined in a given .yaml file"""


    def count(self):
        '''Function which counts the number of input constraints in a topology template'''
        
        try:
            strio = StringIO(self.getStringIOobject)
            inputs = NINP(strio)._get_elements()

            constraints = []
            for input in inputs:
                constraints = [kv[1] for kv in keyValueList(input) if kv[0] == 'constraints']
                constraints = [item for sublist in constraints for item in sublist]
                constraints.append(constraints)

            constraint_count = [len(cpi.keys()) for cpi in constraints if isinstance(cpi, dict)]
            return sum(constraint_count)

        except (KeyError, AttributeError):
            return []   



# from io import StringIO
# string = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template for deploying a single server with predefined properties.\n\ntopology_template:\n  inputs:\n    cpus:\n      type: integer\n      description: Number of CPUs for the server.\n      constraints:\n        - valid_values: [ 1, 2, 4, 8 ]\n        - less_than: 10'
# print(string)
# yml = StringIO(string.expandtabs(2)) 
# metric = NINPC(yml)

# print('NINPC count: ', metric.count())

