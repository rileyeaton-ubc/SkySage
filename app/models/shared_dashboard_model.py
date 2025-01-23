# *************************************************************************************
# COSC 310 Project - SkySage

# Description: Shared Dashboard model for functions on a shared dashboard

# Author: Kai Gehry
# Date: 2024-11-25
# *************************************************************************************

import app.models.db_functions as db
from app.config.db_config import db_config


# allows for adding a shared user connected to a dashboard
def add_shared_to_user(
    table_name,
    shared_dashboard_id,
    shared_to_user_id,
    shared_from_user_id,
):

    return db.insert_into_table(
        table_name,
        db_config.DB_SHARED_DASHBOARD_SCHEMA_INSERTION,
        f'("{shared_dashboard_id}", "{shared_to_user_id}", "{shared_from_user_id}")',
    )


# allows for adding a shared user connected to a dashboard
def remove_shared_to_user(table_name, share_id):

    return db.delete_table_entry(
        table_name, db_config.DB_SHARED_DASH_ID_FIELD, share_id
    )


# allows for viewing the list of users who have acces to a certain shared dashboard
def get_shared_to_user_ids(table_name, shared_dashboard_id):

    return db.select_specific_column_from_table(
        table_name,
        (db_config.DB_SHARED_DASH_USER_ID_TO_FIELD,),
        (db_config.DB_SHARED_DASH_DASHBOARD_ID_FIELD,),
        (f"{shared_dashboard_id}",),
        True,
        "",
        "",
        True,
    )


# allows for retrieving the share id for a particular share instance
def get_share_id(table_name, shared_to_user_id, shared_from_user_id):

    return db.select_specific_column_from_table(
        table_name,
        (db_config.DB_SHARED_DASH_ID_FIELD,),
        (
            db_config.DB_SHARED_DASH_USER_ID_TO_FIELD,
            db_config.DB_SHARED_DASH_USER_ID_FROM_FIELD,
        ),
        (
            f"{shared_to_user_id}",
            f"{shared_from_user_id}",
        ),
        True,
        ("AND",),
    )
