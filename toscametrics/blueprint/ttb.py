from toscametrics.blueprint.blueprint_metric import BlueprintMetric

class TTB(BlueprintMetric):
    """ This class is responsible for providing the methods to check whether or not a topology template is defined in a given .yaml file"""
    
    def check(self):
        try:
            template = self.getyml.get('topology_template')

            if template:
                return True
            else:
                return False
            
        except AttributeError:
            return False      



# #str = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ntopology_template:\n  relationship_templates:\n    storage_attachesto_1:\n      type: MyAttachesTo\n      properties:\n        location: /my_data_location\n\n    storage_attachesto_2:\n      type: MyAttachesTo\n      properties:\n        location: /some_other_data_location\n    \n    my_connectsto_relationship:\n      type: tosca.relationships.ConnectsTo\n      interfaces:\n        Configure:\n          inputs:\n            speed: { get_attribute: [ SOURCE, connect_speed ] }  \n\n  relationship_types:\n    MyAttachesTo:\n      derived_from: AttachesTo\n      interfaces:\n        some_interface_name:\n          some_operation:\n            implementation: default_script.sh\n'
# #str = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\nartifact_types:\n\n  kubernetes.Spec:\n    description: >-\n      Object specification\n    derived_from: tosca.artifacts.Root\n    file_ext: [ yaml, general, json ]'
# str = 'tosca_definitions_version: alien_dsl_2_0_0\n\n#\n# Ystia Forge\n# Copyright (C) 2018 Bull S. A. S. - Bull, Rue Jean Jaures, B.P.68, 78340, Les Clayes-sous-Bois, France.\n# Use of this source code is governed by Apache 2 LICENSE that can be found in the LICENSE file.\n#\n\nmetadata:\n  template_name: org.ystia.logstash.pub\n  template_version: 2.2.0-SNAPSHOT\n  template_author: Ystia\n\ndescription: Public interface types for Logstash support.\n\nimports:\n  - tosca-normative-types:1.0.0-ALIEN20\n  - org.ystia.common:2.2.0-SNAPSHOT\n\ncapability_types:\n  org.ystia.logstash.pub.capabilities.LogstashEndpoint:\n    derived_from: tosca.capabilities.Endpoint\n\n  org.ystia.logstash.pub.capabilities.LogstashConnectorHosting:\n    derived_from: tosca.capabilities.Container\n\n  org.ystia.logstash.pub.capabilities.GeonamesEndpoint:\n    derived_from: tosca.capabilities.Endpoint\n'



# from io import StringIO

# print(str)
# general = StringIO(str.expandtabs(2))
# metric = TTB(general)

# print('check: ', metric.check())
