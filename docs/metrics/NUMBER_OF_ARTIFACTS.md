# Number of Artifacts in a blueprint (NA)

## Description

Returns the number of Artifacts within a blueprint template.

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
The following example has **1 artifact**.

``` yaml
tosca_definitions_version: alien_dsl_2_0_0

topology_template:
  node_templates:
    Logstash:
      type: org.ystia.logstash.linux.bash.nodes.Logstash
      properties:
        repository: { get_input: repository }
      artifacts:
        filters_conf:
          file: config/logstash-apache-generator-filters.conf
          type: tosca.artifacts.File
```

---

Below an example on how to call the metric and the expected output for this example:

```python
>>> from io import StringIO
>>> from toscametrics.blueprint.na import NA

>>> str = 'tosca_definitions_version: alien_dsl_2_0_0\n\ntopology_template:\n  node_templates:\n    Logstash:\n      type: org.ystia.logstash.linux.bash.nodes.Logstash\n      properties:\n        repository: { get_input: repository }\n      artifacts:\n        filters_conf:\n          file: config/logstash-apache-generator-filters.conf\n          type: tosca.artifacts.File'

>>> yml = StringIO(str.expandtabs(2)) #substitute \t with 2 spaces and create the StringIO object
>>> metric = NA(yml)
>>> print('NA: ', metric.count())

NA: 1
```