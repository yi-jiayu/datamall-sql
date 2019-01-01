import json
from elasticsearch import Elasticsearch, helpers


def bus_stops_bulk_generator(bus_stops):
    for stop in bus_stops:
        yield {
            '_index': 'bus_stops',
            '_type': '_doc',
            '_id': stop['BusStopCode'],
            '_source': {
                'bus_stop_code': stop['BusStopCode'],
                'road_name': stop['RoadName'],
                'description': stop['Description'],
                'location': {
                    'lat': stop['Latitude'],
                    'lon': stop['Longitude']
                }
            }
        }


if __name__ == '__main__':
    with open('bus_stops.json') as f:
        bus_stops = json.load(f)

    client = Elasticsearch()
    helpers.bulk(client, bus_stops_bulk_generator(bus_stops))
