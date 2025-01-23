# *************************************************************************************
# COSC 310 Project - SkySage
#
# Description: Model for weather to get data from the OpenWeather API and pass it back
#
# Author: Riley Eaton
# Date: 2024-11-25
# *************************************************************************************

from app.common.http_services import HttpClient
from app.config.global_config import global_settings

# Initialize the OpenWeather API key and HTTP client
api_key = global_settings.OPENWEATHER_API_KEY
http_client = HttpClient(
    base_url="https://api.openweathermap.org/data/2.5/",
    headers={"Content-Type": "application/json"},
)


# Get current weather data for a specific latitude and longitude
# Parameters:
#   => lat (float): Latitude of the location
#   => lon (float): Longitude of the location
#   => units (str): Units of measurement (default: "metric")
def current_weather_request(lat, lon, units="metric"):
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": units,
    }
    # Use the HTTP client to make a GET request to the OpenWeather API
    return http_client.get(endpoint="weather", params=params)


# Get forecasted weather data for a specific latitude and longitude
# Parameters:
#   => lat (float): Latitude of the location
#   => lon (float): Longitude of the location
#   => units (str): Units of measurement (default: "metric")
def forecast_weather_request(lat, lon, units="metric"):
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": units,
    }
    # Use the HTTP client to make a GET request to the OpenWeather API
    return http_client.get(endpoint="forecast", params=params)
