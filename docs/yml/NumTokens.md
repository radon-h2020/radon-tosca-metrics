# Number of tokens

## Description

Returns the number of tokens in a blueprint (separated by black spaces).

---

## Example
The following example has **30 tokens**.

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
```

---

## Parameters


|   | **Type** | **Description** |
|---|---|---|
**Input:**| `io.StringIO`| A TOSCA blueprint|
**Output:**| `unsigned int`| The number of tokens|
**Exception:**| `TypeError`| If the input file is not a valid TOSCA blueprint or is empty |

---


## How to use

Below an example on how to call the metric and the expected output for this example:

```python
from io import StringIO
from toscametrics.yml.num_tokens import NumTokens

str = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template for deploying a single server with predefined properties.\n\ntopology_template:\n  inputs:\n    cpus:\n      type: integer\n      description: Number of CPUs for the server.\n      constraints:\n        - valid_values: [ 1, 2, 4, 8 ]'

yml = StringIO(str.expands(2))  # substitute \t with 2 spaces and create the StringIO object
metric = NumTokens(yml)
print('Number of tokens: ' + NumTokens(yml).count())

>> > Number of tokens: 30
```
