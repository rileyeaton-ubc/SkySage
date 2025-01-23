#!/bin/bash
# ***********************************************************************************
# COSC 310 Project - SkySage
#
# Description: Script for the docker build process to run, which will initialize & 
#              test the sqlite database.
#
# Author: Riley Eaton 
# Date: 11/28/2024
# ***********************************************************************************
# Initialize the database
echo "Initializing the SQLite database..."
pytest --capture=fd ./tests/db_init_test.py || exit 1
echo "Database initialization completed successfully."
exec "$@"