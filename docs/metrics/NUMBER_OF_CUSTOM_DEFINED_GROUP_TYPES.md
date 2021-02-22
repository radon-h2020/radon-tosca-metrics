# Number of Custom Defined Group Types in a blueprint (CDGT)

## Description

Returns the number of custom defined group types within a blueprint template.

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
The following example has **1 custom defined group types**.

``` yaml
tosca_definitions_version: tosca_simple_yaml_1_2

node_types:
  tosca.nodes.Root:
    attributes:
      tosca_id:
        type: string
      tosca_name:
        type: string

  tosca.nodes.Compute:
    attributes:
      private_address:
        type: string
      public_address:
        type: string
        
group_types:
  mycompany.mytypes.groups.placement:
    description: My company’s group type for placing nodes of type Compute
    members: [ tosca.nodes.Compute ]
```

---

Below an example on how to call the metric and the expected output for this example:

```python
>>> from io import StringIO
>>> from toscametrics.blueprint.cdgt import CDGT

>>> str = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\nnode_types:\n  tosca.nodes.Root:\n    attributes:\n      tosca_id:\n        type: string\n      tosca_name:\n        type: string\n\n  tosca.nodes.Compute:\n    attributes:\n      private_address:\n        type: string\n      public_address:\n        type: string\n        \ngroup_types:\n  mycompany.mytypes.groups.placement:\n    description: My companyâ€™s group type for placing nodes of type Compute\n    members: [ tosca.nodes.Compute ]\n'

>>> yml = StringIO(str.expandtabs(2)) #substitute \t with 2 spaces and create the StringIO object
>>> metric = CDGT(yml)
>>> print('CDGT: ', metric.count())

CDGT: 1
```