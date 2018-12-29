create table bus_stops
(
  bus_stop_code text primary key,
  road_name     text,
  description   text,
  latitude      real,
  longitude     real
);

create table bus_routes
(
  service_no    text,
  operator      text,
  direction     integer,
  stop_sequence integer,
  bus_stop_code text references bus_stops(bus_stop_code),
  distance      real,
  wd_first_bus  text,
  wd_last_bus   text,
  sat_first_bus text,
  sat_last_bus  text,
  sun_first_bus text,
  sun_last_bus  text
);
create index bus_routes_bus_stop_codes on bus_routes(bus_stop_code);
