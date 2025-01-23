# *************************************************************************************
# COSC 310 Project - SkySage

# DESCRIPTION: Test cases for the backend location (search) endpoint and its controllers

# Author: Riley Eaton
# Date: 2024-11-30
# *************************************************************************************
import pytest
from fastapi.testclient import TestClient

from app.schemas.location_schema import LocationList, LocationSearch, Location
from app.config.test_config import test_config
from app.config.global_config import global_settings
from app.main import app

# Initialize the TestClient instance
client = TestClient(app)


# Test just the controller for getting a locations coordinates using pytest mocking to avoid api calls
def test_location_coordinates_controller(mocker):
    # Mock the model response
    mock_get = mocker.patch(
        "app.controllers.location_controller.location_coordinates_request"
    )
    mock_get.return_value = test_config.API_TEST_LOCATION_SEARCH_RESPONSE
    from app.controllers.location_controller import get_location_coordinates

    # Define a location search
    test_location = LocationSearch(
        search=test_config.API_TEST_LOCATION_SEARCH,
    )

    # Call the function being tested
    result = get_location_coordinates(test_location)

    # Assertions
    assert Location(**result)


# Test the location coordinates endpoint to ensure it returns a status of 200 and the correct data structure
def test_get_location_coordinates(mocker):
    # Mock the model response
    mock_get = mocker.patch(
        "app.controllers.location_controller.location_coordinates_request"
    )
    mock_get.return_value = test_config.API_TEST_LOCATION_SEARCH_RESPONSE

    # Make the GET request to the api/location/coordinates endpoint
    response = client.get(
        global_settings.GET_LOCATION_COORDINATES_ENDPOINT,
        params={
            "search": test_config.API_TEST_LOCATION_SEARCH,
        },
    )

    # Check the status code to see if its OK (200)
    assert response.status_code == 200

    # Check the response structure to see if it matches the schema
    data = response.json()
    assert Location(**data)


# Test the location coordinates endpoint with missing query parameters
def test_location_coordinates_dependency(mocker):
    # Mock the model response
    mock_get = mocker.patch(
        "app.controllers.location_controller.location_coordinates_request"
    )
    mock_get.return_value = test_config.API_TEST_LOCATION_SEARCH_RESPONSE

    # Send a request with a valid query parameter
    success_response = client.get(
        f"{global_settings.GET_LOCATION_COORDINATES_ENDPOINT}?search={test_config.API_TEST_LOCATION_SEARCH}"
    )
    assert success_response.status_code == 200

    # Test missing parameter
    no_response = client.get(global_settings.GET_LOCATION_COORDINATES_ENDPOINT)
    assert no_response.status_code == test_config.API_TEST_MISSING_PARAMS_RESPONSE


# Test just the controller for getting location autocomplete using pytest mocking to avoid api calls
def test_autocomplete_location_controller(mocker):
    # Mock the model response
    mock_get = mocker.patch(
        "app.controllers.location_controller.autocomplete_location_request"
    )
    mock_get.return_value = test_config.API_TEST_AUTOCOMPLETE_LOCATION_RESPONSE
    from app.controllers.location_controller import get_autocomplete_location

    # Define a location search
    test_location = LocationSearch(
        search=test_config.API_TEST_AUTOCOMPLETE_LOCATION,
    )

    # Call the function being tested
    result = get_autocomplete_location(test_location)

    # Assertions
    assert LocationList(locations=result)


# Test the autocomplete location endpoint to ensure it returns a status of 200 and the correct data structure
def test_get_autocomplete_location(mocker):
    # Mock the model response
    mock_get = mocker.patch(
        "app.controllers.location_controller.autocomplete_location_request"
    )
    mock_get.return_value = test_config.API_TEST_AUTOCOMPLETE_LOCATION_RESPONSE

    # Make the GET request to the api/location/autocomplete endpoint
    response = client.get(
        global_settings.GET_AUTOCOMPLETE_LOCATIONS_ENDPOINT,
        params={
            "search": test_config.API_TEST_AUTOCOMPLETE_LOCATION,
        },
    )

    # Check the status code to see if its OK (200)
    assert response.status_code == 200

    # Check the response structure to see if it matches the schema
    data = response.json()
    assert LocationList(locations=data)


# Test the autocomplete location endpoint with missing query parameters
def test_autocomplete_location_dependency(mocker):
    # Mock the model response
    mock_get = mocker.patch(
        "app.controllers.location_controller.autocomplete_location_request"
    )
    mock_get.return_value = test_config.API_TEST_AUTOCOMPLETE_LOCATION_RESPONSE

    # Send a request with a valid query parameter
    success_response = client.get(
        f"{global_settings.GET_AUTOCOMPLETE_LOCATIONS_ENDPOINT}?search={test_config.API_TEST_AUTOCOMPLETE_LOCATION}"
    )
    assert success_response.status_code == 200

    # Test missing parameter
    no_response = client.get(global_settings.GET_AUTOCOMPLETE_LOCATIONS_ENDPOINT)
    assert no_response.status_code == test_config.API_TEST_MISSING_PARAMS_RESPONSE
