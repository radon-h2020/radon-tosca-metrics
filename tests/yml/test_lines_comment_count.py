import unittest
from parameterized import parameterized_class
from io import StringIO
from toscametrics.yml.lines_comment import LinesComment

yaml_0_1 = '---\n- hosts: localhost\n\n\ttasks:\n\t- name: task 1\n\t\tinclude_vars:\n\t\t\tfile: ' \
           'username_info.yml\n\n\t- name: task 2\n\t\tinclude_vars:\n\t\t\tfile: username_info.yml '
yaml_2_1 = '---\n- hosts: localhost\n\n\ttasks:\n\t- name: task 1    # This is the first ' \
           'task\n\t\tinclude_vars:\n\t\t\tfile: username_info.yml\n\n# This is the second task\n\t- name: task ' \
           '2\n\t\tinclude_vars:\n\t\t\tfile: username_info.yml '


@parameterized_class([
   { 'yaml': yaml_0_1, 'expected': 0},
   { 'yaml': yaml_2_1, 'expected': 2}
])
class TestLinesCommentCount(unittest.TestCase):

    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()

    def test(self):
        metric = LinesComment(self.yaml)
        count = metric.count()
        self.assertEqual(count, self.expected)
