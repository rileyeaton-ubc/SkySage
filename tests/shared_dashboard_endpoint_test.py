# *************************************************************************************
# COSC 310 Project - SkySage

# Description: Dashboard Controller Tests

# Author: Kai Gehry
# Date: 2024-12-01
# *************************************************************************************

from app.config.test_config import test_config
from app.controllers.shared_dashboard_controller import *
from app.schemas.shared_schema import SuccessStatus
from app.schemas.shared_dashboard_schema import (
    AddSharedUser,
    ShareId,
    GetIds,
    SharedIdsList,
    GetShareId,
)
import app.models.db_functions as db

from fastapi.testclient import TestClient
from pydantic import BaseModel
from app.config.global_config import global_settings
from app.main import app

client = TestClient(app)


# tests adding a user to share a dashboard with
def test_add_shared_to_user_controller(mocker):

    mock_get = mocker.patch(
        "app.controllers.shared_dashboard_controller.add_shared_to_user_controller"
    )
    mock_get.return_value = test_config.API_TEST_BOOLEAN_RESPONSE

    db.create_table(test_config.DB_TEST_TABLE, db_config.DB_SHARED_DASHBOARD_SCHEMA)

    db.insert_into_table(
        test_config.DB_TEST_TABLE,
        db_config.DB_SHARED_DASHBOARD_SCHEMA_INSERTION,
        test_config.DB_TEST_SHARED_DASHBOARD_INSERTION,
    )

    # create a add shared user id object to run the test
    test_share = AddSharedUser(
        shared_dashboard_id=test_config.DB_TEST_DASHBOARD_ID,
        shared_to_user_id=test_config.DB_TEST_USER_ID_2,
        shared_from_user_id=test_config.DB_TEST_USER_ID,
    )

    user_addition_status = add_shared_to_user_controller(
        test_share,
        test_config.DB_TEST_TABLE,
    )

    wrapped_result = {"success": user_addition_status}
    assert SuccessStatus(**wrapped_result)

    # db.drop_table(test_config.DB_TEST_TABLE)


# tests unsharing a dashboard from a user with whom a dashboard has been shared
def test_remove_shared_to_user_controller(mocker):

    mock_get = mocker.patch(
        "app.controllers.shared_dashboard_controller.remove_shared_to_user_controller"
    )
    mock_get.return_value = test_config.API_TEST_BOOLEAN_RESPONSE

    db.create_table(test_config.DB_TEST_TABLE, db_config.DB_SHARED_DASHBOARD_SCHEMA)

    db.insert_into_table(
        test_config.DB_TEST_TABLE,
        db_config.DB_SHARED_DASHBOARD_SCHEMA_INSERTION,
        test_config.DB_TEST_SHARED_DASHBOARD_INSERTION,
    )

    # create a ramove shared to user object to run the test
    test_remove_user = ShareId(share_id=test_config.DB_TEST_SHARE_ID)

    removal_status = remove_shared_to_user_controller(
        test_remove_user,
        test_config.DB_TEST_TABLE,
    )

    wrapped_result = {"success": removal_status}
    assert SuccessStatus(**wrapped_result)

    db.drop_table(test_config.DB_TEST_TABLE)


# tests retrieving the ids of users a given dashboard has been shared with
def test_get_shared_to_user_ids_controller(mocker):

    mock_get = mocker.patch(
        "app.controllers.shared_dashboard_controller.get_shared_to_user_ids_controller"
    )
    mock_get.return_value = test_config.API_TEST_GET_SHARED_USER_IDS_RESPONSE

    db.create_table(test_config.DB_TEST_TABLE, db_config.DB_SHARED_DASHBOARD_SCHEMA)

    db.insert_into_table(
        test_config.DB_TEST_TABLE,
        db_config.DB_SHARED_DASHBOARD_SCHEMA_INSERTION,
        test_config.DB_TEST_SHARED_DASHBOARD_INSERTION,
    )

    # create a get to share ids object to run the test
    test_share_id = GetIds(shared_dashboard_id=test_config.DB_TEST_DASHBOARD_ID)

    ids_list = get_shared_to_user_ids_controller(
        test_share_id,
        test_config.DB_TEST_TABLE,
    )

    assert SharedIdsList(**ids_list)

    db.drop_table(test_config.DB_TEST_TABLE)


# tests retrieving the share id of a particular dashboard to a particular user
def test_get_share_id_controller(mocker):

    mock_get = mocker.patch(
        "app.controllers.shared_dashboard_controller.get_share_id_controller"
    )
    mock_get.return_value = test_config.API_TEST_GET_SHARE_ID_RESPONSE

    db.create_table(test_config.DB_TEST_TABLE, db_config.DB_SHARED_DASHBOARD_SCHEMA)

    db.insert_into_table(
        test_config.DB_TEST_TABLE,
        db_config.DB_SHARED_DASHBOARD_SCHEMA_INSERTION,
        test_config.DB_TEST_SHARED_DASHBOARD_INSERTION,
    )

    # create a get share id object to run the test
    test_share_id = GetShareId(
        shared_from_user_id=test_config.DB_TEST_USER_ID,
        shared_to_user_id=test_config.DB_TEST_USER_ID_2,
    )

    share_id = get_share_id_controller(
        test_share_id,
        test_config.DB_TEST_TABLE,
    )

    assert ShareId(**share_id)

    db.drop_table(test_config.DB_TEST_TABLE)
