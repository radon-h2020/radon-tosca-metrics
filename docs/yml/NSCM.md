# Number of suspicious comments (NSCM)

## Description

Returns the number of suspicious comments in a yaml file, i.e., those containing at least one of the following keywords: ```TODO, FIXME, HACK, XXX, CHECKME, DOCME, TESTME, PENDING```

---

## Parameters

**_Input_:**

* ```yaml : StringIO``` -- a StringIO object representing a yaml file;

**_Output_:** 

* an _integer >= 0_.

**_Exception_:**

* ```YAMLError``` if the value of ```yaml``` does not represent a valid yaml file.

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

Below an example on how to call the metric and the expected output for this example:

```python
>>> from io import StringIO
>>> from toscametrics.yml.nscm import NSCM

>>> str = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template for deploying a single server with predefined properties.\n\n#TODO: add extra valid values \ntopology_template:\n  inputs:\n    cpus:\n      type: integer\n      description: Number of CPUs for the server.\n      constraints:\n        - valid_values: [ 1, 2, 4, 8 ]'

>>> yml = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
>>> metric = NSCM(yml)
>>> print('NSCM: ' + str(metric.count()))

NSCM: 1
```