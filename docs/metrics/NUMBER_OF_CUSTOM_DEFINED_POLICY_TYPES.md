# Number of Custom Defined Policy Types in a blueprint (CDPT)

## Description

Returns the number of custom defined policy types within a blueprint template.

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
The following example has **1 custom defined policy types**.

``` yaml
tosca_definitions_version: tosca_simple_yaml_1_2

node_types:
  tosca.nodes.Root:
    attributes:
      tosca_id:
        type: string
      tosca_name:
        type: string

policy_types:
  mycompany.mytypes.policies.placement.Container.Linux:
    description: My company’s placement policy for linux
    derived_from: tosca.policies.Root
```

---

Below an example on how to call the metric and the expected output for this example:

```python
>>> from io import StringIO
>>> from toscametrics.blueprint.cdpt import CDPT

>>> str = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\nnode_types:\n  tosca.nodes.Root:\n    attributes:\n      tosca_id:\n        type: string\n      tosca_name:\n        type: string\n\npolicy_types:\n  mycompany.mytypes.policies.placement.Container.Linux:\n    description: My companyâ€™s placement policy for linux\n    derived_from: tosca.policies.Root\n'

>>> yml = StringIO(str.expandtabs(2)) #substitute \t with 2 spaces and create the StringIO object
>>> metric = CDPT(yml)
>>> print('CDPT: ', metric.count())

CDPT: 1
```