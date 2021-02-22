# Number of Custom Defined Capability Types in a blueprint (CDCT)

## Description

Returns the number of custom defined capability types within a blueprint template.

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
The following example has **1 custom defined capability types**.

``` yaml
tosca_definitions_version: tosca_simple_yaml_1_1

capability_types:

  tosca.capabilities.Root:
    metadata:
      normative: 'true'
      citation: '[TOSCA-Simple-Profile-YAML-v1.1]'
      citation_location: 5.5.1
```

---

Below an example on how to call the metric and the expected output for this example:

```python
>>> from io import StringIO
>>> from toscametrics.blueprint.cdct import CDCT

>>> str = "tosca_definitions_version: tosca_simple_yaml_1_1\n\ncapability_types:\n\n  tosca.capabilities.Root:\n    metadata:\n      normative: 'true'\n      citation: '[TOSCA-Simple-Profile-YAML-v1.1]'\n      citation_location: 5.5.1"

>>> yml = StringIO(str.expandtabs(2)) #substitute \t with 2 spaces and create the StringIO object
>>> metric = CDCT(yml)
>>> print('CDCT: ', metric.count())

CDCT: 1
```