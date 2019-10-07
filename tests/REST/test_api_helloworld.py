import requests
import pytest
# REST flask app 
import sys
sys.path.append(".")
from REST.app import app 

def test_api_helloworld():
    """
    test if can return http 200 if calling the simplest url 
    """
    with app.test_client() as c:
        response = c.get('/')
        assert response.status_code == 200

if __name__ == '__main__':
    pytest.main([__file__])