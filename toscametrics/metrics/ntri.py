from toscametrics.blueprint.blueprint_metric import BlueprintMetric
from toscametrics.utils import keyValueList
from toscametrics.metrics.npol import NPOL
from toscametrics.metrics.cdpt import CDPT
from io import StringIO

class NTRI(BlueprintMetric):
    """ This class is responsible for providing the methods to count the triggers of a policy in a given .yaml file"""

    def count(self):
        '''Function which counts the number of triggers of a policy in a topology template'''

        strio = StringIO(self.getStringIOobject)

        options = [
            CDPT(strio)._get_elements(),
            NPOL(strio)._get_elements()
        ]

        trigger_list = []

        for option in options:
            for element in option:
                try:
                    triggers = [kv[1] for kv in keyValueList(element) if kv[0] == 'triggers']
                    trigger_list.extend(triggers)
                except:
                    continue
        
        return len(trigger_list)
