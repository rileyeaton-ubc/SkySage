# *************************************************************************************
# COSC 310 Project - SkySage
#
# Description: Router for location to handle incoming requests and return
#              responses from the various controllers
#
# Author: Riley Eaton
# Date: 2024-11-30
# *************************************************************************************

from fastapi import APIRouter, Depends, Query
from app.schemas.location_schema import LocationSearch
from app.controllers.location_controller import (
    get_location_coordinates,
    get_autocomplete_location,
)

# Initialize APIRouter instance for all /location routes
router = APIRouter(prefix="/api/location", tags=["location"])


# Define a function to get the search text from query parameter(s)
def get_search(search: str = Query(...)) -> LocationSearch:
    return LocationSearch(search=search)


# Route to get the coordinates for a location
# Expect a location search object as query parameter
# /location/coordinates
@router.get("/coordinates")
def location_coordinates(search: LocationSearch = Depends(get_search)):
    # Call and return the get_current_weather function from the weather controller
    return get_location_coordinates(search)


# Route to get the autocomplete locations for a search
# Expect a location search object as query parameter
# /location/autocomplete
@router.get("/autocomplete")
def autocomplete_weather(search: LocationSearch = Depends(get_search)):
    # Call and return the get_forecast_weather function from the weather controller
    return get_autocomplete_location(search)
