# Text entropy

## Description

Returns the blueprint's text entropy.

---

## Example
The following example has **an entropy of 5.35**.

``` yaml
tosca_definitions_version: tosca_simple_yaml_1_0

description: Template for deploying a single server with predefined properties.

topology_template:
  inputs:
    cpus:
      type: integer
      description: Number of CPUs for the server.
      constraints:
        - valid_values: [ 1, 2, 4, 8 ]

  node_templates:
    my_server:
      type: tosca.nodes.Compute
      capabilities:
        # Host container properties
        host:
          properties:
            # Compute properties
            num_cpus: { get_input: cpus }
            mem_size: 2048  MB
            disk_size: 10 GB
```

---

## Parameters


|   | **Type** | **Description** |
|---|---|---|
**Input:**| `io.StringIO`| A TOSCA blueprint|
**Output:**| `float`| The text entropy|
**Exception:**| `TypeError`| If the blueprint is empty or not valid |

---

## How to use



Below an example on how to call the metric and the expected output for this example:

```python
from io import StringIO
from toscametrics.yml.text_entropy import TextEntropy

str = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template for deploying a single server with predefined properties.\n\ntopology_template:\n  inputs:\n    cpus:\n      type: integer\n      description: Number of CPUs for the server.\n      constraints:\n        - valid_values: [ 1, 2, 4, 8 ]\n\n  node_templates:\n    my_server:\n      type: tosca.nodes.Compute\n      capabilities:\n        # Host container properties\n        host:\n          properties:\n            # Compute properties\n            num_cpus: { get_input: cpus }\n            mem_size: 2048  MB\n            disk_size: 10 GB'
yml = StringIO(str.expands(2))  # substitute \t with 2 spaces and create the StringIO object
print('Text entropy: ' + TextEntropy(yml).count())

>>> Text entropy: 5.35
```