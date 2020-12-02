import unittest
from io import StringIO
from toscametrics.blueprint_metric import BlueprintMetric


class TestBlueprintMetricInit(unittest.TestCase):

    def testInvalidBlueprint(self):
        with self.assertRaises(TypeError):
            BlueprintMetric(StringIO('- Hello\nWorld'))
    
    def testEmptyBlueprint(self):
        with self.assertRaises(TypeError):
            BlueprintMetric(StringIO(''))
