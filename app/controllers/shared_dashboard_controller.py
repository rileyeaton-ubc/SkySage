# *************************************************************************************
# COSC 310 Project - SkySage

# Description: Controller for shared dashboard model

# Author: Kai Gehry
# Date: 2024-11-30
# *************************************************************************************

from app.models.shared_dashboard_model import *
from app.config.db_config import db_config
from app.schemas.shared_dashboard_schema import (
    AddSharedUser,
    ShareId,
    GetIds,
    GetShareId,
)
from fastapi import HTTPException


# Add Shared To User
# Description: Allows a user share a dashboard to another user
#  => shared_dashboard_id: int - dashboard id of the shared dashboard
#  => shared_to_user_id: int - user id of the user the dashboard will be shared with
#  => shared_from_user_id: int - user id of the dashboard owner
#  => table_name: string - indicates the table to query from. Defaults to the user table if not table is specified (for testing)
# Return on Success: bool - True if the share is successful
# Return on Failure: bool - False if the share is unsuccessful
def add_shared_to_user_controller(
    add_shared_user_data: AddSharedUser, table_name=db_config.DB_SHARED_DASHBOARD_TABLE
):

    try:

        # create list of userids for processing
        formatted_id_result = __create_user_ids_list(
            table_name, add_shared_user_data.shared_dashboard_id
        )

        # if the user id is already in the list, it is not added again
        if add_shared_user_data.shared_to_user_id in formatted_id_result:
            return False

        # if the user id is not already in the list, it is added
        else:
            added_user_result = add_shared_to_user(
                table_name,
                add_shared_user_data.shared_dashboard_id,
                add_shared_user_data.shared_to_user_id,
                add_shared_user_data.shared_from_user_id,
            )

            if added_user_result["rows_affected"] == 1:
                added_user_status = True
            else:
                added_user_status = False

            return added_user_status

    except Exception as e:
        # If there is any exception, a 500 status will be returned with the following message
        raise HTTPException(
            status_code=500, detail=f"Share with user failed: Internal Server Error"
        )


# Remove Shared To User
# Description: Allows a user unshare a dashboard to another user
#  => share_id: int - unique id for the share instance
#  => table_name: string - indicates the table to query from. Defaults to the user table if not table is specified (for testing)
# Return on Success: bool - True if the unshare is successful
# Return on Failure: bool - False if the unshare is unsuccessful
def remove_shared_to_user_controller(
    share_id: ShareId, table_name=db_config.DB_SHARED_DASHBOARD_TABLE
):

    try:

        removal_result = remove_shared_to_user(table_name, share_id.share_id)

        if removal_result == 1:
            removal_status = True
        else:
            removal_status = False

        return removal_status

    except Exception as e:
        # If there is any exception, a 500 status will be returned with the following message
        raise HTTPException(
            status_code=500,
            detail=f"Remove shared to user failed: Internal Server Error",
        )


# Get Shared to User Ids
# Description: Allows for viewing the users who have a particular dashboard shared with them
#  => shared_dashboard_id: int - dashboard id of the shared dashboard
#  => table_name: string - indicates the table to query from. Defaults to the user table if not table is specified (for testing)
# Return on Success: list - Returns a tuple containing the user ids
def get_shared_to_user_ids_controller(
    shared_dashboard_id: GetIds, table_name=db_config.DB_SHARED_DASHBOARD_TABLE
):
    try:

        # create list of userids for processing
        formatted_id_result = __create_user_ids_list(
            table_name, shared_dashboard_id.shared_dashboard_id
        )

        return {"shared_user_ids": formatted_id_result}

    except Exception as e:
        # If there is any exception, a 500 status will be returned with the following message
        raise HTTPException(
            status_code=500,
            detail=f"Retieve shared to user ids failed: Internal Server Error",
        )


# Get Share Id
# Description: Allows for retrieving a share id for a particular share insance
#  => shared_dashboard_id: int - dashboard id of the shared dashboard
#  => table_name: string - indicates the table to query from. Defaults to the user table if not table is specified (for testing)
# Return on Success: int - Share id in integer form
def get_share_id_controller(
    share_id: GetShareId, table_name=db_config.DB_SHARED_DASHBOARD_TABLE
):
    try:

        share_id_result = get_share_id(
            table_name, share_id.shared_to_user_id, share_id.shared_from_user_id
        )
        return {"share_id": share_id_result[0]}

    except Exception as e:
        # If there is any exception, a 500 status will be returned with the following message
        raise HTTPException(
            status_code=500,
            detail=f"Retrieve share id failed: Internal Server Error",
        )


# private function to create list of userids for processing
def __create_user_ids_list(table_name, shared_dashboard_id):
    # retrieves the user ids from the table
    ids_result = get_shared_to_user_ids(table_name, shared_dashboard_id)

    # creates an empty list to store the query results
    formatted_id_result = [None] * len(ids_result)

    # the query returns an array of single element arrays, so each element is extacted and added to a new list
    for i in range(len(ids_result)):
        formatted_id_result[i] = ids_result[i][0]

    return formatted_id_result
