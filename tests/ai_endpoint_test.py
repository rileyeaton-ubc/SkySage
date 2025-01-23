# *************************************************************************************
# COSC 310 Project - SkySage

# DESCRIPTION: Test cases for the backend ai (generation) endpoint and its controller(s)

# Author: Riley Eaton
# Date: 2024-12-01
# *************************************************************************************
import pytest
from fastapi.testclient import TestClient

from app.schemas.weather_schema import ForecastWeather
from app.schemas.ai_schema import BasicGeneration
from app.config.test_config import test_config
from app.config.global_config import global_settings
from app.main import app

# Initialize the TestClient instance
client = TestClient(app)


# Test just the controller for getting an ai generation using pytest mocking to avoid api calls
def test_weather_forecast_generation_controller(mocker):
    # Mock the model response
    mock_get = mocker.patch("app.controllers.ai_controller.gpt_generation_request")
    mock_get.return_value = test_config.API_TEST_AI_GENERATION_RESPONSE
    from app.controllers.ai_controller import get_weather_forecast_generation

    # Define an ai text input using a forecast weather object
    test_generation_input = ForecastWeather(
        **test_config.API_TEST_FORECAST_WEATHER_AI_INPUT
    )

    # Call the function being tested
    result = get_weather_forecast_generation(test_generation_input)
    wrapped_result = {"generated_text": result}

    # Assertions
    assert BasicGeneration(**wrapped_result)


# Test the ai generation endpoint to ensure it returns a status of 200 and the correct data structure
def test_get_ai_generation(mocker):
    # Mock the model response
    mock_get = mocker.patch("app.controllers.ai_controller.gpt_generation_request")
    mock_get.return_value = test_config.API_TEST_AI_GENERATION_RESPONSE

    # Make the GET request to the api/ai/generate/forecast endpoint
    response = client.post(
        global_settings.GET_GENERATE_AI_FORECAST_ENDPOINT,
        json=test_config.API_TEST_FORECAST_WEATHER_AI_INPUT,
    )

    # Check the status code to see if its OK (200)
    assert response.status_code == 200

    response_data = response.json()
    generated_text = response_data.get("ai_generation")

    # Wrap the extracted string for validation
    wrapped_result = {"generated_text": generated_text}

    # Assertions
    assert BasicGeneration(**wrapped_result)


# Test the ai generation endpoint with missing data in request body
def test_ai_generation_dependency(mocker):
    # Mock the model response
    mock_get = mocker.patch("app.controllers.ai_controller.gpt_generation_request")
    mock_get.return_value = test_config.API_TEST_AI_GENERATION_RESPONSE

    # Send a request with a valid body with data
    success_response = client.post(
        global_settings.GET_GENERATE_AI_FORECAST_ENDPOINT,
        json=test_config.API_TEST_FORECAST_WEATHER_AI_INPUT,
    )
    assert success_response.status_code == 200

    # Test missing data
    no_response = client.post(global_settings.GET_GENERATE_AI_FORECAST_ENDPOINT)
    assert no_response.status_code == test_config.API_TEST_MISSING_PARAMS_RESPONSE
