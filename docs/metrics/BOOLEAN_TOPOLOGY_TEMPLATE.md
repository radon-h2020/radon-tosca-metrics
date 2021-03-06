# Boolean if there is a topology template defined in a blueprint (TTB)

## Description

Returns the boolean value whether or not a topology template is defined in a blueprint template. 

---

## Parameters

**_Input_:**

* ```yaml : StringIO``` -- a StringIO object representing a yaml file;

**_Output_:** 

* a _boolean_.

**_Exception_:**

* ```YAMLError``` if the value of ```yaml``` does not represent a valid yaml file. 

---

## Example
The following example returns **True**.

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
>>> from toscametrics.metrics.ttb import TTB

>>> str = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ntopology_template:\n  relationship_templates:\n    storage_attachesto_1:\n      type: MyAttachesTo\n      properties:\n        location: /my_data_location\n\n  relationship_types:\n    MyAttachesTo:\n      derived_from: AttachesTo\n      interfaces:\n        some_interface_name:\n          some_operation:\n            implementation: default_script.sh\n'

>>> yml = StringIO(str.expandtabs(2)) #substitute \t with 2 spaces and create the StringIO object
>>> metric = TTB(yml)
>>> print('TTB: ' + str(metric.check()))

TTB: True
```