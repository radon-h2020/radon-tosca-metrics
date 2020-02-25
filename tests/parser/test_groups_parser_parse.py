import unittest

from toscametrics.classes.definitions.group import GroupDefinition
from toscametrics.parser.groups_parser      import GroupsParser

class TestGroupsParserParse(unittest.TestCase):

    def testNone1(self):
        parser = GroupsParser()
        actual = parser.parse([])
        self.assertIsNone(actual, 'Test failed because expected None list and got ' + str(actual) +'!') 

    def testNone2(self):
        parser = GroupsParser()
        actual = parser.parse(None)
        self.assertIsNone(actual, 'Test failed because expected None list and got ' + str(actual) +'!') 

    def testValid(self):
        input={"type": "tosca.groups.Root", "description": "My application’s logical component grouping for placement", "members": [ "my_web_server", "my_sql_database" ]}
        parser = GroupsParser()
        actual = parser.parse(input)
        expected = GroupDefinition(
            type='tosca.groups.Root',
            description="My application’s logical component grouping for placement",
            members=['my_web_server', 'my_sql_database']
        )
        
        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 

if __name__ == "__main__":
    unittest.main()