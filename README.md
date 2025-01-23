# SkySage

This application was built by myself (Riley Eaton), Kai Gehry, Max Oberhellman, and Mridul Nohria as our final project for COSC310: Software Engineering, at UBC.

## Quickstart 

1. Create a `.env` by copying the contents of the `.env_sample` file. The **Database Credentials** can be filled out with whatever you like, but the **API credentials** are real keys from each of the 4 providers. You must acquire each of these to enable the full site's functionalities. Alternatively, you can watch the [video walkthrough](https://youtu.be/xqPW8g70DHU) instead of self-hosting.
2. In the root folder (where this file is located) run `docker compose up --build`. After running this for the first time, you can simply run `docker compose up`.
3. Once the terminal prints that the frontend and backend have started, and the database has been initialized, you can visit the [home page](http://localhost:3000/) of the app on your local machine.
4. Explore SkySage, and enjoy!

If docker is giving you troubles at any point, you can run the docker cleanup script `clean_docker.bat` (or `clean_docker.sh` on mac) in the root directory but **BE WARNED** this will wipe all docker images, containers, volumes etc. from your machine. 

## Project Description

SkySage is a web-based application to view current and upcoming weather trends all across the world in a digestible format, that can also be shared with friends. The weather data users can access is available in two formats: the current weather at a given location, and the 5-day forecast to see the weather trends in the near-future. User's of SkySage are able to search for their desired location (usually cities) with a vast amount of locations to choose from across the globe. This means people from any country can use SkySage to check the weather near them. Users can also create accounts (though not required for general browsing) to favourite the locations they want weather information on the most often. These favourited locations can then be viewed on the user's dashboard, which gives them a brief summary of the weather for each. Users can then share these dashboards with other users, so there is no need to duplicate favourites. A user can unfavourite a location or unshare a dashboard at any time on the site. Finally, SkySage brings unique AI augmentation to the weather forecast. Though natural language, an AI summary will be provided when viewing the 5-day weather forecast which will primarily describe the trend over the next 5 days and what to look out for (any potential hazards users should be aware of).

In terms of technical details, SkySage uses external APIs to allow users to search for locations, retrieve weather data for a given location, and generate AI summaries. User data is stored in a relational database, and all personal identifiable information (including passwords) are hashed (salted) for security.

## Video Walkthrough

[Watch Here](https://youtu.be/xqPW8g70DHU)

---

## Requirements

### User Requirements

- Ability to search for a desired city/location using its name to get subsequent weather details.
  - If a city/location searched by the user does not exist, the user will be notified to alter their search. Users will also be able to search for a specific address instead of city name.
- Once a city/location is selected, the user will first be presented with the current weather there.
- When viewing a city/location, the user can also optionally see the weather forecast for the next 5 days there.
- The website will be accessible to users who use Chrome, Safari, Firefox, or Edge web browsers.
- Users will be able to create accounts and log in, in order to personalize their experience on the site.
  - If users forget their password, they will have the ability to reset it.
- When logged in, users can favourite locations that they have searched for, allowing them to more easily keep track of them.
  - If a user no longer wants to have a location favourited, they will have the ability to unfavourite them.
- Once a user has at least 1 favourited location, they can then view their dashboard which shows a summary view of the weather at each of their favourited locations.
  - Users can favourite up to 8 locations at once.
- Users can share their dashboard with other users.
  - If a user no longer wants to share their dashboard with certain other users, they will have the ability to remove each user who currently has access.

### Functional Requirements

- Location search must be supported. Search can be conducted by city/location name based on what is available from the external API.
  - Locations should not be case sensitive
  - Search will also allow for a specific address instead of city name.
- The application will provide the predicted weather parameters for the next 5 days.
  - An AI summary will be displayed when viewing the 5-day weather forecast, which will primarily describe the trend over the next 5 days using a brief (2-3 sentence) summary.
- The application will display the maximum and minimum weather parameters for the period requested by the user.
- The application will provide the following weather parameters: temperature, wind speed, rainfall and humidity.
- Favorite locations can be saved to dashboard for easy access to a summary of weather conditions at different locations.
- Accounts can be created by users to keep track of things such as favourite locations, dashboards, and dashboard sharing.
  - Accounts are not required to access the base site where searching and viewing weather information for cities/locations

### Non-Functional Requirements

- OpenWeather’s [Weather API](https://openweathermap.org/api) will be used to get weather data as it is free, extensive, and performant for the number of queries we will be making (less than 1000 per day based on estimates of user-base).
- Google's [Places API](https://developers.google.com/maps/documentation/places/web-service) will be used for searching for a location, returning the coordinates which can then be passed to the weather API.
- Mailgun's [mail api](https://documentation.mailgun.com/docs/mailgun/api-reference/) will be used to send notification emails, password reset emails, and more to users of the site.
- Weather results must be returned from the API within 5 seconds.
- Store user details in a secure, relational database (such as MySQL).
  - Secure meaning all PII and password data will be hashed (salted).
  - Access to database will be restricted to administrators who have rotating passwords for authentication.
- Use the **Adapter Pattern** to interface with the external weather API.
  - A REST API layer will be built into the system to then serve up the information retrieved rom the external weather API.
- Use the **Singleton Pattern** to manage a single instance of the API client.
- Use the **Facade Pattern** to simplify the interface for fetching and displaying weather data.
  - A control system will control the flow of data and data transformations between fetching from the API and returning the data to the client.
- An API will be used to generate the AI summaries of forecasted weather conditions.
- Will incorporate Continuous Integration (CI) and automated testing
- For deployment, the application will be dockerized
- Development will follow a TDD model, where tests will be written before implementation
  - Unit tests and integration tests are required to ensure code quality and functionality

---

## Use Cases

### [Use Case Descriptions](/documentation/use_case_descriptions.md)

### Use Case Model

![Use Case Diagram](/documentation/diagrams/use-case-diagram.png)

### Proto-Personas

![Proto-persona 1, Chase](/documentation/diagrams/proto_persona_Chase.png)
![Proto-Persona 2, Toshi](/documentation/diagrams/proto_persona_Toshi.png)
