import unittest
from parameterized import parameterized_class
from toscametrics.general.lines_blank import LinesBlank

yaml_0_1 = '---\n- hosts: localhost\n\ttasks:\n\t- name: task 1    # This is the first ' \
           'task\n\t\tinclude_vars:\n\t\t\tfile: username_info.general\n# This is the second task\n\t- name: task ' \
           '2\n\t\tinclude_vars:\n\t\t\tfile: username_info.general '
yaml_2_1 = '---\n- hosts: localhost\n\n\ttasks:\n\t- name: task 1    # This is the first ' \
           'task\n\t\tinclude_vars:\n\t\t\tfile: username_info.general\n\n# This is the second task\n\t- name: task ' \
           '2\n\t\tinclude_vars:\n\t\t\tfile: username_info.general '


@parameterized_class([
    {'yaml': yaml_0_1, 'expected': 0},
    {'yaml': yaml_2_1, 'expected': 2}
])
class TestLinesBlankCount(unittest.TestCase):

    def setUp(self):
        self.yaml = self.yaml.expandtabs(2)

    def test(self):
        self.assertEqual(LinesBlank(self.yaml).count(), self.expected)
