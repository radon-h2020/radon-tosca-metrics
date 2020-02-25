import unittest

from toscametrics.classes.filters.event import EventFilter

class TestEventFilterEq(unittest.TestCase):
    pass

    def testEqual(self):
        e1 = EventFilter(
             node='A node',
             requirement='A requirement',
             capability='A capability'
        )

        e2 = EventFilter(
             node='A node',
             requirement='A requirement',
             capability='A capability'
        )

        self.assertEqual(e1, e2, 'Test failed because expected equality but actual is \'not equal\'!') 


    def testNotEqual(self):
        e1 = EventFilter(
             node='A node A',
             requirement='A requirement A',
             capability='A capability A'
        )

        e2 = EventFilter(
             node='A node B',
             requirement='A requirement B',
             capability='A capability B'
        )

        self.assertNotEqual(e1, e2, 'Test failed because expected not equal but actual is \'equal\'!') 

if __name__ == "__main__":
    unittest.main()