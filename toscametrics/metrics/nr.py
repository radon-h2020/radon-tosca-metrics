from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscametrics.utils import getRelationshipTemplates
from toscametrics.yml.loc import LOC
from toscametrics.yml.etp import ETP

from io import StringIO


class NR(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of relationship templates defined in a given .yaml file"""
    
    def _get_elements(self):
        '''Function which collects all the relationships in the relationship templates with their attributes in a list'''
        try:
            template = self.getyml     
            relationship_templates = getRelationshipTemplates(template)

            relationships = []
            for relationship_template in relationship_templates:
                if isinstance(relationship_template, dict):
                    for rel_name, rel_values in relationship_template.items():
                        relationships.append({rel_name : rel_values})
                else:
                    continue
            return relationships

        except (KeyError, AttributeError):
            return []     


    def count(self):
        '''Function which counts the number of defined relationships in a relationship template''' 
        try:
            relationships_list = self._get_elements()

            names = []
            for relationships in relationships_list:
                names.extend(relationships.keys())
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



# path = r'C:\Users\s145559\OneDrive - TU Eindhoven\School\JADS\Jaar 2\Thesis\RADON PROJECT\Data\Repositories\A4C\Example\test-types.yml'
# from io import StringIO

# with open(path, 'r') as file:
#             yml = file.read()
#             print(yml)

# yml = StringIO(yml) 
# metric = NR(yml)

# print('NR count: ', metric.count())