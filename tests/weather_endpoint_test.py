# *************************************************************************************
# COSC 310 Project - SkySage

# DESCRIPTION: Test cases for the backend weather endpoint and its controllers

# Author: Riley Eaton
# Date: 2024-11-25
# *************************************************************************************
import pytest
from fastapi.testclient import TestClient
from app.schemas.weather_schema import CurrentWeather, ForecastWeather
from app.schemas.location_schema import Location
from app.config.test_config import test_config
from app.config.global_config import global_settings
from app.main import app

# Initialize the TestClient instance
client = TestClient(app)


# Test just the controller for current weather using pytest mocking to avoid api calls
def test_current_weather_controller(mocker):
    # Mock the model response
    mock_get = mocker.patch(
        "app.controllers.weather_controller.current_weather_request"
    )
    mock_get.return_value = test_config.API_TEST_CURRENT_WEATHER_RESPONSE
    from app.controllers.weather_controller import get_current_weather

    # Define a location
    test_location = Location(
        latitude=test_config.API_TEST_LOCATION_LAT,
        longitude=test_config.API_TEST_LOCATION_LON,
    )

    # Call the function being tested
    result = get_current_weather(test_location)

    # Assertions
    assert CurrentWeather(**result)


# Test the current weather endpoint to ensure it returns a status of 200 and the correct data structure
def test_get_current_weather(mocker):
    # Mock the model response
    mock_get = mocker.patch(
        "app.controllers.weather_controller.current_weather_request"
    )
    mock_get.return_value = test_config.API_TEST_CURRENT_WEATHER_RESPONSE

    # Make the GET request to the /weather/current endpoint
    response = client.get(
        global_settings.GET_CURRENT_WEATHER_ENDPOINT,
        params={
            "latitude": test_config.API_TEST_LOCATION_LAT,
            "longitude": test_config.API_TEST_LOCATION_LON,
        },
    )

    # Check the status code to see if its OK (200)
    assert response.status_code == 200

    # Check the response structure to see if it matches the schema
    data = response.json()
    assert CurrentWeather(**data)


# Test the current weather endpoint with missing query parameters
def test_current_weather_location_dependency(mocker):
    # Mock the model response
    mock_get = mocker.patch(
        "app.controllers.weather_controller.current_weather_request"
    )
    mock_get.return_value = test_config.API_TEST_CURRENT_WEATHER_RESPONSE

    # Send a request with valid query parameters
    success_response = client.get(
        f"{global_settings.GET_CURRENT_WEATHER_ENDPOINT}?latitude={test_config.API_TEST_LOCATION_LAT}&longitude={test_config.API_TEST_LOCATION_LON}"
    )
    assert success_response.status_code == 200

    # Test a single missing parameter
    partial_response = client.get(
        f"{global_settings.GET_CURRENT_WEATHER_ENDPOINT}?latitude={test_config.API_TEST_LOCATION_LAT}"
    )
    assert partial_response.status_code == test_config.API_TEST_MISSING_PARAMS_RESPONSE

    # Test both missing parameters
    no_response = client.get(global_settings.GET_CURRENT_WEATHER_ENDPOINT)
    assert no_response.status_code == test_config.API_TEST_MISSING_PARAMS_RESPONSE


# Test just the controller for forecast weather using pytest mocking to avoid api calls
def test_forecast_weather_controller(mocker):
    # Mock the model response
    mock_get = mocker.patch(
        "app.controllers.weather_controller.forecast_weather_request"
    )
    mock_get.return_value = test_config.API_TEST_FORECAST_WEATHER_RESPONSE
    from app.controllers.weather_controller import get_forecast_weather

    # Define a location
    test_location = Location(
        latitude=test_config.API_TEST_LOCATION_LAT,
        longitude=test_config.API_TEST_LOCATION_LON,
    )

    # Call the function being tested
    result = get_forecast_weather(test_location)

    # Assertions
    assert ForecastWeather(**result)


# Test the forecast weather endpoint to ensure it returns a status of 200 and the correct data structure
def test_get_forecast_weather(mocker):
    # Mock the model response
    mock_get = mocker.patch(
        "app.controllers.weather_controller.forecast_weather_request"
    )
    mock_get.return_value = test_config.API_TEST_FORECAST_WEATHER_RESPONSE

    # Make the GET request to the /weather/forecast endpoint
    response = client.get(
        global_settings.GET_FORECAST_WEATHER_ENDPOINT,
        params={
            "latitude": test_config.API_TEST_LOCATION_LAT,
            "longitude": test_config.API_TEST_LOCATION_LON,
        },
    )

    # Check the status code to see if its OK (200)
    assert response.status_code == 200

    # Check the response structure to see if it matches the schema
    data = response.json()
    assert ForecastWeather(**data)


# Test the forecast weather endpoint with missing query parameters
def test_forecast_weather_location_dependency(mocker):
    # Mock the model response
    mock_get = mocker.patch(
        "app.controllers.weather_controller.forecast_weather_request"
    )
    mock_get.return_value = test_config.API_TEST_FORECAST_WEATHER_RESPONSE
    # Send a request with valid query parameters
    success_response = client.get(
        f"{global_settings.GET_FORECAST_WEATHER_ENDPOINT}?latitude={test_config.API_TEST_LOCATION_LAT}&longitude={test_config.API_TEST_LOCATION_LON}"
    )
    assert success_response.status_code == 200

    # Test a single missing parameter
    partial_response = client.get(
        f"{global_settings.GET_FORECAST_WEATHER_ENDPOINT}?latitude={test_config.API_TEST_LOCATION_LAT}"
    )
    assert partial_response.status_code == test_config.API_TEST_MISSING_PARAMS_RESPONSE

    # Test both missing parameters
    no_response = client.get(global_settings.GET_FORECAST_WEATHER_ENDPOINT)
    assert no_response.status_code == test_config.API_TEST_MISSING_PARAMS_RESPONSE
