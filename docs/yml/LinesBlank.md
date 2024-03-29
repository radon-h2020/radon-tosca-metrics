# Number of blank lines

## Description

Returns the number of _blank_ lines in a yaml file.

---

## Example
The following example has **2 blank lines**.

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

## Parameters


|   | **Type** | **Description** |
|---|---|---|
**Input:**| `str`| A TOSCA blueprint|
**Output:**| `unsigned int`| The number of blank lines|
**Exception:**| `TypeError`| If the input file is not a valid TOSCA blueprint or is empty |


---

## How to use

Below an example on how to call the metric and the expected output for this example:

```python
from toscametrics.general.lines_blank import LinesBlank

yml = 'TODO' 
yml = yml.expands(2)
print('Lines blank: ' + LinesBlank(yml).count())

>>> Lines blank: 2
```