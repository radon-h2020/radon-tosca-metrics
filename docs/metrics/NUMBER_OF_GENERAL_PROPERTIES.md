# Number of General Properties in a blueprint (NGP)

## Description

Returns the number of properties within the entire blueprint template, not only for capabilities. 

---

## Parameters

**_Input_:**

* ```yaml : StringIO``` -- a StringIO object representing a yaml file;

**_Output_:** 

* a _float >= 0_.

**_Exception_:** 

* ```YAMLError``` if the value of ```yaml``` does not represent a valid yaml file. 

---

## Example
The following example has **4 rproperties**.

``` yaml
tosca_definitions_version: alien_dsl_2_0_0

node_types:
  org.ystia.ssl.ansible.certificates.nodes.SSLCertificateGenerator:
    derived_from: tosca.nodes.SoftwareComponent
    properties:
      common_name:
        type: string
        description: Certificate common name
      key_path:
        type: string
        description: Path of a directory where private keys should be stored.
      certificate_path:
        type: string
        description: Path of a directory where certificates should be stored.
      linux_owner:
        type: string
```

---

Below an example on how to call the metric and the expected output for this example:

```python
>>> from io import StringIO
>>> from toscametrics.metrics.ngp import NGP

>>> str = 'tosca_definitions_version: alien_dsl_2_0_0\n\nnode_types:\n  org.ystia.ssl.ansible.certificates.nodes.SSLCertificateGenerator:\n    derived_from: tosca.nodes.SoftwareComponent\n    properties:\n      common_name:\n        type: string\n        description: Certificate common name\n      key_path:\n        type: string\n        description: Path of a directory where private keys should be stored.\n      certificate_path:\n        type: string\n        description: Path of a directory where certificates should be stored.\n      linux_owner:\n        type: string'

>>> yml = StringIO(str.expandtabs(2)) #substitute \t with 2 spaces and create the StringIO object
>>> metric = NGP(yml)
>>> print('NGP count: ', metric.count())

NGP count: 4
```