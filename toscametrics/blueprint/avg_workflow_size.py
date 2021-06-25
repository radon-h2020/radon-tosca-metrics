from toscametrics.blueprint_metric import BlueprintMetric
from toscametrics.utils import key_value_list


class AvgWorkflowSize(BlueprintMetric):
    """ This class counts the number of blueprint's workflows.
        Note, this might be applicable to alien4cloud only
    """

    def count(self):
        total_steps = 0
        total_workflows = 0

        for key, value in key_value_list(self.blueprint):
            if key == 'workflows':
                total_workflows = len(value)

                for _, workflow_dict in value.items():
                    steps = workflow_dict.get('steps', [])
                    total_steps += len(steps)

                break

        if total_workflows > 0:
            return round(total_steps/total_workflows, 1)

        return 0
