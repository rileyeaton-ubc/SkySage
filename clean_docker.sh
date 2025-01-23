#***********************************************************************************
# COSC 310 Project - SkySage
#
# Description: Script for cleaning all docker images, containers, volumes, and 
#              rebuilding for docker compose.
#
# Author: Riley Eaton  
# Date: 12/04/2024
#***********************************************************************************

# turn off and remove docker containers
docker-compose down

# kill all service containers and remove them
docker-compose kill
docker-compose rm -f

# remove all volumes and other docker images, etc.
docker system prune -a -f

# rebuild the docker compose
docker-compose up --build