import os, requests
import pytest
# REST flask app 
import sys
sys.path.append(".")
from REST.app import * 

def test_404_page_not_found():
    """
    test if can return http 404 error if input invalid url 
    """
    response = requests.get('http://0.0.0.0:5000/this_page_not_exists')
    assert response.status_code == 404

if __name__ == '__main__':
    pytest.main([__file__])