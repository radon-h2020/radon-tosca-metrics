import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.metrics.nc import NC


# yaml_nc_id
yaml_2_1 = 'tosca_definitions_version: tosca_simple_yaml_1_0\ndescription: Template with requirements against hosting infrastructure.\n\ntopology_template:\n  inputs:\n    # omitted here for brevity\n\n  node_templates:\n     \n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        # omitted here for brevity\n      requirements:\n        - host:\n            node_filter:\n              capabilities:\n                - host:\n                    properties:\n                      - num_cpus: { in_range: [ 1, 4 ] }\n                      - mem_size: { greater_or_equal: 2 GB }\n                - os:\n                    properties:\n                      - architecture: { equal: x86_64 }\n                      - type: linux\n                      - distribution: ubuntu'
yaml_2_2 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\ndescription: Template with requirements against hosting infrastructure.\n\ntopology_template:\n  inputs:\n    # omitted here for brevity\n    \n  node_templates:\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        # omitted here for brevity\n        \n      requirements:\n        - host: mysql_compute\n        \n    # Abstract node template (placeholder) to be selected by provider\n    mysql_compute:\n      type: Compute\n      node_filter:\n        capabilities:\n          - host:\n              properties:\n                num_cpus: { equal: 2 }\n                mem_size: { greater_or_equal: 2 GB }\n          - os:\n              properties:\n                architecture: { equal: x86_64 }\n                type: linux\n                distribution: ubuntu'
yaml_5_1 = 'tosca_definitions_version: tosca_simple_yaml_1_0\ndescription: Template with requirements against hosting infrastructure.\n\ntopology_template:\n  inputs:\n    # omitted here for brevity\n\n  node_templates:\n    mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        # omitted here for brevity\n      requirements:\n        - host:\n            node_filter:\n              capabilities:\n                - host:\n                    properties:\n                      - num_cpus: { in_range: [ 1, 4 ] }\n                      - mem_size: { greater_or_equal: 2 GB }\n                - os:\n                    properties:\n                      - architecture: { equal: x86_64 }\n                      - type: linux\n                      - distribution: ubuntu\n                - backup_os:\n                    properties:\n                      - architecture: { equal: x86_64 }\n                      - type: linux\n                      - distribution: ubuntu\n                      \n    backup_mysql:\n      type: tosca.nodes.DBMS.MySQL\n      properties:\n        # omitted here for brevity\n      requirements:\n        - host:\n            node_filter:\n              capabilities:\n                - host:\n                    properties:\n                      - num_cpus: { in_range: [ 1, 4 ] }\n                      - mem_size: { greater_or_equal: 2 GB }\n                - os:\n                    properties:\n                      - architecture: { equal: x86_64 }\n                      - type: linux\n                      - distribution: ubuntu'


@parameterized_class([
    {'yaml': yaml_2_1, 'expected': 2},
    {'yaml': yaml_2_2, 'expected': 1},
    {'yaml': yaml_5_1, 'expected': 2.5}
])
class TestNCMedian(unittest.TestCase):
    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()

    """
    def test(self):
        pass
        metric = NC(self.yaml)
        median = metric.median()
        self.assertEqual(median, self.expected, 'Test failed because expected ' +
                         str(self.expected) + ' and got ' + str(median) + '!')
    """

if __name__ == "__main__":
    unittest.main()
