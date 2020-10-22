from io import StringIO
from .import_metrics import general_metrics, tosca_metrics


def extract_all(script: StringIO):
    if script is None:
        raise TypeError('Expected a StringIO object')

    metrics = general_metrics
    metrics.update(tosca_metrics)

    results = dict()

    # Execute metrics
    for name in metrics:
        results[name] = metrics[name](script).count()

    script.close()

    return results