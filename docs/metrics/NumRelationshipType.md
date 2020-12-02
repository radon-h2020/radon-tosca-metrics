# Number of relationship types

## Description

Returns the number of relationship types within a blueprint template. 

---

## Example
The following example has **1 relationship**.

``` yaml
tosca_definitions_version: tosca_simple_yaml_1_0

topology_template:
  relationship_templates:
    storage_attachesto_1:
      type: MyAttachesTo
      properties:
        location: /my_data_location

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
**Output:**| `unsigned int`| The number of relationship types|
**Exception:**| `TypeError`| If blueprint is empty or invalid|

---

## How to use

Below an example on how to call the metric, and the expected output for this example:

```python
from io import StringIO
from toscametrics.metrics.num_relationship_types import NumRelationshipTypes

str = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ntopology_template:\n  relationship_templates:\n    storage_attachesto_1:\n      type: MyAttachesTo\n      properties:\n        location: /my_data_location\n\n  relationship_types:\n    MyAttachesTo:\n      derived_from: AttachesTo\n      interfaces:\n        some_interface_name:\n          some_operation:\n            implementation: default_script.sh\n'
yml = StringIO(str.expandtabs(2))  # substitute \t with 2 spaces and create the StringIO object
print('Number of relationship types: ' + str(NumRelationshipTypes(yml).count))

>>> Number of relationship types: 1
```