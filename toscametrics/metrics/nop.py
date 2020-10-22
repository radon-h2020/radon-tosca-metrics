from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscametrics.utils import getOperations
from toscametrics.metrics.nif import NIF
from toscametrics.metrics.cdit import CDIT

from io import StringIO

class NOP(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of operations in a given .yaml file"""   

    def _get_elements(self):

        strio = StringIO(self.getStringIOobject)

        invalid_keys = ['metadata', 'description', 'derived_from']
               
        operation_list = []

        for element in NIF(strio)._get_elements():
            try:
                operations = getOperations(element)

                for operation in operations:
                    if isinstance(operation, list):
                        operation_list.extend(operation)

                    elif isinstance(operation, dict):
                        operation_list.append(operation)

                    else:
                        continue
            
            except:
                continue

        for element in CDIT(strio)._get_elements():
            try:
                operations = getOperations(element)
                
                if len(operations) != 0:
                    for operation in operations:
                        if isinstance(operation, list):
                            operation_list.extend(operation)

                        elif isinstance(operation, dict):
                            operation_list.append(operation)

                        else:
                            pass
                
                #Added because some operations are directly named without the 'operations' key
                else:
                    for _, value in element.items():
                        operation_list.append({k : v for k, v in value.items() if k not in invalid_keys})


            except:
                continue
        
        return operation_list

    
    def count(self):
        '''Function which counts the operations within the whole script'''
        try:
            operation_list = self._get_elements()

            names = []
            for operation in operation_list:
                names.extend(operation.keys())

            return len(names)

        except AttributeError:
            return 0






# from io import StringIO

# #string = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template with requirements against hosting infrastructure.\n\ntopology_template:\n  inputs:\n    # omitted here for brevity\n    \n  node_templates:\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        - hiergebeurtiets\n        \n      requirements:\n        - host: mysql_compute\n        \n    # Abstract node template (placeholder) to be selected by provider\n    mysql_compute:\n      type: Compute\n      node_filter:\n        capabilities:\n          - host:\n              properties:\n                num_cpus: { equal: 2 }\n                mem_size: { greater_or_equal: 2 GB }\n          - os:\n              properties:\n                architecture: { equal: x86_64 }\n                type: linux\n                distribution: ubuntu'
# string = 'tosca_definitions_version: tosca_simple_yaml_1_0\ndescription: Template with requirements against hosting infrastructure.\n\ntopology_template:\n  inputs:\n    # omitted here for brevity\n\n  node_templates:\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        root_password: { get_input: my_mysql_rootpw }\n        port: { get_input: my_mysql_port }\n      requirements:\n        - host:\n            node_filter:\n              capabilities:\n                database_endpoint: [ database, database_endpoint ]\n                      \n    backup_mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        # omitted here for brevity\n      requirements:\n        - host:\n            node_filter:\n              capabilities:\n                - host:\n                    properties:\n                      - num_cpus: { in_range: [ 1, 4 ] }\n                      - mem_size: { greater_or_equal: 2 GB }\n                - os:\n                    properties:\n                      - architecture: { equal: x86_64 }\n                      - type: linux\n                      - distribution: ubuntu'

# string = "tosca_definitions_version: tosca_simple_yaml_1_1\n\ninterface_types:\n\n  tosca.interfaces.Root:\n    metadata:\n      normative: 'true'\n      citation: '[TOSCA-Simple-Profile-YAML-v1.1]'\n      citation_location: 5.8.3\n    description: >-\n      This is the default (root) TOSCA Interface Type definition that all other TOSCA Interface\n      Types derive from.\n\n  tosca.interfaces.node.lifecycle.Standard:\n    metadata:\n      normative: 'true'\n      citation: '[TOSCA-Simple-Profile-YAML-v1.1]'\n      citation_location: 5.8.4\n    description: >-\n      This lifecycle interface defines the essential, normative operations that TOSCA nodes may\n      support.\n    derived_from: tosca.interfaces.Root\n    create:\n      description: >-\n        Standard lifecycle create operation.\n    configure:\n      description: >-\n        Standard lifecycle configure operation.\n    start:\n      description: >-\n        Standard lifecycle start operation.\n    stop:\n      description: >-\n        Standard lifecycle stop operation.\n    delete:\n      description: >-\n        Standard lifecycle delete operation.\n\n  tosca.interfaces.relationship.Configure:\n    metadata:\n      normative: 'true'\n      citation: '[TOSCA-Simple-Profile-YAML-v1.1]'\n      citation_location: 5.8.5\n    description: >-\n      The lifecycle interfaces define the essential, normative operations that each TOSCA\n      Relationship Types may support.\n    derived_from: tosca.interfaces.Root\n    pre_configure_source:\n      description: >-\n        Operation to pre-configure the source endpoint.\n    pre_configure_target:\n      description: >-\n        Operation to pre-configure the target endpoint.\n    post_configure_source:\n      description: >-\n        Operation to post-configure the source endpoint.\n    post_configure_target:\n      description: >-\n        Operation to post-configure the target endpoint.\n    add_target:\n      description: >-\n        Operation to notify the source node of a target node being added via a relationship.\n    add_source:\n      description: >-\n        Operation to notify the target node of a source node which is now available via a\n        relationship.\n    target_changed:\n      description: >-\n        Operation to notify source some property or attribute of the target changed\n    remove_target:\n      description: >-\n        Operation to remove a target node.\n    remove_source: # ERRATUM: does not appear in spec, but is mentioned\n      description: >-\n        Operation to remove the source node.\n"
# string  ='tosca_definitions_version: tosca_simple_yaml_1_3\n\ntopology_template:\n  description: Template of a database including its hosting stack.\n\n  inputs:\n    mq_service_ip:\n      type: string\n      description: IP address of the message queuing server to receive messages from\n    receiver_port:\n      type: string\n      description: Port to be used for receiving messages '
# # path = r'C:\Users\s145559\OneDrive - TU Eindhoven\School\JADS\Jaar 2\Thesis\RADON PROJECT\Data\All\All\requirements-and-capabilities.yaml'
# # with open(path, 'r') as file:
# #     string = file.read()

# print(string)
# yml = StringIO(string.expandtabs(2)) 
# metric = NOP(yml)

# print('NOP count: ', metric.count())
# x = metric._get_elements()
