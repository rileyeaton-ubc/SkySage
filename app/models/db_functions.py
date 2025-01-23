# *************************************************************************************
# COSC 310 Project - SkySage

# DESCRIPTION: Utility functions to interact with the SQLite database (CRUD)

# Author: Kai Gehry, Riley Eaton
# Date: 2024-11-18
# *************************************************************************************

# import the global settings from the config file and the sqlite utility
import app.models.db_functions as db
from app.config.global_config import global_settings
import sqlite3


# Connect
# Description: Connects to the SQLite database
# Parameters:
#  => database_filepath: string - the path to the database file (default is the global_settings.DB_FILEPATH)
# Return on Success: Connection object
# Return on Failure: False
def connect(database_filepath=global_settings.DB_FILEPATH):
    try:
        # creates a connection to the desired db and returns the connection object
        connection = sqlite3.connect(database_filepath)
        return connection

    # if SQLite raises any errors, log it and return false
    except sqlite3.Error as e:
        print(f"A sqlite3 error occurred: {e}")
        return False


# Disconnect
# Description: Disconnects from the SQLite database
# Parameters:
#  => connection: Connection object - the connection object to be closed
# Return on Success: True
# Return on Failure: False
def disconnect(connection):
    try:
        # close the connection and return true
        connection.close()
        return True

    # if SQLite raises any errors, log it and return false
    except sqlite3.Error as e:
        print(f"A sqlite3 error occurred: {e}")
        return False


# Create Cursor
# Description: Creates a cursor object for the SQLite database
# Parameters:
#  => connection: Connection object - the connection object to create the cursor from
# Return on Success: Cursor object
# Return on Failure: False
def create_cursor(connection):
    try:
        # creates a cursor object and returns it
        cursor = connection.cursor()
        return cursor

    # if SQLite raises any errors, log it and return false
    except sqlite3.Error as e:
        print(f"A sqlite3 error occurred: {e}")
        return False


# Create Table
# Description: Creates a table in the SQLite database
# Parameters:
#  => table_name: string - the name of the table to be created
#  => schema: string - the schema of the table to be created
# Return on Success: True
# Return on Failure: False
def create_table(table_name, schema):
    try:
        # connects to DB
        connection = connect()
        # creates a cursor object
        cursor = create_cursor(connection)
        # if the table to be created does not already exists in the DB, it is created
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name}{schema}")
        # return true to indicate that the table was created
        return True

    # if SQLite raises any errors, log it and return false
    except sqlite3.Error as e:
        print(f"A sqlite3 error occurred: {e}")
        return False

    finally:
        # close connection
        disconnect(connection)


# Drop Table
# Description: Drops a table in the SQLite database
# Parameters:
#  => table_name: string - the name of the table to be dropped
# Return on Success: True
# Return on Failure: False
def drop_table(table_name):
    try:
        # connects to DB
        connection = connect()
        # creates a cursor object
        cursor = create_cursor(connection)
        # drop the indicated table
        cursor.execute(f"DROP TABLE {table_name}")
        # returns true to indicate that the table was dropped
        return True

    # if SQLite raises any errors, log it and return false
    except sqlite3.Error as e:
        print(f"A sqlite3 error occurred: {e}")
        return False

    finally:
        # close connection
        disconnect(connection)


# Select Specific From Table
# Description: Selects from a table in the SQLite database based on identifier (all columns)
# Parameters:
#  => table_name: string - the name of the table to select from
#  => identifier_field: string - the field to identify the rows by
#  => identifier_value: string - the value to identify the rows by
# Return on Success: Tuple - the rows returned by the query
# Return on Failure: False
def select_specific_from_table(table_name, identifier_field, identifier_value):
    try:
        # connects to DB
        connection = connect()
        # creates a cursor object
        cursor = create_cursor(connection)
        # execute and store the select statement results
        result = cursor.execute(
            f"SELECT * FROM {table_name} WHERE {identifier_field} = {identifier_value}"
        )
        # store the rows returned by the query
        values = result.fetchone()
        # return the results
        return values

    # if SQLite raises any errors, log it and return false
    except sqlite3.Error as e:
        print(f"A sqlite3 error occurred: {e}")
        return False

    finally:
        # close connection
        disconnect(connection)


# Select Specific From Table
# Description: Selects a secific row from a table in the SQLite database based on identifier
# Parameters:
#  => table_name: tuple - the name of the table (or tables in the case of a join) to select from
#  => colum_list: tuple - contains the list of columbs to be inserted into
#  => identifier_field: tuple - The field to identify the rows by. Defaulted to empty
#  => identifier_value: tuple - The value to identify the rows by. Defaulted to empty
#  => where_flag: boolean - Used to identify whether the query contains a where clause. Defaulted to false
#  => condition_list: tuple - Contains conditions logical conditions for column values to check (AND, OR, NOT, etc.). Defaulted to empty
#  => join_list: tuple - Contains joins to be added to the query. Defaulted to empty
# Return on Success: Tuple - the rows returned by the query
# Return on Failure: False
def select_specific_column_from_table(
    table_name,
    column_list,
    identifier_field="",
    identifier_value="",
    where_flag=False,
    condition_list="",
    join_list="",
    list_return=False,
):
    try:
        # connects to DB
        connection = connect()
        # creates a cursor object
        cursor = create_cursor(connection)
        # execute and store the select statement results

        # creates a string of any table names that have been passed to the function with added joins if specified
        table_list = ""
        index1 = 0  # used to access a single join element from the join_list
        for table in table_name:
            table_list = table_list + table

            if join_list != "" and index1 < len(join_list):
                table_list = table_list + " " + join_list[index1] + " "
                index1 = index1 + 1

        # variable to hold the column list passed as a parameter as a string
        col_list = ""
        # converts the tuple into a list. This allows for multiple columns to be selected from in the query
        for i in column_list:
            if col_list == "":
                col_list = i
            else:
                col_list = col_list + ", " + i

        # creates an initial string to hold the conditions imposed in the where clause
        if where_flag == True:
            where_clause = "WHERE "

        # iterates through the identifier_field and identifier_value lists to create a where clause with mutliple identifier_fields and values
        index2 = 0
        for j, k in zip(identifier_field, identifier_value):

            where_clause = where_clause + j + " = " + k

            if condition_list != "" and index2 < len(condition_list):
                where_clause = where_clause + " " + condition_list[index2] + " "
                index2 = index2 + 1

        # if an identifier_field has been passed to the function, a WHERE clause is inculded in the query
        if identifier_field != "":
            result = cursor.execute(
                f"SELECT {col_list} FROM {table_list} {where_clause}"
            )
        # if no identifier field has been passed to the function, no where clause is included in the query
        else:
            result = cursor.execute(f"SELECT {col_list} FROM {table_list}")

        if list_return == False:
            # store the rows returned by the query
            values = result.fetchone()
        else:
            values = result.fetchall()

        return values

    # if SQLite raises any errors, log it and return false
    except sqlite3.Error as e:
        print(f"A sqlite3 error occurred: {e}")
        return False

    finally:
        # close connection
        disconnect(connection)


# Select All From Table
# Description: Selects all rows from a table in the SQLite database
# Parameters:
#  => table_name: string - the name of the table to select from
# Return on Success: List of Tuples - the row values
# Return on Failure: False
def select_all_from_table(table_name):
    try:
        # connects to DB
        connection = connect()
        # creates a cursor object
        cursor = create_cursor(connection)
        # execute and store the select statement results for the table
        result = cursor.execute(f"SELECT * FROM {table_name}")
        # stores the row values returned by the query
        values = result.fetchall()
        # return the results
        return values

    # if SQLite raises any errors, log it and return false
    except sqlite3.Error as e:
        print(f"A sqlite3 error occurred: {e}")
        return False

    finally:
        # close connection
        disconnect(connection)


# Insert Into Table
# Description: Inserts a row into a table in the SQLite database
# Parameters:
#  => table_name: string - the name of the table to insert into
#  => schema: string - the schema of the table to insert into
#  => data: tuple - the values to insert into the table
# Return on Success: Dict - the number of rows affected and the last row id
# Return on Failure: False
def insert_into_table(table_name, schema, data):
    try:
        # connects to DB
        connection = connect()
        # creates a cursor object
        cursor = create_cursor(connection)
        # executes an insert for a tuple into the desired table
        cursor.execute(f"INSERT INTO {table_name} {schema} VALUES {data}")
        # store the last row id as this is what was inserted
        last_row_id = cursor.lastrowid
        # commits the changes
        connection.commit()
        # stores the number of rows affected by the insertion
        rows_affected = cursor.rowcount
        # return a dict with the rows affected and the last row id
        return {"rows_affected": rows_affected, "last_row_id": last_row_id}

    # if SQLite raises any errors, log it and return false
    except sqlite3.Error as e:
        print(f"A sqlite3 error occurred: {e}")
        return False

    finally:
        # close connection
        disconnect(connection)


# Insert Many Into Table
# Description: Inserts multiple rows into a table in the SQLite database
# Parameters:
#  => table_name: string - the name of the table to insert into
#  => schema: string - the schema of the table to insert into
#  => data: list of tuples - the values to insert into the table
# Return on Success: Int - the number of rows affected
# Return on Failure: False
def insert_many_into_table(table_name, schema, data):
    try:
        # connects to DB
        connection = connect()
        # creates a cursor object
        cursor = create_cursor(connection)
        # create the placeholder string for the values to be inserted
        placeholders = ", ".join("?" * len(data[0]))
        # inserts an array of tuples into the desired table using the schema
        cursor.executemany(
            f"INSERT INTO {table_name} {schema} VALUES ({placeholders})", data
        )
        # commits the changes
        connection.commit()
        # stores the number of rows affected by the insertion
        rows_affected = cursor.rowcount
        # return the results
        return rows_affected

    # if SQLite raises any errors, log it and return false
    except sqlite3.Error as e:
        print(f"A sqlite3 error occurred: {e}")
        return False

    finally:
        # close connection
        disconnect(connection)


# Update Table Entry
# Description: Updates a row in a table in the SQLite database
# Parameters:
#  => table_name: string - the name of the table to update
#  => set_field: string - the field to update
#  => set_value: string - the value to update the field to
#  => identifier_field: string - the field to identify the row by
#  => identifier_value: string - the value to identify the row by
# Return on Success: Dict - the number of rows affected and the last row id
# Return on Failure: False
def update_table_entry(
    table_name, set_field, set_value, identifier_field, identifier_value
):
    try:
        # connects to DB
        connection = connect()
        # creates a cursor object
        cursor = create_cursor(connection)
        # execute the update statement using the provided fields and values
        cursor.execute(
            f"UPDATE {table_name} SET {set_field} = {set_value} WHERE {identifier_field} = {identifier_value}"
        )
        # store the last row id as this is what was updated
        last_row_id = cursor.lastrowid
        # commits the changes
        connection.commit()
        # stores the number of rows affected by the insertion
        rows_affected = cursor.rowcount
        # return a dict with the rows affected and the last row id
        return {"rows_affected": rows_affected, "last_row_id": last_row_id}

    # if SQLite raises any errors, log it and return false
    except sqlite3.Error as e:
        print(f"A sqlite3 error occurred: {e}")
        return False

    finally:
        # close connection
        disconnect(connection)


# Delete Table Entry
# Description: Deletes a row in a table in the SQLite database
# Parameters:
#  => table_name: string - the name of the table to delete from
#  => identifier_field: string - the field to identify the row by
#  => identifier_value: string - the value to identify the row by
# Return on Success: Int - the number of rows affected
# Return on Failure: False
def delete_table_entry(table_name, identifier_field, identifier_value):
    try:
        # connects to DB
        connection = connect()
        # creates a cursor object
        cursor = create_cursor(connection)
        # delete the desired elements in the given table using the identifier field and value
        cursor.execute(
            f"DELETE FROM {table_name} WHERE {identifier_field} = {identifier_value}"
        )
        # commits the changes
        connection.commit()
        # stores the number of rows affected by the insertion
        rows_affected = cursor.rowcount
        # return the results
        return rows_affected

    # if SQLite raises any errors, log it and return false
    except sqlite3.Error as e:
        print(f"A sqlite3 error occurred: {e}")
        return False

    finally:
        # close connection
        disconnect(connection)
