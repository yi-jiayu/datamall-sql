# DataMall SQL
LTA DataMall data as an SQLite database

## Included datasets
- Bus stops
- Bus routes

## Generating the database
If you want to generate the database using the latest data, you will need a DataMall Account Key. Make sure it is in an exported environment variable called `DATAMALL_ACCOUNT_KEY` then run `create_db.sh`:

```console
$ ./create_db.sh 
[START] Fetch bus stops
Fetched 5007 bus stops.
[END]   Fetch bus stops
[START] Collect bus stops
[END]   Collect bus stops
[START] Write bus stops
[END]   Write bus stops
[START] Fetch bus routes
Fetched 26094 bus routes.
[END]   Fetch bus routes
[START] Collect bus routes
[END]   Collect bus routes
[START] Write bus routes
[END]   Write bus routes
Created sqlite database datamall.sqlite
Inserted 5007 rows into bus_stops
Inserted 26094 rows into bus_routes
```

## Sample queries

```console
$ sqlite3 datamall.sqlite 
SQLite version 3.24.0 2018-06-04 14:10:15
Enter ".help" for usage hints.
sqlite> .headers on
sqlite> .mode column
sqlite> select * from bus_stops where bus_stop_code = '81111';
bus_stop_code  road_name      description            latitude          longitude       
-------------  -------------  ---------------------  ----------------  ----------------
81111          Paya Lebar Rd  Paya Lebar Stn Exit B  1.31860238558389  103.892116897906
sqlite> select service_no from bus_routes where bus_stop_code = '81111';
service_no
----------
134       
135       
135A      
137       
154       
155       
24        
28        
43        
70        
70A       
70M       
76        
sqlite> 
```
