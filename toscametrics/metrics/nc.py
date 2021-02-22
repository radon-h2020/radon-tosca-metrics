from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscametrics.utils import getCapabilities
from toscametrics.metrics.nn import NN
from toscametrics.metrics.cdnt import CDNT
from statistics import mean
from statistics import median
from io import StringIO

class NC(BlueprintMetric):
    """ This class is responsible for providing the methods to count the total number of capabilities, provide the minimum number per node, the maximum number per node, the mean and median defined in a given .yaml file"""

    def _get_elements(self):
        '''Function which collects all the capabilities in the node templates and node types with their attributes in a list'''
        
        try:
            strio = StringIO(self.getStringIOobject)
            nodes = NN(strio)._get_elements()
            custom_nodes = CDNT(strio)._get_elements()

            node_caps = []
            for node in nodes:
                caps_lists = getCapabilities(node)

                if len(caps_lists) == 0:
                    node_caps.append({list(node.keys())[0] : 0})
                    continue

                if isinstance(caps_lists[0], list):
                    caps_lists = [item for sublist in caps_lists for item in sublist]
                
                caps_dict = {}
                for cap in caps_lists:
                    try:
                        if isinstance(cap, str):
                            caps_dict.update({cap : None})

                        elif isinstance(cap, list):
                            for element in cap:
                                caps_dict.update(element)

                        else:
                            caps_dict.update(cap)
                    
                    except:
                        continue
                
                node_caps.append({list(node.keys())[0] : caps_dict})

            for node in custom_nodes:
                caps_lists = getCapabilities(node)

                if len(caps_lists) == 0:
                    node_caps.append({list(node.keys())[0] : 0})
                    continue
                
                if isinstance(caps_lists[0], list):
                    caps_lists = [item for sublist in caps_lists for item in sublist]
                
                caps_dict = {}
                for cap in caps_lists:
                    try:
                        if isinstance(cap, str):
                            caps_dict.update({cap : None})

                        elif isinstance(cap, list):
                            for element in cap:
                                caps_dict.update(element)

                        else:
                            caps_dict.update(cap)
                    
                    except:
                        continue
                
                node_caps.append({list(node.keys())[0] : caps_dict})

            return node_caps

        except (KeyError, AttributeError):
            return []  


    def count(self):
        try:
            node_caps = self._get_elements()

            names = []
            for node in node_caps:
                for _, caps in node.items():
                    if isinstance(caps, dict):
                        names.extend(caps.keys())
            unique_names = set(names)

            return len(unique_names)

        except (ValueError, AttributeError):
            return 0 

    def min(self):   
        try:
            node_caps = self._get_elements()
            
            names = []
            for node in node_caps:
                for _, caps in node.items():
                    if isinstance(caps, dict):
                        names.append(len(caps.keys()))
                    else:
                        names.append(0)

            return min(names)

        except (ValueError, AttributeError):
            return 0 

    def max(self):
        try:
            node_caps = self._get_elements()
            
            names = []
            for node in node_caps:
                for _, caps in node.items():
                    if isinstance(caps, dict):
                        names.append(len(caps.keys()))
                    else:
                        names.append(0)


            return max(names)

        except (ValueError, AttributeError):
            return 0 

    def mean(self):
        try:
            node_caps = self._get_elements()
            
            names = []
            for node in node_caps:
                for _, caps in node.items():
                    if isinstance(caps, dict):
                        names.append(len(caps.keys()))
                    else:
                        names.append(0)


            return mean(names)

        except (ValueError, AttributeError):
            return 0 

    def median(self):
        try:
            node_caps = self._get_elements()
            
            names = []
            for node in node_caps:
                for _, caps in node.items():
                    if isinstance(caps, dict):
                        names.append(len(caps.keys()))
                    else:
                        names.append(0)


            return median(names)

        except (ValueError, AttributeError):
            return 0 




#from io import StringIO


# #str = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template with requirements against hosting infrastructure.\n\ntopology_template:\n  inputs:\n    # omitted here for brevity\n    \n  node_templates:\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        # omitted here for brevity\n        \n      requirements:\n        - host: mysql_compute\n        \n    # Abstract node template (placeholder) to be selected by provider\n    mysql_compute:\n      type: Compute\n      node_filter:\n        capabilities:\n          - host:\n              properties:\n                num_cpus: { equal: 2 }\n                mem_size: { greater_or_equal: 2 GB }\n          - os:\n              properties:\n                architecture: { equal: x86_64 }\n                type: linux\n                distribution: ubuntu'
#str = 'tosca_definitions_version: tosca_simple_yaml_1_0\ndescription: Template with requirements against hosting infrastructure.\n\ntopology_template:\n  inputs:\n    # omitted here for brevity\n\n  node_templates:\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        root_password: { get_input: my_mysql_rootpw }\n        port: { get_input: my_mysql_port }\n      requirements:\n        - host:\n            node_filter:\n              capabilities:\n                - host:\n                    properties:\n                      - num_cpus: { in_range: [ 1, 4 ] }\n                      - mem_size: { greater_or_equal: 2 GB }\n                - os:\n                    properties:\n                      - architecture: { equal: x86_64 }\n                      - type: linux\n                      - distribution: ubuntu\n                - backup_os:\n                    properties:\n                      - architecture: { equal: x86_64 }\n                      - type: linux\n                      - distribution: ubuntu\n                      \n    backup_mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        # omitted here for brevity\n      requirements:\n        - host:\n            node_filter:\n              capabilities:\n                - hostssssss:\n                    properties:\n                      - num_cpus: { in_range: [ 1, 4 ] }\n                      - mem_size: { greater_or_equal: 2 GB }\n                - osssss:\n                    properties:\n                      - architecture: { equal: x86_64 }\n                      - type: linux\n                      - distribution: ubuntu'
#str = 'tosca_definitions_version: alien_dsl_2_0_0\n#\n# Copyright 2018 Bull S.A.S. Atos Technologies - Bull, Rue Jean Jaures, B.P.68, 78340, Les Clayes-sous-Bois, France.\n#\n# Licensed under the Apache License, Version 2.0 (the "License");\n# you may not use this file except in compliance with the License.\n# You may obtain a copy of the License at\n#\n#     http://www.apache.org/licenses/LICENSE-2.0\n#\n# Unless required by applicable law or agreed to in writing, software\n# distributed under the License is distributed on an "AS IS" BASIS,\n# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n# See the License for the specific language governing permissions and\n# limitations under the License.\n#\n\nmetadata:\n  template_name: org.ystia.nfs.pub\n  template_version: 2.2.0-SNAPSHOT\n  template_author: yorc\n\nimports:\n  - tosca-normative-types:1.0.0-ALIEN20\n  - alien-extended-storage-types:2.2.0-SM6\n\nnode_types:\n  org.ystia.nfs.pub.nodes.NFSServer:\n    derived_from: tosca.nodes.SoftwareComponent\n    tags:\n      icon: nfs.png\n    abstract: true\n    capabilities:\n      nfs_server:\n        type: org.ystia.nfs.pub.capabilities.NFSServer\n\n  org.ystia.nfs.pub.nodes.NFSClient:\n    derived_from: alien.nodes.LinuxFileSystem\n    tags:\n      icon: nfs.png\n    abstract: true\n    requirements:\n      - partition:\n          capability: org.ystia.nfs.pub.capabilities.NFSServer\n          occurrences: [1, 1]\n\ncapability_types:\n  org.ystia.nfs.pub.capabilities.NFSServer:\n    derived_from: tosca.capabilities.Endpoint\n\nrelationship_types:\n  org.ystia.nfs.pub.relationships.JoinNFSServer:\n    derived_from: tosca.relationships.ConnectsTo\n    description: >\n      Joins to a NFS Server\n    valid_target_types: [ org.ystia.nfs.pub.capabilities.NFSServer ]\n'

#str = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\nimports:\n  - paypalpizzastore_nodejs_app.yaml'
#str = 'tosca_definitions_version: tosca_simple_yaml_1_0\ndescription: Template with requirements against hosting infrastructure.\n\ntopology_template:\n  inputs:\n    # omitted here for brevity\n\n  node_templates:\n     \n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        # omitted here for brevity\n      requirements:\n        - host:\n            node_filter:\n              capabilities:\n                - host:\n                    properties:\n                      - num_cpus: { in_range: [ 1, 4 ] }\n                      - mem_size: { greater_or_equal: 2 GB }\n                - os:\n                    properties:\n                      - architecture: { equal: x86_64 }\n                      - type: linux\n                      - distribution: ubuntu'
#str = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template with requirements against hosting infrastructure.\n\ntopology_template:\n  inputs:\n    # omitted here for brevity\n    \n  node_templates:\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        # omitted here for brevity\n        \n      requirements:\n        - host: mysql_compute\n        \n    # Abstract node template (placeholder) to be selected by provider\n    mysql_compute:\n      type: Compute\n      node_filter:\n        capabilities:\n          - host:\n              properties:\n                num_cpus: { equal: 2 }\n                mem_size: { greater_or_equal: 2 GB }\n          - os:\n              properties:\n                architecture: { equal: x86_64 }\n                type: linux\n                distribution: ubuntu'
#str = 'tosca_definitions_version: tosca_simple_yaml_1_0\ndescription: Template with requirements against hosting infrastructure.\n\ntopology_template:\n  inputs:\n    # omitted here for brevity\n\n  node_templates:\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        # omitted here for brevity\n      requirements:\n        - host:\n            node_filter:\n              capabilities:\n                - host:\n                    properties:\n                      - num_cpus: { in_range: [ 1, 4 ] }\n                      - mem_size: { greater_or_equal: 2 GB }\n                - os:\n                    properties:\n                      - architecture: { equal: x86_64 }\n                      - type: linux\n                      - distribution: ubuntu\n                - backup_os:\n                    properties:\n                      - architecture: { equal: x86_64 }\n                      - type: linux\n                      - distribution: ubuntu\n                      \n    backup_mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        # omitted here for brevity\n      requirements:\n        - host:\n            node_filter:\n              capabilities:\n                - host:\n                    properties:\n                      - num_cpus: { in_range: [ 1, 4 ] }\n                      - mem_size: { greater_or_equal: 2 GB }\n                - os:\n                    properties:\n                      - architecture: { equal: x86_64 }\n                      - type: linux\n                      - distribution: ubuntu'


# path = r'c:\Users\s145559\OneDrive - TU Eindhoven\School\JADS\Jaar 2\Thesis\RADON PROJECT\GIT projects\ANALYSIS\dataminer\tmp\QualiSystems\Toscana\Industry\Toscana.ToscaPropertyDefinition.general'

# with open(path, 'r', encoding='utf-8') as file:
#     string = file.read()


# print(string)
# general = StringIO(string.expandtabs(2))
# metric = NC(general)
# #print(metric.getyml)
# print('count: ', metric.count())
# # print('min: ', metric.min())
# # print('max: ', metric.max())
# # print('mean: ', metric.mean())
# # print('median: ', metric.median())
# # print('get elements: ', metric._get_elements())
# #x = metric._get_elements()

