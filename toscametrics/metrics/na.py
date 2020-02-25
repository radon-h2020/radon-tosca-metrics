from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscaparser.tosca_template import ToscaTemplate
from toscametrics.utils import getArtifacts

class NA(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of artifacts defined in a given .yaml file"""
    
    # def count(self):
    #     '''Function which counts the number of artifacts for all the nodes'''
    #     try:
    #         template = ToscaTemplate(yaml_dict_tpl=self.getyml)
    #         node_temps = template.nodetemplates
    #         artfs = []
    #         for temp in node_temps:
    #             temp = temp.templates.get(temp.name)
    #             try:
    #                 print(temp)
    #                 artf = getArtifacts(temp)
    #                 print(artf)
    #                 artfs.append(len(artf[0][1]))
    #             except IndexError:
    #                 artfs.append(0)
    #         return sum(artfs)
    #     except: AttributeError:
    #         return 0


    def count(self):
        '''Function which counts the number of artifacts within the whole script'''
        try:
            template = self.getyml
            artifacts = getArtifacts(template)
            count = 0
            for art in artifacts:
                count += len(art)
            return count

        except AttributeError:
            return 0


# from io import StringIO

# string = "tosca_definitions_version: tosca_simple_yaml_1_2\n\nimports:\n- artifacts.yaml\n- relationships.yaml\n\nnode_types:\n\n  tosca.nodes.nfv.VDU.Compute:\n    derived_from: tosca.nodes.Compute\n    capabilities:\n      virtual_compute:\n        description: >-\n          Describes virtual compute resources capabilities.\n        type: tosca.capabilities.nfv.VirtualCompute\n    artifacts:\n      sw_image:\n        description: >-\n          Describes the software image which is directly loaded on the virtualization container\n          realizing this virtual storage.\n        file: '' # ERRATUM: missing value even though it is required in TOSCA\n        type: tosca.artifacts.nfv.SwImage"

# print(string)

# yml = StringIO(string.expandtabs(2)) 
# metric = NA(yml)

# print('NA count: ', metric.count())




