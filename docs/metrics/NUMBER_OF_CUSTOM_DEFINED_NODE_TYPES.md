# Number of Custom Defined Node Types in a blueprint (CDNT)

## Description

Returns the number of custom defined node types within a blueprint template.

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
The following example has **3 custom defined node types**.

``` yaml
tosca_definitions_version: tosca_simple_yaml_1_2

node_types:

  tosca.nodes.Root:
    attributes:
      tosca_id:
        type: string
      tosca_name:
        type: string

  tosca.nodes.Abstract.Compute:
    derived_from: tosca.nodes.Root
    capabilities:
      host:
        type: tosca.capabilities.Compute

  tosca.nodes.Compute:
    attributes:
      private_address:
        type: string
      public_address:
        type: string
```

---

Below an example on how to call the metric and the expected output for this example:

```python
>>> from io import StringIO
>>> from toscametrics.blueprint.cdnt import CDNT

>>> str = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\nnode_types:\n\n  tosca.nodes.Root:\n    attributes:\n      tosca_id:\n        type: string\n      tosca_name:\n        type: string\n\n  tosca.nodes.Abstract.Compute:\n    derived_from: tosca.nodes.Root\n    capabilities:\n      host:\n        type: tosca.capabilities.Compute\n\n  tosca.nodes.Compute:\n    attributes:\n      private_address:\n        type: string\n      public_address:\n        type: string\n'

>>> yml = StringIO(str.expandtabs(2)) #substitute \t with 2 spaces and create the StringIO object
>>> metric = CDNT(yml)
>>> print('CDNT: ', metric.count())

CDNT: 3
```