# Number of General Capabilities in a blueprint (NGC)

## Description

Returns the number of capabilities in an entire blueprint template, not only in node templates. 

---

## Parameters

**_Input_:**

* ```yaml : StringIO``` -- a StringIO object representing a yaml file;

**_Output_:** 

* a _float >= 0_.

**_Exception_:** 

* ```YAMLError``` if the value of ```yaml``` does not represent a valid yaml file. 

---

## Example
The following example has **1 capability**.

``` yaml
tosca_definitions_version: alien_dsl_2_0_0

node_types:
  org.ystia.mysql.linux.bash.nodes.MySQLServer:
    derived_from: org.ystia.nodes.DBMS
    description: MySQL Server component for linux
    capabilities:
      host:
        type: org.ystia.mysql.pub.capabilities.Container.MySQLServer
```

---

Below an example on how to call the metric and the expected output for this example:

```python
>>> from io import StringIO
>>> from toscametrics.blueprint.ngc import NGC

>>> str = 'tosca_definitions_version: alien_dsl_2_0_0\n\nnode_types:\n  org.ystia.mysql.linux.bash.nodes.MySQLServer:\n    derived_from: org.ystia.nodes.DBMS\n    description: MySQL Server component for linux\n    capabilities:\n      host:\n        type: org.ystia.mysql.pub.capabilities.Container.MySQLServer'

>>> yml = StringIO(str.expandtabs(2)) #substitute \t with 2 spaces and create the StringIO object
>>> metric = NGC(yml)
>>> print('NGC count: ', metric.count())

NGC count: 1
```