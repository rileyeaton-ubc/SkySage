# *************************************************************************************
# COSC 310 Project - SkySage

# DESCRIPTION: Configuration file the SQLite database constants

# Author: Riley Eaton
# Date: 2024-11-18
# *************************************************************************************

import os
from pydantic_settings import BaseSettings
from app.config.global_config import global_settings


class Settings(BaseSettings):
    # Core table names
    DB_USER_TABLE: str = "user"
    DB_DASHBOARD_TABLE: str = "dashboard"
    DB_SHARED_DASHBOARD_TABLE: str = "shared_dashboard"

    # User table fields
    DB_USER_ID_FIELD: str = "user_id"
    DB_USER_NAME_FIELD: str = "user_name"
    DB_USER_PASSWORD_FIELD: str = "user_password"
    DB_USER_EMAIL_FIELD: str = "user_email"
    # User table schema using the above fields
    DB_USER_SCHEMA: str = (
        f"({DB_USER_ID_FIELD} INTEGER PRIMARY KEY AUTOINCREMENT, {DB_USER_NAME_FIELD} TEXT, {DB_USER_PASSWORD_FIELD} TEXT, {DB_USER_EMAIL_FIELD} TEXT)"
    )
    # User table schema for insertions (without the primary key)
    DB_USER_SCHEMA_INSERTION: str = (
        f"({DB_USER_NAME_FIELD}, {DB_USER_PASSWORD_FIELD}, {DB_USER_EMAIL_FIELD})"
    )

    # Dashboard table fields
    DB_DASHBOARD_ID_FIELD: str = "dashboard_id"
    DB_DASHBOARD_USER_FIELD: str = f"linked_{DB_USER_ID_FIELD}"
    DB_DASHBOARD_LOCATIONS_FIELD: str = "saved_locations"
    # Dashboard table schema using the above fields
    DB_DASHBOARD_SCHEMA: str = (
        f"({DB_DASHBOARD_ID_FIELD} INTEGER PRIMARY KEY AUTOINCREMENT, {DB_DASHBOARD_USER_FIELD} INTEGER, {DB_DASHBOARD_LOCATIONS_FIELD} TEXT, FOREIGN KEY({DB_DASHBOARD_USER_FIELD}) REFERENCES {DB_USER_TABLE} ({DB_DASHBOARD_USER_FIELD}))"
    )
    # Dashboard table schema for insertions (without the primary key)
    DB_DASHBOARD_SCHEMA_INSERTION: str = (
        f"({DB_DASHBOARD_USER_FIELD}, {DB_DASHBOARD_LOCATIONS_FIELD})"
    )

    # Shared dashboard table fields
    DB_SHARED_DASH_ID_FIELD: str = "share_id"
    DB_SHARED_DASH_DASHBOARD_ID_FIELD: str = f"shared_{DB_DASHBOARD_ID_FIELD}"
    DB_SHARED_DASH_USER_ID_TO_FIELD: str = "shared_to_user_id"
    DB_SHARED_DASH_USER_ID_FROM_FIELD: str = f"shared_from_{DB_USER_ID_FIELD}"
    # Shared dashboard table schema using the above fields
    DB_SHARED_DASHBOARD_SCHEMA: str = (
        f"({DB_SHARED_DASH_ID_FIELD} INTEGER PRIMARY KEY AUTOINCREMENT, {DB_SHARED_DASH_DASHBOARD_ID_FIELD} INTEGER, {DB_SHARED_DASH_USER_ID_TO_FIELD} INTEGER, {DB_SHARED_DASH_USER_ID_FROM_FIELD} INTEGER, FOREIGN KEY({DB_SHARED_DASH_DASHBOARD_ID_FIELD}) REFERENCES {DB_DASHBOARD_TABLE} ({DB_DASHBOARD_ID_FIELD}), FOREIGN KEY({DB_SHARED_DASH_USER_ID_TO_FIELD}) REFERENCES {DB_USER_TABLE} ({DB_USER_ID_FIELD}), FOREIGN KEY({DB_SHARED_DASH_USER_ID_FROM_FIELD}) REFERENCES {DB_USER_TABLE} ({DB_USER_ID_FIELD}))"
    )
    # Shared dashboard table schema for insertions (without the primary key)
    DB_SHARED_DASHBOARD_SCHEMA_INSERTION: str = (
        f"({DB_SHARED_DASH_DASHBOARD_ID_FIELD}, {DB_SHARED_DASH_USER_ID_TO_FIELD}, {DB_SHARED_DASH_USER_ID_FROM_FIELD})"
    )

    # Admin user data
    ADMIN_USER_NAME: str = "Admin"
    ADMIN_USER_PASSWORD: str = global_settings.DB_ADMIN_PASSWORD
    ADMIN_USER_EMAIL: str = global_settings.DB_ADMIN_EMAIL
    ADMIN_DASHBOARD_LOCATIONS: str = "Kelowna, BC"

    # Secondary user data
    SECONDARY_USER_NAME: str = "Kai Gehry"
    SECONDARY_USER_PASSWORD: str = global_settings.DB_SECONDARY_USER_PASSWORD
    SECONDARY_USER_EMAIL: str = global_settings.DB_SECONDARY_USER_EMAIL


# Initialize the test config instance
db_config = Settings()
