from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscametrics.utils import getRelationshipTypes
from toscametrics.utils import getNodeTypes
from toscametrics.utils import keyValueList
from toscametrics.metrics.cdnt import CDNT
from toscametrics.metrics.cdrt import CDRT
from toscametrics.metrics.nn import NN
from toscametrics.metrics.nr import NR
import re
from io import StringIO

class NCYS(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of yaml calls in a given .yaml file"""
    
    def count(self):
        '''Checks for the number of yaml calls within node templates, relationship templates, 
        node type definitions and relationship definitions'''
        
        try:
            strio = StringIO(self.getStringIOobject)
            
            options = [
                CDNT(strio)._get_elements(),
                CDRT(strio)._get_elements(),
                NN(strio)._get_elements(),
                NR(strio)._get_elements()
            ]

            calls = []
            for option in options:
                for element in option:
                    for _, element_values in element.items():

                        splitted_dict = keyValueList(element_values)
                        operands = [re.findall(r'.yaml|.general', tup[1]) for tup in splitted_dict if isinstance(tup[1], str)]
                        flattern = [item for sublist in operands for item in sublist]
                        calls.extend(flattern)

            return len(calls)

        except:
            return 0




# string = 'tosca_definitions_version: alien_dsl_2_0_0\n\nnode_types:\n  org.ystia.ntp.ansible.nodes.NtpServer:\n    derived_from: org.ystia.ntp.pub.nodes.NtpServer\n    interfaces:\n      Standard:\n        create: playbooks/create.yaml\n        configure:\n          inputs:\n            TYPE: "server"\n          implementation: playbooks/configure.yaml\n        start: playbooks/start.yaml\n        stop: playbooks/stop.yaml'

# from io import StringIO

# # path = r'C:\Users\s145559\OneDrive - TU Eindhoven\School\JADS\Jaar 2\Thesis\RADON PROJECT\GIT projects\ANALYSIS\dataminer\tmp\openstack\tosca-parser\Example\node_with_cap.yaml'
# # from io import StringIO

# # with open(path, 'r') as file:
# #     string = file.read()

# print(string)

# general = StringIO(string.expandtabs(2))
# metric = NCYS(general)

# print('NCYS count: ', metric.count())
