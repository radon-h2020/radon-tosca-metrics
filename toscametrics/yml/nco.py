import re

from toscametrics.utils import keyValueList
from toscametrics.blueprint.blueprint_metric import BlueprintMetric

COMPARISON_OPERANDS = re.compile(r'\bequal\b|\bgreater_than\b|\bgreater_or_equal\b|\bless_than\b|\bless_or_equal\b|\bin_range\b|\bvalid_values\b|\blength\b|\bmin_length\b|\bmax_length\b|\bpattern\b|\bschema\b')

class NCO(BlueprintMetric):
    """ This class implements the metric 'Number of comparison operands' in a blueprint script. """

    def count(self):
        operands = [COMPARISON_OPERANDS.findall(str(k)) for k, v in keyValueList(self.getyml)]
        operands = [oper for oper in operands if oper != []]
        return len(operands)


# string = 'topology_template:\n  node_templates:\n    my_server:\n      type: tosca.nodes.Compute\n\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      requirements:\n        - host: my_server\n      interfaces:\n        tosca.interfaces.nodes.custom.Backup:\n          operations:\n            backup: backup.sh\n\n  workflows:\n    start_mysql:\n      steps:\n        start_mysql:\n          target: mysql\n          activities :\n            - set_state: starting\n            - call_operation: tosca.interfaces.node.lifecycle.Standard.start\n            - set_state: started\n\n    stop_mysql:\n      steps:\n        stop_mysql:\n          target: mysql\n          activities:\n            - set_state: stopping\n            - call_operation: tosca.interfaces.node.lifecycle.Standard.stop\n            - set_state: stopped\n\n    backup:\n      description: Performs a snapshot of the MySQL data.\n      preconditions:\n        - target: my_server\n          condition:\n            - assert:\n              - state: [{equal: available}]\n        - target: mysql\n          condition:\n            - assert:\n              - state: [{valid_values: [started, available]}]\n              - my_attribute: [{equal: ready }]\n      steps:\n        backup_step:\n          activities:\n            - inline: stop\n            - call_operation: tosca.interfaces.nodes.custom.Backup.backup\n            - inline: start\n\n    restart:\n      steps:\n        backup_step:\n          activities:\n            - inline: stop\n            - inline: start    '
# from io import StringIO

# print(string)
# yml = StringIO(string.expandtabs(2)) 
# metric = NCO(yml)

# print('NCO count: ', metric.count())