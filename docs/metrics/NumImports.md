# Number of Imports

## Description

Returns the blueprint's number of imports. 

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

## Parameters


|   | **Type** | **Description** |
|---|---|---|
**Input:**| `io.StringIO`| A TOSCA blueprint|
**Output:**| `unsigned int`| The number of imports|
**Exception:**| `TypeError`| If blueprint is empty or invalid|

---

## How to use

Below an example on how to call the metric and the expected output for this example:

```python
from io import StringIO
from toscametrics.metrics.num_imports import NumImports

str = 'imports:\n  - some_definition_file: path1/path2/some_defs.yaml\n  - another_definition_file:\n      file: path1/path2/file2.yaml\n      repository: my_service_catalog\n      namespace_uri: http://mycompany.com/tosca/1.0/platform\n      namespace_prefix: mycompany'
yml = StringIO(str.expandtabs(2))  # substitute \t with 2 spaces and create the StringIO object
print('Number of imports: ' + str(NumImports(yml).count()))

>>> Number of imports: 2
```