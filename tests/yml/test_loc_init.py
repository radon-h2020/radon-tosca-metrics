import unittest
from enum import Enum
from parameterized import parameterized_class
from io import StringIO
from yaml import YAMLError

from toscametrics.yml.loc import LOC

yaml_invalid_1 = '---\n\t\thosts: localhost\n\ttasks:\n\t\t\t-name: a name\n\t\tdebug:\n\t\tmsg: "This is an invalid yaml file. Wrong indentation!"'
yaml_valid_1 = '---\n- hosts: localhost\n\n\ttasks:\n\t- name: task 1    # This is the first task\n\t\tinclude_vars:\n\t\t\tfile: username_info.yml\n\n# This is the second task\n\t- name: task 2\n\t\tinclude_vars:\n\t\t\tfile: username_info.yml'

class Raised(Enum):
    TRUE = 'exception raised',
    FALSE = 'exception not raised'

@parameterized_class([
   { 'yaml': yaml_invalid_1, 'expected': Raised.TRUE},       # raise stands for 'raise exception YAMLError'
   { 'yaml': yaml_valid_1,   'expected': Raised.FALSE}
])
class TestLOCInit(unittest.TestCase):

    def setUp(self):
        self.yaml = StringIO(self.yaml.expandtabs(2))

    def tearDown(self):
        self.yaml.close()

    def test(self):
        raised = Raised.FALSE

        try:
            metric = LOC(self.yaml)
        except YAMLError:
            raised = Raised.TRUE

        self.assertEqual(raised, self.expected, 'Test failed because expected \'' + str(self.expected.value) + '\' and got \'' + str(raised.value) +'\'!') 
    
if __name__ == "__main__":
    unittest.main()