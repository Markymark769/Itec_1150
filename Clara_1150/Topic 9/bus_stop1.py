import requests

#
# API url to get buss arrival at the northbound stop outside MCTC
url_north = 'http://svc.metrotransit.org/NexTrip/17940?format=json'

# API url to get buss arrival at the southbound stop outside MCTC
url_south = ' http://svc.metrotransit.org/NexTrip/17928?format=json'

# what server to connect to: http://svc.metrotransit.org
# what data do you want: NexTrip/17940?format=json for north and NexTrip/17928?format=json for south

north_response = requests.get(url_north).json()  # north_response to clear this data us for northbound buses

print(north_response)

north_departures = north_response['departures']
print(north_departures)

for bus_info in north_departures:
    description = bus_info
    print(bus_info)  # Each one printed out is a simple dictionary
    # todo - departure_text, route_id
