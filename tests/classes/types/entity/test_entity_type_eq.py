import unittest

from toscametrics.classes.types.entity import EntityType

class TestEntityTypeEq(unittest.TestCase):

    def testEqual(self):
        e1 = EntityType(
            derivedFrom='nodes.parent',
            version='1.0.0.alpha-1',
            metadata={'key':'value'},
            description='Testing entity'
        )

        e2 = EntityType(
            derivedFrom='nodes.parent',
            version='1.0.0.alpha-1',
            metadata={'key':'value'},
            description='Testing entity'
        )

        self.assertEqual(e1, e2, 'Test failed because expected equality but actual is \'not equal\'!') 


    def testNotEqual(self):
        e1 = EntityType(
            derivedFrom='nodes.parent.A',
            version='1.0.0.alpha-1',
            metadata={'key':'value'},
            description='Testing entity'
        )

        e2 = EntityType(
            derivedFrom='nodes.parent.B',
            version='1.2.3.alpha-2',
            description='Testing entity version 1.2.3'
        )
        self.assertNotEqual(e1, e2, 'Test failed because expected not equal but actual is \'equal\'!') 
    
if __name__ == "__main__":
    unittest.main()