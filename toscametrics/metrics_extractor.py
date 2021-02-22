from .import_metrics import general_metrics, blueprint_metrics


def extract_all(script: str):

    metrics = general_metrics
    metrics.update(blueprint_metrics)

    results = dict()

    # Execute blueprint
    for name in metrics:
        results[name] = metrics[name](script).count()

    return results
