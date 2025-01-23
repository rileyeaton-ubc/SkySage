# ***********************************************************************************
# COSC 310 Project - SkySage

# Description: Dockerfile to provide Docker the instructions on how and what to run

# Author: Riley Eaton 
# Date: 11/19/2024
# ***********************************************************************************

# Use the official Python image (version 3.12.0)
FROM python:3.12.0

# Set the working directory in the container to the app directory
WORKDIR /skysage

COPY requirements.txt /skysage
# COPY init_db.sh /skysage

#  Set the PYTHONPATH environment variable to the current directory
ENV PYTHONPATH=/skysage

# Install the required packages from the requirements.txt file
RUN pip install --no-cache-dir -r ./requirements.txt