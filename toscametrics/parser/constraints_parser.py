import toscametrics.utils as utils
from toscametrics.classes.clauses.constraints import ConstraintClause 

class ConstraintsParser():

    def parseAll(self, artifact):
        """ 
        Returns a list of ConstraintClause 
        artifact -- a dictionary or a list of dictionary to parse.
        """ 

        if not isinstance(artifact, dict) and not isinstance(artifact, list):
            return []

        clauses = []
        
        keyValueList = utils.keyValueList(artifact)
        for kv in keyValueList:
            if kv[0] ==  'constraints':
                constraits = kv[1]
                clause = self.parse(constraits)
                if clause is not None:
                    clauses.append(clause)

        return clauses

    def parse(self, items):
        """ 
        Returns a ConstraintClause, if any. None otherwise
        items -- a list of constraints to parse.
        """ 

        if not isinstance(items, list):
            return None

        if len(items) == 0:
            return None
        
        clause = ConstraintClause()
        for d in items:
            key = next(iter(d)).strip()  
            if str(key) == 'equal':
                clause.equal = d.get(key)
            elif str(key) == 'greater_than':
                clause.greaterThan = d.get(key)
            elif str(key) == 'greater_or_equal':
                clause.greaterOrEqual = d.get(key)
            elif str(key) == 'less_than':
                clause.lessThan = d.get(key)
            elif str(key) == 'less_or_equal':
                clause.lessOrEqual = d.get(key)
            elif str(key) == 'in_range':
                clause.inRange = d.get(key)
            elif str(key) == 'valid_values':
                clause.validValues = d.get(key)
            elif str(key) == 'length':
                clause.length = d.get(key)
            elif str(key) == 'min_length':
                clause.minLength = d.get(key)
            elif str(key) == 'max_length':
                clause.maxLength = d.get(key)
            elif str(key) == 'pattern':
                clause.pattern = d.get(key)
            elif str(key) == 'schema':
                clause.schema = d.get(key)

        return clause