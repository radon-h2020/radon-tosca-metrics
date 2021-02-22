# Number of Shell Scripts

## Description

Returns the number of shell scripts called by a blueprint. 

---

## Example
The following example has **1 shell script**.

``` yaml
tosca_definitions_version: tosca_simple_yaml_1_3

description: Template for deploying a single server with MySQL software on top.

topology_template:
  node_templates:
    db_server:
      type: tosca.nodes.Compute

    mysql:
      type: tosca.nodes.DBMS.MySQL
      properties:
        root_password: { get_input: mysql_rootpw }
        port: { get_input: mysql_port }
      requirements:
        - host: db_server
      interfaces:
        Standard:
          configure: scripts/my_own_configure.sh
```

---

## Parameters


|   | **Type** | **Description** |
|---|---|---|
**Input:**| `str`| A TOSCA blueprint|
**Output:**| `unsigned int`| The number of imports|
**Exception:**| `TypeError`| If blueprint is empty or invalid|

---

## How to use

Below an example on how to call the metric, and the expected output for this example:

```python
from toscametrics.metrics.num_shell_scripts import NumShellScripts

yml = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ndescription: Template for deploying a single server with MySQL software on top.\n\ntopology_template:\n\tnode_templates:\n\t\tdb_server:\n\t\t\ttype: tosca.nodes.Compute\n\n\t\tmysql:\n\t\t\ttype: tosca.nodes.DBMS.MySQL\n\t\t\tproperties:\n\t\t\t\troot_password: { get_input: mysql_rootpw }\n\t\t\t\tport: { get_input: mysql_port }\n\t\t\trequirements:\n\t\t\t\t- host: db_server\n\t\t\tinterfaces:\n\t\t\t\tStandard:\n\t\t\t\t\tconfigure: scripts/my_own_configure.sh'
yml = str.expandtabs(2)  # substitute \t with 2 spaces and create the StringIO object
print('Number of shell scripts: ' + NumShellScripts(yml).count())

>>> Number of shell scripts: 1
```