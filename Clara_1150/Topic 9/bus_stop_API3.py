import requests


def main():
    url_north = 'http://svc.metrotransit.org/NexTrip/17940?format=json'
    north_departures = get_bus_departures(url_north)

    url_south = 'http://svc.metrotransit.org/NexTrip/17928?format=json'
    south_departures = get_bus_departures(url_south)

    n_route_description, s_route_description = description(north_departures, south_departures)
    n_time_description, s_time_description = departure(north_departures, south_departures)
    n_relationship, s_relationship = schedule(north_departures, south_departures)
    n_dest_description, s_dest_description = departures(north_departures, south_departures)
    outputs(n_route_description,s_route_description,n_time_description, s_time_description,n_relationship,
            s_relationship, n_dest_description,s_dest_description)

def get_bus_departures(url):
    response = requests.get(url).json()
    departures = response['departures']
    return departures


def description(north_departures, south_departures):
    n_route_description = [bus_info_n['route_id'] for bus_info_n in north_departures]
    s_route_description = [bus_info_s['route_id'] for bus_info_s in south_departures]
    # for bus_info_n in north_departures:
    #     n_route_description = bus_info_n['route_id']
    #
    # for bus_info_s in south_departures:
    #     s_route_description = bus_info_s['route_id']
    return n_route_description, s_route_description


def departure(north_departures, south_departures):
    n_time_description = [bus_info_n['departure_time'] for bus_info_n in north_departures]
    s_time_description = [bus_info_s['departure_time'] for bus_info_s in south_departures]
    return n_time_description, s_time_description


def schedule(north_departures, south_departures):
    n_relationship = [bus_info_n['schedule_relationship'] for bus_info_n in north_departures]
    s_relationship = [bus_info_s['schedule_relationship'] for bus_info_s in south_departures]
    return n_relationship, s_relationship


def departures(north_departures, south_departures):
    n_dest_description = [bus_info_n['description'] for bus_info_n in north_departures]
    s_dest_description = [bus_info_s['description'] for bus_info_s in south_departures]
    return n_dest_description, s_dest_description


def outputs(n_route_description,s_route_description,n_time_description, s_time_description,n_relationship,
            s_relationship, n_dest_description,s_dest_description):

    print(f"Route descriptions: North - {n_route_description}, South - {s_route_description}")
    print(f"Departure times: North - {n_time_description}, South - {s_time_description}")
    print(f"Schedule relationships: North - {n_relationship}, South - {s_relationship}")
    print(f"Destination descriptions: North - {n_dest_description}, South - {s_dest_description}")

main()
