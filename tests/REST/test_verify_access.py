import os, requests
import pytest
# REST flask app 
import sys
sys.path.append(".")
from REST.app import * 

def test_verify_access():
    response = requests.get('http://0.0.0.0:5000/REST/api/v1.0/nest')
    assert response.status_code == 405

if __name__ == '__main__':
    pytest.main([__file__])