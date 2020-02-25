# Number of Nodes in a blueprint (NN)

## Description

Returns the number of nodes within a blueprint template. 

---

## Parameters

**_Input_:**

* ```yaml : StringIO``` -- a StringIO object representing a yaml file;

**_Output_:** 

* an _integer >= 0_.

**_Exception_:**

* ```YAMLError``` if the value of ```yaml``` does not represent a valid yaml file. 
* ```AttributeError``` and return of 0 if the yaml file does not contain the key ```node_templates```

---

## Example
The following example has **2 nodes**.

``` yaml
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
>>> from toscametrics.metrics.nn import NN

>>> str = 'topology_template:\n\n  inputs:\n\n    mysql_rootpw:\n\n      type: string\n\n    mysql_port:\n\n      type: integer\n\n    # rest omitted here for brevity\n\n \n\n  node_templates:\n\n    db_server:\n\n      type: tosca.nodes.Compute\n\n      # rest omitted here for brevity\n\n \n\n    mysql:\n\n      type: tosca.nodes.DBMS.MySQL'

>>> yml = StringIO(str.expandtabs(2)) #substitute \t with 2 spaces and create the StringIO object
>>> metric = NN(yml)
>>> print('NN: ' + str(metric.count()))

NN: 2
```