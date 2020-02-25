# Number of Outputs in a blueprint (NOUT)

## Description

Returns the number of outputs within a blueprint template. 

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
The following example has **2 outputs**.

``` yaml
tosca_definitions_version: tosca_simple_yaml_1_3

topology_template:
  description: Template of a database including its hosting stack.

  inputs:
    mq_service_ip:
      type: string
      description: IP address of the message queuing server to receive messages from
    receiver_port:
      type: string
      description: Port to be used for receiving messages 

  outputs:
    receiver_ip:
      description: private IP address of the message receiver application
      value: { get_attribute: [ server, private_address ] }
    receiver_port:
      description: Port of the message receiver endpoint
      value: { get_attribute: [ app, app_endpoint, port ] }
```

---

Below an example on how to call the metric and the expected output for this example:

```python
>>> from io import StringIO
>>> from toscametrics.metrics.NOUT import NOUT

>>> str = 'tosca_definitions_version: tosca_simple_yaml_1_3\n\ntopology_template:\n  description: Template of a database including its hosting stack.\n\n  inputs:\n    mq_service_ip:\n      type: string\n      description: IP address of the message queuing server to receive messages from\n    receiver_port:\n      type: string\n      description: Port to be used for receiving messages \n\n  outputs:\n    receiver_ip:\n      description: private IP address of the message receiver application\n      value: { get_attribute: [ server, private_address ] }\n    receiver_port:\n      description: Port of the message receiver endpoint\n      value: { get_attribute: [ app, app_endpoint, port ] }\n'  #from example 19 TOSCA simple profile v1.3

>>> yml = StringIO(str.expandtabs(2)) #substitute \t with 2 spaces and create the StringIO object
>>> metric = NOUT(yml)
>>> print('NOUT: ' + str(metric.count()))

NOUT: 2
```