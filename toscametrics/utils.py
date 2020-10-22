def keyValueList(d): 
    """ 
    This function iterates over all the key-value pairs of a dictionary and returns a list of tuple (key, value).
    d -- a dictionary to iterate through
    """
    if not isinstance(d, dict) and not isinstance(d, list):
        return []

    keyvalues = []

    if isinstance(d, list):
        for entry in d:
            if isinstance(entry, dict):
                keyvalues.extend(keyValueList(entry))
    else:
        for k, v in d.items():
            if k is None or v is None:
                continue
            
            keyvalues.append((k, v))
            keyvalues.extend(keyValueList(v))
                
    return keyvalues

def str2bool(s):
    """ Casts a string to boolean. Returns None if the passed argument is None or not a string. """
    if s is None or not isinstance(s, str):
        return None
    if s.lower() == 'true':
         return True
    elif s.lower() == 'false':
         return False

def toString(obj):
    """ Converts and returns an object to string if not None, None otherwise """
    if obj is None:
        return None
    else:
        return str(obj)

def getCapabilities(node_dict):
    '''Function which transforms the dict of a node template instance into a list of capability tuples'''
    kvlist = keyValueList(node_dict)
    caps = [cap[1] for cap in kvlist if cap[0] == 'capabilities' or cap[0] == 'capability']
    return caps

def getProperties(cap_dict):
    '''Function which transforms a dictionary instance into a list of property tuples'''
    kvlist = keyValueList(cap_dict)
    props = [prop[1] for prop in kvlist if prop[0] == 'properties']
    return props

def getInputs(top_dict):
    '''Function which transforms the dict of a topology template instance into a list'''
    kvlist = keyValueList(top_dict)
    inps = [inp[1] for inp in kvlist if inp[0] == 'inputs']
    return inps

def getOutputs(top_dict):
    '''Function which transforms the dict of a topology template instance into a list'''
    kvlist = keyValueList(top_dict)
    outs = [out[1] for out in kvlist if out[0] == 'outputs']
    return outs

def getWorkflows(d):
    kvlist = keyValueList(d)
    workflows = [wf[1] for wf in kvlist if wf[0] == 'workflows']
    return workflows

def getArtifacts(d):
    '''Function which finds the 'artifact' keys in a given dictionary and put these into a list'''
    kvlist = keyValueList(d)
    artfs = []
    for kv in kvlist:
        if kv[0] == 'artifacts':
            artfs.append(kv[1])
    return artfs

def getRequirements(d):
    '''Function which finds the 'requirements' keys in a given dictionary and put these into a list'''
    kvlist = keyValueList(d)
    reqs = [req[1] for req in kvlist if req[0] == 'requirements']
    return reqs

def getNodeTypes(blue_dict):
    '''Function which transforms the dict of a blueprint instance into a list of NodeType tuples'''
    kvlist = keyValueList(blue_dict)
    nodetypes = [nt for nt in kvlist if nt[0] == 'node_types']
    return nodetypes

def getRelationshipTypes(blue_dict):
    '''Function which transforms the dict of a blueprint instance into a list of relationshipTypes tuples'''
    kvlist = keyValueList(blue_dict)
    reltypes = [nt for nt in kvlist if nt[0] == 'relationship_types']
    return reltypes

def getInterfaces(blue_dict):
    '''Function which transforms a dict into a list of interface tuples. Useful for interface outside of templates'''
    kvlist = keyValueList(blue_dict)
    intrfcs = [intf[1] for intf in kvlist if intf[0] == 'interfaces']
    return intrfcs

def getGroups(blue_dict):
    '''Function which transforms a dict into a list of group tuples'''
    kvlist = keyValueList(blue_dict)
    groups = [group[1] for group in kvlist if group[0] == 'groups']
    return groups

def getPolicies(blue_dict):
    '''Function which transforms a dict into a list of policy tuples'''
    kvlist = keyValueList(blue_dict)
    policies = [pol[1] for pol in kvlist if pol[0] == 'policies']
    return policies

def getNodeTemplates(d):
    '''Function which transforms a dict into a list of node template tuples'''
    kvlist = keyValueList(d)
    node_temps = []
    for kv in kvlist:
        if kv[0] == 'node_templates':
            node_temps.append(kv[1])
    return node_temps

def getRelationshipTemplates(d):
    '''Function which transforms a dict into a list of relationship template tuples'''
    kvlist = keyValueList(d)
    rel_temps = []
    for kv in kvlist:
        if kv[0] == 'relationship_templates':
            rel_temps.append(kv[1])
    return rel_temps


def getOperations(d):
    '''Function which transforms a dict into a list of operations.'''
    kvlist = keyValueList(d)
    ops = [op[1] for op in kvlist if op[0] == 'operations']
    return ops


def allKeys(d): 
    """ 
    Returns a list of all the keys of a dictionar (duplicates included)
    d -- a dictionary to iterate through
    """
    if d is None or not isinstance(d, dict) and not isinstance(d, list):
        return []
    
    keys = []
    
    if isinstance(d, list):
        for entry in d:
            keys.extend(allKeys(entry))
    else:
        for k, v in d.items():
            if k is None or v is None:
                continue
            
            keys.append(k)
            keys.extend(allKeys(v))
                
    return keys

def allValues(d): 
    """ 
    Returns a list of all the primitive values of a dictionary (duplicates included)
    d -- a dictionary to iterate through
    """
    if d is None:
        return []

    if not isinstance(d, dict) and not isinstance(d, list):
        return [d]
    
    values = []
    
    if isinstance(d, list):
        for entry in d:
            values.extend(allValues(entry))
    else:
        for k, v in d.items():
            values.extend(allValues(v))

    return values
