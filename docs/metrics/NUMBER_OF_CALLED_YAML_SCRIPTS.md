# Number of called yaml scripts in a blueprint (NCYS)

## Description

Returns the number of called yaml scripts within a blueprint template. Only those who are called within templates and type definitions, so not the ones already counted by the import metric. 

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
The following example has **1 yaml call found**.

``` yaml
tosca_definitions_version: tosca_simple_yaml_1_3

topology_template:
  node_templates:
    my_virtual_machine:
      type: SoftwareComponent
      artifacts:
        my_vm_image:
          file: images/fedora-18-x86_64.qcow2
          type: tosca.artifacts.Deployment.Image.VM.QCOW2
          topology: my_VMs_topology.yaml
      requirements:
        - host: my_server
      interfaces:
        Standard:
          create: my_vm_image
```

---

Below an example on how to call the metric and the expected output for this example:

```python
>>> from io import StringIO
>>> from toscametrics.metrics.ncys import NCYS

>>> str = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ntopology_template:\n  node_templates:\n    my_virtual_machine:\n      type: SoftwareComponent\n      artifacts:\n        my_vm_image:\n          file: images/fedora-18-x86_64.qcow2\n          type: tosca.artifacts.Deployment.Image.VM.QCOW2\n          topology: my_VMs_topology.yaml\n      requirements:\n        - host: my_server\n      interfaces:\n        Standard:\n          create: my_vm_image'

>>> yml = StringIO(str.expandtabs(2)) #substitute \t with 2 spaces and create the StringIO object
>>> metric = NCYS(yml)
>>> print('NCYS: ', metric.count())

NCYS: 1
```