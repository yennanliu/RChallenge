import sys
sys.path.append(".")
import unittest
from unittest.mock import patch
from nest.Nest import Json2NestedJson 

class TestAppendNotListed(unittest.TestCase):
    """
    test Json2NestedJson.append_not_listed method 
    """
    def test_run(self):
        json2nestedjon = Json2NestedJson()
        data = {'amount': 100, 'city': 'Boston', 'country': 'US', 'currency': 'USD'}
        json_keys = ["country","currency","city"]
        tmp = json2nestedjon.append_not_listed(json_keys, data) 
        assert tmp == [{'amount': 100}]

if __name__ == '__main__':
    unittest.main()