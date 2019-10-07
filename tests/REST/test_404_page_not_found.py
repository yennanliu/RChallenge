import requests
import pytest
# REST flask app 
import sys
sys.path.append(".")
from REST.app import app 

def test_404_page_not_found():
    """
    test if can return http 404 error if input invalid url 
    """
    with app.test_client() as c:
        response = c.get('/this_page_not_exists')
        assert response.status_code == 404

if __name__ == '__main__':
    pytest.main([__file__])