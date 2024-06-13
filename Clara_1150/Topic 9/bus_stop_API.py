import requests


def get_bus_departures(url):
    response = requests.get(url).json()
    departures = response['departures']
    return departures

# API url to get bus arrival at the northbound stop outside MCTC
url_north = 'http://svc.metrotransit.org/NexTrip/17940?format=json'
north_departures = get_bus_departures(url_north)

url_south = ' http://svc.metrotransit.org/NexTrip/17928?format=json'
south_departures = get_bus_departures(url_south)

for bus_info_n in north_departures:
    route_description = bus_info_n['route_id']
    print('\nyour bus info is the following the north departures:\n ', route_description)  # Each one printed out is a simple dictionary
    # todo - departure_text, route_id

for bus_info_s in south_departures:
    route_description = bus_info_s['route_id']
    print('\nyour bus info is the following for the south departures:\n', route_description)


# TODO: make each function return what we are trying to get, route_id, time, and route description

for bus_info_s in north_departures:
    time_description = bus_info_s['departure_time']
    print('\nyour bus info is the following for the south departures:\n', time_description)

for bus_info_s in south_departures:
    time_description = bus_info_s['departure_time']
    print('\nyour bus info is the following for the south departures:\n', time_description)


for bus_info_s in north_departures:
    relationship = bus_info_s['schedule_relationship']
    print('\nyour bus info is the following for the south departures:\n', relationship)

for bus_info_s in south_departures:
    relationship = bus_info_s['schedule_relationship']
    print('\nyour bus info is the following for the south departures:\n', relationship)


for bus_info_s in north_departures:
    dest_description = bus_info_s['description']
    print('\nyour bus info is the following for the south departures:\n', dest_description)

for bus_info_s in south_departures:
    dest_description = bus_info_s['description']
    print('\nyour bus info is the following for the south departures:\n', dest_description)

