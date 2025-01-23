# *************************************************************************************
# COSC 310 Project - SkySage

# Description: Dashboard Controller Tests

# Author: Kai Gehry
# Date: 2024-11-30
# *************************************************************************************

from app.config.test_config import test_config
from app.controllers.dashboard_controller import *
from app.schemas.shared_schema import SuccessStatus
from app.schemas.dashboard_schema import (
    LocationSearch,
    ViewLocations,
    RemoveLocation,
    GetDashboardId,
    ReturnedLocation,
)
import app.models.db_functions as db

from fastapi.testclient import TestClient
from pydantic import BaseModel
from app.config.global_config import global_settings
from app.main import app

# Initialize the TestClient instance
client = TestClient(app)


# tests saving a location
def test_save_location_controller(mocker):

    mock_get = mocker.patch(
        "app.controllers.dashboard_controller.save_location_controller"
    )
    mock_get.return_value = test_config.API_TEST_BOOLEAN_RESPONSE

    test_save_locations = LocationSearch(
        dashboard_id=test_config.DB_TEST_DASHBOARD_ID,
        location_name=test_config.DB_TEST_LOCATION_2,
    )

    db.create_table(test_config.DB_TEST_TABLE, db_config.DB_DASHBOARD_SCHEMA)

    db.insert_into_table(
        test_config.DB_TEST_TABLE,
        db_config.DB_DASHBOARD_SCHEMA_INSERTION,
        test_config.DB_TEST_DASHBOARD_INSERTION,
    )

    result = save_location_controller(test_save_locations, test_config.DB_TEST_TABLE)
    # assert result.status_code == 200
    wrapped_result = {"success": result}

    assert SuccessStatus(**wrapped_result)
    # db.drop_table(test_config.DB_TEST_TABLE)


# tests returing all saved locations for a user
def test_view_saved_locations_controller(mocker):

    mock_get = mocker.patch(
        "app.controllers.dashboard_controller.view_saved_locations_controller"
    )
    mock_get.return_value = test_config.API_TEST_VIEW_SAVED_LOCATIONS_RESPONSE

    db.create_table(test_config.DB_TEST_TABLE, db_config.DB_DASHBOARD_SCHEMA)

    db.insert_into_table(
        test_config.DB_TEST_TABLE,
        db_config.DB_DASHBOARD_SCHEMA_INSERTION,
        test_config.DB_TEST_DASHBOARD_INSERTION,
    )

    # create a location search object to run the test
    test_save_locations = LocationSearch(
        dashboard_id=test_config.DB_TEST_DASHBOARD_ID,
        location_name=test_config.DB_TEST_LOCATION_2,
    )

    # adds a second location to test returning a list of locations
    save_location_controller(
        test_save_locations,
        test_config.DB_TEST_TABLE,
    )

    # create a view location object to run the test
    test_view_locations = ViewLocations(dashboard_id=test_config.DB_TEST_DASHBOARD_ID)

    location_result = view_saved_locations_controller(
        test_view_locations,
        test_config.DB_TEST_TABLE,
    )

    assert ReturnedLocation(**location_result)


# tests removing a saved location for a particular user
def test_remove_location_controller(mocker):

    mock_get = mocker.patch(
        "app.controllers.dashboard_controller.remove_saved_location_controller"
    )
    mock_get.return_value = test_config.API_TEST_BOOLEAN_RESPONSE

    db.create_table(test_config.DB_TEST_TABLE, db_config.DB_DASHBOARD_SCHEMA)

    db.insert_into_table(
        test_config.DB_TEST_TABLE,
        db_config.DB_DASHBOARD_SCHEMA_INSERTION,
        test_config.DB_TEST_DASHBOARD_INSERTION,
    )

    # create  a remove location object to run the test
    test_remove_location = RemoveLocation(
        dashboard_id=test_config.DB_TEST_DASHBOARD_ID,
        location_name=test_config.DB_TEST_LOCATION,
    )

    removal_result = remove_saved_location_controller(
        test_remove_location,
        test_config.DB_TEST_TABLE,
    )

    wrapped_result = {"success": removal_result}
    assert SuccessStatus(**wrapped_result)

    db.drop_table(test_config.DB_TEST_TABLE)


def test_get_dashboard_id_controller(mocker):

    mock_get = mocker.patch(
        "app.controllers.dashboard_controller.get_dashboard_id_controller"
    )
    mock_get.return_value = test_config.API_TEST_GET_DASHBOARD_ID_RESPONSE

    db.create_table(test_config.DB_TEST_TABLE, db_config.DB_DASHBOARD_SCHEMA)

    db.insert_into_table(
        test_config.DB_TEST_TABLE,
        db_config.DB_DASHBOARD_SCHEMA_INSERTION,
        test_config.DB_TEST_DASHBOARD_INSERTION,
    )

    # create a get dashboard id object to run the test
    test_get_dashboard_id = GetDashboardId(user_id=test_config.DB_TEST_USER_ID)

    dashboard_id = get_dashboard_id_controller(
        test_get_dashboard_id, test_config.DB_TEST_TABLE
    )

    assert ViewLocations(**dashboard_id)
    db.drop_table(test_config.DB_TEST_TABLE)
