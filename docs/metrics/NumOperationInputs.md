# Number of Operations Inputs 

## Description

Returns the blueprint's number of inputs within a `operations` block. 

`Interfaces Types` define *operations* that can be invoked on nodes or relationships by the Orchestrator.
An operation definition defines a named function or procedure that can be bound to an operation implementation.
There might be inputs that need to be provided to each operation.


---

## Example
The following example has **1 input**, namely `storage_url`.


``` yaml
topology_template:
  node_templates:
    my_server:
      type: tosca.nodes.Compute

    mysql:
      type: tosca.nodes.DBMS.MySQL

      requirements:
        - host: my_server

      interfaces:
        tosca.interfaces.nodes.custom.Backup:
          operations:
            backup:
              implementation: backup.sh
              inputs:
                storage_url: { get_input: storage_url }
```

---


## Parameters


|   | **Type** | **Description** |
|---|---|---|
**Input:**| `io.StringIO`| A TOSCA blueprint|
**Output:**| `unsigned int`| The number of `operations` inputs |
**Exception:**| `TypeError`| If blueprint is empty or invalid|

---

## How to use



Below an example on how to call the metric and the expected output for this example:

```python
from io import StringIO
from toscametrics.metrics.num_operation_inputs import NumOperationInputs

str = 'topology_template:\n  inputs:\n    numberOfSites:\n      type: integer\n    locations:\n      type: list\n      entry_schema: Location\n\n  node_templates:\n    sdwan:\n      type: VPN\n    site:\n      type: VPNSite\n      occurrences: [1, UNBOUNDED]\n      instance_count: { get_input: numberOfSites }\n      properties:\n        location: { get_input: [ locations, INDEX ] }\n      requirements:\n        - vpn: sdwan\n'  # part of ninp_2_1.yaml
yml = StringIO(str.expandtabs(2))  # substitute \t with 2 spaces and create the StringIO object
print('Number of operation inputs: ' + str(NumOperationInputs(yml).count()))

>>> Number of operation inputs: 1
```