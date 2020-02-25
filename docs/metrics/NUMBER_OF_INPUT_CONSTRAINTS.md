# Number of relative Input Constraints in a blueprint (NINPC)

## Description

Returns the number of relative input constraints per input statement within a blueprint template. 

---

## Parameters

**_Input_:**

* ```yaml : StringIO``` -- a StringIO object representing a yaml file;

**_Output_:** 

* an _integer >= 0_.

**_Exception_:**

* ```YAMLError``` if the value of ```yaml``` does not represent a valid yaml file. 
* ```AttributeError``` and return of 0 if the yaml file does not contain the key ```topology_template```
* ```ZeroDivisionError``` return 0 if no inputs are found.

---

## Example
The following example has **2.0 input constraints per input**.

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
        - less_than: 10
```

---

Below an example on how to call the metric and the expected output for this example:

```python
>>> from io import StringIO
>>> from toscametrics.metrics.ninp import NINPC

>>> str = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template for deploying a single server with predefined properties.\n\ntopology_template:\n  inputs:\n    cpus:\n      type: integer\n      description: Number of CPUs for the server.\n      constraints:\n        - valid_values: [ 1, 2, 4, 8 ]\n        - less_than: 10' #part of ninpc_2_1.yaml

>>> yml = StringIO(str.expandtabs(2)) #substitute \t with 2 spaces and create the StringIO object
>>> metric = NINPC(yml)
>>> print('NINPC: ' + str(metric.count()))

NINPC: 2.0
```