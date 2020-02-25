from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscaparser.tosca_template import ToscaTemplate
from toscametrics.utils import getRelationshipTypes
from toscametrics.utils import getNodeTypes
import re

class NCYS(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of yaml calls in a given .yaml file"""

    def _for_node_templates(self):
        '''Checks for the number of yaml calls within node templates'''
        template = ToscaTemplate(yaml_dict_tpl=self.getyml)
        node_temps = template.nodetemplates
        calls = []
        for temp in node_temps:
            temp = temp.entity_tpl
            operands = [re.compile(r'.yaml|.yml').findall(str(v)) for k, v in temp.items()]
            flattern = [item for sublist in operands for item in sublist]
            calls.extend(flattern)
        return len(calls)

    def _for_relationship_templates(self):
        '''Checks for the number of yaml calls within relationship templates'''
        template = ToscaTemplate(yaml_dict_tpl=self.getyml)
        rel_temps = template.relationship_templates
        calls = []
        for temp in rel_temps:
            temp = temp.entity_tpl
            operands = [re.compile(r'.yaml|.yml').findall(str(v)) for k, v in temp.items()]
            flattern = [item for sublist in operands for item in sublist]
            calls.extend(flattern)
        return len(calls)

    def _for_relationshiptype_definitions(self):
        '''Checks for the number of yaml calls within relationship definition'''
        calls = []
        reltypes = getRelationshipTypes(self.getyml)[0][1]
        for reltype in reltypes:
            rel_dict = reltypes[reltype]
            operands = [re.compile(r'.yaml|.yml').findall(str(v)) for k, v in rel_dict.items()]
            flattern = [item for sublist in operands for item in sublist]
            calls.extend(flattern)
        return len(calls)
    
    def _for_nodetype_definitions(self):
        '''Checks for the number of yaml calls within nodetype definition'''
        calls = []
        nodetypes = getNodeTypes(self.getyml)[0][1]
        for nodetype in nodetypes:
            node_dict = nodetypes[nodetype]
            operands = [re.compile(r'.yaml|.yml').findall(str(v)) for k, v in node_dict.items()]
            flattern = [item for sublist in operands for item in sublist]
            calls.extend(flattern)
        return len(calls)


    def count(self):
        '''Function which counts the number of yaml calls in a given yaml file'''
        calls = []
        try:
            calls.append(self._for_node_templates())
        except (AttributeError, IndexError):
            calls.append(0)
        
        try:
            calls.append(self._for_relationship_templates())
        except (AttributeError, IndexError):
            calls.append(0)
        
        try:
            calls.append(self._for_relationshiptype_definitions())
        except (AttributeError, IndexError):
            calls.append(0)

        try:
            calls.append(self._for_nodetype_definitions())
        except (AttributeError, IndexError):
            calls.append(0)

        return sum(calls)



# string = 'tosca_definitions_version: alien_dsl_2_0_0\n\nnode_types:\n  org.ystia.ntp.ansible.nodes.NtpServer:\n    derived_from: org.ystia.ntp.pub.nodes.NtpServer\n    interfaces:\n      Standard:\n        create: playbooks/create.yaml\n        configure:\n          inputs:\n            TYPE: "server"\n          implementation: playbooks/configure.yaml\n        start: playbooks/start.yaml\n        stop: playbooks/stop.yaml'

# from io import StringIO

# print(string)

# yml = StringIO(string.expandtabs(2)) 
# metric = NCYS(yml)

# print('NCYS count: ', metric.count())
