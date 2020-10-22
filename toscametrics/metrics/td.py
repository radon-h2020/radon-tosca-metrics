from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscametrics.metrics.nn import NN
from toscametrics.metrics.nr import NR
from toscametrics.metrics.npol import NPOL
from toscametrics.metrics.ngro import NGRO

from toscametrics.metrics.cdnt import CDNT
from toscametrics.metrics.cdrt import CDRT
from toscametrics.metrics.cdat import CDAT
from toscametrics.metrics.cdpt import CDPT
from toscametrics.metrics.cdgt import CDGT
from toscametrics.metrics.cdct import CDCT
from toscametrics.metrics.cdit import CDIT

from statistics import mean
from statistics import median
from io import StringIO

class TD(BlueprintMetric):
    """ This class is responsible for providing the methods to measure the type depths in a given .yaml file"""

    def __strip_types(self, type, identifier):
        splitted_type = type.split('.')

        if identifier in splitted_type:
            ix = splitted_type.index(identifier)

            try:
                splitted_type = splitted_type[ix+1:]
            except IndexError:
                pass

        return len(splitted_type)

    def _get_elements(self):
        '''Function which filters the depths for all types within the whole script'''
        
        types = []

        strio = StringIO(self.getStringIOobject)

        ass_options = {
            'nodes' : NN(strio)._get_elements(),
            'relationships' : NR(strio)._get_elements(),
            'policies' : NPOL(strio)._get_elements(),
            'groups' : NGRO(strio)._get_elements()
        }

        def_options = {
            'nodes' : CDNT(strio)._get_elements(),
            'relationships' : CDRT(strio)._get_elements(),
            'artifacts' : CDAT(strio)._get_elements(),
            'policies' : CDPT(strio)._get_elements(),
            'groups' : CDGT(strio)._get_elements(),
            'capabilities' : CDCT(strio)._get_elements(),
            'interfaces' : CDIT(strio)._get_elements()
        }
        

        for identifier, elements in ass_options.items():
            
            ass_types = []
            try:
                for element in elements:
                    for _, element_values in element.items():

                        if element_values.get('type'):
                            ass_types.append(element_values.get('type'))
                        
                        else:
                            continue

                stripped_types = [self.__strip_types(type, identifier) for type in ass_types]
                types.extend(stripped_types)

            except:
                pass
        
        for identifier, elements in def_options.items():

            def_types = []
            try:
                for element in elements:
                    for name, element_values in element.items():

                        if identifier in name:
                            def_types.append(name)

                        elif element_values.get('derived_from'):
                            def_types.append(element_values.get('derived_from'))
                        
                        else:
                            def_types.append(name)
                
                stripped_types = [self.__strip_types(type, identifier) for type in def_types]
                types.extend(stripped_types)

            except:
                pass

        return types


    # def count(self):
    #     try:
    #         list_of_types = self._get_elements()
    #         return sum(list_of_types)
    #     except (AttributeError, ValueError):
    #         return 0

    def min(self):
        try:
            list_of_types = self._get_elements()
            return min(list_of_types)
        except (AttributeError, ValueError):
            return 0

    def max(self):
        try:
            list_of_types = self._get_elements()
            return max(list_of_types)
        except (AttributeError, ValueError):
            return 0

    def mean(self):
        try:
            list_of_types = self._get_elements()
            return mean(list_of_types)
        except (AttributeError, ValueError):
            return 0

    def median(self):
        try:
            list_of_types = self._get_elements()
            return median(list_of_types)
        except (AttributeError, ValueError):
            return 0




# path = r'C:\Users\s145559\OneDrive - TU Eindhoven\School\JADS\Jaar 2\Thesis\RADON PROJECT\GIT projects\ANALYSIS\dataminer\tmp\NSO-developer\nfvo-converter-tosca-sol6\Example\Tosca_vPE.yaml'
# #path = r'C:\Users\s145559\OneDrive - TU Eindhoven\School\JADS\Jaar 2\Thesis\RADON PROJECT\GIT projects\ANALYSIS\dataminer\tmp\radon-h2020\radon-particles\Industry\ServiceTemplate.yaml'
# #path = r'C:\Users\s145559\OneDrive - TU Eindhoven\School\JADS\Jaar 2\Thesis\RADON PROJECT\GIT projects\ANALYSIS\dataminer\tmp\ystia\forge\Industry\types_12.yml'
# #path = r'C:\Users\s145559\OneDrive - TU Eindhoven\School\JADS\Jaar 2\Thesis\RADON PROJECT\GIT projects\ANALYSIS\dataminer\tmp\tliron\puccini\Industry\relationships_3.yaml'
# with open(path, 'r') as file:
#     string = file.read()

# #string = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\nnode_types:\n\n  tosca.nodes.Root:\n    attributes:\n      tosca_id:\n        type: string\n      tosca_name:\n        type: string\n\n  tosca.nodes.Abstract.Compute:\n    derived_from: tosca.nodes.Root\n    capabilities:\n      host:\n        type: tosca.capabilities.Compute\n\n  tosca.nodes.Compute:\n    attributes:\n      private_address:\n        type: string\n      public_address:\n        type: string\n'
# print(string)
# yml = StringIO(string.expandtabs(2)) 
# metric = TD(yml)
# print('min: ', metric.min())
# print('max: ', metric.max())
# print('mean: ', metric.mean())
# print('median: ', metric.median())
