import unittest
from parameterized import parameterized_class
from toscametrics.blueprint.num_imports import NumImports


yaml_0 = 'tosca_definitions_version: tosca_simple_yaml_1_2\n\ndescription: Template for deploying a single server ' \
         'with MySQL software on top.\n\ntopology_template:\n  inputs:\n    mysql_rootpw:\n      type: string\n    ' \
         'mysql_port:\n      type: integer\n\n  node_templates:\n    db_server:\n      type: tosca.nodes.Compute\n\n  ' \
         '  mysql:\n      type: tosca.nodes.DBMS.MySQL '
yaml_1_1 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\nimports:\n  - paypalpizzastore_nodejs_app.yaml'

yaml_1_2 = '# declare standard mapping based parsers\n- definition: alien4cloud.tosca.model.ArchiveRoot\n	' \
           'tosca_definitions_version: archive.toscaDefinitionsVersion\n	metadata:\n		reference: archive\n	' \
           '	type: meta_data\n	tosca_default_namespace: archive.toscaDefaultNamespace\n	template_name: ' \
           'archive.name\n	template_author: archive.templateAuthor\n	template_version: archive.version\n	' \
           'description: archive.description\n	imports:\n		set: archive.dependencies\n		type: ' \
           'import_definition\n	dsl_definitions: null # this means we take this node in charge but won\'t parse it\'s ' \
           'content\n '

yaml_2 = 'imports:\n  - some_definition_file: path1/path2/some_defs.yaml\n  - another_definition_file:\n      file: ' \
         'path1/path2/file2.yaml\n      repository: my_service_catalog\n      namespace_uri: ' \
         'http://mycompany.com/tosca/1.0/platform\n      namespace_prefix: mycompany '
yaml_3 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\nimports:\n  - paypalpizzastore_nodejs_app.yaml\n  - ' \
         'elasticsearch.yaml\n  - logstash.yaml '


@parameterized_class([
    {'yaml': yaml_0, 'expected': 0},
    {'yaml': yaml_1_1, 'expected': 1},
    {'yaml': yaml_1_2, 'expected': 1},
    {'yaml': yaml_2, 'expected': 2},
    {'yaml': yaml_3, 'expected': 3}
])
class TestNumImportCount(unittest.TestCase):
    def setUp(self):
        self.blueprint = self.yaml.expandtabs(2)

    def test(self):
        self.assertEqual(NumImports(self.blueprint).count(), self.expected)
