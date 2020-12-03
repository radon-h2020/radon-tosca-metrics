# Number of Relationship Template

## Description

Returns the number of relationship templates within a blueprint. 

A Relationship Template specifies the occurrence of a relationship between nodes in a Topology Template. 
Each Relationship Template refers to a Relationship Type that defines the semantics relationship (e.g., properties, attributes, interfaces, etc.). 
Relationship Types are defined separately for reuse purposes.

---

## Example
The following example has **2 relationship templates**, namely, `storage_attachesto_1` and `storage_attachesto_2`).

``` yaml
tosca_definitions_version: tosca_simple_yaml_1_3
topology_template:
  relationship_templates:
    storage_attachesto_1:
      type: MyAttachesTo
      properties:
        location: /my_data_location
    storage_attachesto_2:
      type: MyAttachesTo
      properties:
        location: /some_other_data_location

  relationship_types:
    MyAttachesTo:
      derived_from: AttachesTo
      interfaces:
        some_interface_name:
          some_operation:
            implementation: default_script.sh
```

---

## Parameters


|   | **Type** | **Description** |
|---|---|---|
**Input:**| `io.StringIO`| A TOSCA blueprint|
**Output:**| `unsigned int`| The number of relationship templates|
**Exception:**| `TypeError`| If blueprint is empty or invalid|

---

## How to use



Below an example on how to call the metric, and the expected output for this example:

```python
from io import StringIO
from toscametrics.metrics.num_relationship_templates import NumRelationshipTemplates

str = 'topology_template:\n\n  inputs:\n\n    mysql_rootpw:\n\n      type: string\n\n    mysql_port:\n\n      type: integer\n\n    # rest omitted here for brevity\n\n \n\n  node_templates:\n\n    db_server:\n\n      type: tosca.nodes.Compute\n\n      # rest omitted here for brevity\n\n \n\n    mysql:\n\n      type: tosca.nodes.DBMS.MySQL'
yml = StringIO(str.expandtabs(2))  # substitute \t with 2 spaces and create the StringIO object
print('Number of relationship templates: ' + NumRelationshipTemplates(yml).count())

>>> Number of relationship templates: 2
```