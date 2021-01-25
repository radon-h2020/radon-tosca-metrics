from io import StringIO
from .import_metrics import general_metrics #, tosca_metrics


def extract_all(script: str):

    metrics = general_metrics
    #metrics.update(tosca_metrics)

    results = dict()

    # Execute metrics
    for name in metrics:
        results[name] = metrics[name](script).count()

    return results