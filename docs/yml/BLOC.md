# Number of blank lines of code (BLOC)

## Description

Returns the number of _blank_ lines of code in a yaml file.

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
The following example has **2 blank lines of code**.

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

Below an example on how to call the metric and the expected output for this example:

```python
>>> from io import StringIO
>>> from toscametrics.yml.bloc import BLOC

>>> str = 'TODO' 
>>> yml = StringIO(str.expands(2)) # substitute \t with 2 spaces and create the StringIO object
>>> metric = BLOC(yml)
>>> print('BLOC: ' + str(metric.count()))

BLOC: 2
```