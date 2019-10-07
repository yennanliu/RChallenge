import requests
import pytest
# REST flask app 
import sys
sys.path.append(".")
from REST.app import * 

def test_verify_access():
    """
    test access validation, should return http 405 error since the test doesn't offer any user creds for "login" here 
    """
    with app.test_client() as c:
        response = c.get('/REST/api/v1.0/nest')
        assert response.status_code == 405

if __name__ == '__main__':
    pytest.main([__file__])