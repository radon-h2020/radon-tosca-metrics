import unittest
from toscametrics.classes.types.version import VersionType

class TestVersionTypeInit(unittest.TestCase):
   
    def testValueError2(self):
        with self.assertRaises(ValueError):
            VersionType('10.-5')
   
    def testValueError4(self):
        with self.assertRaises(ValueError):
            VersionType('major=1, minor=0, build=-5')

    def testValid1(self):
        try:
            VersionType('1.0')
        except Exception:
            self.fail("Exception raised when it was not supposed to")

    def testValid2(self):
        try:
            VersionType('1.0.0')
        except Exception:
            self.fail("Exception raised when it was not supposed to")

    def testValid3(self):
        try:
            VersionType('1.0.0.alpha')
        except Exception:
            self.fail("Exception raised when it was not supposed to")

    def testValid4(self):
        try:
            VersionType('1.0.0.alpha-10')
        except Exception:
            self.fail("Exception raised when it was not supposed to")

    def testValid5(self):
        version = VersionType('1.0-10')
        self.assertEqual(version.major, 1)
        self.assertEqual(version.minor, 0)
        self.assertEqual(version.build, 10)

    def testValid6(self):
        version = VersionType('1.0.2.alpha-10')
        self.assertEqual(version.major, 1)
        self.assertEqual(version.minor, 0)
        self.assertEqual(version.fix, 2)
        self.assertEqual(version.qualifier, 'alpha')
        self.assertEqual(version.build, 10)

if __name__ == "__main__":
    unittest.main()