"""
Mark Porraz
weather API
weather call from API site

Short:
https://open-meteo.com/en/docs#current=&hourly=&daily=weather_code,temperature_2m_max,temperature_2m_min,sunrise,daylight_duration,rain_sum,showers_sum,snowfall_sum,wind_speed_10m_max,wind_gusts_10m_max,wind_direction_10m_dominant&timezone=America%2FChicago&forecast_days=14&start_date=2024-08-05&end_date=2024-08-18&time_mode=time_interval

long:
https://open-meteo.com/en/docs#current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,rain,showers,snowfall,weather_code&hourly=temperature_2m,relative_humidity_2m,precipitation_probability,precipitation,rain,cloud_cover,cloud_cover_low,cloud_cover_mid,cloud_cover_high,wind_speed_10m,wind_speed_80m,wind_speed_120m,wind_speed_180m,temperature_120m&daily=weather_code,temperature_2m_max,temperature_2m_min,sunrise,daylight_duration,rain_sum,showers_sum,snowfall_sum,wind_speed_10m_max,wind_gusts_10m_max,wind_direction_10m_dominant&timezone=America%2FChicago&forecast_days=14&start_date=2024-08-05&end_date=2024-08-18&time_mode=time_interval

Install:
pip install openmeteo-requests
pip install requests-cache retry-requests numpy pandas

"""

import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,rain,showers,snowfall,weather_code&hourly=temperature_2m,relative_humidity_2m,precipitation_probability,precipitation,rain,cloud_cover,cloud_cover_low,cloud_cover_mid,cloud_cover_high,wind_speed_10m,wind_speed_80m,wind_speed_120m,wind_speed_180m,temperature_120m&daily=weather_code,temperature_2m_max,temperature_2m_min,sunrise,daylight_duration,rain_sum,showers_sum,snowfall_sum,wind_speed_10m_max,wind_gusts_10m_max,wind_direction_10m_dominant&timezone=America%2FChicago&start_date=2024-08-05&end_date=2024-08-18"
params = {
	"latitude": 52.52,
	"longitude": 13.41,
	"daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "sunrise", "daylight_duration", "rain_sum", "showers_sum", "snowfall_sum", "wind_speed_10m_max", "wind_gusts_10m_max", "wind_direction_10m_dominant"],
	"timezone": "America/Chicago",
	"start_date": "2024-08-05",
	"end_date": "2024-08-18"
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# Process daily data. The order of variables needs to be the same as requested.
daily = response.Daily()
daily_weather_code = daily.Variables(0).ValuesAsNumpy()
daily_temperature_2m_max = daily.Variables(1).ValuesAsNumpy()
daily_temperature_2m_min = daily.Variables(2).ValuesAsNumpy()
daily_sunrise = daily.Variables(3).ValuesAsNumpy()
daily_daylight_duration = daily.Variables(4).ValuesAsNumpy()
daily_rain_sum = daily.Variables(5).ValuesAsNumpy()
daily_showers_sum = daily.Variables(6).ValuesAsNumpy()
daily_snowfall_sum = daily.Variables(7).ValuesAsNumpy()
daily_wind_speed_10m_max = daily.Variables(8).ValuesAsNumpy()
daily_wind_gusts_10m_max = daily.Variables(9).ValuesAsNumpy()
daily_wind_direction_10m_dominant = daily.Variables(10).ValuesAsNumpy()

daily_data = {"date": pd.date_range(
	start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
	end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = daily.Interval()),
	inclusive = "left"
)}
daily_data["weather_code"] = daily_weather_code
daily_data["temperature_2m_max"] = daily_temperature_2m_max
daily_data["temperature_2m_min"] = daily_temperature_2m_min
daily_data["sunrise"] = daily_sunrise
daily_data["daylight_duration"] = daily_daylight_duration
daily_data["rain_sum"] = daily_rain_sum
daily_data["showers_sum"] = daily_showers_sum
daily_data["snowfall_sum"] = daily_snowfall_sum
daily_data["wind_speed_10m_max"] = daily_wind_speed_10m_max
daily_data["wind_gusts_10m_max"] = daily_wind_gusts_10m_max
daily_data["wind_direction_10m_dominant"] = daily_wind_direction_10m_dominant

daily_dataframe = pd.DataFrame(data = daily_data)
print(daily_dataframe)

# # Setup the Open-Meteo API client with cache and retry on error
# cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
# retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
# openmeteo = openmeteo_requests.Client(session = retry_session)
#
# # Make sure all required weather variables are listed here
# # The order of variables in hourly or daily is important to assign them correctly below
# url = "https://api.open-meteo.com/v1/forecast"
# params = {
# 	"latitude": 52.52,
# 	"longitude": 13.41,
# 	"current": ["temperature_2m", "relative_humidity_2m", "apparent_temperature", "is_day", "precipitation", "rain", "showers", "snowfall", "weather_code"],
# 	"hourly": ["temperature_2m", "relative_humidity_2m", "precipitation_probability", "precipitation", "rain", "cloud_cover", "cloud_cover_low", "cloud_cover_mid", "cloud_cover_high", "wind_speed_10m", "wind_speed_80m", "wind_speed_120m", "wind_speed_180m", "temperature_120m"],
# 	"daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "sunrise", "daylight_duration", "rain_sum", "showers_sum", "snowfall_sum", "wind_speed_10m_max", "wind_gusts_10m_max", "wind_direction_10m_dominant"],
# 	"timezone": "America/Chicago",
# 	"start_date": "2024-08-05",
# 	"end_date": "2024-08-18"
# }
# responses = openmeteo.weather_api(url, params=params)
#
# # Process first location. Add a for-loop for multiple locations or weather models
# response = responses[0]
# print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
# print(f"Elevation {response.Elevation()} m asl")
# print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
# print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")
#
# # Current values. The order of variables needs to be the same as requested.
# current = response.Current()
# current_temperature_2m = current.Variables(0).Value()
# current_relative_humidity_2m = current.Variables(1).Value()
# current_apparent_temperature = current.Variables(2).Value()
# current_is_day = current.Variables(3).Value()
# current_precipitation = current.Variables(4).Value()
# current_rain = current.Variables(5).Value()
# current_showers = current.Variables(6).Value()
# current_snowfall = current.Variables(7).Value()
# current_weather_code = current.Variables(8).Value()
#
# print(f"Current time {current.Time()}")
# print(f"Current temperature_2m {current_temperature_2m}")
# print(f"Current relative_humidity_2m {current_relative_humidity_2m}")
# print(f"Current apparent_temperature {current_apparent_temperature}")
# print(f"Current is_day {current_is_day}")
# print(f"Current precipitation {current_precipitation}")
# print(f"Current rain {current_rain}")
# print(f"Current showers {current_showers}")
# print(f"Current snowfall {current_snowfall}")
# print(f"Current weather_code {current_weather_code}")
#
# # Process hourly data. The order of variables needs to be the same as requested.
# hourly = response.Hourly()
# hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
# hourly_relative_humidity_2m = hourly.Variables(1).ValuesAsNumpy()
# hourly_precipitation_probability = hourly.Variables(2).ValuesAsNumpy()
# hourly_precipitation = hourly.Variables(3).ValuesAsNumpy()
# hourly_rain = hourly.Variables(4).ValuesAsNumpy()
# hourly_cloud_cover = hourly.Variables(5).ValuesAsNumpy()
# hourly_cloud_cover_low = hourly.Variables(6).ValuesAsNumpy()
# hourly_cloud_cover_mid = hourly.Variables(7).ValuesAsNumpy()
# hourly_cloud_cover_high = hourly.Variables(8).ValuesAsNumpy()
# hourly_wind_speed_10m = hourly.Variables(9).ValuesAsNumpy()
# hourly_wind_speed_80m = hourly.Variables(10).ValuesAsNumpy()
# hourly_wind_speed_120m = hourly.Variables(11).ValuesAsNumpy()
# hourly_wind_speed_180m = hourly.Variables(12).ValuesAsNumpy()
# hourly_temperature_120m = hourly.Variables(13).ValuesAsNumpy()
#
# hourly_data = {"date": pd.date_range(
# 	start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
# 	end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
# 	freq = pd.Timedelta(seconds = hourly.Interval()),
# 	inclusive = "left"
# )}
# hourly_data["temperature_2m"] = hourly_temperature_2m
# hourly_data["relative_humidity_2m"] = hourly_relative_humidity_2m
# hourly_data["precipitation_probability"] = hourly_precipitation_probability
# hourly_data["precipitation"] = hourly_precipitation
# hourly_data["rain"] = hourly_rain
# hourly_data["cloud_cover"] = hourly_cloud_cover
# hourly_data["cloud_cover_low"] = hourly_cloud_cover_low
# hourly_data["cloud_cover_mid"] = hourly_cloud_cover_mid
# hourly_data["cloud_cover_high"] = hourly_cloud_cover_high
# hourly_data["wind_speed_10m"] = hourly_wind_speed_10m
# hourly_data["wind_speed_80m"] = hourly_wind_speed_80m
# hourly_data["wind_speed_120m"] = hourly_wind_speed_120m
# hourly_data["wind_speed_180m"] = hourly_wind_speed_180m
# hourly_data["temperature_120m"] = hourly_temperature_120m
#
# hourly_dataframe = pd.DataFrame(data = hourly_data)
# print(hourly_dataframe)
#
# # Process daily data. The order of variables needs to be the same as requested.
# daily = response.Daily()
# daily_weather_code = daily.Variables(0).ValuesAsNumpy()
# daily_temperature_2m_max = daily.Variables(1).ValuesAsNumpy()
# daily_temperature_2m_min = daily.Variables(2).ValuesAsNumpy()
# daily_sunrise = daily.Variables(3).ValuesAsNumpy()
# daily_daylight_duration = daily.Variables(4).ValuesAsNumpy()
# daily_rain_sum = daily.Variables(5).ValuesAsNumpy()
# daily_showers_sum = daily.Variables(6).ValuesAsNumpy()
# daily_snowfall_sum = daily.Variables(7).ValuesAsNumpy()
# daily_wind_speed_10m_max = daily.Variables(8).ValuesAsNumpy()
# daily_wind_gusts_10m_max = daily.Variables(9).ValuesAsNumpy()
# daily_wind_direction_10m_dominant = daily.Variables(10).ValuesAsNumpy()
#
# daily_data = {"date": pd.date_range(
# 	start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
# 	end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
# 	freq = pd.Timedelta(seconds = daily.Interval()),
# 	inclusive = "left"
# )}
# daily_data["weather_code"] = daily_weather_code
# daily_data["temperature_2m_max"] = daily_temperature_2m_max
# daily_data["temperature_2m_min"] = daily_temperature_2m_min
# daily_data["sunrise"] = daily_sunrise
# daily_data["daylight_duration"] = daily_daylight_duration
# daily_data["rain_sum"] = daily_rain_sum
# daily_data["showers_sum"] = daily_showers_sum
# daily_data["snowfall_sum"] = daily_snowfall_sum
# daily_data["wind_speed_10m_max"] = daily_wind_speed_10m_max
# daily_data["wind_gusts_10m_max"] = daily_wind_gusts_10m_max
# daily_data["wind_direction_10m_dominant"] = daily_wind_direction_10m_dominant
#
# daily_dataframe = pd.DataFrame(data = daily_data)
# print(daily_dataframe)
