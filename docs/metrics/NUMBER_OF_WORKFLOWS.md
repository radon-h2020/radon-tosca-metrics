# Number of Workflows in a blueprint (NW)

## Description

Returns the number of imperative workflows defined within a blueprint template.

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
The following example has **1 imperative workflow defined**.

``` yaml
tosca_definitions_version: tosca_simple_yaml_1_2

topology_template:
  node_templates:
    my_server:
      type: tosca.nodes.Compute
    mysql:
      type: tosca.nodes.DBMS.MySQL
      requirements:
        - host: my_server
      interfaces:
        tosca.interfaces.nodes.custom.Backup:
          operations:
            backup: backup.sh

  workflows:
    backup:
      description: Performs a snapshot of the MySQL data.
      steps:
        my_step:
          target: mysql
          activities:
            - call_operation: tosca.interfaces.nodes.custom.Backup.backup
```

---

Below an example on how to call the metric and the expected output for this example:

```python
>>> from io import StringIO
>>> from toscametrics.blueprint.nw import NW

>>> str = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\ntopology_template:\n  node_templates:\n    my_server:\n      type: tosca.nodes.Compute\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      requirements:\n        - host: my_server\n      interfaces:\n        tosca.interfaces.nodes.custom.Backup:\n          operations:\n            backup: backup.sh\n\n  workflows:\n    backup:\n      description: Performs a snapshot of the MySQL data.\n      steps:\n        my_step:\n          target: mysql\n          activities:\n            - call_operation: tosca.interfaces.nodes.custom.Backup.backup'

>>> yml = StringIO(str.expandtabs(2)) #substitute \t with 2 spaces and create the StringIO object
>>> metric = NW(yml)
>>> print('NW: ', metric.count())

NW: 1
```