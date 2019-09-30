# RChallenge

### Intro
- SQL | Python | REST
- Tech : python3, pytest, Flask, flask_httpauth, Postgre

### File structure 

```
├── Python             : Python script for json transformation
├── README.md          : Repo intro
├── REST               : REST api flask offer json transformation service 
├── SQL                : query get transactions in GBP with exchange rate
├── data               : input.json as sample data for Python script, Rest api
├── nest               : Class that offer "json to nested json" methods 
├── requirements.txt   : Python app dependency
└── tests              : Collections of unit tests 

```

### SQL 

<details>
<summary>SQL quick start</summary>

###### SQL/spend_GBP_rate_largest_timestamp.sql
	- query that transfrom all spend in GBP by each user with the largest timestamp exchange rate.  
	- Explanation:	
		- Make 1st CTE `largest_exchange_ts` : get largest exchange timestamp 
		- Make 2nd CTE `largest_timestamp_exchange` : get exchange rate at largest exchange timestamp 
		- Make 3rd CTE `trans_to_GBP` : transform non-GBP transactions to GBP based on exchange rate above 
		- Make 4rd CTE `trans_in_GBP` : get GBP transactions
		- Make 5rd CTE `trans_` : get all non-GBP and GBP transactions in GBP currency (via SQL union)
		- Finally query the CTE trans_ and sum transaction amount in GBP per user 

	- Steps:
		- largest timestamp -> exchange rate -> transactions in/non GBP -> final result

###### SQL/spend_GBP_rate_latest_transaction.sql
	- query that transfrom all spend in GBP by each user with the latest exchange rate which is smaller or equal then the transaction timestamp.  
	- 

###### Demo 


</details>


### Python 

<details>
<summary>Python quick start</summary>

```bash
# 1) Run the Json-2-nested-json process
$ pip install -r requirements.txt 
$ cat data/input.json  | python Python/run.py country city currency

# {
#   "FR": {
#     "Lyon": {
#       "EUR": [
#         {
#           "amount": 11.4
#         }
#       ]
#     },
#     "Paris": {
#       "EUR": [
#         {
#           "amount": 20
#         }
#       ]
#     }
#   },
#   "UK": {
#     "London": {
#       "GBP": [
#         {
#           "amount": 12.2
#         }
#       ],
#       "FBP": [
#         {
#           "amount": 10.9
#         }
#       ]
#     }
#   },
#   "US": {
#     "Boston": {
#       "USD": [
#         {
#           "amount": 100
#         }
#       ]
#     }
#   },
#   "ES": {
#     "Madrid": {
#       "EUR": [
#         {
#           "amount": 8.9
#         }
#       ]
#     }
#   }
# }

# 2) Run the tests 
$ pytest -v tests/

# =========================================== test session starts ============================================
# platform darwin -- Python 3.5.4, pytest-5.0.1, py-1.8.0, pluggy-0.12.0 -- /Users/yennanliu/anaconda3/envs/ds_dash/bin/python
# cachedir: .pytest_cache
# rootdir: /Users/yennanliu/RChallenge
# plugins: celery-4.2.1
# collected 5 items                                                                                          

# tests/test_append_not_listed.py::TestAppendNotListed::test_run PASSED                                [ 20%]
# tests/test_input_data_exist.py::test_input_json_exist PASSED                                         [ 40%]
# tests/test_process_for_output.py::TestProcessForOutput::test_run PASSED                              [ 60%]
# tests/test_read_file_input.py::test_read_file_input PASSED                                           [ 80%]
# tests/test_read_stdin_input.py::TestReadStdinInput::test_run PASSED                                  [100%]

# ========================================= 5 passed in 0.18 seconds =========================================

```
</details>

### REST API 

<details>
<summary>REST API quick start</summary>

```bash 
### 1) Run the api server
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