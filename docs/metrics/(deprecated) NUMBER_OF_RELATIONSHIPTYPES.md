# Number of Relationship Types in a blueprint (NRT)

## Description

Returns the number of relationship types within a blueprint template. 

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
The following example has **2 relationship types**.

``` yaml
tosca_definitions_version: tosca_simple_yaml_1_0

topology_template:
  relationship_templates:
    storage_attachesto_1:
      type: MyAttachesTo
      properties:
        location: /my_data_location
    
    my_connectsto_relationship:
      type: tosca.relationships.ConnectsTo
      interfaces:
        Configure:
          inputs:
            speed: { get_attribute: [ SOURCE, connect_speed ] } 
```

---

Below an example on how to call the metric and the expected output for this example:

```python
>> > from io import StringIO
>> > from toscametrics.metrics.nrt import NRT

>> > str = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ntopology_template:\n  relationship_templates:\n    storage_attachesto_1:\n      type: MyAttachesTo\n      properties:\n        location: /my_data_location\n    \n    my_connectsto_relationship:\n      type: tosca.relationships.ConnectsTo\n      interfaces:\n        Configure:\n          inputs:\n            speed: { get_attribute: [ SOURCE, connect_speed ] } '

>> > yml = StringIO(str.expandtabs(2))  # substitute \t with 2 spaces and create the StringIO object
>> > metric = NRT(yml)
>> > print('NRT: ', metric.count)

NRT: 2
```