import toscametrics.utils as utils
from toscametrics.classes.clauses.conditions import ConditionClause 

class ConditionsParser():

    def parseAll(self, artifact):
        """ 
        Returns a list of ConditionClause 
        artifact -- a dictionary or a list of dictionary to parse.
        """ 
        
        if not isinstance(artifact, dict) and not isinstance(artifact, list):
            return []
       
        clauses = []
        
        keyValueList = utils.keyValueList(artifact)
        for kv in keyValueList:
            if kv[0] ==  'condition':
                conditions = kv[1]
                clause = self.parse(conditions)
                if clause is not None:
                    clauses.append(clause)

        return clauses
    
    def parse(self, items):
        """ 
        Returns a ConditionClause 
        items -- a list of conditions to parse.
        """ 
        
        if not isinstance(items, list):
            return None
        
        if len(items) == 0:
            return None
       
        clause = ConditionClause()

        for d in items:
            key = next(iter(d)).strip()  
            if str(key) == 'and':
                clause.And = self.findRecursiveClauses(d.get(key))
            elif str(key) == 'or':
                clause.Or = self.findRecursiveClauses(d.get(key))
            elif str(key) == 'not':
                clause.Not = self.findRecursiveClauses(d.get(key))
            elif str(key) == 'assert':
                clause.Assert = self.findRecursiveClauses(d.get(key))

        return clause
        

    def findRecursiveClauses(self, lst):
        if lst is None or not isinstance(lst, list):
            return lst
        
        clauses = []

        for item in lst:
            if isinstance(item, dict):
                c = ConditionClause()

                key = next(iter(item)).strip()
                if key == 'and':
                    c.And=self.findRecursiveClauses(item.get(key))
                elif key == 'or':
                    c.Or=self.findRecursiveClauses(item.get(key))
                elif key == 'not':
                    c.Not=self.findRecursiveClauses(item.get(key))
                elif key == 'assert':
                    c.Assert=self.findRecursiveClauses(item.get(key))
                else:
                    clauses.append(item)
                    continue
                
                clauses.append(c)

        return clauses
