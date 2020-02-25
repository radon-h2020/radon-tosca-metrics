# Python modules
import argparse
import inspect
import json
import os.path
import sys

from io import StringIO

# Own modules
from toscametrics.import_metrics import METRICS


def getParser():
    """ Returns an ArgumentParser """
    parser = argparse.ArgumentParser(description='Extract metrics from TOSCA \'blueprint\'')
    parser.add_argument(action='store', dest='blueprint', help='Input file path')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')
    return parser


def load(path):
    """ Returns the content of the file at <path>, if any; None otherwise """
    if not os.path.isfile(path):
        return None

    content = ''
    with open(path, 'r') as file:
        content = file.read()

    return content


def executeAll(blueprint):
    """
    Executes all metrics on a given blueprint and returns a dictionary of results per metric
    blueprint -- a StringIO object representing a blueprint
    """

    results = {}
       
    # Execute metrics 
    for name in METRICS:
        
        try:
            m = METRICS[name](toscametrics)

            results[name] = {}
            results[name]['count']  = m.count()
            results[name]['min']    = m.min() 
            results[name]['max']    = m.max()
            results[name]['median'] = m.mean()
            results[name]['mean']   = m.mean()
            
            # Check if the metric uses the argument 'relative' or 'occurrences.'
            spec = inspect.getfullargspec(m.count)
            if 'relative' in spec.args:
                results[name]['count_relative'] = round(m.count(relative=True), 2)
            if 'occurrences' in spec.args:
                results[name]['count_occurrences'] = round(m.count(occurrences=True), 2)

            # Removing value that are None from the dictionary
            filtered = {k : v for k, v in results[name].items() if v is not None}
            results[name].clear()
            results[name].update(filtered)
           
        except Exception:
            print('\033[93m' + 'Warning: exception raised for metric {}.'.format(name) + '\033[0m')

            results[name] = {
                "msg": str(e),
                "blueprint": blueprint.getvalue()
            }

    return results


def main():

    parser = getParser()

    # If no options show help message and exit
    if len(sys.argv[1:]) == 0:
        parser.parse_args(['--help'])

    args = parser.parse_args()

    blueprint = load(args.blueprint)

    if blueprint is None:
        print('\033[91m' + 'Error: failed to load the file {}. Please insert a valid file!'.format(args.blueprint) + '\033[0m')
        sys.exit(1)

    blueprint = StringIO(blueprint.expandtabs(2))
    results = executeAll(blueprint)
    blueprint.close()

    results2Json = json.dumps(results, indent=4, sort_keys=True)
    print(results2Json)

if __name__ == "__main__":
    main()
