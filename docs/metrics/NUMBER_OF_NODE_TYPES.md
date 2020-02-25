# Number of Node Types in a blueprint (NNT)

## Description

Returns the number of node types within a blueprint template.

---

## Parameters

**_Input_:**

* ```yaml : StringIO``` -- a StringIO object representing a yaml file;

**_Output_:** 

* an _integer >= 0_.

**_Exception_:**

* ```YAMLError``` if the value of ```yaml``` does not represent a valid yaml file. 
* ```AttributeError``` and return of 0 if the yaml file does not contain the key ```node_templates``

---

## Example
The following example has **1 node type**.

``` yaml
tosca_definitions_version: tosca_simple_yaml_1_2

description: Template for deploying a single server with MySQL software on top.

topology_template:
  inputs:
    mysql_rootpw:
      type: string
      
    mysql_port:
      type: integer
    
  node_templates:
    db_server:
      type: tosca.nodes.Compute
      
    mysql:
      type: tosca.nodes.DBMS.MySQL
```

---

Below an example on how to call the metric and the expected output for this example:

```python
>>> from io import StringIO
>>> from toscametrics.metrics.nnt import NNT

>>> str = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\n \n\ndescription: Template for deploying a single server with MySQL software on top.\n\n \n\ntopology_template:\n\n  inputs:\n\n    mysql_rootpw:\n\n      type: string\n\n    mysql_port:\n\n      type: integer\n\n    # rest omitted here for brevity\n\n \n\n  node_templates:\n\n    db_server:\n\n      type: tosca.nodes.Compute\n\n      # rest omitted here for brevity\n\n \n\n    mysql:\n\n      type: tosca.nodes.DBMS.MySQL'

>>> yml = StringIO(str.expandtabs(2)) #substitute \t with 2 spaces and create the StringIO object
>>> metric = NNT(yml)
>>> print('NNT: ', metric.count())

NNT: 2
```