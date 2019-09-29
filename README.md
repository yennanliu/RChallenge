# RChallenge

### SQL 

### Python 

```bash
# run the json transformation  process
$ git clone https://github.com/yennanliu/RChallenge.git
$ cd RChallenge  && pip install -r requirements.txt 
$ cat data/input.json  | python Python/run.py country city currency

# run tests 
$ pytest -v tests/

```

### REST

```bash 
curl -i -H "Content-Type: application/json" -X POST -d '{"input_json":"data/input.json", "keys":["country", "city"]}' http://localhost:5000/REST/api/v1.0/nest

```