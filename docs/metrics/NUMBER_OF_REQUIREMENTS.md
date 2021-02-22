# Number of Requirements in a blueprint (NRQ)

## Description

Returns the number of requirements within a blueprint template.

---

## Parameters

**_Input_:**

* ```yaml : StringIO``` -- a StringIO object representing a yaml file;

**_Output_:** 

* a _float >= 0_.

**_Exception_:** CHECK IF THIS SECTION IS CORRECT!!

* ```YAMLError``` if the value of ```yaml``` does not represent a valid yaml file. 

---

## Example
The following example has **1 requirement**.

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
>>> from toscametrics.blueprint.nrq import NRQ

>>> str = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template with requirements against hosting infrastructure.\n\ntopology_template:\n  inputs:\n    # omitted here for brevity\n\n   node_templates:\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        # omitted here for brevity\n      requirements:\n        - host:\n            node_filter:\n              capabilities:\n                - host:\n                    properties:\n                      - num_cpus: { in_range: [ 1, 4 ] }\n                      - mem_size: { greater_or_equal: 2 GB }\n                - os:\n                    properties:\n                      - architecture: { equal: x86_64 }\n                      - type: linux\n                      - distribution: ubuntu'

>>> yml = StringIO(str.expandtabs(2)) #substitute \t with 2 spaces and create the StringIO object
>>> metric = NRQ(yml)
>>> print('NRQ count: ', metric.count())

NRQ count: 2
```