# Number of Custom Defined Interface Types in a blueprint (CDIT)

## Description

Returns the number of custom defined interface types within a blueprint template.

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
The following example has **2 custom defined interface types**.

``` yaml
tosca_definitions_version: tosca_simple_yaml_1_2

interface_types:

  tosca.interfaces.Root:
    metadata:
      normative: 'true'

  tosca.interfaces.node.lifecycle.Standard:
    metadata:
      normative: 'true'
    derived_from: tosca.interfaces.Root
```

---

Below an example on how to call the metric and the expected output for this example:

```python
>>> from io import StringIO
>>> from toscametrics.blueprint.cdit import CDIT

>>> str = "tosca_definitions_version: tosca_simple_yaml_1_2\n\ninterface_types:\n\n  tosca.interfaces.Root:\n    metadata:\n      normative: 'true'\n\n  tosca.interfaces.node.lifecycle.Standard:\n    metadata:\n      normative: 'true'\n    derived_from: tosca.interfaces.Root"

>>> yml = StringIO(str.expandtabs(2)) #substitute \t with 2 spaces and create the StringIO object
>>> metric = CDIT(yml)
>>> print('CDIT: ', metric.count())

CDIT: 2
```