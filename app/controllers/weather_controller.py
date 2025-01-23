# *************************************************************************************
# COSC 310 Project - SkySage
#
# Description: Controller for weather endpoint to get data from the model, run
#              operations on it, and then pass it back to the router for returning
#
# Author: Riley Eaton
# Date: 2024-11-25
# *************************************************************************************
from app.models.weather_model import current_weather_request, forecast_weather_request
from app.schemas.location_schema import Location
from fastapi import HTTPException
from datetime import datetime, timezone


# Function to get the current weather for a location, called by the weather router
# Expects a Location object as a parameter
def get_current_weather(location: Location):
    try:
        # Call the current_weather_request function from the weather model to get data
        weather_obj = current_weather_request(
            lat=location.latitude, lon=location.longitude
        )
        # Return a dictionary with the weather data, which was from the API response in the weather model
        return {
            "id": weather_obj["id"],
            "temperature": weather_obj["main"]["temp"],
            "feels_like": weather_obj["main"]["feels_like"],
            "temp_min": weather_obj["main"]["temp_min"],
            "temp_max": weather_obj["main"]["temp_max"],
            "pressure": weather_obj["main"]["pressure"],
            "humidity": weather_obj["main"]["humidity"],
            "conditions": weather_obj["weather"][0]["description"],
            "wind_speed": weather_obj["wind"]["speed"],
            "wind_direction": weather_obj["wind"]["deg"],
        }
    except Exception as e:
        # If there is any exception, a 500 status will be returned with the following message
        raise HTTPException(
            status_code=500, detail=f"Get current weather failed: Internal Server Error"
        )


# Function to get the forecasted weather for a location, called by the weather router
# Expects a Location object as a parameter
def get_forecast_weather(location: Location):
    try:
        # Call the forecast_weather_request function from the weather model to get data
        weather_obj = forecast_weather_request(
            lat=location.latitude, lon=location.longitude
        )

        # Get the current date and time in UTC for each forecasted time
        forecast_list_new = []
        # Set the timezone offset for the city based on what was returned from the API
        timestamp__zone_offset = weather_obj["city"]["timezone"]
        forecast_list = weather_obj["list"]
        # Loop through each forecasted dict
        for i in range(len(forecast_list)):
            # Get the local date and time in the city's timezone and convert it into a string
            timestamp = forecast_list[i].get("dt") + timestamp__zone_offset
            date_object = datetime.fromtimestamp(timestamp)
            date_string = date_object.strftime("%Y-%m-%d %H:%M")
            # Append the required data to the forecast list
            new_forecast_obj = {
                "date_string": date_string,
                "temperature": forecast_list[i]["main"]["temp"],
                "feels_like": forecast_list[i]["main"]["feels_like"],
                "temp_min": forecast_list[i]["main"]["temp_min"],
                "temp_max": forecast_list[i]["main"]["temp_max"],
                "pressure": forecast_list[i]["main"]["pressure"],
                "humidity": forecast_list[i]["main"]["humidity"],
                "conditions": forecast_list[i]["weather"][0]["description"],
                "cloud_cover_percent": forecast_list[i]["clouds"]["all"],
                "chance_of_precipitation": forecast_list[i]["pop"],
                "wind_speed": forecast_list[i]["wind"]["speed"],
                "wind_direction": forecast_list[i]["wind"]["deg"],
            }
            # Append the new forecast object to the list that will be returned
            forecast_list_new.append(new_forecast_obj)
        # Return a dictionary with the weather data, which was from the API response in the weather model
        return {
            "id": weather_obj["city"]["id"],
            "forecast_list": forecast_list_new,
        }
    except Exception as e:
        # If there is any exception, a 500 status will be returned with the following message
        raise HTTPException(
            status_code=500,
            detail=f"Get forecast weather failed: Internal Server Error",
        )
