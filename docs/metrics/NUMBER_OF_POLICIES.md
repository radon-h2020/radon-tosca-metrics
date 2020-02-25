# Number of Policies in a blueprint (NPOL)

## Description

Returns the number of policies within a blueprint template. 

---

## Parameters

**_Input_:**

* ```yaml : StringIO``` -- a StringIO object representing a yaml file;

**_Output_:** 

* an _integer >= 0_.

**_Exception_:**

* ```YAMLError``` if the value of ```yaml``` does not represent a valid yaml file. 

---

## Example
The following example has **1 policy**.

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

Below an example on how to call the metric and the expected output for this example:

```python
>>> from io import StringIO
>>> from toscametrics.metrics.npol import NPOL

>>> str = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ntopology_template:\n  node_templates:\n    wordpress_server:\n      type: tosca.nodes.WebServer\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n\n  groups:\n    my_co_location_group:\n      type: tosca.groups.Root\n      members: [ wordpress_server, mysql ]\n\t  \n  policies:\n    - my_anti_collocation_policy:\n        type: my.policies.anticolocateion\n        targets: [ my_co_location_group ]'

>>> yml = StringIO(str.expandtabs(2)) #substitute \t with 2 spaces and create the StringIO object
>>> metric = NPOL(yml)
>>> print('NPOL: ' + str(metric.count()))

NPOL: 1
```