# *************************************************************************************
# COSC 310 Project - SkySage

# DESCRIPTION: Global configuration file for the application to store settings and
# environment variables

# Author: Riley Eaton
# Date: 2024-11-18
# *************************************************************************************

import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    # Database settings
    DB_FILENAME: str = "skysage.db"
    DB_FILEPATH: str = "app/models/database/" + DB_FILENAME
    DB_URL: str = os.getenv("DATABASE_URL", "sqlite:///" + DB_FILEPATH)

    # API endpoints
    GET_CURRENT_WEATHER_ENDPOINT: str = "/api/weather/current"
    GET_FORECAST_WEATHER_ENDPOINT: str = "/api/weather/forecast"
    GET_LOCATION_COORDINATES_ENDPOINT: str = "/api/location/coordinates"
    GET_AUTOCOMPLETE_LOCATIONS_ENDPOINT: str = "/api/location/autocomplete"
    GET_GENERATE_AI_FORECAST_ENDPOINT: str = "/api/ai/generate/forecast"
    SEND_EMAIL_ENDPOINT: str = "/api/email/send"

    # AI generation prompts (for forecasting weather)
    AI_FORECAST_WEATHER_PROMPT: str = (
        "You are a knowledgeable and eloquent meteorologist who summarizes the weather. The first day of each summary that is provided to you should be referenced as 'today' and the following day be 'tomorrow'. DO NOT provide any markdown formatting for your responses."
    )
    AI_DEFAULT_MODEL: str = "gpt-4o-mini"

    # Mailgun variables for sending emails
    MAILGUN_SANDBOX_ID: str = "sandbox1d64681aa5714dbb982d74ca8b979cc9.mailgun.org"
    MAILGUN_FROM_EMAIL: str = f"skysage@{MAILGUN_SANDBOX_ID}"

    # Environment variables found in .env
    OPENWEATHER_API_KEY: str = ""
    OPENAI_API_KEY: str = ""
    GOOGLE_MAPS_API_KEY: str = ""
    MAILGUN_API_KEY: str = ""
    DB_ADMIN_PASSWORD: str = ""
    DB_ADMIN_EMAIL: str = ""
    DB_SECONDARY_USER_PASSWORD: str = ""
    DB_SECONDARY_USER_EMAIL: str = ""
    # Import environment variables
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


# Initialize global settings instance
global_settings = Settings()
