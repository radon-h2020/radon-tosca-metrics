import unittest

from toscametrics.classes.types.time import TimeInterval

class TestTimeIntervalEq(unittest.TestCase):

    def testEqual(self):
        t1 = TimeInterval(start='2001-12-15T02:59:43.1Z', end='2002-01-16T03:58:44.2Z')
        t2= TimeInterval(start='2001-12-15T02:59:43.1Z', end='2002-01-16T03:58:44.2Z')

        self.assertEqual(t1, t2, 'Test failed because expected equality but actual is \'not equal\'!') 


    def testNotEqual(self):
        t1 = TimeInterval(start='2001-12-15T02:59:43.1Z', end='2002-01-16T03:58:44.2Z')
        t2= TimeInterval(start='2001-12-14t21:59:43.10-05:00', end='2002-11-15t22:50:43.10-05:00')

        self.assertNotEqual(t1, t2, 'Test failed because expected not equal but actual is \'equal\'!') 
    
if __name__ == "__main__":
    unittest.main()