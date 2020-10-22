from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscametrics.metrics.nif import NIF
from toscametrics.utils import keyValueList
import re
from io import StringIO

class NSH(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of shell commands executed in a given .yaml file"""

    def count(self):
        '''Function which counts the number of shell commands within the whole script'''
        
        files = []
        
        try:
            strio = StringIO(self.getStringIOobject)

            for element in NIF(strio)._get_elements():
                for _, element_values in element.items():
                    splitted_dict = keyValueList(element_values)
                    calls = [re.findall(r'.sh', tup[1]) for tup in splitted_dict if isinstance(tup[1], str)]                    
                    calls = [item for sublist in calls for item in sublist]
                    files.extend(calls)
            return len(files)

        except AttributeError:
            return len(files)



# string = 'tosca_definitions_version: alien_dsl_2_0_0\n\nnode_types:\n  org.ystia.cloudera.linux.bash.nodes.ClouderaServer:\n    derived_from: org.ystia.consul.pub.nodes.ConsulUser\n    interfaces:\n      Standard:\n        create:\n          inputs:\n            CLOUDERA_MANAGER_REPO: { get_property: [SELF, cloudera_manager_repository] }\n            NTP_SERVER: { get_property: [SELF, ntp_server] }\n          implementation: scripts/clouderamanager_install.sh\n        configure:\n          implementation: scripts/clouderamanager_config.sh\n        start:\n          implementation: scripts/clouderamanager_start.sh\n        stop:\n          implementation: scripts/clouderamanager_stop.sh'
# from io import StringIO
# print(string)
# yml = StringIO(string.expandtabs(2)) 
# metric = NSH(yml)
# print('NSH count: ', metric.count())
