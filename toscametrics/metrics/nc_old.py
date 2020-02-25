from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscaparser.tosca_template import ToscaTemplate
from statistics import mean
from statistics import median

class NC(BlueprintMetric):
    """ This class is responsible for providing the methods to count the total number of capabilities, provide the minimum number per node, the maximum number per node, the mean and median defined in a given .yaml file"""
    
    def _create_list_of_node_capabilities(self):
        '''Function which creates a list containing the number of capabilities per identified node'''
        
        template = ToscaTemplate(yaml_dict_tpl=self.getyml)
        node_temps = template.nodetemplates
        list_number_caps = []
        for temp in node_temps:
            temp = temp.templates.get(temp.name)
            try:
                list_number_caps.append(len(temp.get('capabilities')))
            except:
                try:
                    node_filter = temp.get('node_filter')
                    caps = node_filter.get('capabilities')
                    if len(caps) > 0:
                            list_number_caps.append(len(caps))
                except:
                    try:
                        reqs = temp.get('requirements')
                        for req in reqs:
                            for key, value in req.items():
                                node_filter = value.get('node_filter')
                                caps = node_filter.get('capabilities')
                                if len(caps) > 0:
                                    list_number_caps.append(len(caps))
                    except:
                        list_number_caps.append(0)
        return list_number_caps 


    def count(self):
        try:
            list_of_capabilities = self._create_list_of_node_capabilities()
            return sum(list_of_capabilities)

        except AttributeError:
            return 0

    def min(self):
        try:
            list_of_capabilities = self._create_list_of_node_capabilities()
            return min(list_of_capabilities)

        except AttributeError:
            return 0

    def max(self):
        try:
            list_of_capabilities = self._create_list_of_node_capabilities()
            return max(list_of_capabilities)

        except AttributeError:
            return 0

    def mean(self):
        try:
            list_of_capabilities = self._create_list_of_node_capabilities()
            return mean(list_of_capabilities)

        except AttributeError:
            return 0

    def median(self):
        try:
            list_of_capabilities = self._create_list_of_node_capabilities()
            return median(list_of_capabilities)

        except AttributeError:
            return 0


#from io import StringIO

# #str = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template with requirements against hosting infrastructure.\n\ntopology_template:\n  inputs:\n    # omitted here for brevity\n    \n  node_templates:\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        # omitted here for brevity\n        \n      requirements:\n        - host: mysql_compute\n        \n    # Abstract node template (placeholder) to be selected by provider\n    mysql_compute:\n      type: Compute\n      node_filter:\n        capabilities:\n          - host:\n              properties:\n                num_cpus: { equal: 2 }\n                mem_size: { greater_or_equal: 2 GB }\n          - os:\n              properties:\n                architecture: { equal: x86_64 }\n                type: linux\n                distribution: ubuntu'
# str = 'tosca_definitions_version: tosca_simple_yaml_1_0\ndescription: Template with requirements against hosting infrastructure.\n\ntopology_template:\n  inputs:\n    # omitted here for brevity\n\n  node_templates:\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        # omitted here for brevity\n      requirements:\n        - host:\n            node_filter:\n              capabilities:\n                - host:\n                    properties:\n                      - num_cpus: { in_range: [ 1, 4 ] }\n                      - mem_size: { greater_or_equal: 2 GB }\n                - os:\n                    properties:\n                      - architecture: { equal: x86_64 }\n                      - type: linux\n                      - distribution: ubuntu\n                - backup_os:\n                    properties:\n                      - architecture: { equal: x86_64 }\n                      - type: linux\n                      - distribution: ubuntu\n                      \n    backup_mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        # omitted here for brevity\n      requirements:\n        - host:\n            node_filter:\n              capabilities:\n                - host:\n                    properties:\n                      - num_cpus: { in_range: [ 1, 4 ] }\n                      - mem_size: { greater_or_equal: 2 GB }\n                - os:\n                    properties:\n                      - architecture: { equal: x86_64 }\n                      - type: linux\n                      - distribution: ubuntu'
# #print(str)
# yml = StringIO(str.expandtabs(2)) 
# metric = NC(yml)
# print('NC count: ', metric.count())
# print('NC min: ', metric.min())
# print('NC max: ', metric.max())
# print('NC mean: ', metric.mean())
# print('NC median: ', metric.median())