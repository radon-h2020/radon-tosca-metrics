# Number of lines of code

## Description

Returns the number of _executable_ source lines of code in a yaml file.
Blank and commented lines do not count as _source lines of code_.

---


## Example
The following example has **8 source lines of code**. 

``` yaml
---
- hosts: localhost

  tasks:
  - name: task 1
    include_vars:
      file: username_info.yml

  - name: task 2
    include_vars:
      file: username_info.yml
```

---

|   | **Type** | **Description** |
|---|---|---|
**Input:**| `io.StringIO`| A TOSCA blueprint|
**Output:**| `unsigned int`| The number of executable source lines of code|
**Exception:**| `TypeError`| If the input file is not a valid TOSCA blueprint or is empty |


---

## How to use


Below an example on how to call the metric and the expected output for this example:

```python
from io import StringIO
from toscametrics.yml.lines_code import LinesCode

str = 'TODO' 
blueprint = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
metric = LinesCode(blueprint)
print('Lines of code: ' + str(metric.count()))

>>> Lines of code: 8
```