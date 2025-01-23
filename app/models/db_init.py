# *************************************************************************************
# COSC 310 Project - SkySage

# DESCRIPTION: Responsible for initializing the database and creating the tables

# Author: Kai Gehry, Riley Eaton
# Date: 2024-11-18
# *************************************************************************************

# import the global settings from the config file the db functions
from app.config.db_config import db_config as config
import app.models.db_functions as db


# Create the initial user table with two users
def init_users():
    # Create the user table
    # The AUTOINCREMENT keyword allows for the user of auto number keys and forces the field to be unique
    db.create_table(
        config.DB_USER_TABLE,
        config.DB_USER_SCHEMA,
    )

    # Insert initial admin and secondary user into user table
    db.insert_many_into_table(
        config.DB_USER_TABLE,
        config.DB_USER_SCHEMA_INSERTION,
        [
            (
                config.ADMIN_USER_NAME,
                config.ADMIN_USER_PASSWORD,
                config.ADMIN_USER_EMAIL,
            ),
            (
                config.SECONDARY_USER_NAME,
                config.SECONDARY_USER_PASSWORD,
                config.SECONDARY_USER_EMAIL,
            ),
        ],
    )

    # Get all rows from the user table to ensure admin was inserted correctly
    return db.select_all_from_table(config.DB_USER_TABLE)


# Create the initial admin dashboard
def init_dashboard():
    # Create the dashboard table
    db.create_table(
        config.DB_DASHBOARD_TABLE,
        config.DB_DASHBOARD_SCHEMA,
    )

    # Insert initial admin dashboard into dashboard table
    db.insert_into_table(
        config.DB_DASHBOARD_TABLE,
        config.DB_DASHBOARD_SCHEMA_INSERTION,
        (1, config.ADMIN_DASHBOARD_LOCATIONS),
    )

    # Insert second user dashboard into dashboard table
    db.insert_into_table(
        config.DB_DASHBOARD_TABLE,
        config.DB_DASHBOARD_SCHEMA_INSERTION,
        (2, config.ADMIN_DASHBOARD_LOCATIONS),
    )

    # Get all rows from the dashboard table to ensure admin's dashboard was inserted correctly
    return db.select_all_from_table(config.DB_DASHBOARD_TABLE)[0]


# Create the initial shared dashboard
def init_shared_dashboard():
    # Create the shared_dashboard table
    db.create_table(
        config.DB_SHARED_DASHBOARD_TABLE,
        config.DB_SHARED_DASHBOARD_SCHEMA,
    )

    # Insert initial admin shared dashboard into shared dashboard table
    db.insert_into_table(
        config.DB_SHARED_DASHBOARD_TABLE,
        config.DB_SHARED_DASHBOARD_SCHEMA_INSERTION,
        (
            1,
            2,
            1,
        ),
    )

    # Get all rows from the dashboard table to ensure admin's dashboard was inserted correctly
    return db.select_all_from_table(config.DB_SHARED_DASHBOARD_TABLE)[0]
