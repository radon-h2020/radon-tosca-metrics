from math import log2

import toscametrics.utils as utils
from toscametrics.blueprint_metric import BlueprintMetric

class ETP(BlueprintMetric):
    """ This class implements the metric 'Text Entropy' of blueprint script. """

    def count(self, custom=None):
        
        if isinstance(custom, dict):
            keys = utils.allKeys(custom)
            values = utils.allValues(custom)
        else:
            keys = utils.allKeys(self.blueprint)
            values = utils.allValues(self.blueprint)
        
        words = keys

        for v in values:
            words.extend(str(v).split())

        wordset = set(words)
        freq={word: words.count for word in wordset}

        entropy = 0
        for word in wordset:
            p = freq[word] / len(words)
            entropy -= p * log2(p)

        return round(entropy, 2)



# # string = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ntopology_template:\n  description: Template of a database including its hosting stack.\n\n  inputs:\n    mq_service_ip:\n      type: string\n      description: IP address of the message queuing server to receive messages from\n    receiver_port:\n      type: string\n      description: Port to be used for receiving messages \n\n  outputs:\n    receiver_ip:\n      description: private IP address of the message receiver application\n      value: { get_attribute: [ server, private_address ] }\n    receiver_port:\n      description: Port of the message receiver endpoint\n      value: { get_attribute: [ app, app_endpoint, port ] }'
# # string = "tosca_definitions_version: tosca_simple_yaml_1_3\n\nartifact_types:\n\n  tosca.artifacts.Root:\n    metadata:\n      normative: 'true'\n      citation: '[TOSCA-Simple-Profile-YAML-v1.3]'\n      citation_location: 5.4.1\n    description: >-\n      This is the default (root) TOSCA Artifact Type definition that all other TOSCA base Artifact\n      Types derive from.\n      \n  tosca.artifacts.GEENROOT:\n    metadata:\n      normative: 'true'\n      citation: '[TOSCA-Simple-Profile-YAML-v1.3]'\n      citation_location: 5.4.1\n    description: >-\n      This is the default (root) TOSCA Artifact Type definition that all other TOSCA base Artifact\n      Types derive from."
# string = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\ntopology_template:\n  node_templates:\n    my_server:\n      type: tosca.nodes.Compute\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      requirements:\n        - host: my_server\n      interfaces:\n        tosca.interfaces.nodes.custom.Backup:\n          operations:\n            backup: backup.sh\n\n  workflows:\n    backup:\n      description: Performs a snapshot of the MySQL data.\n      steps:\n        my_step:\n          target: mysql\n          activities:\n            - call_operation: tosca.interfaces.nodes.custom.Backup.backup\n    remove:\n      steps:\n        my_step:\n          target: mysql\n          activities:\n            - call_operation: tosca.interfaces.nodes.custom.Remove.remove'

# from io import StringIO

# print(string)
# yml = StringIO(string.expandtabs(2)) 
# metric = ETP(yml)

# print('ETP count: ', metric.count())