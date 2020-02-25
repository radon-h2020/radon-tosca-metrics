import unittest
from parameterized import parameterized_class

from toscametrics.classes.definitions.group import GroupDefinition


@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': ['my_web_server', 'my_sql_database'],   'expected': False},
   { 'input': [],   'expected': False},
   { 'input': 'MD5', 'expected': True},
   { 'input': 'String', 'expected': True},
   { 'input': True, 'expected': True},
   { 'input': 2,    'expected': True},
   { 'input': 2.0,  'expected': True},
   { 'input': {},   'expected': True},
   { 'input': ['my_web_server', 2],   'expected': True}
])
class TestGroupDefinitionMembers(unittest.TestCase):

    def test(self):
        raised = False

        try:
            GroupDefinition(type='type', members=self.input)
        except (TypeError, ValueError):
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()