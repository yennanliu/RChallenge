import sys
sys.path.append(".")
import unittest
from unittest.mock import patch
from io import StringIO
from nest.Nest import Json2NestedJson 


# class test_read_stdin_input(unittest.TestCase):
#     @patch('builtins.input', side_effect=[{"country": "US","city": "Boston","currency": "USD","amount": 100}])
#     def run_test(self):
#         json2nestedjons = Json2NestedJson()
#         json_file = json2nestedjons.read_stdin_input()
#         assert isinstance(json_file, list) == True 

class test_read_stdin_input(unittest.TestCase):
    @patch("sys.stdin", StringIO("country: US"))
    def run_test(self):
        json2nestedjons = Json2NestedJson()
        json_file = json2nestedjons.read_stdin_input()
        self.assertEqual(compare(), [{"country": "US"}]) 

if __name__ == '__main__':
    #unittest.main()
    pytest.main([__file__])