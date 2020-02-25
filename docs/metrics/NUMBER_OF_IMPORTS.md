# Number of Imports in a blueprint (NI)

## Description

Returns the number of imports within a blueprint template. 

---

## Parameters

**_Input_:**

* ```yaml : StringIO``` -- a StringIO object representing a yaml file;

**_Output_:** 

* an _integer >= 0_.

**_Exception_:**

* ```YAMLError``` if the value of ```yaml``` does not represent a valid yaml file. 
* ```TypeError``` and return of 0 if the yaml file does not contain the key ```imports```

---

## Example
The following example has **2 imports**.

``` yaml
imports:
  - some_definition_file: path1/path2/some_defs.yaml
  - another_definition_file:
      file: path1/path2/file2.yaml
      repository: my_service_catalog
      namespace_uri: http://mycompany.com/tosca/1.0/platform
      namespace_prefix: mycompany
```

---

Below an example on how to call the metric and the expected output for this example:

```python
>>> from io import StringIO
>>> from toscametrics.metrics.ni import NI

>>> str = 'imports:\n  - some_definition_file: path1/path2/some_defs.yaml\n  - another_definition_file:\n      file: path1/path2/file2.yaml\n      repository: my_service_catalog\n      namespace_uri: http://mycompany.com/tosca/1.0/platform\n      namespace_prefix: mycompany'

>>> yml = StringIO(str.expandtabs(2)) #substitute \t with 2 spaces and create the StringIO object
>>> metric = NI(yml)
>>> print('NI: ' + str(metric.count()))

NI: 2
```