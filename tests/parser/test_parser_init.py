import unittest
from parameterized import parameterized_class

from toscametrics.parser.parser import Parser

@parameterized_class([
   { 'input': None, 'expected': True},
   { 'input': 2,    'expected': True},
   { 'input': 2.0,  'expected': True},
   { 'input': [], 'expected': True},
   { 'input': {}, 'expected': True},
   { 'input': '', 'expected': True},
   { 'input': '-\nHello world', 'expected': True},
   { 'input': '-node_filter:\n\tproperties:\n\t- property_1'.expandtabs(2), 'expected': False}
])
class TestParserInit(unittest.TestCase):

    def test(self):
        raised = False

        try:
            Parser(self.input)
        except Exception:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()


