import unittest
from parameterized import parameterized_class

from toscametrics.classes.clauses.constraints import ConstraintClause
from toscametrics.classes.filters.node        import NodeFilter
from toscametrics.classes.filters.property    import PropertyFilter

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': [], 'expected': False},
   { 'input': [PropertyFilter('property', [ConstraintClause(equal=1)])], 'expected': False},
   { 'input': [PropertyFilter('property', [ConstraintClause(equal=1)]), 1], 'expected': True},
   { 'input': 'tosca.nodes.A', 'expected': True},
   { 'input': True, 'expected': True},
   { 'input': 2, 'expected': True},
   { 'input': 2.0, 'expected': True},
   { 'input': {}, 'expected': True}
])
class TestNodeFilterProperties(unittest.TestCase):

    def test(self):
        raised = False

        try:
            NodeFilter(properties=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
        
if __name__ == "__main__":
    unittest.main()