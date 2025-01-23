# *************************************************************************************
# COSC 310 Project - SkySage

# Description: Controller for user model

# Author: Kai Gehry
# Date: 2024-11-30
# *************************************************************************************

from app.models.user_model import *
from app.config.db_config import db_config
from app.schemas.user_schema import (
    UserDetails,
    UpdateEmail,
    UpdatePassword,
    CreateAccount,
    GetOrRemove,
)
from fastapi import HTTPException


# Verify User Login
# Description: Verifies if user infomation is entered correctly or of the user has an account.
# Parameters:
#  => entered_user_name: string - user name entered by the user
#  => entered_password: string - password entered by the user
#  => table_name: string - indicates the table to query from. Defaults to the user table if not table is specified (for testing)
# Return on Success: bool - True if the user has an account and the credentials are correct
# Return on Failure: bool - False if the credentials are incorrect or the user does not have an account
def verify_user_login_controller(
    user_details: UserDetails, table_name=db_config.DB_USER_TABLE
):

    try:

        is_verfied = verify_login(
            table_name, user_details.user_name, user_details.user_password
        )

        if isinstance(is_verfied, tuple):
            verified = True
        else:
            verified = False

        return verified

    except Exception as e:
        # If there is any exception, a 500 status will be returned with the following message
        raise HTTPException(
            status_code=500, detail=f"Verify login failed: Internal Server Error"
        )


# Create New Account
# Description: Creates a new account
# Parameters:
#  => user_name: string - user name chosen by the user
#  => user_password: string - password entered by the user
#  => user_email: string - email provided by the user
#  => table_name: string - indicates the table to query from. Defaults to the user table if not table is specified (for testing)
# Return on Success: True - Indicates the account has been created successfully
# Return on Failure: False - Indicates the account has not been created
def create_new_account_controller(
    account_creation_details: CreateAccount,
    table_name=db_config.DB_USER_TABLE,
    table_name_2=db_config.DB_DASHBOARD_TABLE,
):

    try:

        is_verfied = verify_login(
            table_name,
            account_creation_details.user_name,
            account_creation_details.user_password,
            account_creation_details.user_email,
        )

        # if an account already exists with the username, the account creation is terminated, and false is returned
        if isinstance(is_verfied, tuple):
            return False

        else:

            # creates a new user
            creation_status = create_new_user(
                table_name,
                account_creation_details.user_name,
                account_creation_details.user_password,
                account_creation_details.user_email,
            )

            # Retrieves the newly created user id for the user
            user_id_tuple = get_user_id(table_name, account_creation_details.user_name)
            user_id = user_id_tuple[0]

            # creates a new dashboard associated with that user
            dashboard_status = create_linked_dashboard(table_name_2, user_id)

            # true is onlu returned if both the account and the dashboard are successfully created
            if (
                creation_status["rows_affected"] == 1
                and dashboard_status["rows_affected"] == 1
            ):
                return True
            else:
                return False

    except Exception as e:
        # If there is any exception, a 500 status will be returned with the following message
        raise HTTPException(
            status_code=500, detail=f"Create account failed: Internal Server Error"
        )


# Update Email
# Description: Updates a user's email
# Parameters:
#  => user_name: string - user name of the account holder
#  => new_user_email: string - new email entetered by the user
#  => table_name: string - indicates the table to query from. Defaults to the user table if not table is specified (for testing)
# Returns: True if the the update was successful, and false otherwise
def update_email_controller(
    user_email_update: UpdateEmail, table_name=db_config.DB_USER_TABLE
):

    try:
        update_result = update_user_email(
            table_name, user_email_update.user_name, user_email_update.new_user_email
        )

        if update_result["rows_affected"] == 1:
            update_status = True
        else:
            update_status = False

        return update_status

    except Exception as e:
        # If there is any exception, a 500 status will be returned with the following message
        raise HTTPException(
            status_code=500, detail=f"Update email failed: Internal Server Error"
        )


# Update Password
# Description: Updates a user's password
# Parameters:
#  => user_name: string - user name of the account holder
#  => new_user_password: string - new email entetered by the user
#  => table_name: string - indicates the table to query from. Defaults to the user table if not table is specified (for testing)
# Returns: True if the the update was successful, and false otherwise
def update_password_controller(
    user_password_update: UpdatePassword, table_name=db_config.DB_USER_TABLE
):

    try:
        update_result = update_user_password(
            table_name,
            user_password_update.user_name,
            user_password_update.new_user_password,
        )

        if update_result["rows_affected"] == 1:
            update_status = True
        else:
            update_status = False

        return update_status

    except Exception as e:
        # If there is any exception, a 500 status will be returned with the following message
        raise HTTPException(
            status_code=500, detail=f"Update password failed: Internal Server Error"
        )


# Delete Account
# Description: Deletes a user's account
# Parameters:
#  => user_name: string - user name of the account holder
#  => table_name: string - indicates the table to query from. Defaults to the user table if not table is specified (for testing)
# Returns: Number of rows affected
def delete_account_controller(
    user_name: GetOrRemove, table_name=db_config.DB_USER_TABLE
):

    try:

        remove_status = remove_user(table_name, user_name.user_name)

        if remove_status == 1:
            return True
        else:
            return False

    except Exception as e:
        # If there is any exception, a 500 status will be returned with the following message
        raise HTTPException(
            status_code=500, detail=f"Delete account failed: Internal Server Error"
        )


# Get User Id
# Description: Retrieves a user id
# Parameters:
#  => user_name: string - user name of the account holder
#  => table_name: string - indicates the table to query from. Defaults to the user table if not table is specified (for testing)
# Returns: User id in integer form
def get_user_id_controller(user_name: GetOrRemove, table_name=db_config.DB_USER_TABLE):

    try:

        id_tuple = get_user_id(table_name, user_name.user_name)
        return {"user_id": id_tuple[0]}

    except Exception as e:
        # If there is any exception, a 500 status will be returned with the following message
        raise HTTPException(
            status_code=500, detail=f"Get user id failed: Internal Server Error"
        )


# Get User Email
# Description: Retrieves a user email
# Parameters:
#  => user_name: string - user name of the account holder
#  => table_name: string - indicates the table to query from. Defaults to the user table if not table is specified (for testing)
# Returns: User email in string form
def get_user_email_controller(
    user_name: GetOrRemove, table_name=db_config.DB_USER_TABLE
):

    try:

        email_tuple = get_user_email(table_name, user_name.user_name)
        return {"user_email": email_tuple[0]}

    except Exception as e:
        # If there is any exception, a 500 status will be returned with the following message
        raise HTTPException(
            status_code=500, detail=f"Get user email failed: Internal Server Error"
        )
