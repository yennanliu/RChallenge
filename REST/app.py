import os, json 
from flask_httpauth import HTTPBasicAuth
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
auth = HTTPBasicAuth()

## Credentials to access the API
USER_PASSWORD = {'api_user': 'password'}

# API hello world 
@app.route('/')
def index():
    return "API Hello World!", 200

# return 404 if not valid API url 
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# auth verify if user can access API service  
@auth.verify_password
def verify_access(username, password):
    # not allowing access API if no username or password 
    if not username or not password:
        return False 
    return USER_PASSWORD.get(username) == password

# main method run REST nest api via POST 
@app.route('/REST/api/v1.0/nest', methods=['POST'])
@auth.login_required
def transorm_json_2_nested_json():
    cli_args = request.json 
    json2nestedjson = Json2NestedJson()
    input_data = json2nestedjson.read_file_input(cli_args['input_json'])
    response = json.dumps(json2nestedjson.process_for_output(input_data, cli_args['keys']), indent=2,sort_keys=True)
    print (response)
    return (response), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
