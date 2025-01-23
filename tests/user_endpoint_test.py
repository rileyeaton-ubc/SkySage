# *************************************************************************************
# COSC 310 Project - SkySage

# Description: User Controller Tests

# Author: Kai Gehry
# Date: 2024-11-30
# *************************************************************************************

from app.config.test_config import test_config
from app.controllers.user_controller import *
from app.schemas.shared_schema import SuccessStatus
from app.schemas.user_schema import (
    UserDetails,
    UpdateEmail,
    UpdatePassword,
    CreateAccount,
    GetOrRemove,
    GetUserId,
    GetUserEmail,
)
import app.models.db_functions as db

from fastapi.testclient import TestClient
from pydantic import BaseModel
from app.config.global_config import global_settings
from app.main import app

client = TestClient(app)


# tests the controller for logging in to an account (checks if the user has an account)
def test_verify_user_login_controller(mocker):

    mock_get = mocker.patch(
        "app.controllers.user_controller.verify_user_login_controller"
    )
    mock_get.return_value = test_config.API_TEST_BOOLEAN_RESPONSE

    db.create_table(test_config.DB_TEST_TABLE, db_config.DB_USER_SCHEMA)

    db.insert_into_table(
        test_config.DB_TEST_TABLE,
        db_config.DB_USER_SCHEMA_INSERTION,
        test_config.DB_TEST_USER_INSERTION,
    )

    test_verify = UserDetails(
        user_name=test_config.DB_TEST_USERNAME,
        user_password=test_config.DB_TEST_PASSWORD,
    )

    # passes test parameters to the controller
    has_account = verify_user_login_controller(
        test_verify,
        test_config.DB_TEST_TABLE,
    )

    wrapped_result = {"success": has_account}
    assert SuccessStatus(**wrapped_result)

    db.drop_table(test_config.DB_TEST_TABLE)


# tests the controller for creating an account
def test_create_new_account_controller(mocker):

    mock_get = mocker.patch(
        "app.controllers.user_controller.create_new_account_controller"
    )
    mock_get.return_value = test_config.API_TEST_BOOLEAN_RESPONSE

    db.create_table(test_config.DB_TEST_TABLE, db_config.DB_USER_SCHEMA)
    db.create_table(test_config.DB_TEST_TABLE_2, db_config.DB_DASHBOARD_SCHEMA)

    test_create_account = CreateAccount(
        user_name=test_config.DB_TEST_USERNAME,
        user_password=test_config.DB_TEST_PASSWORD,
        user_email=test_config.DB_TEST_EMAIL,
    )

    # passes test parameters to the controller
    account_status = create_new_account_controller(
        test_create_account, test_config.DB_TEST_TABLE, test_config.DB_TEST_TABLE_2
    )

    wrapped_result = {"success": account_status}
    assert SuccessStatus(**wrapped_result)

    db.drop_table(test_config.DB_TEST_TABLE)


# tests the controller for updating an email
def test_update_email_controller(mocker):

    mock_get = mocker.patch("app.controllers.user_controller.update_email_controller")
    mock_get.return_value = test_config.API_TEST_BOOLEAN_RESPONSE

    db.create_table(test_config.DB_TEST_TABLE, db_config.DB_USER_SCHEMA)

    db.insert_into_table(
        test_config.DB_TEST_TABLE,
        db_config.DB_USER_SCHEMA_INSERTION,
        test_config.DB_TEST_USER_INSERTION,
    )

    test_update_email = UpdateEmail(
        user_name=test_config.DB_TEST_USERNAME,
        new_user_email=test_config.DB_TEST_EMAIL_2,
    )

    # passes test parameters to the controller
    update_result = update_email_controller(
        test_update_email,
        test_config.DB_TEST_TABLE,
    )

    wrapped_result = {"success": update_result}
    assert SuccessStatus(**wrapped_result)

    db.drop_table(test_config.DB_TEST_TABLE)


# tests the controller for updating a password
def test_update_password_controller(mocker):

    mock_get = mocker.patch(
        "app.controllers.user_controller.update_password_controller"
    )
    mock_get.return_value = test_config.API_TEST_BOOLEAN_RESPONSE

    db.create_table(test_config.DB_TEST_TABLE, db_config.DB_USER_SCHEMA)

    db.insert_into_table(
        test_config.DB_TEST_TABLE,
        db_config.DB_USER_SCHEMA_INSERTION,
        test_config.DB_TEST_USER_INSERTION,
    )

    test_update_password = UpdatePassword(
        user_name=test_config.DB_TEST_USERNAME,
        new_user_password=test_config.DB_TEST_PASSWORD_2,
    )

    # passes test parameters to the controller
    update_result = update_password_controller(
        test_update_password,
        test_config.DB_TEST_TABLE,
    )

    wrapped_result = {"success": update_result}
    assert SuccessStatus(**wrapped_result)

    db.drop_table(test_config.DB_TEST_TABLE)


# tests the controller for deleting an existing account
def test_delete_account_controller(mocker):

    mock_get = mocker.patch("app.controllers.user_controller.delete_account_controller")
    mock_get.return_value = test_config.API_TEST_BOOLEAN_RESPONSE

    db.create_table(test_config.DB_TEST_TABLE, db_config.DB_USER_SCHEMA)

    db.insert_into_table(
        test_config.DB_TEST_TABLE,
        db_config.DB_USER_SCHEMA_INSERTION,
        test_config.DB_TEST_USER_INSERTION,
    )

    test_remove_user = GetOrRemove(user_name=test_config.DB_TEST_USERNAME)

    # passes test parameters to the controller
    delete_result = delete_account_controller(
        test_remove_user, test_config.DB_TEST_TABLE
    )

    if delete_result == 1:
        delete_status = True
    else:
        delete_status = False

    wrapped_result = {"success": delete_status}
    assert SuccessStatus(**wrapped_result)

    db.drop_table(test_config.DB_TEST_TABLE)


# tests the controller for retrieving a user id
def test_get_user_id_controller(mocker):

    mock_get = mocker.patch("app.controllers.user_controller.get_user_id_controller")
    mock_get.return_value = test_config.API_TEST_GET_USER_ID_RESPONSE

    db.create_table(test_config.DB_TEST_TABLE, db_config.DB_USER_SCHEMA)

    db.insert_into_table(
        test_config.DB_TEST_TABLE,
        db_config.DB_USER_SCHEMA_INSERTION,
        test_config.DB_TEST_USER_INSERTION,
    )

    test_get_user_id = GetOrRemove(user_name=test_config.DB_TEST_USERNAME)

    # passes test parameters to the controller
    user_id = get_user_id_controller(test_get_user_id, test_config.DB_TEST_TABLE)

    assert GetUserId(**user_id)

    db.drop_table(test_config.DB_TEST_TABLE)


# tests the controller for retrieving a user email
def test_get_user_email_controller(mocker):

    mock_get = mocker.patch("app.controllers.user_controller.get_user_email_controller")
    mock_get.return_value = test_config.API_TEST_GET_USER_EMAIL_RESPONSE

    db.create_table(test_config.DB_TEST_TABLE, db_config.DB_USER_SCHEMA)

    db.insert_into_table(
        test_config.DB_TEST_TABLE,
        db_config.DB_USER_SCHEMA_INSERTION,
        test_config.DB_TEST_USER_INSERTION,
    )

    test_get_user_email = GetOrRemove(user_name=test_config.DB_TEST_USERNAME)

    # passes test parameters to the controller
    user_email = get_user_email_controller(
        test_get_user_email, test_config.DB_TEST_TABLE
    )

    assert GetUserEmail(**user_email)

    db.drop_table(test_config.DB_TEST_TABLE)
