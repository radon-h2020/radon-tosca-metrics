from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscametrics.general.loc import LOC
from toscametrics.general.etp import ETP

from io import StringIO

class CDCT(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of custom defined capability types in a given .yaml file"""

    def _get_elements(self):
        '''Function which collects all the custom capability type definitions in the service template with their attributes in a list'''
        try:
            cd_capability_types = self.getyml.get('capability_types')

            cap_defs = []
            for cap_name, cap_values in cd_capability_types.items():
                cap_defs.append({cap_name : cap_values})
            return cap_defs

        except (KeyError, AttributeError):
            return []  



    def count(self):
        '''Function which counts the number of custom defined artifact types''' 
        try:
            caps_list = self._get_elements()

            names = []
            for caps in caps_list:
                names.extend(caps.keys())
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