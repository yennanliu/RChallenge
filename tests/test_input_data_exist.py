# test module 
import pytest, unittest
import os 

def test_input_json_exist():
	"""
	test if input json file exist 
	"""
    file_exist = os.path.isfile('data/input.json')
    assert file_exist == True   

if __name__ == '__main__':
    pytest.main([__file__])