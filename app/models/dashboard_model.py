# *************************************************************************************
# COSC 310 Project - SkySage

# Description: Dashboard model for functions on a user dashboard

# Author: Kai Gehry
# Date: 2024/11/25
# *************************************************************************************

import app.models.db_functions as db
from app.config.db_config import db_config


# allows for saving a dashboard location
def save_location(table_name, dashboard_id, location_list):

    return db.update_table_entry(
        table_name,
        db_config.DB_DASHBOARD_LOCATIONS_FIELD,
        f'"{location_list}"',
        db_config.DB_DASHBOARD_ID_FIELD,
        dashboard_id,
    )


# allows for viewing saved locations
def get_saved_locations(table_name, dashboard_id):

    return db.select_specific_column_from_table(
        table_name, ("saved_locations",), ("dashboard_id",), (f"{dashboard_id}",), True
    )


# allows for removing a saved loction from the table
def remove_location(table_name, dashboard_id, location_list):

    # the table is updated accordingly
    return db.update_table_entry(
        table_name,
        db_config.DB_DASHBOARD_LOCATIONS_FIELD,
        f'"{location_list}"',
        db_config.DB_DASHBOARD_ID_FIELD,
        dashboard_id,
    )


# allows for retrieving a dashboard id
def get_dashboard_id(table_name, user_id):

    return db.select_specific_column_from_table(
        table_name,
        (db_config.DB_DASHBOARD_ID_FIELD,),
        (db_config.DB_DASHBOARD_USER_FIELD,),
        (f'"{user_id}"',),
        True,
    )


def create_dashboard(table_name, user_id):

    return db.insert_into_table(table_name, db_config.DB_DASHBOARD_USER_FIELD, user_id)
