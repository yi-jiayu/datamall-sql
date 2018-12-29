# DataMall SQL
LTA DataMall data as an SQLite database

## Included datasets
- Bus stops
- Bus routes

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
