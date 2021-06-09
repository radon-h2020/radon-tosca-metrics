<h2 align="center">The static source code measurement tool for Tosca</h2>
<p align="center">
<a><img alt="Build Status" src="https://github.com/radon-h2020/radon-tosca-metrics/workflows/Build/badge.svg"></a>
<a><img alt="LGTM Grade" src="https://img.shields.io/lgtm/grade/python/github/radon-h2020/radon-tosca-metrics"></a>
<a><img alt="Codecov coverage" src="https://img.shields.io/codecov/c/github/radon-h2020/radon-tosca-metrics"></a>
<a><img alt="pypi-version" src="https://img.shields.io/pypi/v/tosca-metrics"></a>
<a><img alt="python-version" src="https://img.shields.io/pypi/pyversions/tosca-metrics"></a>
</p>

**ToscaMetrics** is a Python-based static source code measurement tool to characterize Infrastructure-as-Code.
It helps quantify the characteristics of Tosca blueprints to support DevOps engineers when maintaining and evolving it. 
It currently supports 17 source code metrics, though other metrics can be derived by combining the implemented ones.

-------------------

## How to install

Installation is made simple by the [PyPI repository](https://pypi.org/project/tosca-metrics).
Download the tool and install it with:

```pip install tosca-metrics```

or, alternatively from the source code project directory:

```
pip install -r requirements.txt
pip install .
```

## How to use

### **Command-line**

Run ```tosca-metrics --help``` for instructions about the usage:

```
usage: tosca-metrics [-h] [--omit-zero-metrics] [-d DEST] [-o] [-v] src

Extract metrics from Ansible scripts.

positional arguments:
  src                   source file (Tosca blueprint) or directory

optional arguments:
  -h, --help            show this help message and exit
  --omit-zero-metrics   omit metrics with value equal 0
  -d DEST, --dest DEST  destination path to save results
  -o, --output          shows output
  -v, --version         show program's version number and exit
```

Assume that the following example is named *blueprint1.tosca*:

```yaml
tosca_definitions_version: tosca_simple_yaml_1_0

imports:
  - indigo_custom_types: https://raw.githubusercontent.com/indigo-dc/tosca-types/master/custom_types.yaml

description: >
  TOSCA example for launching the generic_deepaas mesos job
topology_template:
       

  node_templates:

    marathon-job:
      type: tosca.nodes.indigo.Container.Application.Docker.Marathon
      properties:
        uris: []
        command: 'deepaas-run --listen-ip 0.0.0.0'
        labels:
          HAPROXY_GROUP: external
      artifacts:
        image:
          file: deephdc/deep-oc-plant-classification-theano
          type: tosca.artifacts.Deployment.Image.Container.Docker
      requirements:
        - host: docker_runtime

    docker_runtime:
      type: tosca.nodes.indigo.Container.Runtime.Docker
      capabilities:
        host:
          properties:
            num_cpus: 1.0
            mem_size: 1024 MB
            publish_ports:
               - protocol: tcp
                 source: 5000

  outputs:
    endpoint: 
      value: { concat: [ { get_attribute : [ marathon-job, load_balancer_ips, 0 ] }, ':', { get_attribute : [ docker_runtime, host, publish_ports, 0, target ] } ] }
```

and is located within the folder *blueprints* as follows:

blueprints <br>
&nbsp;&nbsp;&nbsp;|- blueprint1.yml <br>
&nbsp;&nbsp;&nbsp;|- blueprint2.yml <br>
&nbsp;&nbsp;&nbsp;|- blueprint3.yml <br>


Also, assume the user's working directory is the *blueprints* folder. 
Then, it is possible to extract source code characteristics from that blueprint by running the following command:

```tosca-metrics --omit-zero-metrics playbook1.yml --dest report.json```

For this example, the `report.json` will result in 

```
[
    {
        "filepath": "blueprint1.tosca",
        "lines_blank": 7,
        "lines_code": 33,
        "num_imports": 1,
        "num_keys": 35,
        "num_node_templates": 2,
        "num_properties": 6,
        "num_tokens": 68,
        "text_entropy": 5.76
    }
]
```

<br>

### **Python**

*AnsibleMetrics* currently supports up to 46 source code metrics, implemented in Python. 
To extract the value for a given metric follow this pattern:

```python
from toscametrics.<general|blueprint>.metric import Metric

script = 'a valid yaml script'
value = Metric(script).count()
```

where <metric> has to be replaced with the name of the desired metric module to compute the value of a specific metric. <br>
The difference between the *general* and the *blueprint* modules is that the *blueprint* module contains metrics specific 
to blueprints (for example, the number of node types), while the *general* module contains metrics that can be generalized 
to other languages (for example, the lines of code).

For example, to count the number of lines of code:

```python
from toscametrics.general.lines_code import LinesCode

blueprint = """
tosca_definitions_version: tosca_simple_yaml_1_0

imports:
  - indigo_custom_types: https://raw.githubusercontent.com/indigo-dc/tosca-types/master/custom_types.yaml

description: >
  TOSCA example for launching the generic_deepaas mesos job
"""

print('Lines of executable code:', LinesCode(blueprint).count())
```


To extract the value for all the metrics at once,  import the ```toscametrics.metrics_extractor``` package and call the 
method ```extract_all()``` (in this case the return value will be a json object):

```python
from toscametrics.metrics_extractor import extract_all

blueprint = """
tosca_definitions_version: tosca_simple_yaml_1_0

imports:
  - indigo_custom_types: https://raw.githubusercontent.com/indigo-dc/tosca-types/master/custom_types.yaml

description: >
  TOSCA example for launching the generic_deepaas mesos job
"""

metrics = extract_all(blueprint)
print('Lines of executable code:', metrics['lines_code'])
```


