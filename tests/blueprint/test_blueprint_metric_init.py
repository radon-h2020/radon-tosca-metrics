import unittest
from io import StringIO
from toscametrics.exceptions import NotBlueprintError, NotStringIOError
from toscametrics.blueprint.blueprint_metric import BlueprintMetric

class TestBlueprintMetricInit(unittest.TestCase):

    @classmethod
    def __createStream(cls, content):
        return StringIO(content.expandtabs(2))

    @classmethod
    def setUpClass(cls): 
        cls.emptyYmlStream     = cls.__createStream('')
        cls.invalidYmlStream   = cls.__createStream('-\nHello world')

    @classmethod
    def tearDownClass(cls): 
        cls.emptyYmlStream.close()
        cls.invalidYmlStream.close()
    
    def testNone(self):
        with self.assertRaises(NotStringIOError): 
            BlueprintMetric(None) 

    def testNotStringIO(self):
        with self.assertRaises(NotStringIOError): 
            BlueprintMetric('Not a stream io!')

    def testNotPlaybookError1(self):
        with self.assertRaises(NotBlueprintError): 
            BlueprintMetric(self.invalidYmlStream) 
    
    def testNotPlaybookError2(self):
        with self.assertRaises(NotBlueprintError): 
            BlueprintMetric(self.emptyYmlStream)
   
if __name__ == "__main__":
    unittest.main()