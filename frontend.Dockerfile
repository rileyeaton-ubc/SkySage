# Use the official Nginx image to serve up the frontend
FROM nginx:alpine

# Set the working directory toi the standard ngix HTML directory
WORKDIR /usr/share/nginx/html

# Copy the static files from the project directory to the Nginx HTML directory
# COPY ./app/static/ /usr/share/nginx/html

# Expose port 80 to serve the frontend
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
