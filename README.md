# RChallenge

### SQL 

<details>
<summary>SQL quick start</summary>

```bash
# dev
```
</details>


### Python 

<details>
<summary>Python quick start</summary>

```bash
# run the json transformation  process
$ git clone https://github.com/yennanliu/RChallenge.git
$ cd RChallenge  && pip install -r requirements.txt 
$ cat data/input.json  | python Python/run.py country city currency

# run tests 
$ pytest -v tests/

```
</details>

### REST API 

<details>
<summary>REST API quick start</summary>

```bash 
### 1) Aun the api server
$ python REST/app.py 

### 2) Access API without userid, password 
$ curl -i -H "Content-Type: application/json" -X POST -d '{"input_json":"data/input.json", "keys":["country", "city"]}' http://localhost:5000/REST/api/v1.0/nest

# HTTP/1.0 401 UNAUTHORIZED
# Content-Type: text/html; charset=utf-8
# Content-Length: 19
# WWW-Authenticate: Basic realm="Authentication Required"
# Server: Werkzeug/0.14.1 Python/3.5.4
# Date: Sun, 29 Sep 2019 06:30:01 GMT

### 2)' Access API with userid, password 
$ curl -i -H "Content-Type: application/json" -X POST -d '{"input_json":"data/input.json", "keys":["country", "city"]}' http://localhost:5000/REST/api/v1.0/nest --user api_user:password

# HTTP/1.0 201 CREATED
# Content-Type: text/html; charset=utf-8
# Content-Length: 576
# Server: Werkzeug/0.14.1 Python/3.5.4
# Date: Sun, 29 Sep 2019 06:31:44 GMT

# {
#   "ES": {
#     "Madrid": [
#       {
#         "amount": 8.9
#       },
#       {
#         "currency": "EUR"
#       }
#     ]
#   },
#   "FR": {
#     "Lyon": [
#       {
#         "amount": 11.4
#       },
#       {
#         "currency": "EUR"
#       }
#     ],
#     "Paris": [
#       {
#         "amount": 20
#       },
#       {
#         "currency": "EUR"
#       }
#     ]
#   },
#   "UK": {
#     "London": [
#       {
#         "amount": 10.9
#       },
#       {
#         "currency": "FBP"
#       }
#     ]
#   },
#   "US": {
#     "Boston": [
#       {
#         "amount": 100
#       },
#       {
#         "currency": "USD"
#       }
#     ]
#   }
# }

```
</details>