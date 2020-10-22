from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscametrics.yml.loc import LOC
from toscametrics.yml.etp import ETP

from io import StringIO

class CDAT(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of custom defined artifact types in a given .yaml file"""

    def _get_elements(self):
        '''Function which collects all the custom artifact type definitions in the service template with their attributes in a list'''
        try:
            cd_artifact_types = self.getyml.get('artifact_types')

            art_defs = []
            for art_name, art_values in cd_artifact_types.items():
                art_defs.append({art_name : art_values})
            return art_defs

        except (KeyError, AttributeError):
            return []  



    def count(self):
        '''Function which counts the number of custom defined artifact types''' 
        try:
            arts_list = self._get_elements()

            names = []
            for arts in arts_list:
                names.extend(arts.keys())
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





# #string = 'tosca_definitions_version: tosca_simple_yaml_1_3\ncapability_types:\n  radon.capabilities.kafka.KafkaHosting:\n    derived_from: tosca.capabilities.Container\n'
# string = "tosca_definitions_version: tosca_simple_yaml_1_3\n\nartifact_types:\n\n  tosca.artifacts.Root:\n    metadata:\n      normative: 'true'\n      citation: '[TOSCA-Simple-Profile-YAML-v1.3]'\n      citation_location: 5.4.1\n    description: >-\n      This is the default (root) TOSCA Artifact Type definition that all other TOSCA base Artifact\n      Types derive from.\n      \n  tosca.artifacts.GEENROOT:\n    metadata:\n      normative: 'true'\n      citation: '[TOSCA-Simple-Profile-YAML-v1.3]'\n      citation_location: 5.4.1\n    description: >-\n      This is the default (root) TOSCA Artifact Type definition that all other TOSCA base Artifact\n      Types derive from."
# # path = r'C:\Users\s145559\OneDrive - TU Eindhoven\School\JADS\Jaar 2\Thesis\RADON PROJECT\GIT projects\ANALYSIS\dataminer\tmp\openstack\tosca-parser\Example\node_with_cap.yaml'
# # from io import StringIO

# # with open(path, 'r') as file:
# #     string = file.read()

# print(string)
# yml = StringIO(string.expandtabs(2)) 
# metric = CDAT(yml)

# # print('CDAT count: ', metric.count())
# metric.entropy()

