from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscametrics.yml.loc import LOC
from toscametrics.yml.etp import ETP

from io import StringIO

class CDDT(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of custom defined data types in a given .yaml file"""

    def _get_elements(self):
        '''Function which collects all the custom data type definitions in the service template with their attributes in a list'''
        try:
            cd_data_types = self.getyml.get('data_types')

            data_defs = []
            for data_name, data_values in cd_data_types.items():
                data_defs.append({data_name : data_values})
            return data_defs

        except (KeyError, AttributeError):
            return []  



    def count(self):
        '''Function which counts the number of custom defined data types''' 
        try:
            datas_list = self._get_elements()

            names = []
            for datas in datas_list:
                names.extend(datas.keys())
            unique_names = set(names)

            return len(unique_names)

        except AttributeError:
            return 0   


    def relative(self):
        '''Count relative to the lines of code'''
        try:
            strio = StringIO(self.getStringIOobject)
            return self.count() / LOC(strio).count()

        except (KeyError, AttributeError, ZeroDivisionError):
            return 0


    def entropy(self):
        '''Counts the entropy for the _get_elements blocks'''
        try:
            strio = StringIO(self.getStringIOobject)

            block = {}
            for element in self._get_elements():
                if isinstance(element, dict):
                    block.update(element)
            
            return ETP(strio).count(custom=block)

        except (KeyError, AttributeError, ZeroDivisionError):
            return 0