import requests
import pytest
# REST flask app 
import sys
sys.path.append(".")
from REST.app import * 

def test_transorm_json_2_nested_json():
    """
    simulate http POST with requests call with headers, data (CLI args), and auth (user, password)
    test if API can work fine with http 201 status 
    """
    headers = {'Content-Type': 'application/json'}
    data = '{"input_json":"data/input.json", "keys":["country", "city"]}'
    auth = ('api_user', 'password')
    response = requests.post('http://localhost:5000/REST/api/v1.0/nest', headers=headers, data=data, auth=auth)
    assert response.status_code == 201

if __name__ == '__main__':
    pytest.main([__file__])