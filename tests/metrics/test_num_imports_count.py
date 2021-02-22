import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.blueprint.num_imports import NumImports


yaml_0 = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\ndescription: Template for deploying a single server ' \
         'with MySQL software on top.\n\ntopology_template:\n  inputs:\n    mysql_rootpw:\n      type: string\n    ' \
         'mysql_port:\n      type: integer\n\n  node_templates:\n    db_server:\n      type: tosca.nodes.Compute\n\n  ' \
         '  mysql:\n      type: tosca.nodes.DBMS.MySQL '
yaml_1 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\nimports:\n  - paypalpizzastore_nodejs_app.yaml'
yaml_2 = 'imports:\n  - some_definition_file: path1/path2/some_defs.yaml\n  - another_definition_file:\n      file: ' \
         'path1/path2/file2.yaml\n      repository: my_service_catalog\n      namespace_uri: ' \
         'http://mycompany.com/tosca/1.0/platform\n      namespace_prefix: mycompany '
yaml_3 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\nimports:\n  - paypalpizzastore_nodejs_app.yaml\n  - ' \
         'elasticsearch.yaml\n  - logstash.yaml '


@parameterized_class([
   {'yaml': yaml_0, 'expected': 0},
   {'yaml': yaml_1, 'expected': 1},
   {'yaml': yaml_2, 'expected': 2},
   {'yaml': yaml_3, 'expected': 3}
])
class TestNumImportCount(unittest.TestCase):
    def setUp(self):
        self.blueprint = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.blueprint.close()
    
    def test(self):
        self.assertEqual(NumImports(self.blueprint).count(), self.expected)
