# Number of Filters in a blueprint (NF)

## Description

Returns the number of node and/or substition filters used in a blueprint template.

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
The following example has **1 node filter**.

``` yaml
tosca_definitions_version: tosca_simple_yaml_1_3
             
description: Template with requirements against hosting infrastructure.

topology_template:
  node_templates:
    mysql:
      type: tosca.nodes.DBMS.MySQL
      requirements:
        - host: mysql_compute

    mysql_compute:
      type: Compute
      directives: [ select ]
      node_filter:
        capabilities:
          - host:
              properties:
                num_cpus: { equal: 2 }
                mem_size: { greater_or_equal: 2 GB }
          - os:
              properties:
                architecture: { equal: x86_64 }
                type: linux
                distribution: ubuntu
```

---

Below an example on how to call the metric and the expected output for this example:

```python
>>> from io import StringIO
>>> from toscametrics.metrics.nf import NF

>>> str = 'tosca_definitions_version: tosca_simple_yaml_1_3\n             \ndescription: Template with requirements against hosting infrastructure.\n\ntopology_template:\n  node_templates:\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      requirements:\n        - host: mysql_compute\n\n    mysql_compute:\n      type: Compute\n      directives: [ select ]\n      node_filter:\n        capabilities:\n          - host:\n              properties:\n                num_cpus: { equal: 2 }\n                mem_size: { greater_or_equal: 2 GB }\n          - os:\n              properties:\n                architecture: { equal: x86_64 }\n                type: linux\n                distribution: ubuntu'

>>> yml = StringIO(str.expandtabs(2)) #substitute \t with 2 spaces and create the StringIO object
>>> metric = NF(yml)
>>> print('NF: ', metric.count())

NF: 1
```