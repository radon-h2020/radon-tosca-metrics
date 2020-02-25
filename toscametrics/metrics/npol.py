from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscaparser.tosca_template import ToscaTemplate
from toscametrics.utils import getPolicies

class NPOL(BlueprintMetric):
    """ This class is responsible for providing the methods to count the number of policies defined in a given .yaml file"""

    def count(self):
        '''Function which counts the number of policies within the whole script'''
        try:
            template = self.getyml
            policies = getPolicies(template)
            count = 0
            for pol in policies:
                count += len(pol[1])
            return count

        except AttributeError:
            return 0