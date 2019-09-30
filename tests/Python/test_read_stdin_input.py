import sys
sys.path.append(".")
import unittest
from unittest.mock import patch
from io import StringIO 
import json 
# UDF 
from nest.Nest import Json2NestedJson 

class Json2NestedJson_inherit(Json2NestedJson):
    """
    Inherit Json2NestedJson class 
    and re-write load stdin part in read_stdin_input method 
    for below unit test
    """
    def read_stdin_input(self, mock_stdin):
        output = ''
        for line in mock_stdin:
            output += line 
        return json.loads(output)


class TestReadStdinInput(unittest.TestCase):
    """
    mock Json2NestedJson.read_stdin_input method  
    and check if method return is in needed form
    """
    def test_run(self):
        json2nestedjon = Json2NestedJson_inherit()
        output = json2nestedjon.read_stdin_input('{"country":"UK","city": "London"}')
        expetcted_output = {'country': 'UK', "city": "London"}  
        assert output == expetcted_output

if __name__ == '__main__':
    unittest.main()