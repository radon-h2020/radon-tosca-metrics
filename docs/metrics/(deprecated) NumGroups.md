# Number of Groups

## Description

Returns the number of groups within a blueprint template. 

---

## Example
The following example has **1 group**.

``` yaml
tosca_definitions_version: tosca_simple_yaml_1_3

topology_template:
  node_templates:
    wordpress_server:
      type: tosca.nodes.WebServer
    mysql:
      type: tosca.nodes.DBMS.MySQL

  groups:
    my_co_location_group:
      type: tosca.groups.Root
      members: [ wordpress_server, mysql ]
	  
  policies:
    - my_anti_collocation_policy:
        type: my.policies.anticolocateion
        targets: [ my_co_location_group ]
```

---

## Parameters


|   | **Type** | **Description** |
|---|---|---|
**Input:**| `io.StringIO`| A TOSCA blueprint|
**Output:**| `unsigned int`| The number of groups|
**Exception:**| `TypeError`| If blueprint is empty or invalid|

---

## How to use



Below an example on how to call the metric and the expected output for this example:

```python
>> > from io import StringIO
>> > from toscametrics.blueprint.gro import NGRO

>> > str = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ntopology_template:\n  node_templates:\n    wordpress_server:\n      type: tosca.nodes.WebServer\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n\n  groups:\n    my_co_location_group:\n      type: tosca.groups.Root\n      members: [ wordpress_server, mysql ]\n\t  \n  policies:\n    - my_anti_collocation_policy:\n        type: my.policies.anticolocateion\n        targets: [ my_co_location_group ]'

>> > yml = StringIO(str.expandtabs(2))  # substitute \t with 2 spaces and create the StringIO object
>> > metric = NGRO(yml)
>> > print('NGRO: ' + str(metric.count))

NGRO: 1
```