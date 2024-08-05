"""
Mark Porraz
weather API.py
this program makes a call to a weather API, next step is to place in function

13 - day weather forecast
"""
import requests

# The URL for the weather API
url = ('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&daily=weather_code,temperature_2m_max,temperature_2m_min,sunrise,daylight_duration,rain_sum,showers_sum,snowfall_sum,wind_speed_10m_max,wind_gusts_10m_max,wind_direction_10m_dominant&timezone=America%2FChicago&start_date=2024-08-05&end_date=2024-08-18')

forecast = requests.get(url).json()  # correct syntax for getting a URL request in the JSON format

# accessing the key from the API that we want to locate, which is daily to access the key which is in a list of values
list_of_weather_conditions = forecast['daily']

# we are creating an empty list to store our data into from the 'daily' key from the dictionary
weather = {}

# create a loop that goes over the list of weather conditions within API call
for daily_data in list_of_weather_conditions:
    if weather:  # if the data in the daily key exists, put it in an empty list called weather
        # below we are specific again on what data to pull out.
        time = daily_data['time']  # we would like the daily time from the 5th to the 18th
        temperature_max = daily_data['temperature_2m_max']  # we would like the daily temperature from the 5th to the 18th
        temperature_min = daily_data['temperature_2m_min']
        daylight_duration = daily_data['daylight_duration']
        rain_sum = daily_data['rain_sum']
        showers_sum = daily_data['showers_sum']
        snowfall_sum = daily_data['snowfall_sum']
        wind_speed_max = daily_data['wind_speed_10m_max']
    print(list_of_weather_conditions)  # print a new list of weather conditions

#TODO: place this into a function
