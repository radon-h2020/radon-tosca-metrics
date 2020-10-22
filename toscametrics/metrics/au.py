from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscametrics.utils import keyValueList

class AU(BlueprintMetric):
    """ This class is responsible for providing the methods to count the anchor usage in a given .yaml file"""
      
    def count(self):
        try:
            dsl_defs = self.getyml.get('dsl_definitions')

            if dsl_defs:
                raw_text = self.getStringIOobject
                splitted_lines = raw_text.splitlines()
                anchors = [value.split('&')[1] for value in splitted_lines if '&' in value]                
                
                return sum([raw_text.count('*'+anchor) for anchor in anchors])

            else:
                return 0
        
        except:
            return 0




# string = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ndescription: >\n  TOSCA simple profile that just defines a YAML macro for commonly reused Compute\n  properties.\n\ndsl_definitions:\n  my_compute_node_props: &my_compute_node_props\n    disk_size: 10 GB\n    num_cpus: 1\n    mem_size: 2 GB\n\ntopology_template:\n  node_templates:\n    my_server:\n      type: Compute\n      capabilities:\n        host:\n          properties: *my_compute_node_props\n\n    my_database:\n      type: Compute\n      capabilities:\n        host:\n          properties: *my_compute_node_props'

# from io import StringIO

# print(string)
# yml = StringIO(string.expandtabs(2)) 
# metric = AU(yml)


# print('AU count: ', metric.count())