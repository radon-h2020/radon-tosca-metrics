# Number of node types

## Description

Returns the number of node types within a blueprint. 

---

## Example
The following example has **2 node types**.

``` yaml
tosca_definitions_version: tosca_simple_yaml_1_0

description: >
  Node type that has a requirement of a capability with a defined value

node_types:

  tosca.nodes.SomeNode:
    derived_from: tosca.nodes.Root
    properties:
      some_prop:
        type: string
        required: false
        default: some
    requirements:
      - some_req:
          capability: tosca.capabilities.SomeCap
          node: tosca.nodes.NodeWithCap
          relationship: tosca.relationships.HostedOn

  tosca.nodes.NodeWithCap:
    derived_from: tosca.nodes.Root
    capabilities:
        some_req:
          type: tosca.capabilities.SomeCap
```

---


## Parameters


|   | **Type** | **Description** |
|---|---|---|
**Input:**| `str`| A TOSCA blueprint|
**Output:**| `unsigned int`| The number of relationship types|
**Exception:**| `TypeError`| If blueprint is empty or invalid|

---

## How to use

Below an example on how to call the metric, and the expected output for this example:

```python
from toscametrics.metrics.num_node_types import NumNodeTypes

yml = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: >\n\tNode type that has a requirement of a capability with a defined value\n\nnode_types:\n\n\ttosca.nodes.SomeNode:\n\t\tderived_from: tosca.nodes.Root\n\t\tproperties:\n\t\t\tsome_prop:\n\t\t\t\ttype: string\n\t\t\t\trequired: false\n\t\t\t\tdefault: some\n\t\trequirements:\n\t\t\t- some_req:\n\t\t\t\t\tcapability: tosca.capabilities.SomeCap\n\t\t\t\t\tnode: tosca.nodes.NodeWithCap\n\t\t\t\t\trelationship: tosca.relationships.HostedOn\n\n\ttosca.nodes.NodeWithCap:\n\t\tderived_from: tosca.nodes.Root\n\t\tcapabilities:\n\t\t\t\tsome_req:\n\t\t\t\t\ttype: tosca.capabilities.SomeCap'
yml = yml.expandtabs(2)
print('Number of node types: ' + NumNodeTypes(yml).count())

>>> Number of node types: 2
```