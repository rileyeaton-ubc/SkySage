# *************************************************************************************
# COSC 310 Project - SkySage
#
# Description: Controller for location endpoints to get data from the model, run
#              operations on it, and then pass it back to the router for returning
#
# Author: Riley Eaton
# Date: 2024-11-30
# *************************************************************************************
from app.models.location_model import (
    location_coordinates_request,
    autocomplete_location_request,
)
from app.schemas.location_schema import LocationSearch
from fastapi import HTTPException


# Function to get the coordinates location search, called by the location router
# Expects a Location search object as a parameter
def get_location_coordinates(search: LocationSearch):
    try:
        # Call the location_coordinates_request function from the location model to get data
        coordinates_obj = location_coordinates_request(search=search.search)
        location = coordinates_obj["places"][0]

        return {
            "latitude": location["location"]["latitude"],
            "longitude": location["location"]["longitude"],
        }
    except Exception as e:
        # If there is any exception, a 500 status will be returned with the following message
        raise HTTPException(
            status_code=500,
            detail=f"Get location coordinates failed: Internal Server Error",
        )


# Function to get a list of autocompleted locations for a search, called by the location router
# Expects a Location search object as a parameter
def get_autocomplete_location(search: LocationSearch):
    try:
        # Call the autocomplete_location_request function from the location model to get data
        autocomplete_obj = autocomplete_location_request(search=search.search)
        suggestion_list = autocomplete_obj["suggestions"]
        return_suggestions = []
        # Loop through each suggestion list
        for i in range(len(suggestion_list)):
            # Get the name and key for each suggestion
            suggestion = suggestion_list[i]["placePrediction"]
            return_suggestions.append(
                {
                    "name": suggestion["text"]["text"],
                }
            )

        return return_suggestions
    except Exception as e:
        # If there is any exception, a 500 status will be returned with the following message
        raise HTTPException(
            status_code=500,
            detail=f"Get autocomplete location failed: Internal Server Error",
        )
