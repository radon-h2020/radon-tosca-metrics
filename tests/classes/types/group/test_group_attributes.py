import unittest
from parameterized import parameterized_class

from toscametrics.classes.definitions.attribute import AttributeDefinition
from toscametrics.classes.types.group      import GroupType

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': {}, 'expected': False},
   { 'input': {'a1':AttributeDefinition(type='tosca.attributes.A')}, 'expected': False},
   { 'input': {'a1':AttributeDefinition(type='tosca.attributes.A'), 'a2':'custom'}, 'expected': True},
   { 'input': True, 'expected': True},
   { 'input': 2, 'expected': True},
   { 'input': 2.0, 'expected': True},
   { 'input': [], 'expected': True}
])
class TestGroupTypeAttributes(unittest.TestCase):

    def test(self):
        raised = False

        try:
            GroupType(attributes=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()