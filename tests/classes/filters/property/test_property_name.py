import unittest
from parameterized import parameterized_class

from toscametrics.classes.filters.property import PropertyFilter

@parameterized_class([
   { 'input': 'name', 'expected': False},
   { 'input': None, 'expected': True},
   { 'input': True, 'expected': True},
   { 'input': 2, 'expected': True},
   { 'input': 2.0, 'expected': True},
   { 'input': [], 'expected': True},
   { 'input': {}, 'expected': True}
])
class TestPropertyFilterName(unittest.TestCase):

    def test(self):
        raised = False

        try:
            PropertyFilter(name=self.input, constraints=[])
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()