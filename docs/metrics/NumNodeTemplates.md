# Number of Node Template

## Description

Returns the number of node templates within a blueprint. 

---

## Example
The following example has **2 node templates** (i.e., `db_server` and `mysql`).

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

## Parameters


|   | **Type** | **Description** |
|---|---|---|
**Input:**| `str`| A TOSCA blueprint|
**Output:**| `unsigned int`| The number of node templates|
**Exception:**| `TypeError`| If blueprint is empty or invalid|

---

## How to use



Below an example on how to call the metric and the expected output for this example:

```python
from toscametrics.blueprint.num_node_templates import NumNodeTemplates

yml = 'topology_template:\n\n  inputs:\n\n    mysql_rootpw:\n\n      type: string\n\n    mysql_port:\n\n      type: integer\n\n    # rest omitted here for brevity\n\n \n\n  node_templates:\n\n    db_server:\n\n      type: tosca.nodes.Compute\n\n      # rest omitted here for brevity\n\n \n\n    mysql:\n\n      type: tosca.nodes.DBMS.MySQL'
yml = yml.expandtabs(2)
print('Number of node templates: ' + NumNodeTemplates(yml).count())

>>> Number of node templates: 2
```