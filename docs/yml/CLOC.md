# Number of commented lines of code (CLOC)

## Description

Returns the number of _commented_ lines of code in a yaml file.

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

Below an example on how to call the metric and the expected output for this example:

```python
>>> from io import StringIO
>>> from toscametrics.yml.cloc import CLOC

>>> str = 'tasks:\n\t- name: Find all instances in the specified region\n\t\tali_instance_facts ...' 
>>> yml = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
>>> metric = CLOC(yml)
>>> print('CLOC: ' + str(metric.count()))

CLOC: 2
```