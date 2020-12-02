# Number of tokens

## Description

Returns the number of tokens in a yaml file (separated by black spaces).

---

## Parameters


|   | **Type** | **Description** |
|---|---|---|
**Input:**| `io.StringIO`| a TOSCA blueprint|
**Output:**| `unsigned int`| the number of tokens|
**Exception:**| `TypeError`| a TOSCA blueprint|

**_Output_:** 

* an _integer >= 0_.

**_Exception_:**

* ```YAMLError``` if the value of ```yaml``` does not represent a valid yaml file.

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

Below an example on how to call the metric and the expected output for this example:

```python
from io import StringIO
from toscametrics.yml.ntkn import NTKN

str = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template for deploying a single server with predefined properties.\n\ntopology_template:\n  inputs:\n    cpus:\n      type: integer\n      description: Number of CPUs for the server.\n      constraints:\n        - valid_values: [ 1, 2, 4, 8 ]'

yml = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
metric = NTKN(yml)
print('Number of tokens: ' + str(metric.count()))
```

`>>> Number of tokens: 30` 