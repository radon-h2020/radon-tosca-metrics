import re
import yaml
import json
from io import StringIO
from toscametrics.blueprint.blueprint_metric import BlueprintMetric


class NSCM(BlueprintMetric):
    """ This class implements the metric 'Number of suspicious comments' in a blueprint script. """   
    
    def count(self):
        """ Return the number of suspicious comments in the script. """
        content = StringIO(self.getStringIOobject)

        suspicious = 0

        for l in content.getvalue().splitlines():            
            comment = re.search(r'#.+', str(l.strip()))
            if comment is not None:   
                if re.search(r'TODO|FIXME|HACK|XXX|CHECKME|DOCME|TESTME|PENDING', comment.group()) is not None:
                    suspicious += 1

        return suspicious    


# string = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template for deploying a single server with predefined properties.\n\n#TODO: add extra valid values \ntopology_template:\n  inputs:\n    cpus:\n      type: integer\n      description: Number of CPUs for the server.\n      constraints:\n        - valid_values: [ 1, 2, 4, 8 ]\n\n  node_templates:\n    my_server:\n      type: tosca.nodes.Compute\n      capabilities:\n        # Host container properties\n        host:\n          properties:\n            #TESTME: test the memory size\n            num_cpus: { get_input: cpus }\n            mem_size: 2048  MB\n            disk_size: 10 GB'

# from io import StringIO

# print(string)
# yml = StringIO(string.expandtabs(2)) 
# metric = NSCM(yml)

# print('NSCM count: ', metric.count())