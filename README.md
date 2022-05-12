# Flask Web API

This repository contains:
1. api.py - The Flask web application containing the API.
2. csv_to_db.py - A Python file with some basic Sqlite3 helper functions to generate.
3. data - A folder containing the CSV file and sqlite3 database.
3. chart in curtain circumstances

## Install

This project uses [Flask](https://pypi.org/project/Flask/) and [Sqlite3](https://pypi.org/project/pysqlite/). Go check them out if you don't have them locally installed.


## WARNING!THIS PROGRAM CANNOT BE RUNNING IF YOU DONT GENERATE CSV DATA TO SQL. FOLLOW THIS STEP
```sh
1. Generate csv to database sql
2. you can use the api
3. you can generate every chart/graph based on sql
```


## HOW TO GENERATE THE CSV TO DATABASE
```sh

$ pip install sqlite
$ pip install flask
$ python3 csv_to_db.py
```
![alt text](https://github.com/faurelgema/simple_api_and_graph_jumlah_pns/blob/main/restapi1.jpg)

## HOW TO RUN THE API 
```sh

$ python3 api.py

and use postman to hit, example with this link:
127.0.0.1:5000/api/v1/pns/getAll
```

## HOW TO RUN LINE GRAPH TO COUNT JABATAN 
```sh
$ python3 chart.py
```
![alt text](https://github.com/faurelgema/simple_api_and_graph_jumlah_pns/blob/main/chart1.jpg)

## HOW TO RUN BAR GRAPH TO SEE EVERY JABATAN PNS
```sh

$ python3 chart2.py
```
![alt text](https://github.com/faurelgema/simple_api_and_graph_jumlah_pns/blob/main/chart2.jpg)

## HOW TO RUN PIE GRAPH TO COUNT PNS IN EVERY YEARS
```sh

$ python3 chart3.py
```

![alt text](https://github.com/faurelgema/simple_api_and_graph_jumlah_pns/blob/main/chart3.jpg)
