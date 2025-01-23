# *************************************************************************************
# COSC 310 Project - SkySage

# DESCRIPTION: Configuration file for testing the SQLite database using the db_test.py
# file

# Author: Riley Eaton
# Date: 2024-11-18
# *************************************************************************************

import os
from pydantic_settings import BaseSettings
from app.config.db_config import db_config
from app.config.weather_current_sample import (
    sample_response as current_weather_sample_response,
)
from app.config.weather_forecast_sample import (
    sample_response as forecast_weather_sample_response,
)
from app.config.location_autocomplete_sample import (
    sample_response as autocomplete_location_sample_response,
)
from app.config.location_search_sample import (
    sample_response as location_search_sample_response,
)
from app.config.ai_generation_sample import (
    sample_response as ai_generation_sample_response,
)
from app.config.ai_weather_forecast_sample import (
    sample_response as forecast_weather_ai_input,
)
from app.config.send_email_sample import sample_response as send_email_sample_response


class Settings(BaseSettings):
    # Test table names
    DB_TEST_TABLE: str = "test_table"
    DB_TEST_TABLE_2: str = "test_table_2"

    # Test table fields
    DB_TEST_ID_FIELD: str = "id"
    DB_TEST_NAME_FIELD: str = "name"
    DB_TEST_PASSWORD_FIELD: str = "password"

    # Test table columns
    DB_TEST_TABLE_COLUMNS: tuple = ("id", "name", "password")

    # Test table schema using the above fields
    DB_TEST_SCHEMA: str = (
        f"({DB_TEST_ID_FIELD} INTEGER PRIMARY KEY AUTOINCREMENT, {DB_TEST_NAME_FIELD} TEXT, {DB_TEST_PASSWORD_FIELD} TEXT)"
    )

    # Test table schema without the primary key (for insertions as the primary key is autoincremented)
    DB_TEST_SCHEMA_NOKEY: str = f"({DB_TEST_NAME_FIELD}, {DB_TEST_PASSWORD_FIELD})"

    # A pair of test usernames and passwords
    DB_TEST_USERNAME: str = "John Doe"
    DB_TEST_PASSWORD: str = "password"
    DB_TEST_USERNAME_2: str = "Mike Smith"
    DB_TEST_PASSWORD_2: str = "qwerty"

    # A test dashboard id
    DB_TEST_DASHBOARD_ID: int = 1

    # A test share id
    DB_TEST_SHARE_ID: int = 1

    # Test emails
    DB_TEST_EMAIL: str = "testemail@gmail.com"
    DB_TEST_EMAIL_2: str = "testemail2@gmail.com"

    # Test user ids
    DB_TEST_USER_ID: int = 1
    DB_TEST_USER_ID_2: int = 2

    # Test locations
    DB_TEST_LOCATION: str = "Vancouver, BC"
    DB_TEST_LOCATION_2: str = "Kelowna, BC"

    # Test password to update to
    DB_TEST_UPDATE_PASSWORD: str = "updated_pwd"

    # Test Insertion into user table
    DB_TEST_USER_INSERTION: str = (
        f'("{DB_TEST_USERNAME}", "{DB_TEST_PASSWORD}", "{DB_TEST_EMAIL}")'
    )

    # Test insertion into shared_dashboard table
    DB_TEST_SHARED_DASHBOARD_INSERTION: str = (
        f'("{DB_TEST_DASHBOARD_ID}", "{DB_TEST_USER_ID_2}", "{DB_TEST_USER_ID}")'
    )

    # Test insertion into dashboard table
    DB_TEST_DASHBOARD_INSERTION: str = f'("{DB_TEST_USER_ID}", "{DB_TEST_LOCATION}")'

    # Result of inserting the first test user (admin)
    DB_TEST_ADMIN_USER_ENTRY: tuple = (
        1,
        db_config.ADMIN_USER_NAME,
        db_config.ADMIN_USER_PASSWORD,
        db_config.ADMIN_USER_EMAIL,
    )

    # Result of inserting the second test user
    DB_TEST_SECONDARY_USER_ENTRY: tuple = (
        2,
        db_config.SECONDARY_USER_NAME,
        db_config.SECONDARY_USER_PASSWORD,
        db_config.SECONDARY_USER_EMAIL,
    )

    # Results of inserting both above users
    DB_TEST_USER_ENTRIES: list = [
        DB_TEST_ADMIN_USER_ENTRY,
        DB_TEST_SECONDARY_USER_ENTRY,
    ]

    # Result of inserting the first test user's dashboard
    DB_TEST_ADMIN_DASHBOARD_ENTRY: tuple = (1, 1, db_config.ADMIN_DASHBOARD_LOCATIONS)

    # Result of inserting the first user's shared dashboard
    DB_TEST_ADMIN_SHARED_DASHBOARD_ENTRY: tuple = (1, 1, 2, 1)

    # Test location coordinates
    API_TEST_LOCATION_LAT: float = 49.93972633855876
    API_TEST_LOCATION_LON: float = -119.39641232286611

    # Test API response for current weather and forecast weather
    API_TEST_CURRENT_WEATHER_RESPONSE: dict = current_weather_sample_response
    API_TEST_FORECAST_WEATHER_RESPONSE: dict = forecast_weather_sample_response

    # Test API response for location autocomplete and location search
    API_TEST_AUTOCOMPLETE_LOCATION_RESPONSE: dict = (
        autocomplete_location_sample_response
    )
    API_TEST_LOCATION_SEARCH_RESPONSE: dict = location_search_sample_response

    # Test API response for ai generation
    API_TEST_AI_GENERATION_RESPONSE: dict = ai_generation_sample_response

    # Sample forecast weather response for testing ai generation
    API_TEST_FORECAST_WEATHER_AI_INPUT: dict = forecast_weather_ai_input

    # Sample send email api response
    API_SEND_EMAIL_RESPONSE: dict = send_email_sample_response
    API_SEND_EMAIL_SUCCESS_MESSAGE: str = "Queued. Thank you."

    # Examples for email testing API
    API_TEST_EMAIL_SEND_TO: str = "riley.j.eaton@gmail.com"
    API_TEST_EMAIL_SEND_SUBJECT: str = "SkySage Test"
    API_TEST_EMAIL_SEND_BODY: str = "This is a test from the SkySage team!"

    # Sample location for testing the location search endpoint
    API_TEST_LOCATION_SEARCH: str = "The University of British Columbia, Kelowna"

    # Sample partial location for testing the autocomplete location endpoint
    API_TEST_AUTOCOMPLETE_LOCATION: str = "The University of British Columbia O"

    # API response code for missing parameters
    API_TEST_MISSING_PARAMS_RESPONSE: int = 422

    # added for db controller/router testing
    API_TEST_BOOLEAN_RESPONSE: bool = True

    API_TEST_VIEW_SAVED_LOCATIONS_RESPONSE: dict = {
        "saved_locations": ["Kelowna, BC", "Vancouver, BC"]
    }

    API_TEST_GET_DASHBOARD_ID_RESPONSE: dict = {"dashboard_id": 1}

    API_TEST_GET_SHARED_USER_IDS_RESPONSE: dict = {"shared_user_ids": [2]}

    API_TEST_GET_SHARE_ID_RESPONSE: dict = {"share_id": 1}

    API_TEST_GET_USER_ID_RESPONSE: dict = {"user_id": 1}

    API_TEST_GET_USER_EMAIL_RESPONSE: dict = {"user_email": "testemail@gmail.com"}


# Initialize the test config instance
test_config = Settings()
