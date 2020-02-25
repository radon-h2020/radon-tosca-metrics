from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscaparser.tosca_template import ToscaTemplate
from toscametrics.utils import keyValueList

class NINPC(BlueprintMetric):
    """ This class is responsible for providing the methods to count the relative number of input constraints per input defined in a given .yaml file"""
    
    # def count(self):
    #     '''Function which counts the number of relative input constraints'''
    #     try:
    #         template = ToscaTemplate(yaml_dict_tpl=self.getyml)
    #         inputs = template.inputs
    #         inputs_list = [input.name for input in inputs]
    #         consts = []
    #         for input in inputs:
    #             for constraint in input.constraints:
    #                 consts.append(constraint.constraint_key)
    #         return len(consts)/len(inputs_list)
    #     except (AttributeError, TypeError, ZeroDivisionError):
    #         return 0



    def count(self):
        '''Function which counts the number of input constraints in a topology template'''
        try:
            template = self.getyml.get('topology_template')
            kvlist = keyValueList(template)
            inputs = []
            consts = []
            for kv in kvlist:
                if kv[0] == 'inputs':
                    for input, values in kv[1].items():
                        inputs.append(input)
                        if 'constraints' in values.keys():
                            consts.append(len(values.get('constraints')))              
            return sum(consts)/len(inputs)
        
        except (AttributeError, ZeroDivisionError):
            return 0





# from io import StringIO

# string = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template for deploying a single server with predefined properties.\n\ntopology_template:\n  inputs:\n    cpus:\n      type: integer\n      description: Number of CPUs for the server.\n      constraints:\n        - valid_values: [ 1, 2, 4, 8 ]\n        - less_than: 10'
# print(string)
# yml = StringIO(string.expandtabs(2)) 
# metric = NINPC(yml)

# print('NINPC count: ', metric.count())

