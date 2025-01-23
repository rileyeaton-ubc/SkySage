# *************************************************************************************
# COSC 310 Project - SkySage

# DESCRIPTION: Test cases for SQLite functionality

# Author: Kai Gehry, Riley Eaton
# Date: 2024-11-18
# *************************************************************************************

from app.config.test_config import test_config
import app.models.db_functions as db_functions


# Test to ensure the connection to the database is successful
def test_connection():
    assert db_functions.connect()


# Test to ensure the disconnection from the database is successful
def test_disconnect():
    connection = db_functions.connect()
    assert db_functions.disconnect(connection)


# Test to ensure the cursor creation is successful
# The connection is closed after the test
def test_cursor_creation():
    try:
        connection = db_functions.connect()
        assert db_functions.create_cursor(connection)
    finally:
        db_functions.disconnect(connection)


# Test to ensure a table can be created in the database
def test_create_table():
    create_table_result = db_functions.create_table(
        test_config.DB_TEST_TABLE, test_config.DB_TEST_SCHEMA
    )
    assert create_table_result


# Test to ensure a table can be dropped from the database
def test_drop_table():
    assert db_functions.drop_table(test_config.DB_TEST_TABLE)


# Test to ensure all rows can be selected from a table
# The table is dropped after the test
def test_select_all_from_table():
    try:
        db_functions.create_table(test_config.DB_TEST_TABLE, test_config.DB_TEST_SCHEMA)
        assert db_functions.select_all_from_table(test_config.DB_TEST_TABLE) == []
    finally:
        db_functions.drop_table(test_config.DB_TEST_TABLE)


# Test to ensure values can be inserted into a table
# The table is dropped after the test
def test_insert_into_table():
    try:
        db_functions.create_table(test_config.DB_TEST_TABLE, test_config.DB_TEST_SCHEMA)
        insert_results = db_functions.insert_into_table(
            test_config.DB_TEST_TABLE,
            test_config.DB_TEST_SCHEMA_NOKEY,
            (test_config.DB_TEST_USERNAME, test_config.DB_TEST_PASSWORD),
        )
        assert insert_results
        assert insert_results["rows_affected"] == 1
    finally:
        db_functions.drop_table(test_config.DB_TEST_TABLE)


# Test to ensure a specific row can be selected from a table
# The table is dropped after the test
def test_select_specific_from_table():
    try:
        db_functions.create_table(test_config.DB_TEST_TABLE, test_config.DB_TEST_SCHEMA)
        insert_results = db_functions.insert_into_table(
            test_config.DB_TEST_TABLE,
            test_config.DB_TEST_SCHEMA_NOKEY,
            (test_config.DB_TEST_USERNAME, test_config.DB_TEST_PASSWORD),
        )
        select_results = db_functions.select_specific_from_table(
            test_config.DB_TEST_TABLE,
            test_config.DB_TEST_ID_FIELD,
            insert_results["last_row_id"],
        )
        assert select_results
        assert insert_results["last_row_id"] in select_results
    finally:
        db_functions.drop_table(test_config.DB_TEST_TABLE)


# Test to ensure specific column(s) can be selected from a table
# The table is dropped after the test
def test_select_specific_column_from_table():
    try:
        db_functions.create_table(test_config.DB_TEST_TABLE, test_config.DB_TEST_SCHEMA)
        insert_results = db_functions.insert_into_table(
            test_config.DB_TEST_TABLE,
            test_config.DB_TEST_SCHEMA_NOKEY,
            (test_config.DB_TEST_USERNAME, test_config.DB_TEST_PASSWORD),
        )
        select_results = db_functions.select_specific_column_from_table(
            test_config.DB_TEST_TABLE,
            test_config.DB_TEST_TABLE_COLUMNS,
            (test_config.DB_TEST_ID_FIELD,),
            (f"{insert_results["last_row_id"]}",),
            True,
        )
        assert select_results
        assert insert_results["last_row_id"] in select_results
    finally:
        db_functions.drop_table(test_config.DB_TEST_TABLE)


# Test to ensure multiple rows can be inserted into a table
# The table is dropped after the test
def test_insert_many_into_table():
    try:
        db_functions.create_table(test_config.DB_TEST_TABLE, test_config.DB_TEST_SCHEMA)
        insert_many_results = db_functions.insert_many_into_table(
            test_config.DB_TEST_TABLE,
            test_config.DB_TEST_SCHEMA_NOKEY,
            [
                (test_config.DB_TEST_USERNAME, test_config.DB_TEST_PASSWORD),
                (test_config.DB_TEST_USERNAME_2, test_config.DB_TEST_PASSWORD_2),
            ],
        )
        assert insert_many_results
        assert insert_many_results == 2
    finally:
        db_functions.drop_table(test_config.DB_TEST_TABLE)


# Test to ensure a row can be updated in a table
# The table is dropped after the test
def test_update_table_entry():
    try:
        db_functions.create_table(test_config.DB_TEST_TABLE, test_config.DB_TEST_SCHEMA)
        insert_results = db_functions.insert_into_table(
            test_config.DB_TEST_TABLE,
            test_config.DB_TEST_SCHEMA_NOKEY,
            (test_config.DB_TEST_USERNAME, test_config.DB_TEST_PASSWORD),
        )
        update_results = db_functions.update_table_entry(
            test_config.DB_TEST_TABLE,
            test_config.DB_TEST_PASSWORD_FIELD,
            f"'{test_config.DB_TEST_UPDATE_PASSWORD}'",
            test_config.DB_TEST_ID_FIELD,
            insert_results["last_row_id"],
        )
        assert update_results
        assert update_results["rows_affected"] == 1
    finally:
        db_functions.drop_table(test_config.DB_TEST_TABLE)


# Test to ensure a row can be deleted from a table
# The table is dropped after the test
def test_delete_table_entry():
    try:
        db_functions.create_table(test_config.DB_TEST_TABLE, test_config.DB_TEST_SCHEMA)
        insert_results = db_functions.insert_into_table(
            test_config.DB_TEST_TABLE,
            test_config.DB_TEST_SCHEMA_NOKEY,
            (test_config.DB_TEST_USERNAME, test_config.DB_TEST_PASSWORD),
        )
        delete_results = db_functions.delete_table_entry(
            test_config.DB_TEST_TABLE,
            test_config.DB_TEST_ID_FIELD,
            insert_results["last_row_id"],
        )
        assert delete_results == 1
    finally:
        db_functions.drop_table(test_config.DB_TEST_TABLE)
