import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.yml.lines_code import LinesCode

yaml_8_1 = '---\n- hosts: localhost\n\n\ttasks:\n\t- name: task 1    # This is the first ' \
           'task\n\t\tinclude_vars:\n\t\t\tfile: username_info.yml\n\n# This is the second task\n\t- name: task ' \
           '2\n\t\tinclude_vars:\n\t\t\tfile: username_info.yml '


@parameterized_class([
    {'yaml': yaml_8_1, 'expected': 8}
])
class TestLOCCount(unittest.TestCase):

    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()

    def test(self):
        self.assertEqual(LinesCode(self.yaml).count(), self.expected)
