# Number of Parameters 

## Description

Returns the number of inputs within a blueprint template. 

`Interfaces Types` define inputs that need to be provided to each operation. 
This inputs can be considered as method's parameters. 

---

## Example
The following example has **5 parameters**, namely `db_host`, `db_port`, `db_name`, `db_user`, `db_password`.


``` yaml
tosca_definitions_version: tosca_simple_yaml_1_3
topology_template:

  inputs:
    # Admin user name and password to use with the WordPress application
    wp_admin_username:
      type: string
    wp_admin_password:
      type: string
    context_root:
      type: string

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
            db_name: { get_property: [ wordpress_db, name ] }
            db_user: { get_property: [ wordpress_db, user ] }
            db_password: { get_property: [ wordpress_db, password ] }
```

---


## Parameters


|   | **Type** | **Description** |
|---|---|---|
**Input:**| `io.StringIO`| A TOSCA blueprint|
**Output:**| `unsigned int`| The number of parameters |
**Exception:**| `TypeError`| If blueprint is empty or invalid|

---

## How to use



Below an example on how to call the metric and the expected output for this example:

```python
from io import StringIO
from toscametrics.metrics.num_parameters import NumParameters

str = 'topology_template:\n  inputs:\n    numberOfSites:\n      type: integer\n    locations:\n      type: list\n      entry_schema: Location\n\n  node_templates:\n    sdwan:\n      type: VPN\n    site:\n      type: VPNSite\n      occurrences: [1, UNBOUNDED]\n      instance_count: { get_input: numberOfSites }\n      properties:\n        location: { get_input: [ locations, INDEX ] }\n      requirements:\n        - vpn: sdwan\n'  # part of ninp_2_1.yaml
yml = StringIO(str.expandtabs(2))  # substitute \t with 2 spaces and create the StringIO object
print('Number of parameters: ' + str(NumParameters(yml).count()))

>>> Number of parameters: 2
```