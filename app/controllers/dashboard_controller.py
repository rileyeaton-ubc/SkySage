# *************************************************************************************
# COSC 310 Project - SkySage

# Description: Controller for dashboard model

# Author: Kai Gehry
# Date: 2024-11-30
# *************************************************************************************

from app.models.dashboard_model import *
from app.config.db_config import db_config
from app.schemas.dashboard_schema import (
    LocationSearch,
    ViewLocations,
    RemoveLocation,
    GetDashboardId,
)
from fastapi import HTTPException


# Save Location
# Description: Allows a user to save a location to their dashboard
# Parameters:
#  => user_id: int - user id of user
#  => location_name: string - location to be saved
#  => table_name: string - indicates the table to query from. Defaults to the user table if not table is specified (for testing)
# Return on Success: bool - True if the user has an account and the credentials are correct
# Return on Failure: bool - False if the credentials are incorrect or the user does not have an account
def save_location_controller(
    save_location_data: LocationSearch, table_name=db_config.DB_DASHBOARD_TABLE
):

    try:

        location_list = get_saved_locations(table_name, save_location_data.dashboard_id)

        # checks if the location list is empty (a user has no saved locations). Replaces the "None" variable that is initially present
        if None in location_list:
            # stores the new location name
            new_list = "'" + save_location_data.location_name + "'"

        else:

            # converts the location list from the table from a tuple to a string
            location_list = str(location_list)

            # removes single quotes around location names, any round brackets and commas whcich were part of the
            new_list = (
                location_list.replace('"', "").replace("(", "").replace(")", "")
            ).rstrip(",")

            # checks if the list location to be added is already in the saved locations list. If it is, the loction to be saved is not removed.
            if new_list.find(save_location_data.location_name) == -1:
                new_list = (
                    new_list + ", " + "'" + save_location_data.location_name + "'"
                )  # concatenates the new location name to the list

            # location is already in the list
            else:
                return False

        save_status = save_location(
            table_name, save_location_data.dashboard_id, new_list
        )

        if save_status["rows_affected"] == 1:
            return True

        else:
            return False

    except Exception as e:
        # If there is any exception, a 500 status will be returned with the following message
        raise HTTPException(
            status_code=500, detail=f"Save location failed: Internal Server Error"
        )


# View Saved Locations
# Description: Allows a user to view their saved locations
# Parameters:
#  => dashboard_id: int - user id of user
#  => table_name: string - indicates the table to query from. Defaults to the user table if not table is specified (for testing)
# Return on Success: list - A list of the location names
def view_saved_locations_controller(
    view_data: ViewLocations, table_name=db_config.DB_DASHBOARD_TABLE
):
    try:

        location_tup = get_saved_locations(table_name, view_data.dashboard_id)

        location_list = str(location_tup[0])
        location_list = location_list.split("', ")

        for i, val in enumerate(location_list):
            location_list[i] = val.replace("'", "")

        return {"saved_locations": location_list}

    except Exception as e:
        # If there is any exception, a 500 status will be returned with the following message
        raise HTTPException(
            status_code=500,
            detail=f"View saved locations failed: Internal Server Error",
        )


# Remove Saved Location
# Description: Allows a user to remove a saved location
# Parameters:
#  => dashboard_id: int - user id of user
#  => location_name: string - location to be removed
#  => table_name: string - indicates the table to query from. Defaults to the user table if not table is specified (for testing)
# Return on Success: bool - True if the location has been succesfully removed
# Return on Failure: bool - False if the location has not been successfully removed
def remove_saved_location_controller(
    remove_location_data: RemoveLocation, table_name=db_config.DB_DASHBOARD_TABLE
):

    try:

        # returns a tuple containing all saved locations
        location_tup = get_saved_locations(
            table_name, remove_location_data.dashboard_id
        )

        location_list = str(location_tup[0])
        location_list = location_list.split("', ")

        for i, val in enumerate(location_list):
            location_list[i] = val.replace("'", "")

        # if the location is in the list, it is removed
        if remove_location_data.location_name in location_list:

            location_list.remove(remove_location_data.location_name)
            new_list = str(location_list).replace("[", "").replace("]", "")

            removal_result = remove_location(
                table_name, remove_location_data.dashboard_id, new_list
            )

            if removal_result["rows_affected"] == 1:
                return True
            else:
                return False

        else:
            return False

    except Exception as e:
        # If there is any exception, a 500 status will be returned with the following message
        raise HTTPException(
            status_code=500,
            detail=f"Remove saved location failed: Internal Server Error",
        )


# Get Dashboard Id
# Description: Allows for retrieval of a dashboard id
# Parameters:
#  => user_id: int - user id of user
#  => table_name: string - indicates the table to query from. Defaults to the user table if not table is specified (for testing)
# Returns: int - The user id in integer form
def get_dashboard_id_controller(
    get_dashboard_id_param: GetDashboardId, table_name=db_config.DB_DASHBOARD_TABLE
):
    try:
        dashboard_id = get_dashboard_id(table_name, get_dashboard_id_param.user_id)
        return {"dashboard_id": dashboard_id[0]}

    except Exception as e:
        # If there is any exception, a 500 status will be returned with the following message
        raise HTTPException(
            status_code=500, detail=f"Get dashboard id failed: Internal Server Error"
        )


def create_dashboard_controller(
    get_dashboard_id_param: GetDashboardId, table_name=db_config.DB_DASHBOARD_TABLE
):

    try:
        create_status = create_dashboard(table_name, get_dashboard_id_param.user_id)

        if create_status["rows_affected"] == 1:
            return True
        else:
            return False

    except Exception as e:
        # If there is any exception, a 500 status will be returned with the following message
        raise HTTPException(
            status_code=500, detail=f"Create dashboard failed: Internal Server Error"
        )
