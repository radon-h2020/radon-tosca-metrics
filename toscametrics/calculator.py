#-------------Load modules-------------
import yaml
import os
from io import StringIO
import pandas as pd
import json

#Own
from toscametrics.import_metrics import tosca_metrics
from toscametrics.import_metrics import general_metrics


class MetricCalculator():

    def __init__(self, path_list, metrics_type):
        """Calculates all the blueprint over a set of yaml files defined in a list containing
        all the file paths"""

        valid_metrics_types = ['general', 'tosca', 'tosca_and_general']

        if not metrics_type in valid_metrics_types:
            raise ValueError('Enter a valid blueprint type (general, tosca, tosca_and_general)')
        try:
            self.all_results = {}
            count = 0
            total = len(path_list)
            for filePath in path_list:
                try:
                    self.all_results = self.appendMetrics(self.all_results, filePath, metrics_type)
                except Exception as e:
                    print(e)
                count = count + 1
                print(f'[{count} / {total}]')
        except:
            raise

    #-------------Calculate blueprint-------------
    def calculateMetrics(self, yml, metrics_type='tosca_and_general'):
        """
        Executes blueprint on a given script and returns a dictionary of results
        script: str  -- a StringIO object representing a IaC script in TOSCA
        blueprint: str -- possible options: 'general', 'tosca' or 'tosca_and_general'
        """

        metrics = general_metrics
        results = {}

        if metrics_type == 'tosca':
            metrics = tosca_metrics
        
        elif metrics_type == 'tosca_and_general':
            metrics = dict(list(general_metrics.items()) + list(tosca_metrics.items()))

        # calculate blueprint
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
                if 'relative' in method_list:
                    results[name]['relative']   = m.relative()
                if 'entropy' in method_list:
                    results[name]['entropy']   = m.entropy()
                
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

    #-------------Append script blueprint-------------
    def appendMetrics(self, all_results, filePath, metrics_type='general'):
        try:
            with open(filePath, 'r') as file:
                yml = file.read()
        except UnicodeDecodeError:
            with open(filePath, 'r', encoding='utf-8') as file:
                yml = file.read()

        yml = StringIO(yml.expandtabs(2))
        all_results[filePath] = self.calculateMetrics(yml, metrics_type)
        return all_results

    @property
    def getresults(self):
        return self.all_results

