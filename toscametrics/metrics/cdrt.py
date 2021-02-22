from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscametrics.general.loc import LOC
from toscametrics.general.etp import ETP

from io import StringIO

class CDRT(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of custom defined relationship types in a given .yaml file"""


    def _get_elements(self):
        '''Function which collects all the custom relationship type definitions in the service template with their attributes in a list'''
        try:
            cd_relationship_types = self.getyml.get('relationship_types')

            rel_defs = []
            for rel_name, rel_values in cd_relationship_types.items():
                rel_defs.append({rel_name : rel_values})
            return rel_defs

        except (KeyError, AttributeError):
            return []  



    def count(self):
        '''Function which counts the number of custom defined relationship types''' 
        try:
            rels_list = self._get_elements()

            names = []
            for rels in rels_list:
                names.extend(rels.keys())
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


# string = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\nrelationship_types:\n\n  tosca.relationships.Root:\n    attributes:\n      tosca_id:\n        type: string\n\n  tosca.relationships.DependsOn:\n    derived_from: tosca.relationships.Root\n    valid_target_types: [ tosca.capabilities.Node ]'
# from io import StringIO

# print(string)
# general = StringIO(string.expandtabs(2))
# metric = CDRT(general)

# print('CDRT count: ', metric.relative())