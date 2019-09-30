import os, requests
import pytest
# REST flask app 
import sys
sys.path.append(".")
from REST.app import * 

def test_api_helloworld():
    """
    test if can return http 200 if calling the simplest url 
    """
    response = requests.get('http://0.0.0.0:5000/')
    assert response.status_code == 200

if __name__ == '__main__':
    pytest.main([__file__])