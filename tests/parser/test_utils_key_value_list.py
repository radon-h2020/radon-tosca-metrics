import unittest
from parameterized import parameterized_class

import toscametrics.utils as utils

@parameterized_class([
   { 'input': None, 'expected': []},
   { 'input': 2,    'expected': []},
   { 'input': 2.0,  'expected': []},
   { 'input': [], 'expected': []},
   { 'input': {}, 'expected': []},
   { 'input': {"key_1": {"key_2": {"key_3": "value_1", "key_4": {"key_5": "value_2","key_6": "value_3"}}}}, 'expected': [("key_1",{"key_2":{"key_3":"value_1","key_4":{"key_5":"value_2","key_6":"value_3"}}}),("key_2",{"key_3":"value_1","key_4":{"key_5":"value_2","key_6":"value_3"}}),("key_3","value_1"),("key_4",{"key_5":"value_2","key_6":"value_3"}),("key_5","value_2"),("key_6","value_3")]}
])
class TestUtilsKeyValueList(unittest.TestCase):

    def test(self):
        actual = utils.keyValueList(self.input)
        self.assertEqual(actual, self.expected, 'Test failed because expected ' + str(self.expected) + ' and got ' + str(actual) +'!') 
    
if __name__ == "__main__":
    unittest.main()


