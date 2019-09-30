import sys
sys.path.append(".")
from nest.Nest import Json2NestedJson 

def test_read_file_input():
    """
    test Json2NestedJson.read_file_input method 
    """
    expected_output = [
      {
        "country": "US",
        "city": "Boston",
        "currency": "USD",
        "amount": 100
      },
      {
        "country": "FR",
        "city": "Paris",
        "currency": "EUR",
        "amount": 20
      },
      {
        "country": "FR",
        "city": "Lyon",
        "currency": "EUR",
        "amount": 11.4
      },
      {
        "country": "ES",
        "city": "Madrid",
        "currency": "EUR",
        "amount": 8.9
      },
      {
        "country": "UK",
        "city": "London",
        "currency": "GBP",
        "amount": 12.2
      },
      {
        "country": "UK",
        "city": "London",
        "currency": "FBP",
        "amount": 10.9
      }
    ]
    json2nestedjons = Json2NestedJson()
    json_file = json2nestedjons.read_file_input('data/input.json')
    assert json_file == expected_output  

if __name__ == '__main__':
    pytest.main([__file__])