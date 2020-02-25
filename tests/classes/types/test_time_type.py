import unittest
from toscametrics.classes.types.time import TimeInterval

class TestTimeIntervalInit(unittest.TestCase):
   
    def testValid1(self):
        try:
            TimeInterval(start='2001-12-15T02:59:43.1Z', end='2002-01-16T03:58:44.2Z')
        except Exception:
            self.fail("Exception raised when it was not supposed to")

    def testValid2(self):
        try:
            TimeInterval(start='2001-12-14t21:59:43.10-05:00', end='2002-11-15t22:50:43.10-05:00')
        except Exception:
            self.fail("Exception raised when it was not supposed to")

    def testValid3(self):
        try:
            TimeInterval(start='2001-09-14 21:59:43.10 -5', end='2002-10-15 22:00:40.10 -5')
        except Exception:
            self.fail("Exception raised when it was not supposed to")

    def testValid4(self):
        try:
            TimeInterval(start='2001-02-15 2:59:43.10', end='2002-03-16 3:58:44.11')
        except Exception:
            self.fail("Exception raised when it was not supposed to")

    def testValid5(self):
        try:
            TimeInterval(start='2002-12-14', end='2002-12-15')
        except Exception:
            self.fail("Exception raised when it was not supposed to")


if __name__ == "__main__":
    unittest.main()