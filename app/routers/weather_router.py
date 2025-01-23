# *************************************************************************************
# COSC 310 Project - SkySage
#
# Description: Router for weather endpoint to handle incoming requests and return
#              responses from the various controllers
#
# Author: Riley Eaton
# Date: 2024-11-25
# *************************************************************************************

from fastapi import APIRouter, Depends, Query
from app.schemas.location_schema import Location
from app.controllers.weather_controller import get_current_weather, get_forecast_weather

# Initialize APIRouter instance for all /weather routes
router = APIRouter(prefix="/api/weather", tags=["weather"])


# Define a function to get the location details (lat & lon) from query parameters
def get_location(
    latitude: float = Query(...), longitude: float = Query(...)
) -> Location:
    return Location(latitude=latitude, longitude=longitude)


# Route to get the current weather for a location
# Expect a Location object as query parameter
# /weather/current
@router.get("/current")
def current_weather(location: Location = Depends(get_location)):
    # Call and return the get_current_weather function from the weather controller
    return get_current_weather(location)


# Route to get the forecasted weather for a location
# Expect a Location object as query parameter
# /weather/forecast
@router.get("/forecast")
def forecast_weather(location: Location = Depends(get_location)):
    # Call and return the get_forecast_weather function from the weather controller
    return get_forecast_weather(location)
