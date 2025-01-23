# *************************************************************************************
# COSC 310 Project - SkySage

# DESCRIPTION: Test cases for the backend email endpoint and its controller(s)

# Author: Riley Eaton
# Date: 2024-12-02
# *************************************************************************************
import pytest
from fastapi.testclient import TestClient
from app.schemas.email_schema import BasicEmail
from app.schemas.shared_schema import SuccessStatus
from app.config.global_config import global_settings
from app.config.test_config import test_config
from app.main import app

# Initialize the TestClient instance
client = TestClient(app)


# Test the email send endpoint to ensure it returns a status of 200 and the correct data structure
def test_send_email(mocker):
    # Mock the model response
    mock_get = mocker.patch("app.controllers.email_controller.send_single_email")
    mock_get.return_value = test_config.API_SEND_EMAIL_RESPONSE

    # Make the post request to the api/email/send endpoint with the correct data structure
    sample_email_data = BasicEmail(
        to=test_config.API_TEST_EMAIL_SEND_TO,
        subject=test_config.API_TEST_EMAIL_SEND_SUBJECT,
        body=test_config.API_TEST_EMAIL_SEND_BODY,
    )
    response = client.post(
        global_settings.SEND_EMAIL_ENDPOINT,
        json=sample_email_data.model_dump(),
    )

    # Check the status code to see if its OK (200)
    assert response.status_code == 200

    response_data = response.json()
    success_status = response_data.get("success") == True
    wrapped_result = {"success": success_status}

    # assert success_status
    assert success_status
    assert SuccessStatus(**wrapped_result)


# Test the email send endpoint with missing data in request body
def test_send_email_dependency(mocker):
    # Mock the model response
    mock_get = mocker.patch("app.controllers.email_controller.send_single_email")
    mock_get.return_value = test_config.API_SEND_EMAIL_RESPONSE

    # Make the post request to the api/email/send endpoint with the correct data structure
    sample_email_data = BasicEmail(
        to=test_config.API_TEST_EMAIL_SEND_TO,
        subject=test_config.API_TEST_EMAIL_SEND_SUBJECT,
        body=test_config.API_TEST_EMAIL_SEND_BODY,
    )
    success_response = client.post(
        global_settings.SEND_EMAIL_ENDPOINT,
        json=sample_email_data.model_dump(),
    )

    assert success_response.status_code == 200

    # Test missing data
    no_response = client.post(global_settings.SEND_EMAIL_ENDPOINT)
    assert no_response.status_code == test_config.API_TEST_MISSING_PARAMS_RESPONSE
