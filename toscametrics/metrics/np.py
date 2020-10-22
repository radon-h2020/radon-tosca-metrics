from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscametrics.utils import getCapabilities
from toscametrics.utils import getProperties

from toscametrics.metrics.cdat import CDAT
from toscametrics.metrics.cdct import CDCT
from toscametrics.metrics.cddt import CDDT
from toscametrics.metrics.cdgt import CDGT
from toscametrics.metrics.cdnt import CDNT
from toscametrics.metrics.cdpt import CDPT
from toscametrics.metrics.cdrt import CDRT
from toscametrics.metrics.na import NA
from toscametrics.metrics.nn import NN
from toscametrics.metrics.nc import NC
from toscametrics.metrics.nr import NR
from toscametrics.metrics.nrq import NRQ
from toscametrics.metrics.npol import NPOL
from toscametrics.metrics.ngro import NGRO

from statistics import mean
from statistics import median
from io import StringIO

class NP(BlueprintMetric):
    """ This class is responsible for providing the methods to count the total number of capability properties, provide the minimum number per capability, the maximum number per entity, the mean and median defined in a given .yaml file"""

    def _get_elements(self, option=False):

        #ALS OPTION BEPAALDE METRIC DAN ALLEEN DIE MEENEMEN, ANDERS ALLEMAAL! 
        #WEL ALLEMAAL IN DEZE FUNCTIE VOOR LATER

        strio = StringIO(self.getStringIOobject)

        #Only the top keys are included, otherwise properties are counted double
        options = [
            CDAT(strio)._get_elements(),
            CDCT(strio)._get_elements(),
            CDGT(strio)._get_elements(),
            CDNT(strio)._get_elements(),
            CDPT(strio)._get_elements(),
            CDRT(strio)._get_elements(),
            NA(strio)._get_elements(),
            NN(strio)._get_elements(),
            NR(strio)._get_elements(),
            #NRQ(strio)._get_elements(),
            #NC(strio)._get_elements(),
            NPOL(strio)._get_elements(),
            NGRO(strio)._get_elements()
        ]
               
        props = []
        for option in options:

            try:
            
                if option != NC(strio)._get_elements():
                    for element in option:
                        element_props = getProperties(element)
                        props_per_element = [len(props) for props in element_props]
                        props.append(sum(props_per_element))
                
                if option == NC(strio)._get_elements():
                    #For NC ff een aparte schrijven, die werkt niet op deze
                    #Wrs ook niet voor requirements
                    pass
            
            except:
                continue

        return props


    def count(self):
        try:
            list_of_properties = self._get_elements()
            return sum(list_of_properties)
        except (AttributeError, ValueError):
            return 0

    def min(self):
        try:
            list_of_properties = self._get_elements()
            return min(list_of_properties)
        except (AttributeError, ValueError):
            return 0

    def max(self):
        try:
            list_of_properties = self._get_elements()
            return max(list_of_properties)
        except (AttributeError, ValueError):
            return 0

    def mean(self):
        try:
            list_of_properties = self._get_elements()
            return mean(list_of_properties)
        except (AttributeError, ValueError):
            return 0

    def median(self):
        try:
            list_of_properties = self._get_elements()
            return median(list_of_properties)
        except (AttributeError, ValueError):
            return 0



# from io import StringIO

# #string = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template with requirements against hosting infrastructure.\n\ntopology_template:\n  inputs:\n    # omitted here for brevity\n    \n  node_templates:\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        - hiergebeurtiets\n        \n      requirements:\n        - host: mysql_compute\n        \n    # Abstract node template (placeholder) to be selected by provider\n    mysql_compute:\n      type: Compute\n      node_filter:\n        capabilities:\n          - host:\n              properties:\n                num_cpus: { equal: 2 }\n                mem_size: { greater_or_equal: 2 GB }\n          - os:\n              properties:\n                architecture: { equal: x86_64 }\n                type: linux\n                distribution: ubuntu'
# #string = 'tosca_definitions_version: tosca_simple_yaml_1_0\ndescription: Template with requirements against hosting infrastructure.\n\ntopology_template:\n  inputs:\n    # omitted here for brevity\n\n  node_templates:\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        root_password: { get_input: my_mysql_rootpw }\n        port: { get_input: my_mysql_port }\n      requirements:\n        - host:\n            node_filter:\n              capabilities:\n                database_endpoint: [ database, database_endpoint ]\n                      \n    backup_mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        # omitted here for brevity\n      requirements:\n        - host:\n            node_filter:\n              capabilities:\n                - host:\n                    properties:\n                      - num_cpus: { in_range: [ 1, 4 ] }\n                      - mem_size: { greater_or_equal: 2 GB }\n                - os:\n                    properties:\n                      - architecture: { equal: x86_64 }\n                      - type: linux\n                      - distribution: ubuntu'

# #string = 'tosca_definitions_version: alien_dsl_2_0_0\n#\n# Copyright 2018 Bull S.A.S. Atos Technologies - Bull, Rue Jean Jaures, B.P.68, 78340, Les Clayes-sous-Bois, France.\n#\n# Licensed under the Apache License, Version 2.0 (the "License");\n# you may not use this file except in compliance with the License.\n# You may obtain a copy of the License at\n#\n#     http://www.apache.org/licenses/LICENSE-2.0\n#\n# Unless required by applicable law or agreed to in writing, software\n# distributed under the License is distributed on an "AS IS" BASIS,\n# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n# See the License for the specific language governing permissions and\n# limitations under the License.\n#\n\nmetadata:\n  template_name: org.ystia.nfs.pub\n  template_version: 2.2.0-SNAPSHOT\n  template_author: yorc\n\nimports:\n  - tosca-normative-types:1.0.0-ALIEN20\n  - alien-extended-storage-types:2.2.0-SM6\n\nnode_types:\n  org.ystia.nfs.pub.nodes.NFSServer:\n    derived_from: tosca.nodes.SoftwareComponent\n    tags:\n      icon: nfs.png\n    abstract: true\n    capabilities:\n      nfs_server:\n        type: org.ystia.nfs.pub.capabilities.NFSServer\n\n  org.ystia.nfs.pub.nodes.NFSClient:\n    derived_from: alien.nodes.LinuxFileSystem\n    tags:\n      icon: nfs.png\n    abstract: true\n    requirements:\n      - partition:\n          capability: org.ystia.nfs.pub.capabilities.NFSServer\n          occurrences: [1, 1]\n\ncapability_types:\n  org.ystia.nfs.pub.capabilities.NFSServer:\n    derived_from: tosca.capabilities.Endpoint\n\nrelationship_types:\n  org.ystia.nfs.pub.relationships.JoinNFSServer:\n    derived_from: tosca.relationships.ConnectsTo\n    description: >\n      Joins to a NFS Server\n    valid_target_types: [ org.ystia.nfs.pub.capabilities.NFSServer ]\n'

# path = r'C:\Users\s145559\OneDrive - TU Eindhoven\School\JADS\Jaar 2\Thesis\RADON PROJECT\Data\All\All\requirements-and-capabilities.yaml'
# with open(path, 'r') as file:
#     string = file.read()

# print(string)
# yml = StringIO(string.expandtabs(2)) 
# metric = NP(yml)

# print('NP count: ', metric.count())
# print('NP min: ', metric.min())
# print('NP max: ', metric.max())
# print('NP mean: ', metric.mean())
# print('NP median: ', metric.median())
# #metric._get_elements()