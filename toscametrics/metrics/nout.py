from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscametrics.utils import getOutputs

class NOUT(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of outputs defined in a given .yaml file"""
    
    # def count(self):
    #     '''Function which counts the number of outputs'''
    #     try:
    #         template = ToscaTemplate(yaml_dict_tpl=self.getyml)
    #         outputs = template.outputs
    #         return len([output.name for output in outputs])
    #     except AttributeError:
    #         return 0



    def _get_elements(self):
        '''Function which collects all the outputs with their attributes in a list'''
        try:
            template = self.getyml     
            outputs = getOutputs(template)

            output_list = []
            for output in outputs:
                if isinstance(output, dict):
                    output_list.append(output)
                else:
                    continue
            return output_list

        except (KeyError, AttributeError):
            return []   

    def count(self):
        '''Function which counts the number of outputs in a given .yaml file'''
        try:
            output_list = self._get_elements()

            outputs = []
            for output in output_list:
                outputs.extend(output.keys())

            unique_outputs = set(outputs)
            return len(unique_outputs)
        
        except AttributeError:
            return 0
        

# from io import StringIO

# str = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ntopology_template:\n  description: Template of a database including its hosting stack.\n\n  inputs:\n    mq_service_ip:\n      type: string\n      description: IP address of the message queuing server to receive messages from\n    receiver_port:\n      type: string\n      description: Port to be used for receiving messages \n\n  outputs:\n    receiver_ip:\n      description: private IP address of the message receiver application\n      value: { get_attribute: [ server, private_address ] }\n    receiver_port:\n      description: Port of the message receiver endpoint\n      value: { get_attribute: [ app, app_endpoint, port ] }\n'
# #str = 'tosca_definitions_version: alien_dsl_2_0_0\n#\n# Copyright 2018 Bull S.A.S. Atos Technologies - Bull, Rue Jean Jaures, B.P.68, 78340, Les Clayes-sous-Bois, France.\n#\n# Licensed under the Apache License, Version 2.0 (the "License");\n# you may not use this file except in compliance with the License.\n# You may obtain a copy of the License at\n#\n#     http://www.apache.org/licenses/LICENSE-2.0\n#\n# Unless required by applicable law or agreed to in writing, software\n# distributed under the License is distributed on an "AS IS" BASIS,\n# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n# See the License for the specific language governing permissions and\n# limitations under the License.\n#\n\nmetadata:\n  template_name: org.ystia.nfs.pub\n  template_version: 2.2.0-SNAPSHOT\n  template_author: yorc\n\nimports:\n  - tosca-normative-types:1.0.0-ALIEN20\n  - alien-extended-storage-types:2.2.0-SM6\n\nnode_types:\n  org.ystia.nfs.pub.nodes.NFSServer:\n    derived_from: tosca.nodes.SoftwareComponent\n    tags:\n      icon: nfs.png\n    abstract: true\n    capabilities:\n      nfs_server:\n        type: org.ystia.nfs.pub.capabilities.NFSServer\n\n  org.ystia.nfs.pub.nodes.NFSClient:\n    derived_from: alien.nodes.LinuxFileSystem\n    tags:\n      icon: nfs.png\n    abstract: true\n    requirements:\n      - partition:\n          capability: org.ystia.nfs.pub.capabilities.NFSServer\n          occurrences: [1, 1]\n\ncapability_types:\n  org.ystia.nfs.pub.capabilities.NFSServer:\n    derived_from: tosca.capabilities.Endpoint\n\nrelationship_types:\n  org.ystia.nfs.pub.relationships.JoinNFSServer:\n    derived_from: tosca.relationships.ConnectsTo\n    description: >\n      Joins to a NFS Server\n    valid_target_types: [ org.ystia.nfs.pub.capabilities.NFSServer ]\n'
# print(str)
# general = StringIO(str.expandtabs(2))
# metric = NOUT(general)
# print(metric.count())

# print('NOUT count: ', metric.count())
