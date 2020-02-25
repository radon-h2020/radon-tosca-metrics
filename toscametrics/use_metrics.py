#-------------Load modules-------------
import yaml
import os
from io import StringIO
import pandas as pd
import json

#Own
from toscametrics.import_metrics import general_metrics
from toscametrics.import_metrics import tosca_metrics

#-------------Get locations of Tosca scripts-------------
def getToscaScripts(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()

    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getToscaScripts(fullPath)
        else:
            allFiles.append(fullPath)       
    
    return allFiles

#-------------Calculate metrics-------------
def calculateMetrics(yml, metrics_type='general'):
    """
    Executes metrics on a given script and returns a dictionary of results
    script: str  -- a StringIO object representing a IaC script in TOSCA
    metrics: str -- possible options: 'general', 'tosca' or 'tosca_and_general'
    """

    metrics = general_metrics
    results = {}

    if metrics_type == 'tosca':
        metrics = tosca_metrics
    
    elif metrics_type == 'tosca_and_general':
        metrics = dict(list(general_metrics.items()) + list(tosca_metrics.items()))

    # Execute metrics 
    for name in metrics:
        try:
            m = metrics[name](yml)
            method_list = [func for func in dir(m) if callable(getattr(m, func)) and not func.startswith("_") and func != 'getyml']

            results[name] = {}
            if 'count' in method_list:
                results[name]['count']  = m.count()
            if 'min' in method_list:
                results[name]['min']    = m.min() 
            if 'max' in method_list:
                results[name]['max']    = m.max()
            if 'median' in method_list:
                results[name]['median'] = m.median()
            if 'mean' in method_list:
                results[name]['mean']   = m.mean()
            if 'check' in method_list:
                results[name]['check']   = m.check()
            
            # Removing value that are None from the dictionary
            filtered = {k : v for k, v in results[name].items() if v is not None}
            results[name].clear()
            results[name].update(filtered)
           
        except Exception as e:
            print('\033[93m' + 'Warning: exception raised for metric {}.'.format(name) + '\033[0m')

            results[name] = {
                "msg": str(e)
            }

    return results

#-------------Append script metrics-------------
def appendMetrics(all_results, filePath, metrics_type='general'):
    with open(filePath, 'r') as file:
        yml = file.read()
    yml = StringIO(yml.expandtabs(2))
    all_results[filePath] = calculateMetrics(yml, metrics_type)
    return all_results

#-------------Run program-------------
def main(metrics_type='general', example_files=False):
    example_files = example_files

    if example_files == True:
        dirName = r'C:\Users\s145559\OneDrive - TU Eindhoven\School\JADS\Jaar 2\Thesis\RADON PROJECT\Data\\1. Total Examples'

    elif example_files == False:
        dirName = r'C:\Users\s145559\OneDrive - TU Eindhoven\School\JADS\Jaar 2\Thesis\RADON PROJECT\Data\\2. Total Industry'
   
    all_results = {}
    filePaths = getToscaScripts(dirName)
    count = 0
    for filePath in filePaths:
        print('count: ', count)
        try:
            all_results = appendMetrics(all_results, filePath, metrics_type)
        except Exception as e:
            print(e)
        count = count + 1

    if example_files == True:
        i = 0
        while os.path.exists('results/example_metric_results_{}.json'.format(i)):
            i += 1

        with open('results/example_metric_results_{}.json'.format(i), 'w') as fp:
            json.dump(all_results, fp)

    elif example_files == False:
        i = 0
        while os.path.exists('results/industry_metric_results_{}.json'.format(i)):
            i += 1
        
        with open('results/industry_metric_results_{}.json'.format(i), 'w') as fp:
            json.dump(all_results, fp)

main(metrics_type='tosca', example_files=False)





