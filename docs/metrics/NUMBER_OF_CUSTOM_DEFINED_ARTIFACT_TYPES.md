# Number of Custom Defined Artifact Types in a blueprint (CDAT)

## Description

Returns the number of custom defined artifact types within a blueprint template.

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
The following example has **2 custom defined artifact types**.

``` yaml
tosca_definitions_version: tosca_simple_yaml_1_1

artifact_types:

  tosca.artifacts.Root:
    metadata:
      normative: 'true'
      
  tosca.artifacts.File:
    metadata:
      normative: 'true'
```

---

Below an example on how to call the metric and the expected output for this example:

```python
>>> from io import StringIO
>>> from toscametrics.blueprint.cdat import CDAT

>>> str = "tosca_definitions_version: tosca_simple_yaml_1_1\n\nartifact_types:\n\n  tosca.artifacts.Root:\n    metadata:\n      normative: 'true'\n      \n  tosca.artifacts.File:\n    metadata:\n      normative: 'true'"

>>> yml = StringIO(str.expandtabs(2)) #substitute \t with 2 spaces and create the StringIO object
>>> metric = CDAT(yml)
>>> print('CDAT: ', metric.count())

CDAT: 2
```