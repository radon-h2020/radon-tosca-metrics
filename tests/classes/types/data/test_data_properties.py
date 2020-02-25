import unittest
from parameterized import parameterized_class

from toscametrics.classes.definitions.property import PropertyDefinition
from toscametrics.classes.types.data           import DataType

@parameterized_class([
   { 'input': None, 'expected': False},
   { 'input': {}, 'expected': False},
   { 'input': {'p1':PropertyDefinition(type='tosca.properties.A')}, 'expected': False},
   { 'input': {'p1':PropertyDefinition(type='tosca.properties.A'), 'p2':'custom'}, 'expected': True},
   { 'input': True, 'expected': True},
   { 'input': 2, 'expected': True},
   { 'input': 2.0, 'expected': True},
   { 'input': [], 'expected': True}
])
class TestDataTypeProperties(unittest.TestCase):

    def test(self):
        raised = False

        try:
            DataType(properties=self.input)
        except TypeError:
            raised = True
        finally:
            self.assertEqual(raised, self.expected, 'Test failed because expected raised = ' + str(self.expected) + ' and got raised = ' + str(raised) +'!') 
    
if __name__ == "__main__":
    unittest.main()