import unittest
from parameterized import parameterized_class
from toscametrics.blueprint.num_parameters import NumParameters

yaml_0 = 'tosca_definitions_version: tosca_simple_yaml_1_0\n\nimports:\n  - paypalpizzastore_nodejs_app.yaml'
yaml_5 = 'inputs:\n\tdb_host: { get_attribute: [ db_server, private_address ] }\n\tdb_port: { get_property: [ mysql, ' \
         'port ] }\n\tdb_name: { get_property: [ wordpress_db, name ] }\n\tdb_user: { get_property: [ wordpress_db, ' \
         'user ] }\n\tdb_password: { get_property: [ wordpress_db, password ] } '


@parameterized_class([
    {'yaml': yaml_0, 'expected': 0},
    {'yaml': yaml_5, 'expected': 5}
])
class TestNumParameters(unittest.TestCase):
    def setUp(self):
        self.yaml = self.yaml.expandtabs(2)

    def test(self):
        self.assertEqual(NumParameters(self.yaml).count(), self.expected)
