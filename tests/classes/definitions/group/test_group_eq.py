import unittest

from toscametrics.classes.definitions.group   import GroupDefinition

class TestGroupDefinitionEq(unittest.TestCase):

    def testEqual(self):
        g1 = GroupDefinition(
            type='tosca.groups.Root',
            description="My application’s logical component grouping for placement",
            metadata={'key_1': 'value_1', 'key_2': 'value_2'},
            properties={'name': 'vSRX', 
                        'container_format': 'BARE',
                        'disk_format': 'QCOW2',
                        'min_disk': '1 GB',
                        'size': '649 MB'
            },
            members=['my_web_server', 'my_sql_database']
        )

        g2 = GroupDefinition(
            type='tosca.groups.Root',
            description="My application’s logical component grouping for placement",
            metadata={'key_1': 'value_1', 'key_2': 'value_2'},
            properties={'name': 'vSRX', 
                        'container_format': 'BARE',
                        'disk_format': 'QCOW2',
                        'min_disk': '1 GB',
                        'size': '649 MB'
            },
            members=['my_web_server', 'my_sql_database']
        )

        self.assertEqual(g1, g2, 'Test failed because expected equality but actual is \'not equal\'!') 


    def testNotEqual(self):
        g1 = GroupDefinition(
            type='tosca.groups.Root',
            description="My application’s logical component grouping for placement",
            properties={'name': 'vSRX', 
                        'container_format': 'BARE',
                        'disk_format': 'QCOW2',
                        'min_disk': '1 GB',
                        'size': '649 MB'
            },
            members=['my_web_server', 'my_sql_database']
        )

        g2 = GroupDefinition(
            type='tosca.groups.Root',
            description="Logical component grouping for placement",
            members=['my_web_server']
        )

        self.assertNotEqual(g1, g2, 'Test failed because expected not equal but actual is \'equal\'!') 
    
if __name__ == "__main__":
    unittest.main()