# Number of Properties

## Description

Returns the number of properties within a blueprint template. 

---


## Example
The following example has **7 properties**.

``` yaml
tosca_definitions_version: tosca_simple_yaml_1_0
description: Template with requirements against hosting infrastructure.

topology_template:

  node_templates:
     
    mysql:
      type: tosca.nodes.DBMS.MySQL
      properties:
        root_password: { get_input: my_mysql_rootpw }
        port: { get_input: my_mysql_port }
        
      requirements:
        - host:
            node_filter:
              capabilities:
                - host:
                    properties:
                      - num_cpus: { in_range: [ 1, 4 ] }
                      - mem_size: { greater_or_equal: 2 GB }
                - os:
                    properties:
                      - architecture: { equal: x86_64 }
                      - type: linux
                      - distribution: ubuntu
```

---

## Parameters


|   | **Type** | **Description** |
|---|---|---|
**Input:**| `io.StringIO`| A TOSCA blueprint|
**Output:**| `unsigned int`| The number of properties |
**Exception:**| `TypeError`| If blueprint is empty or invalid|

---

## How to use


Below an example on how to call the metric and the expected output for this example:

```python
from io import StringIO
from toscametrics.metrics.num_properties import NumProperties

str = 'tosca_definitions_version: tosca_simple_yaml_1_0\ndescription: Template with requirements against hosting infrastructure.\n\ntopology_template:\n  inputs:\n    # omitted here for brevity\n\n  node_templates:\n     \n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        root_password: { get_input: my_mysql_rootpw }\n        port: { get_input: my_mysql_port }\n        \n      requirements:\n        - host:\n            node_filter:\n              capabilities:\n                - host:\n                    properties:\n                      - num_cpus: { in_range: [ 1, 4 ] }\n                      - mem_size: { greater_or_equal: 2 GB }\n                - os:\n                    properties:\n                      - architecture: { equal: x86_64 }\n                      - type: linux\n                      - distribution: ubuntu'
yml = StringIO(str.expandtabs(2))  # substitute \t with 2 spaces and create the StringIO object
metric = 
print('Number of properties: ', NumProperties(yml).count)

>>> Number of properties: 7
```