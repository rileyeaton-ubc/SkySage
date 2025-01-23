# *************************************************************************************
# COSC 310 Project - SkySage
#
# Description: Model for location to get data from the Google API and pass it back
#
# Author: Riley Eaton
# Date: 2024-11-25
# *************************************************************************************

from app.common.http_services import HttpClient
from app.config.global_config import global_settings

# Initialize the Google API key and HTTP client
http_client = HttpClient(
    base_url="https://places.googleapis.com/v1/places:",
    headers={
        "Content-Type": "application/json",
        "X-Goog-Api-Key": global_settings.GOOGLE_MAPS_API_KEY,
    },
)


# Get coordinate data for a specific location
# Parameters:
#   => search (str): String to search for the location
def location_coordinates_request(search):
    body = {
        "textQuery": search,
    }
    # Define extra headers for this request
    extra_headers = {
        "X-Goog-FieldMask": "places.displayName,places.formattedAddress,places.location"
    }
    # Use the HTTP client to make a POST request to Google API
    return http_client.post(endpoint="searchText", data=body, headers=extra_headers)


# Get forecasted weather data for a specific latitude and longitude
# Parameters:
#   => search (str): String to search for the location
def autocomplete_location_request(search):
    body = {
        "input": search,
    }
    # Use the HTTP client to make a POST request to the Google API
    return http_client.post(endpoint="autocomplete", data=body)
