# Number of Custom Defined Data Types in a blueprint (CDDT)

## Description

Returns the number of custom defined data types within a blueprint template.

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
The following example has **1 custom defined data types**.

``` yaml
tosca_definitions_version: tosca_simple_yaml_1_1

data_types:
  NetworkInfo:
    derived_from: tosca.Data.Root
    properties:
      name:
        type: string
      gateway:
        type: string      

  RouterInfo:
    derived_from: tosca.Data.Root
    properties:
      ip:
        type: string
      external:
        type: string

topology_template:
  inputs:
    management_network:
      type: NetworkInfo
    router:
      type: RouterInfo
```

---

Below an example on how to call the metric and the expected output for this example:

```python
>>> from io import StringIO
>>> from toscametrics.metrics.cddt import CDDT

>>> str = 'tosca_definitions_version: tosca_simple_yaml_1_1\n\ndata_types:\n  NetworkInfo:\n    derived_from: tosca.Data.Root\n    properties:\n      name:\n        type: string\n      gateway:\n        type: string      \n\n  RouterInfo:\n    derived_from: tosca.Data.Root\n    properties:\n      ip:\n        type: string\n      external:\n        type: string\n\ntopology_template:\n  inputs:\n    management_network:\n      type: NetworkInfo\n    router:\n      type: RouterInfo'

>>> yml = StringIO(str.expandtabs(2)) #substitute \t with 2 spaces and create the StringIO object
>>> metric = CDDT(yml)
>>> print('CDDT: ', metric.count())

CDDT: 2
```