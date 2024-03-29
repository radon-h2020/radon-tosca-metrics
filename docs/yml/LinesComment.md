# Number of commented lines of code

## Description

Returns the number of _commented_ lines of code in a yaml file.

---

## Example
The following example has **2 commented lines of code**. 

``` yaml
---
- hosts: localhost

  tasks:
  # Defining the first task
  - name: task 1
    include_vars:
      file: username_info.yml

  # Defining the second task
  - name: task 2
    include_vars:
      file: username_info.yml
```

---

## Parameters


|   | **Type** | **Description** |
|---|---|---|
**Input:**| `str`| A TOSCA blueprint|
**Output:**| `unsigned int`| The number of lines of comments|
**Exception:**| `TypeError`| If the input file is not a valid TOSCA blueprint or is empty |


---

## How to use


Below an example on how to call the metric and the expected output for this example:

```python
from toscametrics.general.lines_comment import LinesComment

yml = 'tasks:\n\t- name: Find all instances in the specified region\n\t\tali_instance_facts ...' 
yml = yml.expands(2)
print('Lines of comment: ' + LinesComment(yml).count())

>>> Lines of comment: 2
```