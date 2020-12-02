# Number of suspicious comments

## Description

Returns the number of suspicious comments in a blueprint, i.e., 
those containing at least one of the following keywords: `TODO, FIXME, HACK, XXX, CHECKME, DOCME, TESTME, PENDING`.


---


## Example
The following example has **1 suspicious comment**.

``` yaml
tosca_definitions_version: tosca_simple_yaml_1_0

description: Template for deploying a single server with predefined properties.

#TODO: add extra valid values 
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
**Output:**| `unsigned int`| The number of suspicious comments|
**Exception:**| `TypeError`| If blueprint is empty or invalid|

---

## How to use


Below an example on how to call the metric and the expected output for this example:

```python
from io import StringIO
from toscametrics.yml.num_suspicious_comments import NumSuspiciousComments

str = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template for deploying a single server with predefined properties.\n\n#TODO: add extra valid values \ntopology_template:\n  inputs:\n    cpus:\n      type: integer\n      description: Number of CPUs for the server.\n      constraints:\n        - valid_values: [ 1, 2, 4, 8 ]'
yml = StringIO(str.expands(2))  # substitute \t with 2 spaces and create the StringIO object
print('Number of suspicious comments: ' + NumSuspiciousComments(yml).count)

>>> Number of suspicious comments: 1
```