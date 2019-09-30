# RChallenge

### INTRO
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
- Query that transfrom all spend in GBP by each user with the largest timestamp exchange rate.

- Explanation:	
	- Make 1st CTE `largest_exchange_ts` : get largest exchange timestamp 
	- Make 2nd CTE `largest_timestamp_exchange` : get exchange rate at largest exchange timestamp 
	- Make 3rd CTE `trans_to_GBP` : transform non-GBP transactions to GBP based on exchange rate above 
	- Make 4rd CTE `trans_in_GBP` : get GBP transactions
	- Make 5rd CTE `trans_` : get all non-GBP and GBP transactions in GBP currency (via SQL union)
	- Finally query the CTE `trans_` and sum transaction amount in GBP per user 

- Steps:
	- largest timestamp -> exchange rate -> transactions in/non GBP -> final result

###### SQL/spend_GBP_rate_latest_transaction.sql
- Query that transfrom all spend in GBP by each user with the latest exchange rate which is smaller or equal then the transaction timestamp.  

- Explanation:
	- Make 1st CTE `exchange_ts` : get the all exchange rate with timestamp, from_currency, to_from_currency and exchange rate
	- Make 2nd CTE `exchange_ts_lag` : create "time intervals" by lagging exchange_rates timestamp for getting latest exchange_rates before every transaction 
	- Make 3rd CTE `trans_to_GBP` : transform  non-GBP transactions to GBP 
                            based on exchange_rates defined above  
	- Make 4rd CTE `trans_in_GBP` : get GBP transactions
	- Make 5rd CTE `trans_` : get all non-GBP and GBP transactions in GBP currency (via SQL union)
	- Finally query the CTE `trans_` and sum transaction amount in GBP per user 

- Steps:
	- all exchange rate with from/to currency and timestamp -> exchange rate lag -> transactions in/non GBP within latest exchange_rates before every transaction -> final result

###### Demo 

```sql 

# SQL/spend_GBP_rate_largest_timestamp.sql

psql> 

WITH largest_exchange_ts AS
  (SELECT from_currency,
          to_currency,
          max(ts) AS ts
   FROM exchange_rates
   WHERE to_currency = 'GBP'
   GROUP BY from_currency,
            to_currency),
     largest_timestamp_exchange AS
  (SELECT e.from_currency AS from_currency,
          e.rate AS rate
   FROM exchange_rates e
   INNER JOIN largest_exchange_ts l ON e.from_currency = l.from_currency
   AND e.to_currency = l.to_currency
   AND e.ts = l.ts),
     trans_to_GBP AS
  (SELECT t.user_id AS user_id,
          t.ts AS ts,
          l.from_currency AS currency,
          t.amount*l.rate AS amount_GBP
   FROM transactions t
   INNER JOIN largest_timestamp_exchange l ON l.from_currency = t.currency),
     trans_in_GBP AS
  (SELECT user_id,
          ts,
          currency,
          amount AS amount_gbp
   FROM transactions
   WHERE currency = 'GBP' ),
     trans_ AS
  (SELECT *
   FROM trans_to_GBP
   UNION ALL SELECT *
   FROM trans_in_GBP)
SELECT user_id AS user_id,
       SUM(amount_gbp) AS total_spent_gbp
FROM trans_
GROUP BY user_id
ORDER BY user_id; 

 user_id | total_spent_gbp 
---------+-----------------
       1 |         23.7970
       2 |         42.7370
       3 |               2
       4 |            3.24
(4 rows)


```

```sql

# SQL/spend_GBP_rate_latest_transaction.sql

psql> 

WITH exchange_ts AS
  (SELECT ts,
          from_currency,
          to_currency,
          rate
   FROM exchange_rates
   WHERE to_currency = 'GBP'),
     exchange_ts_lag AS
  (SELECT *,
          lag(ts, -1, NULL) OVER (PARTITION BY from_currency,
                                               to_currency
                                  ORDER BY ts) AS ts_lag
   FROM exchange_rates
   WHERE to_currency = 'GBP' ),
     trans_to_GBP AS
  (SELECT t.user_id AS user_id,
          t.ts AS ts,
          t.currency AS currency,
          t.amount*e.rate AS amount_GBP
   FROM transactions t
   INNER JOIN exchange_ts_lag e ON e.from_currency = t.currency
   AND (t.ts >= e.ts
        AND (e.ts_lag > t.ts
             OR e.ts_lag IS NULL))),
     trans_in_GBP AS
  (SELECT user_id,
          ts,
          currency,
          amount AS amount_gbp
   FROM transactions
   WHERE currency = 'GBP' ),
     trans_ AS
  (SELECT *
   FROM trans_to_GBP
   UNION ALL SELECT *
   FROM trans_in_GBP)
SELECT user_id AS user_id,
       SUM(amount_gbp) AS total_spent_gbp
FROM trans_
GROUP BY user_id
ORDER BY user_id;

 user_id | total_spent_gbp 
---------+-----------------
       1 |         24.7780
       2 |         43.4720
       3 |               2
       4 |            3.84
(4 rows)



```


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
$ python REST/app.py  # run the REST app first for REST api unit tests as well 
$ pytest -v tests/    # run all the unit tests 

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