from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscametrics.utils import getNodeTemplates
from toscametrics.general.loc import LOC

from toscametrics.blueprint.na import NA
from toscametrics.blueprint.nn import NN
from toscametrics.blueprint.nr import NR
from toscametrics.blueprint.npol import NPOL
from toscametrics.blueprint.ngro import NGRO
from toscametrics.blueprint.nw import NW

from io import StringIO

class TETT(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of entities in a topology template"""
    
    def count(self):
        '''Function which counts all the entities in the topology template'''
        
        strio = StringIO(self.getStringIOobject)

        try:
            options = [
                NA(strio)._get_elements(),
                NN(strio)._get_elements(),
                NR(strio)._get_elements(),
                NPOL(strio)._get_elements(),
                NGRO(strio)._get_elements(),
                NW(strio)._get_elements()
            ]
                
            return sum([len(option) for option in options])
        
        except (AttributeError, ValueError):
            return 0


    def relative(self):
        '''Count relative to the lines of code'''
        try:
            strio = StringIO(self.getStringIOobject)
            return self.count() / LOC(strio).count()

        except (KeyError, AttributeError, ZeroDivisionError):
            return 0

# # from io import StringIO

# # path = r'C:\Users\s145559\OneDrive - TU Eindhoven\School\JADS\Jaar 2\Thesis\RADON PROJECT\GIT projects\ANALYSIS\dataminer\tmp\tliron\puccini\Example\artifacts.yaml'
# # with open(path, 'r') as file:
# #             string = file.read()


# # #string = 'tosca_definitions_version: tosca_simple_yaml_1_0\ndescription: Template with requirements against hosting infrastructure.\n\ntopology_template:\n  inputs:\n    # omitted here for brevity\n\n  node_templates:\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        root_password: { get_input: my_mysql_rootpw }\n        port: { get_input: my_mysql_port }\n      requirements:\n        - host:\n            node_filter:\n              capabilities:\n                - host:\n                    properties:\n                      - num_cpus: { in_range: [ 1, 4 ] }\n                      - mem_size: { greater_or_equal: 2 GB }\n                - os:\n                    properties:\n                      - architecture: { equal: x86_64 }\n                      - type: linux\n                      - distribution: ubuntu\n                - backup_os:\n                    properties:\n                      - architecture: { equal: x86_64 }\n                      - type: linux\n                      - distribution: ubuntu\n                      \n    backup_mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        # omitted here for brevity\n      requirements:\n        - host:\n            node_filter:\n              capabilities:\n                - host:\n                    properties:\n                      - num_cpus: { in_range: [ 1, 4 ] }\n                      - mem_size: { greater_or_equal: 2 GB }\n                - os:\n                    properties:\n                      - architecture: { equal: x86_64 }\n                      - type: linux\n                      - distribution: ubuntu'

# string = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template for deploying a single server with predefined properties.\n\ntopology_template:\n  inputs:\n    cpus:\n      type: integer\n      description: Number of CPUs for the server.\n      constraints:\n        - valid_values: [ 1, 2, 4, 8 ]\n\n  node_templates:\n    my_server:\n      type: tosca.nodes.Compute\n      capabilities:\n        # Host container properties\n        host:\n          properties:\n            # Compute properties\n            num_cpus: { get_input: cpus }\n            mem_size: 2048  MB\n            disk_size: 10 GB'
# print(string)
# general = StringIO(string)
# metric = TETT(general)
# metric.relative()

