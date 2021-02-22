# Number of Interfaces

## Description

Returns the blueprint's number of interfaces. 
Interfaces can occur in Nodes and Relationships. 

---

## Example
The following example has **2 interface**, namely `Standard` and `Configure`.

``` yaml
tosca_definitions_version: tosca_simple_yaml_1_3
topology_template:

  node_templates:
    wordpress:
      type: tosca.nodes.WebApplication.WordPress
      properties:
        admin_user: { get_input: wp_admin_username }
        admin_password: { get_input: wp_admin_password }
        db_host: { get_attribute: [ db_server, private_address ] }
      interfaces:
        Standard:
          inputs:
            db_host: { get_attribute: [ db_server, private_address ] }
            db_port: { get_property: [ mysql, port ] }

  relationship_templates:
    wp_db_connection:
      type: ConnectsTo
      interfaces:
        Configure:
          pre_configure_source: scripts/wp_db_configure.sh
```

---

## Parameters


|   | **Type** | **Description** |
|---|---|---|
**Input:**| `str`| A TOSCA blueprint|
**Output:**| `unsigned int`| The number of interfaces |
**Exception:**| `TypeError`| If blueprint is empty or invalid|

---

## How to use
Below an example on how to call the metric, and the expected output for this example:

```python
from toscametrics.blueprint.num_interfaces import NumInterfaces

yml = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\ndescription: Template for deploying a single server with MySQL software on top.\n\ntopology_template:\n  inputs:\n    mysql_rootpw:\n      type: string\n      \n    mysql_port:\n      type: integer\n    \n  node_templates:\n    db_server:\n      type: tosca.nodes.Compute\n      \n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        root_password: { get_input: my_mysql_rootpw }\n        port: { get_input: my_mysql_port }\n      requirements:\n        - host: db_server\n      interfaces:\n        Standard:\n          configure: scripts/my_own_configure.sh'
yml = yml.expandtabs(2)  # substitute \t with 2 spaces and create the StringIO object
print('Number of interfaces: ', NumInterfaces(yml).count())

>>> Number of interfaces: 2
```