"""
Mark Porraz
weather API.py
this program makes a call to a weather API, next step is to place in function
"""
import requests

# The URL for the weather API
url = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'
forecast = requests.get(url).json()  # correct syntax for getting a URL request in the JSON format

# accessing the key from the API that we want to locate, which is hours
list_of_weather_conditions = forecast['hourly']

# we are creating an empty list to store our data into from the 'hourly' key from the dictionary
weather = {}

# create a loop that goes over the list of weather conditions within API call
for hourly_data in list_of_weather_conditions:
    if weather:  # if the data in the hourly key exists, put it in an empty list called weather
        # below we are specific again on what data to pull out.
        time = hourly_data['time']  # we would like the hourly time
        temperature_2m = hourly_data['temperature_2m']  # we would like the hourly temperature
        relative_humidity_2m = hourly_data['relative_humidity_2m']  # we would like the hourly humidity
        wind_speed_10m = hourly_data['wind_speed_10m']  # we would like the hourly wind speed
    print(list_of_weather_conditions)  # print a new list of weather conditions

#TODO: place this into a function
