import sys
sys.path.append(".")
from nest.Nest import Json2NestedJson 

def test_read_file_input():
    """
    test Json2NestedJson.read_file_input method 
    """
    json2nestedjons = Json2NestedJson()
    json_file = json2nestedjons.read_file_input('data/input.json')
    assert isinstance(json_file, list) == True 

if __name__ == '__main__':
    pytest.main([__file__])