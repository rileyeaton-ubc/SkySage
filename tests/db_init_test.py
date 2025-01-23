# *************************************************************************************
# COSC 310 Project - SkySage

# DESCRIPTION: Test cases for SQLite functionality

# Author: Kai Gehry, Riley Eaton
# Date: 2024-11-18
# *************************************************************************************

# Import config and shared functions for the database
from app.config.test_config import test_config
from app.config.db_config import db_config
import app.models.db_init as init
import app.models.db_functions as db


# Test to ensure the admin and secondary user are successfully loaded into the database
def test_init_users_loaded():
    # Query the database to ensure the admin and secondary user are present by using the first and second IDs
    admin_results = db.select_specific_from_table(
        db_config.DB_USER_TABLE, db_config.DB_USER_ID_FIELD, 1
    )
    secondary_results = db.select_specific_from_table(
        db_config.DB_USER_TABLE, db_config.DB_USER_ID_FIELD, 2
    )

    # if the admin and secondary user are present in the database and match the correct values, pass the test
    if admin_results != (None or False) and secondary_results != (None or False):
        if (
            test_config.DB_TEST_ADMIN_USER_ENTRY in admin_results
            and test_config.DB_TEST_SECONDARY_USER_ENTRY in secondary_results
        ):
            assert True
            return

    # Run the initialization function to add the admin and secondary user to the database and assert that it matches the test values
    user_init_results = init.init_users()
    print(user_init_results)
    assert test_config.DB_TEST_SECONDARY_USER_ENTRY in user_init_results
    assert test_config.DB_TEST_ADMIN_USER_ENTRY in user_init_results


# Test to ensure the first dashboard is successfully loaded into the database
def test_init_dashboard_loaded():
    # Query the database to ensure the first dashboard is present by using the first ID
    dashboard_results = db.select_specific_from_table(
        db_config.DB_DASHBOARD_TABLE, db_config.DB_DASHBOARD_ID_FIELD, 1
    )

    # if the first dashboard is present in the database and matches the correct values, pass the test
    if dashboard_results != (None or False):
        if test_config.DB_TEST_ADMIN_DASHBOARD_ENTRY == dashboard_results:
            assert True
            return

    # Run the initialization function to add the first dashboard to the database and assert that it matches the test values
    assert init.init_dashboard() == test_config.DB_TEST_ADMIN_DASHBOARD_ENTRY


# Test to ensure the first shared dashboard is successfully loaded into the database
def test_init_shared_dashboard_loaded():
    # Query the database to ensure the first shared dashboard is present by using the first ID
    shared_dashboard_results = db.select_specific_from_table(
        db_config.DB_SHARED_DASHBOARD_TABLE, db_config.DB_SHARED_DASH_ID_FIELD, 1
    )

    # if the first shared dashboard is present in the database and matches the correct values, pass the test
    if shared_dashboard_results != (None or False):
        if test_config.DB_TEST_ADMIN_SHARED_DASHBOARD_ENTRY == shared_dashboard_results:
            assert True
            return

    # Run the initialization function to add the first shared dashboard to the database and assert that it matches the test values
    assert (
        init.init_shared_dashboard() == test_config.DB_TEST_ADMIN_SHARED_DASHBOARD_ENTRY
    )
