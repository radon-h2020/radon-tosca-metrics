import unittest
from parameterized import parameterized_class

from toscametrics.classes.filters.event import EventFilter

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': 'requirement', 'expected': False},
   { 'input': True, 'expected': True},
   { 'input': 2, 'expected': True},
   { 'input': 2.0, 'expected': True},
   { 'input': [], 'expected': True},
   { 'input': {}, 'expected': True}
])
class TestEventFilterNode(unittest.TestCase):

    def test(self):
        raised = False

        try:
            EventFilter(node='test', requirement=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()