import sys
sys.path.append(".")
import unittest
from unittest.mock import patch
from nest.Nest import Json2NestedJson 

class TestReadStdinInput(unittest.TestCase):
    """
    mock Json2NestedJson.read_stdin_input method  
    and check if method return is in needed form
    """
    def test_run(self):
        with patch.object(Json2NestedJson, 'read_stdin_input', return_value=None) as mock_method:
            json2nestedjon = Json2NestedJson()
            json2nestedjon.read_stdin_input("country: US") 
            mock_method.assert_called_once_with("country: US")

if __name__ == '__main__':
    unittest.main()