# Number of Interfaces in a blueprint (NIF)

## Description

Returns the number of interfaces within a blueprint template. These interfaces can occur in a node template, or a relationship template. 

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
The following example has **1 interface**.

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
      properties:
        root_password: { get_input: my_mysql_rootpw }
        port: { get_input: my_mysql_port }
      requirements:
        - host: db_server
      interfaces:
        Standard:
          configure: scripts/my_own_configure.sh
```

---

Below an example on how to call the metric and the expected output for this example:

```python
>>> from io import StringIO
>>> from toscametrics.metrics.nif import NIF

>>> str = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\ndescription: Template for deploying a single server with MySQL software on top.\n\ntopology_template:\n  inputs:\n    mysql_rootpw:\n      type: string\n      \n    mysql_port:\n      type: integer\n    \n  node_templates:\n    db_server:\n      type: tosca.nodes.Compute\n      \n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        root_password: { get_input: my_mysql_rootpw }\n        port: { get_input: my_mysql_port }\n      requirements:\n        - host: db_server\n      interfaces:\n        Standard:\n          configure: scripts/my_own_configure.sh'

>>> yml = StringIO(str.expandtabs(2)) #substitute \t with 2 spaces and create the StringIO object
>>> metric = NIF(yml)
>>> print('NIF: ', metric.count())

NIF: 1
```