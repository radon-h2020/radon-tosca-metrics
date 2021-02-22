# Number of Custom Defined Relationship Types in a blueprint (CDRT)

## Description

Returns the number of custom defined relationship types within a blueprint template.

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
The following example has **1 custom defined relationship types**.

``` yaml
tosca_definitions_version: tosca_simple_yaml_1_0

topology_template:
  relationship_templates:
    storage_attachesto_1:
      type: MyAttachesTo
      properties:
        location: /my_data_location

relationship_types:
  MyAttachesTo:
    derived_from: AttachesTo
    interfaces:
      some_interface_name:
        some_operation:
          implementation: default_script.sh
```

---

Below an example on how to call the metric and the expected output for this example:

```python
>>> from io import StringIO
>>> from toscametrics.blueprint.cdrt import CDRT

>>> str = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ntopology_template:\n  relationship_templates:\n    storage_attachesto_1:\n      type: MyAttachesTo\n      properties:\n        location: /my_data_location\n\n  relationship_types:\n    MyAttachesTo:\n      derived_from: AttachesTo\n      interfaces:\n        some_interface_name:\n          some_operation:\n            implementation: default_script.sh\n'

>>> yml = StringIO(str.expandtabs(2)) #substitute \t with 2 spaces and create the StringIO object
>>> metric = CDRT(yml)
>>> print('CDRT: ', metric.count())

CDRT: 1
```