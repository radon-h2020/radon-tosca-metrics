from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscaparser.tosca_template import ToscaTemplate
from toscametrics.tosca_versions import OFFICIAL_VERSIONS

class TOB(BlueprintMetric):
    """ This class is responsible for providing the method to check whether or not a tosca_definitions_version is official in a given .yaml file"""
    
    def check(self):
        '''Function which checks the existance of a tosca_definitions_version''' 
        try:
            tosca_df = self.getyml.get('tosca_definitions_version')
            if tosca_df in OFFICIAL_VERSIONS:
                return True
            return False
        
        except AttributeError:
            return False


# string = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ntopology_template:\n  relationship_templates:\n    storage_attachesto_1:\n      type: MyAttachesTo\n      properties:\n        location: /my_data_location\n\n    storage_attachesto_2:\n      type: MyAttachesTo\n      properties:\n        location: /some_other_data_location\n    \n    my_connectsto_relationship:\n      type: tosca.relationships.ConnectsTo\n      interfaces:\n        Configure:\n          inputs:\n            speed: { get_attribute: [ SOURCE, connect_speed ] }  \n\n  relationship_types:\n    MyAttachesTo:\n      derived_from: AttachesTo\n      interfaces:\n        some_interface_name:\n          some_operation:\n            implementation: default_script.sh\n'

# from io import StringIO

# yml = StringIO(string.expandtabs(2)) 
# metric = TOB(yml)

# print('check TOB: ', metric.check())
