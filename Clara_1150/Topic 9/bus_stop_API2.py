import requests

def main():
    url_north = 'http://svc.metrotransit.org/NexTrip/17940?format=json'
    north_departures = get_bus_departures(url_north)

    url_south = ' http://svc.metrotransit.org/NexTrip/17928?format=json'
    south_departures = get_bus_departures(url_south)
def get_bus_departures(url):
    response = requests.get(url).json()
    departures = response['departures']
    return departures


def description():
    for bus_info_n in north_departures:
        n_route_description = bus_info_n['route_id']

    for bus_info_s in south_departures:
        s_route_description = bus_info_s['route_id']
    return n_route_description,s_route_description


def departure():
    for bus_info_s in north_departures:
        n_time_description = bus_info_s['departure_time']

    for bus_info_s in south_departures:
        s_time_description = bus_info_s['departure_time']
    return n_time_description,s_time_description


def schedule():
    for bus_info_s in north_departures:
        n_relationship = bus_info_s['schedule_relationship']

    for bus_info_s in south_departures:
        s_relationship = bus_info_s['schedule_relationship']
   return n_relationship,s_relationship

def departures():
    for bus_info_s in north_departures:
        n_dest_description = bus_info_s['description']

    for bus_info_s in south_departures:
        s_dest_description = bus_info_s['description']
    return n_dest_description, s_dest_description

main():
