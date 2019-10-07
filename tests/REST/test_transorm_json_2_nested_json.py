import requests
import pytest
from base64 import b64encode
# REST flask app 
import sys
sys.path.append(".")
from REST.app import app

def test_transorm_json_2_nested_json():
    """
    simulate http POST with requests call with headers, data (CLI args), and auth (user, password)
    test if API can work fine with http 201 status 
    """
    headers={"Content-Type": "application/json", 
             'Authorization': 'Basic %s' % b64encode(b"api_user:password").decode("ascii")}
    data = '{"input_json":"data/input.json", "keys":["country", "city"]}'
    auth = {'username': 'api_user', 'password': 'password'}

    with app.test_client()as c:
        response = c.post('/REST/api/v1.0/nest', headers=headers, data=data)
        assert response.status_code == 201

if __name__ == '__main__':
    pytest.main([__file__])