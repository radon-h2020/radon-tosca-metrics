# Number of Capabilities per node in a blueprint (NC)

## Description

Returns the number of capabilities per node within a blueprint template. To aggregate them, the number, min, max, mean and median are calculated.

---

## Parameters

**_Input_:**

* ```yaml : StringIO``` -- a StringIO object representing a yaml file;

**_Output_:** 

* a _float >= 0_.

**_Exception_:** CHECK IF THIS SECTION IS CORRECT!!

* ```YAMLError``` if the value of ```yaml``` does not represent a valid yaml file. 
* ```AttributeError``` and return of 0 if the yaml file does not contain the key ```node_templates```

---

## Example
The following example has **1 node, which contains 2 capabilities**.

``` yaml
tosca_definitions_version: tosca_simple_yaml_1_0

description: Template with requirements against hosting infrastructure.

topology_template:
  inputs:
    # omitted here for brevity

   node_templates:
    mysql:
      type: tosca.nodes.DBMS.MySQL
      properties:
        # omitted here for brevity

      requirements:
        - host:
            node_filter:
              capabilities:
                - host:
                    properties:
                      - num_cpus: { in_range: [ 1, 4 ] }
                      - mem_size: { greater_or_equal: 2 GB }
                - os:
                    properties:
                      - architecture: { equal: x86_64 }
                      - type: linux
                      - distribution: ubuntu
```

---

Below an example on how to call the metric and the expected output for this example:

```python
>>> from io import StringIO
>>> from toscametrics.blueprint.nc import NC

>>> str = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template with requirements against hosting infrastructure.\n\ntopology_template:\n  inputs:\n    # omitted here for brevity\n\n   node_templates:\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        # omitted here for brevity\n      requirements:\n        - host:\n            node_filter:\n              capabilities:\n                - host:\n                    properties:\n                      - num_cpus: { in_range: [ 1, 4 ] }\n                      - mem_size: { greater_or_equal: 2 GB }\n                - os:\n                    properties:\n                      - architecture: { equal: x86_64 }\n                      - type: linux\n                      - distribution: ubuntu'

>>> yml = StringIO(str.expandtabs(2)) #substitute \t with 2 spaces and create the StringIO object
>>> metric = NC(yml)
>>> print('NC count: ', metric.count())
>>> print('NC min: ', metric.min())
>>> print('NC max: ', metric.max())
>>> print('NC mean: ', metric.mean())
>>> print('NC median: ', metric.median())

NC count: 2
NC min: 2
NC max: 2
NC mean: 2
NC median: 2
```