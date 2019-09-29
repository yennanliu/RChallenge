import sys
sys.path.append(".")
import unittest
from unittest.mock import patch
from nest.Nest import Json2NestedJson 

class TestProcessForOutput(unittest.TestCase):
    """
    test Json2NestedJson.process_for_output method 
    """
    def test_run(self):
        json2nestedjon = Json2NestedJson()
        data = [{'amount': 100, 'city': 'Boston', 'country': 'US', 'currency': 'USD'},
                {'amount': 20, 'city': 'Paris', 'country': 'FR', 'currency': 'EUR'},
                {'amount': 11.4, 'city': 'Lyon', 'country': 'FR', 'currency': 'EUR'},
                {'amount': 8.9, 'city': 'Madrid', 'country': 'ES', 'currency': 'EUR'},
                {'amount': 12.2, 'city': 'London', 'country': 'UK', 'currency': 'GBP'},
                {'amount': 10.9, 'city': 'London', 'country': 'UK', 'currency': 'FBP'}]
        json_keys = ["country","currency","city"]
        output = json2nestedjon.process_for_output(data, json_keys) 
        assert output == {'ES': {'EUR': {'Madrid': [{'amount': 8.9}]}},
                          'FR': {'EUR': {'Lyon': [{'amount': 11.4}], 'Paris': [{'amount': 20}]}},
                          'UK': {'FBP': {'London': [{'amount': 10.9}]},
                          'GBP': {'London': [{'amount': 12.2}]}},
                          'US': {'USD': {'Boston': [{'amount': 100}]}}}

if __name__ == '__main__':
    unittest.main()