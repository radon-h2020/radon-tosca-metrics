from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscaparser.tosca_template import ToscaTemplate
from toscametrics.utils import getCapabilities
from toscametrics.utils import keyValueList

class NGC(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of capabilities defined in a given .yaml file"""

    def count(self):
        '''Function which counts the number of capabilities within the whole script. Inline capabilities are included as well'''
        try:
            template = self.getyml
            capabilities = getCapabilities(template)
            count = 0
            for cap in capabilities:
                count += len(cap[1])
            
            inline_caps = keyValueList(template)
            count += len([(k,v) for k, v in inline_caps if k == 'capability'])

            return count

        except AttributeError:
            return 0



# from io import StringIO

# string = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ntopology_template:\n  node_templates:\n    log_ip:\n      type: tosca.nodes.samples.LogIp\n      requirements:\n        - host:\n            node: compute\n            capability: tosca.capabilities.Container\n            relationship: tosca.relationships.HostedOn'

# print(string)
# yml = StringIO(string.expandtabs(2)) 
# metric = NGC(yml)

# print('NGC count: ', metric.count())
