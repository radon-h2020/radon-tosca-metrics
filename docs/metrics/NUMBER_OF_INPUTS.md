# Number of Inputs in a blueprint (NINP)

## Description

Returns the number of inputs within a blueprint template. 

---

## Parameters

**_Input_:**

* ```yaml : StringIO``` -- a StringIO object representing a yaml file;

**_Output_:** 

* an _integer >= 0_.

**_Exception_:**

* ```YAMLError``` if the value of ```yaml``` does not represent a valid yaml file. 
* ```AttributeError``` and return of 0 if the yaml file does not contain the key ```node_templates```

---

## Example
The following example has **2 inputs**.

``` yaml
topology_template:
  inputs:
    numberOfSites:
      type: integer
    locations:
      type: list
      entry_schema: Location

  node_templates:
    sdwan:
      type: VPN
    site:
      type: VPNSite
      occurrences: [1, UNBOUNDED]
      instance_count: { get_input: numberOfSites }
      properties:
        location: { get_input: [ locations, INDEX ] }
      requirements:
        - vpn: sdwan
```

---

Below an example on how to call the metric and the expected output for this example:

```python
>>> from io import StringIO
>>> from toscametrics.metrics.ninp import NINP

>>> str = 'topology_template:\n  inputs:\n    numberOfSites:\n      type: integer\n    locations:\n      type: list\n      entry_schema: Location\n\n  node_templates:\n    sdwan:\n      type: VPN\n    site:\n      type: VPNSite\n      occurrences: [1, UNBOUNDED]\n      instance_count: { get_input: numberOfSites }\n      properties:\n        location: { get_input: [ locations, INDEX ] }\n      requirements:\n        - vpn: sdwan\n' #part of ninp_2_1.yaml

>>> yml = StringIO(str.expandtabs(2)) #substitute \t with 2 spaces and create the StringIO object
>>> metric = NINP(yml)
>>> print('NINP: ' + str(metric.count()))

NINP: 2
```