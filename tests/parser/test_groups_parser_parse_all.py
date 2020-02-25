import unittest

from toscametrics.classes.definitions.group import GroupDefinition
from toscametrics.parser.groups_parser      import GroupsParser


class TestGroupsParserParseAll(unittest.TestCase):

    def testEmpty1(self):
        parser = GroupsParser()
        actual = parser.parseAll([])
        self.assertEqual(actual, [], 'Test failed because expected empty list and got ' + str(actual) +'!') 

    def testEmpty2(self):
        input = {'node_type': {'type': 'MySQL', 'attributes': [{'attribute_1':{'type': 'string'}}]}}
        parser = GroupsParser()
        actual = parser.parseAll(input)
        self.assertEqual(actual, [], 'Test failed because expected empty list and got ' + str(actual) +'!') 

    def testValid(self):
        input={"groups": { "my_app_placement_group": { "type": "tosca.groups.Root", "description": "My application’s logical component grouping for placement", "members": [ "my_web_server", "my_sql_database" ]}}}
        parser = GroupsParser()
        actual = parser.parseAll(input)
        expected = []
        expected.append(GroupDefinition(
            type='tosca.groups.Root',
            description="My application’s logical component grouping for placement",
            members=['my_web_server', 'my_sql_database']
        ))
        
        self.assertEqual(actual, expected, 'Test failed because expected ' + str(expected) + ' and got ' + str(actual) +'!') 

if __name__ == "__main__":
    unittest.main()
