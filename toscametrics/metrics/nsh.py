from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscaparser.tosca_template import ToscaTemplate
from toscametrics.utils import getInterfaces
import re

class NSH(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of shell commands executed in a given .yaml file"""

    def count(self):
        '''Function which counts the number of shell commands within the whole script'''
        try:
            template = self.getyml
            interfaces = getInterfaces(template)
            files = []
            for interface in interfaces:
                operands = [re.compile(r'.sh').findall(str(v)) for k, v in interface[1].items()]
                flattern = [item for sublist in operands for item in sublist]
                files.extend(flattern)
            return len(files)
        except AttributeError:
            return 0


# string = 'tosca_definitions_version: alien_dsl_2_0_0\n\nnode_types:\n  org.ystia.cloudera.linux.bash.nodes.ClouderaServer:\n    derived_from: org.ystia.consul.pub.nodes.ConsulUser\n    interfaces:\n      Standard:\n        create:\n          inputs:\n            CLOUDERA_MANAGER_REPO: { get_property: [SELF, cloudera_manager_repository] }\n            NTP_SERVER: { get_property: [SELF, ntp_server] }\n          implementation: scripts/clouderamanager_install.sh\n        configure:\n          implementation: scripts/clouderamanager_config.sh\n        start:\n          implementation: scripts/clouderamanager_start.sh\n        stop:\n          implementation: scripts/clouderamanager_stop.sh'

# from io import StringIO

# print(string)

# yml = StringIO(string.expandtabs(2)) 
# metric = NSH(yml)

# print('NSH count: ', metric.count())
