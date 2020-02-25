from math import log2

import toscametrics.utils as utils
from toscametrics.blueprint.blueprint_metric import BlueprintMetric

class ETP(BlueprintMetric):
    """ This class implements the metric 'Text Entropy' of blueprint script. """

    def count(self):
        
        keys = utils.allKeys(self.getyml)
        values = utils.allValues(self.getyml)
        
        words = keys

        for v in values:
            words.extend(str(v).split())

        wordset = set(words)
        freq={word: words.count(word) for word in wordset}

        entropy = 0
        for word in wordset:
            p = freq[word] / len(words)
            entropy -= p * log2(p)

        return round(entropy, 2)


# string = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ntopology_template:\n  description: Template of a database including its hosting stack.\n\n  inputs:\n    mq_service_ip:\n      type: string\n      description: IP address of the message queuing server to receive messages from\n    receiver_port:\n      type: string\n      description: Port to be used for receiving messages \n\n  outputs:\n    receiver_ip:\n      description: private IP address of the message receiver application\n      value: { get_attribute: [ server, private_address ] }\n    receiver_port:\n      description: Port of the message receiver endpoint\n      value: { get_attribute: [ app, app_endpoint, port ] }'
# from io import StringIO

# print(string)
# yml = StringIO(string.expandtabs(2)) 
# metric = ETP(yml)

# print('ETP count: ', metric.count())