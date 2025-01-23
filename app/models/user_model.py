# *************************************************************************************
# COSC 310 Project - SkySage

# DESCRIPTION: Functions defined for a user (insert, delete, update)

# Author: Kai Gehry
# Date: 2024-11-24
# *************************************************************************************

import app.models.db_functions as db
from app.config.db_config import db_config


# allows for verifying a user's login information
def verify_login(table_name, user_name, user_password, user_email=""):

    # if the login information is simplh being checked on a login to the site, this case is entered
    if user_email == "":
        return db.select_specific_column_from_table(
            table_name,
            ("user_id", "user_password"),
            ("user_name", "user_password"),
            (f'"{user_name}"', f'"{user_password}"'),
            True,
            ("AND",),
        )
    # if a user is attempting to create an account, this case is entered where the
    # user name and user email are checked to make sure they do not already exist in the user db
    else:
        return db.select_specific_column_from_table(
            table_name,
            ("user_id", "user_password"),
            ("user_name", "user_email"),
            (f'"{user_name}"', f'"{user_email}"'),
            True,
            ("OR",),
        )


# adds a new user to the user DB
def create_new_user(table_name, user_name, user_password, user_email):

    return db.insert_into_table(
        table_name,
        db_config.DB_USER_SCHEMA_INSERTION,
        f'("{user_name}", "{user_password}", "{user_email}")',
    )


# allows for atomatic creation of a dashboard when a user account is created
def create_linked_dashboard(table_name, user_id):

    return db.insert_into_table(
        table_name,
        f"({db_config.DB_DASHBOARD_USER_FIELD})",
        f'("{user_id}")',
    )


# updates an existing user's email
def update_user_email(table_name, user_name, new_user_email):

    # single quotes are used around the f-string to allow for passing a delimited input. SQL will only except a text input if it is delimited by single quotation marks
    return db.update_table_entry(
        table_name,
        db_config.DB_USER_EMAIL_FIELD,
        f'"{new_user_email}"',
        db_config.DB_USER_NAME_FIELD,
        f'"{user_name}"',
    )


# updates and existing user's password
def update_user_password(table_name, user_name, new_user_password):

    # single quotes are used around the f-string to allow for passing a delimited input. SQL will only except a text input if it is delimited by single quotation marks
    return db.update_table_entry(
        table_name,
        db_config.DB_USER_PASSWORD_FIELD,
        f'"{new_user_password}"',
        db_config.DB_USER_NAME_FIELD,
        f'"{user_name}"',
    )


# removes an existing user from the DB
def remove_user(table_name, user_name):

    return db.delete_table_entry(
        table_name, db_config.DB_USER_NAME_FIELD, f'"{user_name}"'
    )


def get_user_id(table_name, user_name):

    return db.select_specific_column_from_table(
        table_name,
        (db_config.DB_USER_ID_FIELD,),
        (db_config.DB_USER_NAME_FIELD,),
        (f'"{user_name}"',),
        True,
    )


def get_user_email(table_name, user_name):

    return db.select_specific_column_from_table(
        table_name,
        (db_config.DB_USER_EMAIL_FIELD,),
        (db_config.DB_USER_NAME_FIELD,),
        (f'"{user_name}"',),
        True,
    )
