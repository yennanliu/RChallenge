import os, json 
from flask import (Flask, 
                   jsonify, 
                   abort, 
                   make_response, 
                   request) 
# UDF 
import sys
sys.path.append(".")
from nest.Nest import Json2NestedJson 

app = Flask(__name__)

# api hello world 
@app.route('/')
def index():
    return "API Hello, World!"

# handle error
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# POST method 
@app.route('/REST/api/v1.0/nest', methods=['POST'])
def transorm_json_2_nested_json():
    data = request.json 
    json2nestedjson = Json2NestedJson()
    input_data = json2nestedjson.read_file_input(data['input_json'])
    response = json.dumps(json2nestedjson.process_for_output(input_data,data['keys']), indent=2,sort_keys=True)
    print (response)
    return (response), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
